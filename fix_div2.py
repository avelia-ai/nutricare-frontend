with open("app.html", "r") as f:
    content = f.read()

pos = content.find('    <div id="menusLoading"')
print(f"Position menusLoading: {pos}")
print(f"10 chars avant: {repr(content[pos-10:pos])}")

new_content = content[:pos] + '    </div>\n' + content[pos:]
with open("app.html", "w") as f:
    f.write(new_content)
print("OK - div fermeture insere")
