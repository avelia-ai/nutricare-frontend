# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = """  var _pcLastProfileForSummary = null;
  function renderPersonalSummary(profile) {
    _pcLastProfileForSummary = profile;"""
new1 = """  window._pcLastProfileForSummary = null;
  function renderPersonalSummary(profile) {
    window._pcLastProfileForSummary = profile;"""

count1 = content.count(old1)
print("Bloc 1 (declaration) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

old2 = """  if (typeof _pcLastProfileForSummary !== 'undefined' && _pcLastProfileForSummary) {
    renderPersonalSummary(_pcLastProfileForSummary);
  }"""
new2 = """  if (window._pcLastProfileForSummary) {
    renderPersonalSummary(window._pcLastProfileForSummary);
  }"""

count2 = content.count(old2)
print("Bloc 2 (usage dans refreshHarmonyAvatar) trouve " + str(count2) + " fois")
assert count2 == 1
content = content.replace(old2, new2)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: _pcLastProfileForSummary rendue globale (window.)")
