with open("app.html", "r") as f:
    content = f.read()

debut = 350343
fin = 354921

new_content = content[:debut] + content[fin:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - {fin-debut} chars supprimes, taille avant:{len(content)} apres:{len(new_content)}")
