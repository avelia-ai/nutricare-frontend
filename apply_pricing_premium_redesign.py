"""
apply_pricing_premium_redesign.py
Refonte de la vue abonnement (#pricingView) pour matcher la DA de l'app.
"""
PATH = "app.html"

with open(PATH, encoding="utf-8") as f:
    content = f.read()

START = "    <!-- PRICING VIEW -->"
END = "  <!-- PROFESSIONALS VIEW -->"

i = content.find(START)
j = content.find(END)
if i == -1 or j == -1:
    raise SystemExit("Marqueurs PRICING VIEW introuvables.")

NEW_BLOCK = r"""    <!-- PRICING VIEW -->
    <div id="pricingView">
      <div class="view-header" style="background:linear-gradient(135deg,#FF6B6B,#FF9A3C) !important;padding:16px 20px 18px !important;min-height:auto !important;justify-content:flex-start !important">
        <div style="font-size:2rem;font-weight:800;color:white;font-family:'Open Sans',sans-serif;line-height:1.2">Choisissez votre plan</div>
        <div style="font-size:0.85rem;color:rgba(255,255,255,0.85);margin-top:4px">Commencez gratuitement. Évoluez quand vous êtes prêt.</div>
      </div>
      <div style="padding:16px 16px 100px">

      <style>
        /* Eyebrow label, identique au pattern utilisé dans le reste de l'app (evo-eyebrow) */
        .p-eyebrow{display:flex;align-items:center;gap:7px;margin-bottom:2px}
        .p-eyebrow-bar{width:3px;height:14px;border-radius:2px;flex-shrink:0;background:linear-gradient(180deg,#FF6B6B,#FF9A3C)}
        .p-eyebrow-bar.gold{background:linear-gradient(180deg,#F0D28A,#C9A84C)}
        .p-eyebrow-bar.dim{background:rgba(255,255,255,0.25)}
        .p-eyebrow-text{font-size:10px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase}

        .ptoggle-wrap{display:flex;background:#FFFCFA;border:1px solid rgba(0,0,0,0.06);border-radius:30px;padding:4px;margin:0 auto 20px;width:fit-content;box-shadow:0 2px 10px rgba(0,0,0,0.03)}
        .ptbtn{padding:9px 20px;border-radius:26px;border:none;font-size:12px;font-weight:700;cursor:pointer;font-family:DM Sans,sans-serif;transition:all 0.2s;color:#9a9a9a;background:transparent}
        .ptbtn.pton{background:linear-gradient(135deg,#FF6B6B,#FF9A3C);color:white;box-shadow:0 6px 16px rgba(255,107,107,0.3)}
        .peco{font-size:9px;background:rgba(76,175,130,0.15);color:#2f9e63;padding:2px 6px;border-radius:8px;margin-left:5px;font-weight:800}
        .ptbtn.pton .peco{background:rgba(255,255,255,0.25);color:white}

        /* FREE — même carte crème que le reste de l'app */
        .card-free{background:#FFFCFA;border-radius:20px;border:1px solid rgba(255,154,108,0.14);padding:20px;box-shadow:0 3px 10px rgba(0,0,0,0.03),0 16px 32px -12px rgba(230,110,70,0.18);margin-bottom:12px}
        .cf-top{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:16px}
        .cf-price{font-size:1.7rem;font-weight:800;color:#1a1a1a;margin-top:6px;font-family:'Open Sans',sans-serif}
        .cf-price span{font-size:11px;font-weight:600;color:#b0a49c}
        .cf-feats{display:grid;grid-template-columns:1fr 1fr;gap:9px}
        .cf-feat{display:flex;align-items:center;gap:7px;font-size:11.5px;color:var(--charcoal,#2D2D2D);font-weight:600}
        .cf-feat-ico{width:22px;height:22px;border-radius:7px;display:flex;align-items:center;justify-content:center;background:rgba(255,107,107,0.1);flex-shrink:0}
        .cf-feat-ico i{font-size:12px;color:#FF6B6B}
        .cf-btn-free{padding:8px 16px;border-radius:20px;border:1.5px solid rgba(0,0,0,0.1);background:white;font-size:11.5px;font-weight:700;color:#8a8a8a;cursor:pointer;font-family:DM Sans,sans-serif;white-space:nowrap}

        /* STANDARD — carte sombre premium, ombres chaudes comme le reste de l'app */
        .card-std{background:#18181B;border-radius:22px;padding:22px;position:relative;overflow:hidden;box-shadow:0 3px 10px rgba(0,0,0,0.1),0 24px 48px -14px rgba(230,110,70,0.3);margin-bottom:12px;border:1px solid rgba(255,255,255,0.06)}
        .card-std::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#FF6B6B,#FF9A3C)}
        .cs-glow{position:absolute;top:-60px;right:-60px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(255,107,107,0.14) 0%,transparent 70%);pointer-events:none}
        .cs-glow2{position:absolute;bottom:-40px;left:-40px;width:140px;height:140px;border-radius:50%;background:radial-gradient(circle,rgba(255,154,60,0.08) 0%,transparent 70%);pointer-events:none}
        .cs-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
        .cs-popular{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:700;color:#FF9A3C;background:rgba(255,154,60,0.14);padding:4px 10px;border-radius:20px}
        .cs-price-row{display:flex;align-items:baseline;gap:10px;margin-bottom:2px}
        .cs-price{font-size:2.7rem;font-weight:800;color:white;line-height:1;letter-spacing:-0.02em;font-family:'Open Sans',sans-serif}
        .cs-old{font-size:13px;text-decoration:line-through;color:rgba(255,255,255,0.25)}
        .cs-period{font-size:11px;color:rgba(255,255,255,0.4);margin-bottom:4px}
        .cs-perday{display:inline-flex;align-items:center;gap:5px;background:rgba(74,222,128,0.1);border-radius:8px;padding:5px 10px;font-size:11px;color:rgba(255,255,255,0.55);margin-top:14px;margin-bottom:18px}
        .cs-feats{display:flex;flex-direction:column;gap:10px;margin-bottom:20px}
        .cs-feat{display:flex;align-items:center;gap:10px}
        .cs-feat-ico{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(255,107,107,0.12);flex-shrink:0}
        .cs-feat-ico i{font-size:13px;color:#FF9A3C}
        .cs-feat-txt{font-size:12px;color:rgba(255,255,255,0.8);font-weight:500}
        .cs-cta{width:100%;padding:14px;border-radius:14px;border:none;font-size:14px;font-weight:800;cursor:pointer;font-family:DM Sans,sans-serif;background:white;color:#18181B;letter-spacing:0.01em;display:flex;align-items:center;justify-content:center;gap:6px}

        /* PREMIUM — carte haut de gamme, dégradé corail/or, effet shimmer sur la bordure */
        .card-prm{border-radius:22px;padding:22px;position:relative;overflow:hidden;background:linear-gradient(150deg,#FF5A5A 0%,#FF6B6B 45%,#FF9A3C 100%);box-shadow:0 3px 10px rgba(0,0,0,0.08),0 26px 54px -12px rgba(230,110,70,0.45);margin-bottom:12px}
        .card-prm::before{content:'';position:absolute;inset:0;border-radius:22px;padding:1.5px;background:linear-gradient(120deg,rgba(240,210,138,0.95),rgba(255,255,255,0.15) 30%,rgba(240,210,138,0.6) 60%,rgba(255,255,255,0.1));background-size:220% 220%;-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;animation:cpBorderFlow 5s ease infinite}
        @keyframes cpBorderFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
        .cp-maxsave{display:none;align-items:center;gap:5px;font-size:10px;font-weight:800;color:#5C4310;background:linear-gradient(135deg,#FFE9B8,#F0D28A);padding:4px 10px;border-radius:20px;margin-left:6px;box-shadow:0 3px 8px rgba(201,168,76,0.35)}
        .cp-maxsave.show{display:inline-flex}
        .cp-shine{position:absolute;top:-30px;right:-30px;width:160px;height:160px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.18) 0%,transparent 65%);pointer-events:none}
        .cp-shine2{position:absolute;bottom:-50px;left:20px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.06) 0%,transparent 65%);pointer-events:none}
        .cp-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px}
        .cp-best{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:800;color:#7A5A1A;background:linear-gradient(135deg,#FFE9B8,#F0D28A);padding:4px 10px;border-radius:20px;box-shadow:0 3px 8px rgba(201,168,76,0.35)}
        .cp-price{font-size:2.7rem;font-weight:800;color:white;line-height:1;letter-spacing:-0.02em;font-family:'Open Sans',sans-serif}
        .cp-old{font-size:13px;text-decoration:line-through;color:rgba(255,255,255,0.4)}
        .cp-period{font-size:11px;color:rgba(255,255,255,0.65);margin-bottom:4px}
        .cp-perday{display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,0.15);border-radius:8px;padding:5px 10px;font-size:11px;color:rgba(255,255,255,0.75);margin-top:14px;margin-bottom:18px}
        .cp-feats{display:flex;flex-direction:column;gap:10px;margin-bottom:20px}
        .cp-feat{display:flex;align-items:center;gap:10px}
        .cp-feat-ico{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,0.2);flex-shrink:0}
        .cp-feat-ico i{font-size:13px;color:white}
        .cp-feat-txt{font-size:12px;color:rgba(255,255,255,0.92);font-weight:500}
        .cp-cta{width:100%;padding:14px;border-radius:14px;border:none;font-size:14px;font-weight:800;cursor:pointer;font-family:DM Sans,sans-serif;background:linear-gradient(135deg,#FFE9B8,#F0D28A);color:#5C4310;letter-spacing:0.01em;display:flex;align-items:center;justify-content:center;gap:6px;box-shadow:0 10px 26px rgba(201,168,76,0.4)}

        .pfooter{text-align:center;margin-top:16px;font-size:11px;color:#b0a49c;display:flex;align-items:center;justify-content:center;gap:6px}
      </style>

      <div style="text-align:center;margin-bottom:16px">
        <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,107,107,0.08);border-radius:20px;padding:6px 14px">
          <i class="ti ti-info-circle" style="font-size:13px;color:#FF6B6B"></i>
          <span style="font-size:11px;font-weight:600;color:#FF6B6B">Économisez 50% avec l'abonnement annuel</span>
        </div>
      </div>
      <div class="ptoggle-wrap">
        <button id="toggleMonthly" class="ptbtn pton" onclick="window.setPricingPeriod('monthly')">Mensuel</button>
        <button id="toggleAnnual" class="ptbtn" onclick="window.setPricingPeriod('annual')">Annuel <span class="peco">-50%</span></button>
      </div>

      <!-- FREE -->
      <div class="card-free">
        <div class="cf-top">
          <div>
            <div class="p-eyebrow"><div class="p-eyebrow-bar" style="background:#d8cfc8"></div><div class="p-eyebrow-text" style="color:#b0a49c">Gratuit · Essentiel</div></div>
            <div class="cf-price">0€ <span>/ toujours</span></div>
          </div>
          <div class="current-plan-tag" id="freePlanTag" style="display:none">Plan actuel</div>
          <button class="cf-btn-free" id="freePlanBtn" onclick="selectPlan('free')">Plan actuel</button>
        </div>
        <div class="cf-feats">
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-message-circle"></i></div>5 messages/jour</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-heart-rate-monitor"></i></div>Suivi santé</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-book"></i></div>30 recettes offertes</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-stethoscope"></i></div>Pathologies</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-trophy"></i></div>Programmes</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-shield-check"></i></div>Sécurité médicale</div>
        </div>
      </div>

      <!-- STANDARD -->
      <div class="card-std">
        <div class="cs-glow"></div>
        <div class="cs-glow2"></div>
        <div class="cs-top">
          <div class="p-eyebrow"><div class="p-eyebrow-bar dim"></div><div class="p-eyebrow-text" style="color:rgba(255,255,255,0.4)">Standard · Complet</div></div>
          <div class="cs-popular"><i class="ti ti-flame" style="font-size:11px"></i> Le plus populaire</div>
        </div>
        <div class="cs-price-row">
          <div class="cs-price" id="standardPrice">2,99€</div>
          <div class="cs-old" id="standardOldPrice">5,99€</div>
        </div>
        <div class="cs-period" id="standardPeriod">/ mois · <b style="color:#4ade80">-50% de réduction</b></div>
        <div class="cs-perday" id="standardPerDay"><i class="ti ti-sun" style="font-size:12px"></i>soit seulement <b style="color:#4ade80;font-size:13px">0,09€</b> / jour</div>
        <div class="cs-feats">
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-message-circle"></i></div><span class="cs-feat-txt">Chat IA illimité</span></div>
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-salad"></i></div><span class="cs-feat-txt">Plans nutritionnels personnalisés</span></div>
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-chart-line"></i></div><span class="cs-feat-txt">Dashboard santé complet</span></div>
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-calendar-week"></i></div><span class="cs-feat-txt">Menus hebdomadaires IA</span></div>
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-book-2"></i></div><span class="cs-feat-txt">Catalogue 7 000+ recettes</span></div>
          <div class="cs-feat"><div class="cs-feat-ico"><i class="ti ti-bulb"></i></div><span class="cs-feat-txt">Nudges & protocoles pathologies</span></div>
        </div>
        <div id="standardDiscount" style="display:none;justify-content:center" ></div>
        <button class="cs-cta" id="standardPlanBtn" onclick="selectPlan(window._pricingPeriod==='annual'?'standard_annual':'standard')"><i class="ti ti-arrow-right" style="font-size:15px"></i>Choisir Standard</button>
      </div>

      <!-- PREMIUM -->
      <div class="card-prm">
        <div class="cp-shine"></div>
        <div class="cp-shine2"></div>
        <div class="cp-top">
          <div class="p-eyebrow"><div class="p-eyebrow-bar gold"></div><div class="p-eyebrow-text" style="color:rgba(255,255,255,0.75)">Premium · Excellence</div></div>
          <div style="display:flex;align-items:center">
            <div class="cp-best"><i class="ti ti-crown" style="font-size:11px"></i> Meilleure offre</div>
            <div class="cp-maxsave" id="premiumMaxSave"><i class="ti ti-bolt" style="font-size:11px"></i> Économie max</div>
          </div>
        </div>
        <div class="cs-price-row">
          <div class="cp-price" id="premiumPrice">4,99€</div>
          <div class="cp-old" id="premiumOldPrice">9,99€</div>
        </div>
        <div class="cp-period" id="premiumPeriod">/ mois · <b style="color:white">-50% de réduction</b></div>
        <div class="cp-perday" id="premiumPerDay"><i class="ti ti-sun" style="font-size:12px"></i>soit seulement <b style="color:white;font-size:13px">0,16€</b> / jour</div>
        <div class="cp-feats">
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-checks"></i></div><span class="cp-feat-txt">Tout du plan Standard</span></div>
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-camera"></i></div><span class="cp-feat-txt">Analyse photo repas par IA</span></div>
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-stethoscope"></i></div><span class="cp-feat-txt">Intégration professionnels santé</span></div>
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-brain"></i></div><span class="cp-feat-txt">Mémoire long terme Mirella</span></div>
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-mood-happy"></i></div><span class="cp-feat-txt">Coaching comportemental</span></div>
          <div class="cp-feat"><div class="cp-feat-ico"><i class="ti ti-star"></i></div><span class="cp-feat-txt">Programmes & contenus exclusifs</span></div>
        </div>
        <div id="premiumDiscount" style="display:none;justify-content:center"></div>
        <button class="cp-cta" id="premiumPlanBtn" onclick="selectPlan(window._pricingPeriod==='annual'?'premium_annual':'premium')"><i class="ti ti-crown" style="font-size:15px"></i>Choisir Premium</button>
      </div>

      <div class="pfooter">
        <i class="ti ti-lock" style="font-size:12px"></i>
        Paiement sécurisé · Sans engagement · Remboursé 30 jours
      </div>
    </div>
    </div>

"""

content = content[:i] + NEW_BLOCK + content[j:]

old_js = """  if (tm) { tm.style.background = isAnnual ? 'transparent' : 'white'; tm.style.color = isAnnual ? 'white' : '#2D2D2D'; }
  if (ta) { ta.style.background = isAnnual ? 'white' : 'transparent'; ta.style.color = isAnnual ? '#2D2D2D' : 'white'; }"""
new_js = """  if (tm) { tm.classList.toggle('pton', !isAnnual); tm.style.background = ''; tm.style.color = ''; }
  if (ta) { ta.classList.toggle('pton', isAnnual); ta.style.background = ''; ta.style.color = ''; }
  var pms = document.getElementById('premiumMaxSave');
  if (pms) pms.classList.toggle('show', isAnnual);"""

if old_js in content:
    content = content.replace(old_js, new_js)
else:
    print("Attention: bloc JS du toggle non trouve tel quel - peut-etre deja patche.")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("OK - vue abonnement redessinee dans app.html")
