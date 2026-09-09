# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = """        <div style="font-size:0.85rem;color:white;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,0.4)">Suivez vos indicateurs chaque jour pour progresser vers vos objectifs \U0001F4AA</div>"""
new1 = """        <div style="font-size:0.85rem;color:white;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,0.4);display:flex;align-items:center;gap:8px">Suivez vos indicateurs chaque jour pour progresser vers vos objectifs<i class="ti ti-trending-up" style="font-size:18px;color:#FFD166"></i></div>"""

count1 = content.count(old1)
print("Bloc 1 (banniere emoji) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

old2 = """    <div id="healthScoreGoalWrap" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.08);position:relative;z-index:1">"""
new2 = """    <div id="healthScoreGoalWrap" style="display:none;margin-top:24px;padding-top:20px;border-top:1px solid rgba(255,255,255,0.08);position:relative;z-index:1">"""

count2 = content.count(old2)
print("Bloc 2 (espacement) trouve " + str(count2) + " fois")
assert count2 == 1
content = content.replace(old2, new2)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: banniere et espacement corriges")
