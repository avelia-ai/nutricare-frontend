import anthropic, json, urllib.request, time, sys

KEY_A = "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"
KEY_S = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNtZ2J5Yml3dXVjaWNnbWxjam9oIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NjA0NTg3OSwiZXhwIjoyMDkxNjIxODc5fQ.Vn5cF-iPJVrBGWexGnA9_CZQq94E38xD83nh0HtAmRU"
URL_S = "https://smgbybiwuucicgmlcjoh.supabase.co"

client = anthropic.Anthropic(api_key=KEY_A)

def insert(recs):
    data = json.dumps(recs).encode()
    req = urllib.request.Request(URL_S+"/rest/v1/recettes", data=data,
        headers={"apikey":KEY_S,"Authorization":"Bearer "+KEY_S,"Content-Type":"application/json","Prefer":"return=minimal"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as r: return r.status < 400
    except Exception as e: print("Insert err:"+str(e)[:80]); return False

combos = []
for cat in ["petit_dejeuner","dejeuner","diner","snack","dessert"]:
    for theme in ["poulet","saumon","lentilles","quinoa","tofu","oeufs","patate douce","pois chiches","brocoli","epinards","avocat","courgettes","aubergines","champignons","haricots","sardines","thon","crevettes","boeuf","dinde"]:
        for regime in ["standard","vegetarien","vegan","sans_gluten","anti_inflammatoire","mediterraneen"]:
            combos.append((cat,theme,regime))

total=0; target=3340; errors=0
print("Start: "+str(len(combos))+" combos", flush=True)

for i,(cat,theme,regime) in enumerate(combos):
    if total>=target: break
    try:
        msg = client.messages.create(model="claude-haiku-4-5-20251001", max_tokens=3000,
            messages=[{"role":"user","content":
                "Genere 3 recettes "+cat+" a base de "+theme+" regime "+regime+". "+
                "JSON tableau 3 objets sans texte ni markdown. Champs exacts: "+
                "nom(string), categorie(""+cat+""), calories(int), prep_minutes(int), portions(int 2-4), "+
                "ingredients(array strings), etapes(array 3-4 strings courtes), tags(array strings incluant ""+regime+""), "+
                "pathologies(array strings ex ["sante_generale"]), proteines(int), glucides(int), lipides(int), "+
                "photo_keyword(string), cuisine(string ex francaise), difficulte(string facile/moyen/difficile), cout_estime(float)"
            }])
        text = msg.content[0].text.strip()
        s=text.find("["); e=text.rfind("]")+1
        if s>=0 and e>s:
            recs = json.loads(text[s:e])
            if isinstance(recs,list) and len(recs)>0 and insert(recs):
                total+=len(recs)
                print("OK "+str(i+1)+": +"+str(len(recs))+" total="+str(total)+"/"+str(target), flush=True)
        time.sleep(0.5)
    except Exception as ex:
        errors+=1
        print("ERR: "+str(ex)[:60], flush=True)
        time.sleep(1)

print("Termine: +"+str(total)+" recettes "+str(errors)+" erreurs", flush=True)
