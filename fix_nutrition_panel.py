with open("app.html", "r") as f:
    content = f.read()

old = '        </div>\n        <div style="display:flex;flex-direction:column;align-items:center;gap:14px">'
new = '        </div>\n      </div>\n      <div style="padding:18px 20px;background:white">\n        <div style="display:flex;flex-direction:column;align-items:center;gap:14px">'

if old in content and content.count(old) == 1:
    # Adapter les couleurs de la jauge et metriques pour fond blanc
    result = content.replace(old, new, 1)
    # Donut texte : blanc -> noir
    result = result.replace(
        '<div id="donutCalories" style="font-size:20px;font-weight:900;color:white;line-height:1">',
        '<div id="donutCalories" style="font-size:20px;font-weight:900;color:#2D2D2D;line-height:1">'
    )
    result = result.replace(
        '<div id="donutLabel" style="font-size:9px;font-weight:600;color:rgba(255,255,255,0.6)">',
        '<div id="donutLabel" style="font-size:9px;font-weight:600;color:#999">'
    )
    result = result.replace(
        '<div style="font-size:9px;color:rgba(255,255,255,0.5);margin-top:2px">kcal</div>',
        '<div style="font-size:9px;color:#999;margin-top:2px">kcal</div>'
    )
    # Cartes metriques : fond sombre -> fond clair
    result = result.replace(
        'background:rgba(255,255,255,0.08);border-radius:10px;padding:8px 10px',
        'background:#f8f4f0;border-radius:10px;padding:8px 10px'
    )
    result = result.replace(
        'color:rgba(255,255,255,0.4);text-transform:uppercase;letter-spacing:.5px;margin-bottom:2px',
        'color:#999;text-transform:uppercase;letter-spacing:.5px;margin-bottom:2px'
    )
    result = result.replace(
        '<div id="donutObjectif" style="font-size:12px;font-weight:700;color:white">',
        '<div id="donutObjectif" style="font-size:12px;font-weight:700;color:#2D2D2D">'
    )
    result = result.replace(
        '<div id="donutDepensees" style="font-size:12px;font-weight:700;color:white">',
        '<div id="donutDepensees" style="font-size:12px;font-weight:700;color:#2D2D2D">'
    )
    with open("app.html", "w") as f:
        f.write(result)
    print("OK - jauge et metriques sur fond blanc")
else:
    print("ERREUR - count=" + str(content.count(old)))
