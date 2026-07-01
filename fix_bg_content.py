with open("app.html", "r") as f:
    content = f.read()

old = '<div id="iaMenusContent" style="display:block;padding:18px;display:flex;flex-direction:column;gap:14px">'
new = '<div id="iaMenusContent" style="display:block;padding:18px;display:flex;flex-direction:column;gap:14px;background:transparent">'

if old in content:
    content = content.replace(old, new, 1)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK")
else:
    # Chercher le vrai style actuel
    import re
    match = re.search(r'<div id="iaMenusContent" style="([^"]*)">', content)
    if match:
        print(f"Style actuel: {match.group(1)}")
    else:
        print("ERREUR: non trouve")
