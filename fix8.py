# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Ligne 3639 (index 3638) doit contenir la fermeture de la fonction
target_idx = 3638
print("Ligne " + str(target_idx+1) + " avant modif: " + repr(lines[target_idx]))

if lines[target_idx].strip() != "}":
    print("ERREUR: la ligne 3639 n'est pas '}' comme attendu, contenu: " + repr(lines[target_idx]))
    raise SystemExit(1)

lines.insert(target_idx+1, "  window.renderPersonalSummary = renderPersonalSummary;\n")

with open('app.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("OK: window.renderPersonalSummary expose")
