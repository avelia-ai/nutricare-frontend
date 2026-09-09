import sys

with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'function renderActiviteTab() {'
func_code = 'function renderPredictionTab() {\n  var contentEl = document.getElementById(\'predictionContent\');\n  if (!contentEl) return;\n  contentEl.innerHTML = \'Analyse en cours...\';\n  var token = localStorage.getItem(\'nutricare_token\');\n  fetch(BACKEND_URL + \'/api/health/predict\', {\n    method: \'GET\',\n    headers: {\'Content-Type\':\'application/json\', \'Authorization\': \'Bearer \' + token}\n  }).then(function(r){return r.json();}).then(function(d){\n    if (d.error) {\n      contentEl.innerHTML = \'<div style="color:rgba(255,255,255,0.7)">Impossible de charger la prediction pour le moment.</div>\';\n      return;\n    }\n    if (!d.suffisant) {\n      var pct = Math.round((d.jours_disponibles / d.jours_requis) * 100);\n      contentEl.innerHTML =\n        \'<div style="margin-bottom:10px">\' + d.message + \'</div>\' +\n        \'<div style="background:rgba(255,255,255,0.1);border-radius:8px;height:6px;overflow:hidden;margin-bottom:6px">\' +\n          \'<div style="background:linear-gradient(90deg,#FF9A3C,#FF6B6B);height:100%;width:\' + Math.min(100,pct) + \'%"></div>\' +\n        \'</div>\' +\n        \'<div style="font-size:0.72rem;color:rgba(255,255,255,0.5)">\' + d.jours_disponibles + \' / \' + d.jours_requis + \' jours de suivi</div>\';\n      return;\n    }\n    var couleurs = { faible: \'#8FD9A8\', moderee: \'#FFC876\', elevee: \'#FF8F8F\' };\n    var couleur = couleurs[d.niveau_vigilance] || \'#FFC876\';\n    var tendancesHtml = (d.tendances_observees || []).map(function(t) {\n      return \'<li style="margin-bottom:4px">\' + t + \'</li>\';\n    }).join(\'\');\n    contentEl.innerHTML =\n      \'<div style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.08);border-radius:20px;padding:4px 12px;margin-bottom:12px">\' +\n        \'<span style="width:7px;height:7px;border-radius:50%;background:\' + couleur + \'"></span>\' +\n        \'<span style="font-size:0.72rem;font-weight:600;color:\' + couleur + \';text-transform:uppercase;letter-spacing:0.03em">Vigilance \' + d.niveau_vigilance + \'</span>\' +\n      \'</div>\' +\n      \'<div style="font-size:1rem;font-weight:700;color:#fff;margin-bottom:10px">\' + d.titre + \'</div>\' +\n      (tendancesHtml ? \'<ul style="margin:0 0 12px;padding-left:18px;font-size:0.8rem;color:rgba(255,255,255,0.75)">\' + tendancesHtml + \'</ul>\' : \'\') +\n      \'<div style="font-size:0.85rem;color:rgba(255,255,255,0.85);margin-bottom:14px;line-height:1.6">\' + d.prediction + \'</div>\' +\n      \'<div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:12px 14px;font-size:0.82rem;color:#fff;line-height:1.5">\' +\n        \'<i class="ti ti-bulb" style="margin-right:6px;color:#FFC876"></i>\' + d.conseil_principal +\n      \'</div>\';\n  }).catch(function(e){\n    console.error(e);\n    contentEl.innerHTML = \'<div style="color:rgba(255,255,255,0.7)">Erreur de connexion. Reessayez plus tard.</div>\';\n  });\n}\n'
new = func_code + '\nfunction renderActiviteTab() {'

count = content.count(old)
if count != 1:
    print(f'ERREUR: {count} occurrence(s) trouvee(s), attendu 1')
    sys.exit(1)
content = content.replace(old, new, 1)

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: fonction renderPredictionTab ajoutee')
