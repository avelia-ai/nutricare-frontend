import sys

with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '  <div id="predictionCard" data-suivi-tab="prediction" style="display:none;background:linear-gradient(135deg,#1B1B2F,#232946);border-radius:20px;margin-bottom:16px;overflow:hidden;padding:22px;position:relative;box-shadow:0 0 0 1.5px rgba(255,154,108,0.22),0 16px 40px rgba(0,0,0,0.18)">\n    <div style="position:absolute;top:-40px;right:-30px;width:140px;height:140px;background:radial-gradient(circle,rgba(108,92,231,0.22),transparent 70%);pointer-events:none"></div>\n    <div style="position:relative">\n      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">\n        <div style="width:38px;height:38px;border-radius:12px;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;flex-shrink:0">\n          <i class="ti ti-telescope" style="font-size:19px;color:#fff"></i>\n        </div>\n        <div>\n          <div style="font-size:1.02rem;font-weight:700;color:#fff">Prédiction Mirella</div>\n          <div style="font-size:0.72rem;color:rgba(255,255,255,0.6)">Basée sur votre suivi récent</div>\n        </div>\n      </div>\n      <div id="predictionContent" style="font-size:0.85rem;color:rgba(255,255,255,0.85);line-height:1.6">\n        Analyse en cours...\n      </div>\n    </div>\n  </div>'
new = '  <div id="predictionCard" data-suivi-tab="prediction" style="display:none;background:#FFFCFA;border-radius:16px;margin-bottom:16px;overflow:hidden;box-shadow:0 0 0 1.5px rgba(255,154,108,0.22),0 14px 32px rgba(230,110,70,0.14)">\n    <div style="background:linear-gradient(135deg,#1B1B2F,#232946);padding:16px 20px 30px;position:relative;overflow:hidden">\n      <div style="position:absolute;top:-40px;right:-30px;width:160px;height:160px;background:radial-gradient(circle,rgba(108,92,231,0.25),transparent 70%);pointer-events:none"></div>\n      <div style="position:absolute;bottom:-60px;left:-20px;width:140px;height:140px;background:radial-gradient(circle,rgba(255,107,107,0.15),transparent 70%);pointer-events:none"></div>\n      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;position:relative">\n        <div>\n          <div style="font-size:0.7rem;color:rgba(255,255,255,0.6);font-weight:700;letter-spacing:0.04em;margin-bottom:4px">PREDICTION</div>\n          <div style="font-size:1.05rem;color:white;font-weight:700">Votre etat a venir</div>\n        </div>\n        <div style="width:56px;height:56px;border-radius:14px;overflow:hidden;flex-shrink:0;box-shadow:0 4px 10px rgba(0,0,0,0.2)">\n          <video autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;display:block">\n            <source src="https://www.mirella-ai.fr/renard_cardio.mp4" type="video/mp4">\n          </video>\n        </div>\n      </div>\n    </div>\n    <div style="padding:20px" id="predictionContent">\n      <div style="text-align:center;padding:30px 0;color:#888;font-size:0.85rem">Analyse en cours...</div>\n    </div>\n  </div>'

if old not in content:
    print('ERREUR: ancre introuvable')
    sys.exit(1)
content = content.replace(old, new, 1)

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: carte Prediction redessinee avec video')
