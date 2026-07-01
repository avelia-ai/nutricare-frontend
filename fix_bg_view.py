with open("app.html", "r") as f:
    content = f.read()

old = '<div id="menusView" style="display:none;padding:8px 32px 32px 32px;padding-bottom:120px;overflow-y:auto;background:var(--cream);width:100%">'
new = '<div id="menusView" style="display:none;padding:8px 16px 32px 16px;padding-bottom:120px;overflow-y:auto;background:transparent;width:100%">'

if old in content:
    content = content.replace(old, new, 1)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK - fond transparent")
else:
    print("ERREUR")
