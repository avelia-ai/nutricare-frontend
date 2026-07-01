with open("app.html", "r") as f:
    content = f.read()

old = '    <div id="iaMenusContent" style="display:block;padding:20px;display:flex;flex-direction:column;background:#FFFCFA">'
new = '    <div id="iaMenusContent" style="display:block;padding:20px;display:flex;flex-direction:column;">'

if old in content:
    content = content.replace(old, new, 1)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK - background retire de iaMenusContent")
else:
    print("ERREUR - pattern non trouve")
