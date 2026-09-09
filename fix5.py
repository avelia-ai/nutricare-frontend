# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = """function getHealthGoalTips(log) {
  var norm = normalizeHealthLog(log);
  var pillars = [
    {val: norm.sleep, icon: "\U0001F634", tip: "Dors au moins 8h"},
    {val: norm.hydra, icon: "\U0001F4A7", tip: "Bois au moins 2L d'eau"},
    {val: norm.activ, icon: "\U0001F3C3", tip: "Bouge au moins 30 min"},
    {val: norm.calm, icon: "\U0001F9D8", tip: "Prends un moment pour te detendre"}
  ];
  pillars.sort(function(a,b) { return a.val - b.val; });
  return pillars.slice(0,2).filter(function(p) { return p.val < 0.8; });
}"""

new1 = """function getHealthGoalTips(log) {
  var norm = normalizeHealthLog(log);
  var energyNorm = (log && log.energy_level != null) ? Math.min(log.energy_level / 10, 1) : null;
  var pillars = [
    {val: norm.sleep, icon: "ti-moon", tip: "Vise au moins 8h de sommeil ce soir"},
    {val: norm.hydra, icon: "ti-droplet", tip: "Bois encore un peu d'eau, objectif 2L"},
    {val: norm.activ, icon: "ti-walk", tip: "Ajoute 30 min de marche ou de sport"},
    {val: norm.calm, icon: "ti-yoga", tip: "Accorde-toi un moment de detente ou de respiration"}
  ];
  if (energyNorm !== null) pillars.push({val: energyNorm, icon: "ti-bolt", tip: "Prends soin de ton energie : petite pause ou collation saine"});
  if (log && log.stress_level != null && log.stress_level >= 7) pillars.push({val: 0.1, icon: "ti-brain", tip: "Ton stress est eleve : essaie une seance de coherence cardiaque"});
  if (log && log.blood_pressure_sys && log.blood_pressure_sys >= 140) pillars.push({val: 0.1, icon: "ti-heart-rate-monitor", tip: "Ta tension est un peu haute, pense a en parler a ton medecin"});
  pillars.sort(function(a,b) { return a.val - b.val; });
  return pillars.slice(0,4).filter(function(p) { return p.val < 0.8; });
}"""

count1 = content.count(old1)
print("Bloc 1 (tips) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

old2 = """          goalChipsEl.innerHTML = tips.map(function(t) {
            return '<div style="display:flex;align-items:center;gap:6px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:7px 13px;font-size:0.78rem;color:#F5E6D8;font-weight:600"><span style="font-size:0.95rem">' + t.icon + '</span>' + t.tip + '</div>';
          }).join('');"""

new2 = """          goalChipsEl.innerHTML = tips.map(function(t) {
            return '<div style="display:flex;align-items:center;gap:7px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.12);border-radius:20px;padding:8px 14px;font-size:0.78rem;color:#F5E6D8;font-weight:600"><i class="ti ' + t.icon + '" style="font-size:14px;color:#FFD166"></i>' + t.tip + '</div>';
          }).join('');"""

count2 = content.count(old2)
print("Bloc 2 (rendu chips) trouve " + str(count2) + " fois")
assert count2 == 1
content = content.replace(old2, new2)

old3 = """          goalChipsEl.innerHTML = '<div style="display:flex;align-items:center;gap:6px;background:rgba(139,226,139,0.12);border:1px solid rgba(139,226,139,0.3);border-radius:20px;padding:7px 13px;font-size:0.78rem;color:#8BE28B;font-weight:600">\U0001F31F Continue comme ca, tu es sur la bonne voie !</div>';"""

new3 = """          goalChipsEl.innerHTML = '<div style="display:flex;align-items:center;gap:7px;background:rgba(139,226,139,0.12);border:1px solid rgba(139,226,139,0.3);border-radius:20px;padding:8px 14px;font-size:0.78rem;color:#8BE28B;font-weight:600"><i class="ti ti-sparkles" style="font-size:14px"></i>Continue comme ca, tu es sur la bonne voie !</div>';"""

count3 = content.count(old3)
print("Bloc 3 (message positif) trouve " + str(count3) + " fois")
assert count3 == 1
content = content.replace(old3, new3)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: conseils enrichis avec icones premium")
