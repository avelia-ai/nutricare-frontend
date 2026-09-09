# -*- coding: utf-8 -*-
import sys

path = "app.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = [
    (
        "pushAdvice('pour ton rééquilibrage alimentaire, construis chaque assiette avec la règle moitié-quart-quart : moitié légumes, un quart protéines, un quart féculents complets, plus une source de bonnes graisses (huile d'olive, oléagineux)', 2);",
        "pushAdvice('pour ton rééquilibrage alimentaire, construis chaque assiette avec la règle moitié-quart-quart : moitié légumes, un quart protéines, un quart féculents complets, plus une source de bonnes graisses (huile d\\'olive, oléagineux)', 2);",
        1, "fix apostrophe huile d'olive (ligne ~3886)"
    ),
    (
        "pushAdvice('pour maintenir ton poids, garde 150 à 200 min d'activité modérée par semaine et pèse-toi une fois par semaine pour repérer toute dérive avant qu'elle ne s'installe', 1);",
        "pushAdvice('pour maintenir ton poids, garde 150 à 200 min d\\'activité modérée par semaine et pèse-toi une fois par semaine pour repérer toute dérive avant qu\\'elle ne s\\'installe', 1);",
        1, "fix apostrophes maintien (ligne ~3889)"
    ),
]

all_ok = True
for old, new, expected, label in fixes:
    actual = content.count(old)
    status = "OK" if actual == expected else "MISMATCH"
    if actual != expected:
        all_ok = False
    print("[" + status + "] " + label + ": attendu=" + str(expected) + " trouve=" + str(actual))

if not all_ok:
    print("")
    print("ABANDON: verifier manuellement.")
    sys.exit(1)

for old, new, expected, label in fixes:
    content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("")
print("OK: apostrophes corrigees.")
