import sys

path = "app.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Fix 1: bouton croix (ferme la modal) ---
old1 = '''<button onclick="document.getElementById('editGoalsModal').style.display='none';var n=document.getElementById('bottomNav');if(n){n.style.zIndex='1000';n.style.visibility='visible';}" style="background:#f5f5f5;border:none;border-radius:50%;width:32px;height:32px;cursor:pointer;font-size:0.9rem;color:#999">&#10005;</button>'''

new1 = '''<button onclick="document.getElementById('editGoalsModal').style.display='none';var n=document.getElementById('bottomNav');if(n){n.style.display='block';n.style.zIndex='1000';n.style.visibility='visible';}" style="background:#f5f5f5;border:none;border-radius:50%;width:32px;height:32px;cursor:pointer;font-size:0.9rem;color:#999">&#10005;</button>'''

# --- Fix 2: saveEditGoals (bouton Enregistrer) ---
old2 = '''    document.getElementById('editGoalsModal').style.display = 'none';
    var nav2 = document.getElementById('bottomNav');
    if (nav2) { nav2.style.zIndex = '1000'; nav2.style.visibility = 'visible'; }'''

new2 = '''    document.getElementById('editGoalsModal').style.display = 'none';
    var nav2 = document.getElementById('bottomNav');
    if (nav2) { nav2.style.display = 'block'; nav2.style.zIndex = '1000'; nav2.style.visibility = 'visible'; }'''

c1 = content.count(old1)
c2 = content.count(old2)
print("Fix1 (bouton croix) occurrences:", c1)
print("Fix2 (saveEditGoals) occurrences:", c2)

if c1 != 1 or c2 != 1:
    print("ABANDON: verifier manuellement, pas exactement 1 occurrence pour chaque fix")
    sys.exit(1)

content = content.replace(old1, new1)
content = content.replace(old2, new2)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("OK, les deux corrections ont ete appliquees")
