with open("app.html", "r") as f:
    content = f.read()

# Etat actuel : ...filtres</div>\n    </div>\n      <button...>Generer</button>\n    <div menusLoading>
# Etat voulu  : ...filtres</div>\n      <button...>Generer</button>\n    </div>\n    <div menusLoading>

ancien = '        </select>\n      </div>\n    </div>\n      <button onclick="generateMenu()" id="generateMenuBtn" style="background:linear-gradient(135deg,#FF6B6B,#FF9A3C);color:white;padding:14px;border:none;border-radius:14px;font-size:0.88rem;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;gap:8px;white-space:nowrap;font-weight:700;width:100%;justify-content:center;margin-bottom:14px;margin-top:14px">\n        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>\n        Generer mon menu IA\n      </button>\n    <div id="menusLoading"'

nouveau = '        </select>\n      </div>\n      <button onclick="generateMenu()" id="generateMenuBtn" style="background:linear-gradient(135deg,#FF6B6B,#FF9A3C);color:white;padding:14px;border:none;border-radius:14px;font-size:0.88rem;cursor:pointer;font-family:DM Sans,sans-serif;display:flex;align-items:center;gap:8px;white-space:nowrap;font-weight:700;width:100%;justify-content:center;margin-bottom:14px;margin-top:14px">\n        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>\n        Generer mon menu IA\n      </button>\n    </div>\n    <div id="menusLoading"'

if ancien in content:
    new_content = content.replace(ancien, nouveau, 1)
    with open("app.html", "w") as f:
        f.write(new_content)
    print("OK - structure corrigee")
else:
    print("ERREUR - pattern non trouve")
    print("Verification: select fin present:", '        </select>' in content)
    print("Verification: bouton present:", 'id="generateMenuBtn"' in content)
