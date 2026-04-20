let currentLang = localStorage.getItem('nutricare_lang') || 'fr';
let translationsCache = JSON.parse(localStorage.getItem('nutricare_trans_cache') || '{}');

function collectTexts() {
  const texts = new Set();
  document.querySelectorAll('button, a, label, h1, h2, h3, h4, p, div, span, li, td, th').forEach(el => {
    const text = el.childNodes[0]?.nodeValue?.trim();
    if (text && text.length > 1 && text.length < 200 && /[a-zA-ZÀ-ÿ]/.test(text)) {
      texts.add(text);
    }
  });
  document.querySelectorAll('[placeholder]').forEach(el => {
    const p = el.getAttribute('placeholder');
    if (p && p.length > 1) texts.add(p);
  });
  return [...texts];
}

async function preloadTranslations() {
  const texts = collectTexts();
  for (const lang of ['en', 'es', 'ar']) {
    if (translationsCache[lang]) continue;
    try {
      const res = await fetch(BACKEND_URL + '/api/translate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({texts, lang})
      });
      if (res.ok) {
        const translated = await res.json();
        const map = {};
        texts.forEach((t, i) => { map[t] = translated[i]; });
        translationsCache[lang] = map;
        localStorage.setItem('nutricare_trans_cache', JSON.stringify(translationsCache));
        console.log(`Translations preloaded for ${lang}`);
      }
    } catch(e) { console.error('preload error:', e); }
  }
}

function applyTranslation(lang) {
  if (lang === 'fr') {
    location.reload();
    return;
  }
  const map = translationsCache[lang];
  if (!map) {
    console.log('No cache for', lang, '- loading...');
    translateAndApply(lang);
    return;
  }
  
  document.querySelectorAll('button, a, label, h1, h2, h3, h4, p, div, span, li, td, th').forEach(el => {
    const node = el.childNodes[0];
    if (node?.nodeType === 3) {
      const text = node.nodeValue.trim();
      if (map[text]) node.nodeValue = node.nodeValue.replace(text, map[text]);
    }
  });
  document.querySelectorAll('[placeholder]').forEach(el => {
    const p = el.getAttribute('placeholder');
    if (map[p]) el.setAttribute('placeholder', map[p]);
  });

  document.documentElement.lang = lang;
}

async function translateAndApply(lang) {
  const texts = collectTexts();
  try {
    const res = await fetch(BACKEND_URL + '/api/translate', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({texts, lang})
    });
    if (res.ok) {
      const translated = await res.json();
      const map = {};
      texts.forEach((t, i) => { map[t] = translated[i]; });
      translationsCache[lang] = map;
      localStorage.setItem('nutricare_trans_cache', JSON.stringify(translationsCache));
      applyTranslation(lang);
    }
  } catch(e) { console.error('translate error:', e); }
}

async function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('nutricare_lang', lang);
  const sel = document.getElementById('langSelector');
  if (sel) sel.value = lang;
  applyTranslation(lang);
}

function initTranslator() {
  const saved = localStorage.getItem('nutricare_lang') || 'fr';
  const sel = document.getElementById('langSelector');
  if (sel) sel.value = saved;
  if (saved !== 'fr') applyTranslation(saved);
  // Précharger en arrière-plan après 3 secondes
  setTimeout(preloadTranslations, 3000);
}
