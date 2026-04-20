const ANTHROPIC_API_URL = null;

let translationCache = JSON.parse(localStorage.getItem('nutricare_translations') || '{}');

async function translateTexts(texts, targetLang) {
  const langNames = { en: 'English', es: 'Spanish', ar: 'Arabic' };
  const cacheKey = targetLang + '_' + btoa(unescape(encodeURIComponent(texts.join('|')))).slice(0, 32);
  if (translationCache[cacheKey]) return translationCache[cacheKey];

  const response = await fetch(BACKEND_URL + '/api/translate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ texts, lang: targetLang })
  });
  const translated = await response.json();
  translationCache[cacheKey] = translated;
  localStorage.setItem('nutricare_translations', JSON.stringify(translationCache));
  return translated;
}

function getTextNodes(root) {
  const walker = document.createTreeWalker(
    root,
    NodeFilter.SHOW_TEXT,
    {
      acceptNode(node) {
        const text = node.textContent.trim();
        if (!text || text.length < 2) return NodeFilter.FILTER_REJECT;
        const parent = node.parentElement;
        if (!parent) return NodeFilter.FILTER_REJECT;
        const tag = parent.tagName?.toLowerCase();
        if (['script', 'style', 'noscript'].includes(tag)) return NodeFilter.FILTER_REJECT;
        if (parent.closest('script, style')) return NodeFilter.FILTER_REJECT;
        if (/^[\d\s\.\,\%\€\$\+\-\=\/\:\;\!\?\(\)\[\]\{\}]*$/.test(text)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    }
  );
  const nodes = [];
  let node;
  while (node = walker.nextNode()) nodes.push(node);
  return nodes;
}

let originalTexts = {};
let isTranslating = false;

async function applyAutoTranslation(lang) {
  if (lang === 'fr') {
    restoreOriginalTexts();
    document.documentElement.dir = 'ltr';
    document.documentElement.lang = 'fr';
    return;
  }

  if (isTranslating) return;
  isTranslating = true;

  document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
  document.documentElement.lang = lang;

  const root = document.getElementById('appPage') || document.body;
  const nodes = getTextNodes(root);

  // Sauvegarder les textes originaux
  nodes.forEach((node, i) => {
    if (!originalTexts[i]) originalTexts[i] = node.textContent;
  });

  const texts = nodes.map(n => n.textContent.trim()).filter(t => t.length > 1);
  const unique = [...new Set(texts)];

  try {
    // Traduire par batch de 50
    const batchSize = 50;
    const allTranslated = {};
    for (let i = 0; i < unique.length; i += batchSize) {
      const batch = unique.slice(i, i + batchSize);
      const translated = await translateTexts(batch, lang);
      batch.forEach((orig, j) => { allTranslated[orig] = translated[j]; });
    }

    // Appliquer les traductions
    nodes.forEach(node => {
      const orig = node.textContent.trim();
      if (allTranslated[orig]) node.textContent = allTranslated[orig];
    });

    // Traduire aussi les placeholders
    document.querySelectorAll('[placeholder]').forEach(el => {
      const orig = el.getAttribute('placeholder');
      if (allTranslated[orig]) el.setAttribute('placeholder', allTranslated[orig]);
    });

  } catch(e) {
    console.error('Translation error:', e);
  }

  isTranslating = false;
}

function restoreOriginalTexts() {
  const root = document.getElementById('appPage') || document.body;
  const nodes = getTextNodes(root);
  nodes.forEach((node, i) => {
    if (originalTexts[i]) node.textContent = originalTexts[i];
  });
  document.querySelectorAll('[placeholder]').forEach(el => {
    const orig = el.getAttribute('data-orig-placeholder');
    if (orig) el.setAttribute('placeholder', orig);
  });
  originalTexts = {};
}

async function setLang(lang) {
  localStorage.setItem('nutricare_lang', lang);
  const sel = document.getElementById('langSelector');
  if (sel) sel.value = lang;
  await applyAutoTranslation(lang);
}

function initTranslator() {
  const saved = localStorage.getItem('nutricare_lang') || 'fr';
  const sel = document.getElementById('langSelector');
  if (sel) sel.value = saved;
  if (saved !== 'fr') applyAutoTranslation(saved);
}
