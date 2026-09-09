import sys

path = "app.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''  <div id="rituelsBienEtreCard" data-suivi-tab="rituels" style="display:none;background:#FFFCFA;border-radius:16px;margin-bottom:16px;overflow:hidden;box-shadow:0 0 0 1.5px rgba(255,154,108,0.22),0 14px 32px rgba(230,110,70,0.14)">
    <div style="background:linear-gradient(135deg,#6C9F70,#A8D8A8);padding:16px 20px 30px">
      <div style="font-size:0.7rem;color:rgba(255,255,255,0.85);font-weight:700;letter-spacing:0.04em;margin-bottom:4px">RITUELS</div>
      <div style="display:flex;align-items:center;justify-content:space-between">
        <div style="font-size:1.05rem;color:white;font-weight:700">Rituels bien-\u00eatre</div>
        <div style="font-size:0.72rem;color:rgba(255,255,255,0.9);font-weight:700;background:rgba(255,255,255,0.18);padding:4px 10px;border-radius:20px">+pts Harmonie</div>
      </div>
    </div>'''

new = '''  <div id="rituelsBienEtreCard" data-suivi-tab="rituels" style="display:none;background:#FFFCFA;border-radius:16px;margin-bottom:16px;overflow:hidden;box-shadow:0 0 0 1.5px rgba(255,154,108,0.22),0 14px 32px rgba(230,110,70,0.14)">
    <div style="background:linear-gradient(135deg,#6C9F70,#A8D8A8);padding:16px 20px 30px;position:relative;overflow:hidden">
      <div style="font-size:0.7rem;color:rgba(255,255,255,0.85);font-weight:700;letter-spacing:0.04em;margin-bottom:4px">RITUELS</div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px">
        <div style="flex:1;min-width:0">
          <div style="font-size:1.05rem;color:white;font-weight:700;margin-bottom:6px">Rituels bien-\u00eatre</div>
          <div style="font-size:0.72rem;color:rgba(255,255,255,0.9);font-weight:700;background:rgba(255,255,255,0.18);padding:4px 10px;border-radius:20px;display:inline-block">+pts Harmonie</div>
        </div>
        <div style="width:56px;height:56px;border-radius:14px;overflow:hidden;flex-shrink:0;box-shadow:0 4px 10px rgba(0,0,0,0.2)">
          <video autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;display:block">
            <source src="https://raw.githubusercontent.com/avelia-ai/nutricare-frontend/main/renard_rituels_compressed.mp4" type="video/mp4">
          </video>
        </div>
      </div>
    </div>'''

count = content.count(old)
print("Occurrences trouvees:", count)
if count != 1:
    print("ABANDON: pas exactement 1 occurrence, verifier le fichier manuellement")
    sys.exit(1)

content = content.replace(old, new)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("OK, remplacement effectue")
