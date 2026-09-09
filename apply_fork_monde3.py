import sys

with open('/workspaces/nutricare-frontend/app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = '      if (_forkLabelAEl && _forkLabelBEl) {\n        if (mondeIdx === 0) {\n          _forkLabelAEl.textContent = "Foret de l\'Energie";\n          _forkLabelBEl.textContent = \'Montagne de la Force\';\n        } else {\n          _forkLabelAEl.textContent = \'Lac Cristallin\';\n          _forkLabelBEl.textContent = \'Territoire Zen\';\n        }\n      }'
new1 = '      if (_forkLabelAEl && _forkLabelBEl) {\n        if (mondeIdx === 0) {\n          _forkLabelAEl.textContent = "Foret de l\'Energie";\n          _forkLabelBEl.textContent = \'Montagne de la Force\';\n        } else if (mondeIdx === 1) {\n          _forkLabelAEl.textContent = \'Lac Cristallin\';\n          _forkLabelBEl.textContent = \'Territoire Zen\';\n        } else {\n          _forkLabelAEl.textContent = \'Plaine de Plenitude\';\n          _forkLabelBEl.textContent = \'Royaume de la Vitalite\';\n        }\n      }'
if old1 not in content:
    print('ERREUR: ancre 1 introuvable')
    sys.exit(1)
content = content.replace(old1, new1, 1)

old2 = "    fork: function(m) { return PC_VIDEO_BASE + 'pc_fork_arrival_monde' + m + '.mp4'; },"
new2 = "    fork: function(m) { return m === 3 ? (PC_VIDEO_BASE + 'bifurcation_monde3_compressed.mp4') : (PC_VIDEO_BASE + 'pc_fork_arrival_monde' + m + '.mp4'); },"
if old2 not in content:
    print('ERREUR: ancre 2 introuvable')
    sys.exit(1)
content = content.replace(old2, new2, 1)

with open('/workspaces/nutricare-frontend/app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: bifurcation du monde 3 ajoutee (libelles + video dediee)')
