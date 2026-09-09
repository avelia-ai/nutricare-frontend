# -*- coding: utf-8 -*-
with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1) HTML : avatar premium (anneau degrade) + carte texte glassmorphism
# ============================================================
old_html = """        <div style="position:relative;display:flex;align-items:center;gap:12px;margin-bottom:14px">
          <div id="homeAvatar" style="width:42px;height:42px;border-radius:50%;background:rgba(255,255,255,0.3);display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:700;color:white;flex-shrink:0">?</div>
          <div>
            <div id="homeGreeting" style="font-size:1.1rem;font-weight:700;color:white">Bonjour !</div>
            <div id="homeDate" style="font-size:0.78rem;color:rgba(255,255,255,0.8)"></div>
          </div>
        </div>
        <div id="homeScoreResume" style="position:relative;background:rgba(255,255,255,0.18);border-radius:12px;padding:10px 14px">
          <div style="font-size:0.82rem;color:white;line-height:1.5" id="homeScoreText">Chargement...</div>
        </div>"""

new_html = """        <div style="position:relative;display:flex;align-items:center;gap:14px;margin-bottom:16px">
          <div style="position:relative;width:52px;height:52px;flex-shrink:0">
            <div style="position:absolute;inset:0;border-radius:50%;padding:2px;background:linear-gradient(135deg,rgba(255,255,255,0.95),rgba(255,255,255,0.25));box-shadow:0 6px 16px rgba(0,0,0,0.12)">
              <div id="homeAvatar" style="width:100%;height:100%;border-radius:50%;background:rgba(255,255,255,0.22);display:flex;align-items:center;justify-content:center;font-size:1.05rem;font-weight:800;color:white;letter-spacing:0.02em">?</div>
            </div>
          </div>
          <div>
            <div id="homeGreeting" style="font-size:1.24rem;font-weight:800;color:white;letter-spacing:-0.01em">Bonjour !</div>
            <div id="homeDate" style="font-size:0.76rem;color:rgba(255,255,255,0.75);margin-top:2px"></div>
          </div>
        </div>
        <div id="homeScoreResume" style="position:relative;display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.16);border:1px solid rgba(255,255,255,0.22);border-radius:14px;padding:12px 14px">
          <div style="width:34px;height:34px;border-radius:10px;background:rgba(255,255,255,0.22);display:flex;align-items:center;justify-content:center;flex-shrink:0">
            <i class="ti ti-sparkles" id="homeScoreIcon" style="font-size:17px;color:#fff"></i>
          </div>
          <div style="font-size:0.82rem;color:white;line-height:1.5;flex:1" id="homeScoreText">Chargement...</div>
        </div>"""

count = content.count(old_html)
if count != 1:
    print("ERREUR ETAPE 1: bloc HTML header trouve " + str(count) + " fois, attendu 1")
    raise SystemExit(1)
content = content.replace(old_html, new_html, 1)
print("OK etape 1: header HTML refait (avatar + carte texte)")

# ============================================================
# 2) JS : texte plus chaleureux et personnel pour homeScoreText
# ============================================================
old_js = """  if (yScore) {
    if (scoreEl) scoreEl.textContent = yScore.score + '/100';
    if (scoreText) scoreText.innerHTML = 'Votre score sante hier etait de <strong>' + yScore.score + '/100</strong>. ' + (yScore.score >= 70 ? 'Continuez sur cette lancee !' : 'Essayons de faire mieux aujourd hui !');
  } else {
    if (scoreEl) scoreEl.textContent = '--';
    if (scoreText) scoreText.textContent = 'Remplissez votre score de sante quotidien pour suivre votre progression.';
  }"""

new_js = """  var scoreIconEl = document.getElementById('homeScoreIcon');
  if (yScore) {
    if (scoreEl) scoreEl.textContent = yScore.score + '/100';
    var scoreMsg = yScore.score >= 70
      ? 'Hier, ton score etait de <strong>' + yScore.score + '/100</strong> \\u2014 belle energie ! Continue a t ecouter aujourd hui, chaque petit pas compte.'
      : 'Hier, ton score etait de <strong>' + yScore.score + '/100</strong>. Aujourd hui est une nouvelle occasion de prendre soin de toi, doucement mais surement.';
    if (scoreText) scoreText.innerHTML = scoreMsg;
    if (scoreIconEl) scoreIconEl.className = 'ti ' + (yScore.score >= 70 ? 'ti-flame' : 'ti-heart');
  } else {
    if (scoreEl) scoreEl.textContent = '--';
    if (scoreText) scoreText.textContent = 'Je suis la pour t accompagner aujourd hui' + (prenom ? ', ' + prenom : '') + '. Prends un instant pour remplir ton bilan sante du jour.';
    if (scoreIconEl) scoreIconEl.className = 'ti ti-sparkles';
  }"""

count = content.count(old_js)
if count != 1:
    print("ERREUR ETAPE 2: bloc JS score trouve " + str(count) + " fois, attendu 1")
    raise SystemExit(1)
content = content.replace(old_js, new_js, 1)
print("OK etape 2: texte du header rendu plus chaleureux/personnel")

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("TERMINE: header premium + texte chaleureux appliques")
