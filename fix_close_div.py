with open("app.html", "r") as f:
    content = f.read()

old = '        Generer mon menu IA\n      </button>\n    <div id="menusLoading"'
new = '        Generer mon menu IA\n      </button>\n    </div>\n    <div id="menusLoading"'

if old in content:
    content = content.replace(old, new, 1)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK - div fermeture ajoute")
else:
    print("ERREUR")
