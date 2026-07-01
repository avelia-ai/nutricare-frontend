with open("app.html", "r") as f:
    content = f.read()

old = '#appPage, #dashboardView, #profileView, #chatView, #pricingView, #proView, #protocolsView { background: transparent !important; }'
new = '#appPage, #dashboardView, #profileView, #chatView, #pricingView, #proView, #protocolsView, #menusView { background: transparent !important; }'

if old in content:
    content = content.replace(old, new, 1)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK - menusView ajoute a la regle transparent")
else:
    print("ERREUR")
