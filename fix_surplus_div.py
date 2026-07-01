with open("app.html", "r") as f:
    lines = f.readlines()

# Supprimer lignes 4917 et 4918 (index 4916 et 4917)
print(f"Ligne 4917: {repr(lines[4916])}")
print(f"Ligne 4918: {repr(lines[4917])}")

del lines[4916:4918]

with open("app.html", "w") as f:
    f.writelines(lines)
print("OK - 2 div parasites supprimes")
