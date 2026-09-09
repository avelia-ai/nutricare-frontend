# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = """              <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
                <div style="width:32px;height:32px;border-radius:10px;background:linear-gradient(135deg,#FFB347,#FF6B6B);display:flex;align-items:center;justify-content:center;flex-shrink:0">
                  <i class="ti ti-bulb" style="font-size:16px;color:#fff"></i>
                </div>
                <div style="font-size:0.72rem;font-weight:700;color:#D4730A;text-transform:uppercase;letter-spacing:0.04em">Conseils de Mirella</div>
              </div>"""

new1 = """              <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
                <div style="width:38px;height:38px;border-radius:11px;overflow:hidden;flex-shrink:0;box-shadow:0 4px 10px rgba(255,107,107,0.25)">
                  <video autoplay muted loop playsinline style="width:100%;height:100%;object-fit:cover;display:block">
                    <source src="https://raw.githubusercontent.com/avelia-ai/nutricare-frontend/main/renard_conseils_compressed.mp4" type="video/mp4">
                  </video>
                </div>
                <div style="font-size:0.72rem;font-weight:700;color:#D4730A;text-transform:uppercase;letter-spacing:0.04em">Conseils de Mirella</div>
              </div>"""

count1 = content.count(old1)
print("Bloc 1 (video renard conseils) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: video renard integree dans le bloc Conseils de Mirella")
