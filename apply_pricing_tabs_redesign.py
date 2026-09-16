"""
apply_pricing_tabs_redesign.py
Refonte v2 de la vue abonnement (#pricingView) : selecteur a onglets +
carte hero par palier, typo editoriale (Fraunces) sur les prix, carte
Premium en degrade cuivre/or avec liseré anime + renard mascotte,
bandeau promo annuel, badge parrainage, et sheet de comparaison des 3 offres.
Tous les id existants (standardPrice, standardDiscount, freePlanBtn, etc.)
et toute la logique JS deja en place (reductions parrainage, etat
"Plan actuel", etc.) sont conserves a l'identique.
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
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&display=swap" rel="stylesheet">
      <div class="view-header" style="background:linear-gradient(135deg,#FF6B6B,#FF9A3C) !important;padding:16px 20px 18px !important;min-height:auto !important;justify-content:flex-start !important">
        <div style="font-size:2rem;font-weight:800;color:white;font-family:'Open Sans',sans-serif;line-height:1.2">Choisis ton niveau</div>
        <div style="font-size:0.85rem;color:rgba(255,255,255,0.85);margin-top:4px">Commence gratuitement. Évolue quand tu es prêt.</div>
      </div>
      <div style="padding:16px 16px 100px">

      <style>
        .pv-promo{display:flex;align-items:center;gap:8px;background:rgba(255,107,107,0.08);border-radius:14px;padding:10px 14px;margin-bottom:16px;font-size:12px;font-weight:600;color:#C24A3E}

        .pv-tabs{display:flex;background:#FFFCFA;border:1px solid rgba(0,0,0,0.06);border-radius:18px;padding:4px;margin-bottom:18px;box-shadow:0 2px 10px rgba(0,0,0,0.03)}
        .pv-tab{flex:1;text-align:center;padding:10px 4px;border-radius:14px;cursor:pointer;transition:all 0.25s}
        .pv-tab .pv-t-name{display:block;font-size:12px;font-weight:700;color:#9a9a9a}
        .pv-tab .pv-t-price{display:block;font-size:10px;font-weight:600;color:#b0a49c;margin-top:1px}
        .pv-tab.active{background:#18181B}
        .pv-tab.active .pv-t-name{color:white}
        .pv-tab.active .pv-t-price{color:rgba(255,255,255,0.55)}
        .pv-tab.active.gold{background:linear-gradient(135deg,#FFE9B8,#C9A84C)}
        .pv-tab.active.gold .pv-t-name{color:#4A3610}
        .pv-tab.active.gold .pv-t-price{color:#6b5320}

        .pv-panel{display:none}
        .pv-panel.active{display:block;animation:pvIn 0.4s cubic-bezier(.16,1,.3,1)}
        @keyframes pvIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

        /* Eyebrow label, identique au pattern utilisé dans le reste de l'app (evo-eyebrow) */
        .p-eyebrow{display:flex;align-items:center;gap:7px;margin-bottom:2px}
        .p-eyebrow-bar{width:3px;height:14px;border-radius:2px;flex-shrink:0;background:linear-gradient(180deg,#FF6B6B,#FF9A3C)}
        .p-eyebrow-bar.gold{background:linear-gradient(180deg,#F0D28A,#C9A84C)}
        .p-eyebrow-bar.dim{background:rgba(255,255,255,0.25)}
        .p-eyebrow-text{font-size:10px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase}

        .ptoggle-wrap{display:flex;background:#FFFCFA;border:1px solid rgba(0,0,0,0.06);border-radius:30px;padding:4px;margin:18px auto 0;width:fit-content;box-shadow:0 2px 10px rgba(0,0,0,0.03)}
        .ptbtn{padding:9px 20px;border-radius:26px;border:none;font-size:12px;font-weight:700;cursor:pointer;font-family:DM Sans,sans-serif;transition:all 0.2s;color:#9a9a9a;background:transparent}
        .ptbtn.pton{background:linear-gradient(135deg,#FF6B6B,#FF9A3C);color:white;box-shadow:0 6px 16px rgba(255,107,107,0.3)}
        .peco{font-size:9px;background:rgba(76,175,130,0.15);color:#2f9e63;padding:2px 6px;border-radius:8px;margin-left:5px;font-weight:800}
        .ptbtn.pton .peco{background:rgba(255,255,255,0.25);color:white}

        /* FREE — même carte crème que le reste de l'app */
        .card-free{background:#FFFCFA;border-radius:24px;border:1px solid rgba(255,154,108,0.14);padding:24px;box-shadow:0 3px 10px rgba(0,0,0,0.03),0 16px 32px -12px rgba(230,110,70,0.18)}
        .cf-top{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:20px}
        .cf-price{font-family:'Fraunces',serif;font-weight:500;font-size:2.6rem;color:#1a1a1a;margin-top:8px;letter-spacing:-0.02em}
        .cf-price span{font-size:12px;font-weight:600;color:#b0a49c;font-family:DM Sans,sans-serif}
        .cf-feats{display:flex;flex-direction:column;gap:12px}
        .cf-feat{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--charcoal,#2D2D2D);font-weight:600}
        .cf-feat-ico{width:24px;height:24px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(255,107,107,0.1);flex-shrink:0}
        .cf-feat-ico i{font-size:13px;color:#FF6B6B}
        .cf-btn-free{padding:10px 18px;border-radius:20px;border:1.5px solid rgba(0,0,0,0.1);background:white;font-size:12px;font-weight:700;color:#8a8a8a;cursor:pointer;font-family:DM Sans,sans-serif;white-space:nowrap}

        /* STANDARD — anthracite avec dégradé radial doux */
        .card-std{background:radial-gradient(120% 140% at 15% 0%,#34302C 0%,#18181B 55%,#131211 100%);border-radius:26px;padding:26px;position:relative;overflow:hidden;box-shadow:0 3px 10px rgba(0,0,0,0.1),0 24px 48px -14px rgba(230,110,70,0.3);border:1px solid rgba(255,255,255,0.06)}
        .card-std::after{content:'';position:absolute;top:24px;left:24px;right:24px;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.2),transparent)}
        .cs-glow{position:absolute;top:-60px;right:-60px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(255,107,107,0.14) 0%,transparent 70%);pointer-events:none}
        .cs-glow2{position:absolute;bottom:-40px;left:-40px;width:140px;height:140px;border-radius:50%;background:radial-gradient(circle,rgba(255,154,60,0.08) 0%,transparent 70%);pointer-events:none}
        .cs-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;position:relative;z-index:1}
        .cs-popular{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:700;color:#FF9A3C;background:rgba(255,154,60,0.14);padding:4px 10px;border-radius:20px}
        .cs-price-row{display:flex;align-items:baseline;gap:10px;margin-bottom:4px;position:relative;z-index:1}
        .cs-price{font-family:'Fraunces',serif;font-weight:500;font-size:2.9rem;color:white;line-height:1;letter-spacing:-0.02em}
        .cs-old{font-size:13px;text-decoration:line-through;color:rgba(255,255,255,0.25)}
        .cs-period{font-size:12px;color:rgba(255,255,255,0.45);margin-bottom:4px;position:relative;z-index:1}
        .cs-perday{display:inline-flex;align-items:center;gap:5px;background:rgba(74,222,128,0.1);border-radius:10px;padding:6px 12px;font-size:11.5px;color:rgba(255,255,255,0.6);margin-top:14px;margin-bottom:20px;position:relative;z-index:1}
        .cs-feats{display:flex;flex-direction:column;gap:12px;margin-bottom:8px;position:relative;z-index:1}
        .cs-feat{display:flex;align-items:center;gap:10px}
        .cs-feat-ico{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(255,107,107,0.12);flex-shrink:0}
        .cs-feat-ico i{font-size:13px;color:#FF9A3C}
        .cs-feat-txt{font-size:13px;color:rgba(255,255,255,0.85);font-weight:500}
        .cs-cta{width:100%;padding:15px;border-radius:16px;border:none;font-size:14px;font-weight:800;cursor:pointer;font-family:DM Sans,sans-serif;background:#EFE9E2;color:#18181B;letter-spacing:0.01em;display:flex;align-items:center;justify-content:center;gap:6px;margin-top:20px;position:relative;z-index:1}

        /* PREMIUM — dégradé cuivre/or profond, liseré doré animé, renard mascotte */
        .card-prm{border-radius:26px;padding:26px;position:relative;overflow:hidden;background:linear-gradient(160deg,#2A1810 0%,#4A2416 30%,#7A3418 62%,#C9863D 100%);box-shadow:0 3px 10px rgba(0,0,0,0.15),0 26px 54px -12px rgba(140,70,20,0.5)}
        .card-prm .pv-glow{position:absolute;inset:0;background:radial-gradient(circle at 85% -10%,rgba(255,215,150,0.35),transparent 45%),radial-gradient(circle at -10% 110%,rgba(255,150,100,0.2),transparent 50%);pointer-events:none}
        .card-prm::after{content:'';position:absolute;inset:0;border-radius:26px;padding:1.5px;background:linear-gradient(120deg,rgba(255,224,168,0.9),rgba(255,255,255,0.1) 35%,rgba(255,224,168,0.55) 65%,rgba(255,255,255,0.05));background-size:240% 240%;-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;animation:cpBorderFlow 6s ease infinite}
        @keyframes cpBorderFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
        .cp-fox{position:absolute;bottom:-4px;right:-2px;width:84px;opacity:0.95;pointer-events:none;filter:drop-shadow(0 8px 18px rgba(0,0,0,0.35))}
        .cp-maxsave{display:none;align-items:center;gap:5px;font-size:10px;font-weight:800;color:#5C4310;background:linear-gradient(135deg,#FFE9B8,#F0D28A);padding:4px 10px;border-radius:20px;margin-left:6px;box-shadow:0 3px 8px rgba(201,168,76,0.35)}
        .cp-maxsave.show{display:inline-flex}
        .cp-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;position:relative;z-index:1}
        .cp-best{display:flex;align-items:center;gap:4px;font-size:10px;font-weight:800;color:#7A5A1A;background:linear-gradient(135deg,#FFE9B8,#F0D28A);padding:4px 10px;border-radius:20px;box-shadow:0 3px 8px rgba(201,168,76,0.35)}
        .cp-price{font-family:'Fraunces',serif;font-weight:500;font-size:2.9rem;color:#FFF6EA;line-height:1;letter-spacing:-0.02em}
        .cp-old{font-size:13px;text-decoration:line-through;color:rgba(255,255,255,0.4)}
        .cp-period{font-size:12px;color:rgba(255,255,255,0.65);margin-bottom:4px;position:relative;z-index:1}
        .cp-perday{display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,0.15);border-radius:10px;padding:6px 12px;font-size:11.5px;color:rgba(255,255,255,0.8);margin-top:14px;margin-bottom:20px;position:relative;z-index:1}
        .cp-feats{display:flex;flex-direction:column;gap:12px;margin-bottom:8px;position:relative;z-index:1}
        .cp-feat{display:flex;align-items:center;gap:10px}
        .cp-feat-ico{width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,0.2);flex-shrink:0}
        .cp-feat-ico i{font-size:13px;color:white}
        .cp-feat-txt{font-size:13px;color:rgba(255,255,255,0.95);font-weight:500}
        .cp-cta{width:100%;padding:15px;border-radius:16px;border:none;font-size:14px;font-weight:800;cursor:pointer;font-family:DM Sans,sans-serif;background:linear-gradient(135deg,#FFE9B8,#F0D28A);color:#3D2A0A;letter-spacing:0.01em;display:flex;align-items:center;justify-content:center;gap:6px;box-shadow:0 12px 28px rgba(201,168,76,0.45);margin-top:20px;position:relative;z-index:1}

        .pv-compare-link{text-align:center;margin:18px 0 4px}
        .pv-compare-link button{background:none;border:none;font-size:12.5px;font-weight:700;color:#8a8a8a;text-decoration:underline;text-underline-offset:3px;cursor:pointer;font-family:DM Sans,sans-serif}

        .pfooter{text-align:center;margin-top:16px;font-size:11px;color:#b0a49c;display:flex;align-items:center;justify-content:center;gap:6px}

        .pv-sheet{position:fixed;inset:0;background:rgba(20,16,13,0.55);display:none;align-items:flex-end;justify-content:center;z-index:99999}
        .pv-sheet.open{display:flex}
        .pv-sheet-panel{width:100%;max-width:480px;background:#FBF5F0;border-radius:26px 26px 0 0;padding:22px 20px 30px;max-height:78vh;overflow-y:auto;animation:pvSheetUp 0.35s cubic-bezier(.16,1,.3,1)}
        @keyframes pvSheetUp{from{transform:translateY(30px);opacity:0}to{transform:translateY(0);opacity:1}}
        .pv-sheet-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
        .pv-sheet-head h3{font-family:'Fraunces',serif;font-weight:500;font-size:19px;color:#1a1a1a}
        .pv-sheet-close{width:28px;height:28px;border-radius:50%;background:#F5EBE2;display:flex;align-items:center;justify-content:center;font-size:13px;color:#8a8a8a;cursor:pointer}
        .pv-cmp-table{width:100%;border-collapse:collapse;font-size:11.5px}
        .pv-cmp-table th{font-weight:700;text-align:center;padding:8px 4px;color:#8a8a8a;font-size:10.5px}
        .pv-cmp-table th:first-child{text-align:left}
        .pv-cmp-table td{padding:9px 4px;border-top:1px solid rgba(0,0,0,0.06);text-align:center;font-weight:600;color:#2D2D2D}
        .pv-cmp-table td:first-child{text-align:left;color:#8a8a8a;font-weight:500}
        .pv-cmp-yes{color:#3E9E6B;font-weight:800}
        .pv-cmp-no{color:#c9c0b6}
      </style>

      <div class="pv-promo">
        <i class="ti ti-info-circle" style="font-size:14px"></i>
        Économise 50% avec l'abonnement annuel, sur Standard comme sur Premium
      </div>

      <div class="pv-tabs">
        <div class="pv-tab" id="pvTabFree" onclick="pvSelectTier('free')">
          <span class="pv-t-name">Essentiel</span>
          <span class="pv-t-price">Gratuit</span>
        </div>
        <div class="pv-tab active" id="pvTabStandard" onclick="pvSelectTier('standard')">
          <span class="pv-t-name">Standard</span>
          <span class="pv-t-price" id="pvTabStdPrice">2,99€/mois</span>
        </div>
        <div class="pv-tab gold" id="pvTabPremium" onclick="pvSelectTier('premium')">
          <span class="pv-t-name">Premium</span>
          <span class="pv-t-price" id="pvTabPrmPrice">4,99€/mois</span>
        </div>
      </div>

      <!-- FREE -->
      <div class="pv-panel" id="pvPanelFree">
      <div class="card-free">
        <div class="cf-top">
          <div>
            <div class="p-eyebrow"><div class="p-eyebrow-bar" style="background:#d8cfc8"></div><div class="p-eyebrow-text" style="color:#b0a49c">Gratuit · Essentiel</div></div>
            <div class="cf-price">0€ <span>/ toujours</span></div>
          </div>
          <div class="current-plan-tag" id="freePlanTag" style="display:none">Plan actuel</div>
        </div>
        <div class="cf-feats">
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-message-circle"></i></div>5 messages/jour</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-heart-rate-monitor"></i></div>Suivi santé</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-book"></i></div>30 recettes offertes</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-stethoscope"></i></div>Pathologies</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-trophy"></i></div>Programmes</div>
          <div class="cf-feat"><div class="cf-feat-ico"><i class="ti ti-shield-check"></i></div>Sécurité médicale</div>
        </div>
        <button class="cf-btn-free" id="freePlanBtn" onclick="selectPlan('free')" style="width:100%;margin-top:20px">Plan actuel</button>
      </div>
      </div>

      <!-- STANDARD -->
      <div class="pv-panel active" id="pvPanelStandard">
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
        <div id="standardDiscount" style="display:none;justify-content:center;position:relative;z-index:1"></div>
        <button class="cs-cta" id="standardPlanBtn" onclick="selectPlan(window._pricingPeriod==='annual'?'standard_annual':'standard')"><i class="ti ti-arrow-right" style="font-size:15px"></i>Choisir Standard</button>
      </div>
      </div>

      <!-- PREMIUM -->
      <div class="pv-panel" id="pvPanelPremium">
      <div class="card-prm">
        <div class="pv-glow"></div>
        <img class="cp-fox" src="https://www.mirella-ai.fr/renard_transparent.png" alt="">
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
        <div id="premiumDiscount" style="display:none;justify-content:center;position:relative;z-index:1"></div>
        <button class="cp-cta" id="premiumPlanBtn" onclick="selectPlan(window._pricingPeriod==='annual'?'premium_annual':'premium')"><i class="ti ti-crown" style="font-size:15px"></i>Choisir Premium</button>
      </div>
      </div>

      <div class="pv-compare-link">
        <button onclick="pvOpenCompare()">Comparer les 3 offres en détail</button>
      </div>

      <div class="ptoggle-wrap">
        <button id="toggleMonthly" class="ptbtn pton" onclick="window.setPricingPeriod('monthly')">Mensuel</button>
        <button id="toggleAnnual" class="ptbtn" onclick="window.setPricingPeriod('annual')">Annuel <span class="peco">-50%</span></button>
      </div>

      <div class="pfooter">
        <i class="ti ti-lock" style="font-size:12px"></i>
        Paiement sécurisé · Sans engagement · Remboursé 30 jours
      </div>
    </div>
    </div>

    <div class="pv-sheet" id="pvCompareSheet" onclick="if(event.target===this)pvCloseCompare()">
      <div class="pv-sheet-panel">
        <div class="pv-sheet-head">
          <h3>Comparer les offres</h3>
          <div class="pv-sheet-close" onclick="pvCloseCompare()">✕</div>
        </div>
        <table class="pv-cmp-table">
          <tr><th></th><th>Essentiel</th><th>Standard</th><th>Premium</th></tr>
          <tr><td>Chat IA</td><td>5/jour</td><td class="pv-cmp-yes">Illimité</td><td class="pv-cmp-yes">Illimité</td></tr>
          <tr><td>Recettes</td><td>30</td><td class="pv-cmp-yes">7 000+</td><td class="pv-cmp-yes">7 000+</td></tr>
          <tr><td>Menus IA hebdo</td><td class="pv-cmp-no">—</td><td class="pv-cmp-yes">✓</td><td class="pv-cmp-yes">✓</td></tr>
          <tr><td>Dashboard santé</td><td>Basique</td><td class="pv-cmp-yes">Complet</td><td class="pv-cmp-yes">Complet</td></tr>
          <tr><td>Analyse photo repas</td><td class="pv-cmp-no">—</td><td class="pv-cmp-no">—</td><td class="pv-cmp-yes">✓</td></tr>
          <tr><td>Pro. de santé</td><td class="pv-cmp-no">—</td><td class="pv-cmp-no">—</td><td class="pv-cmp-yes">✓</td></tr>
          <tr><td>Mémoire long terme</td><td class="pv-cmp-no">—</td><td class="pv-cmp-no">—</td><td class="pv-cmp-yes">✓</td></tr>
          <tr><td>Coaching comportemental</td><td class="pv-cmp-no">—</td><td class="pv-cmp-no">—</td><td class="pv-cmp-yes">✓</td></tr>
          <tr><td>Prix / mois</td><td>0€</td><td>2,99€</td><td>4,99€</td></tr>
        </table>
      </div>
    </div>

"""

content = content[:i] + NEW_BLOCK + content[j:]

OLD_JS_START = "window.setPricingPeriod = function(period) {"
OLD_JS_END_MARK = "\nwindow._catalogueFilters"
k1 = content.find(OLD_JS_START)
k2 = content.find(OLD_JS_END_MARK, k1)
if k1 == -1 or k2 == -1:
    raise SystemExit("Bloc JS setPricingPeriod introuvable - deja patche ou structure changee.")

NEW_JS = r"""window.setPricingPeriod = function(period) {
  window._pricingPeriod = period;
  var isAnnual = period === 'annual';
  var tm = document.getElementById('toggleMonthly');
  var ta = document.getElementById('toggleAnnual');
  if (tm) { tm.classList.toggle('pton', !isAnnual); tm.style.background = ''; tm.style.color = ''; }
  if (ta) { ta.classList.toggle('pton', isAnnual); ta.style.background = ''; ta.style.color = ''; }
  var pms = document.getElementById('premiumMaxSave');
  if (pms) pms.classList.toggle('show', isAnnual);
  var sp = document.getElementById('standardPrice');
  var sop = document.getElementById('standardOldPrice');
  var sper = document.getElementById('standardPeriod');
  var spd = document.getElementById('standardPerDay');
  var pp = document.getElementById('premiumPrice');
  var pop = document.getElementById('premiumOldPrice');
  var pper = document.getElementById('premiumPeriod');
  var ppd = document.getElementById('premiumPerDay');
  if (isAnnual) {
    if (sp) sp.textContent = '35,90€';
    if (sop) sop.textContent = '71,90€';
    if (sper) sper.innerHTML = '/ an · <span style="color:#4ade80;font-weight:700">-50%</span> · soit 2,99€/mois';
    if (spd) spd.innerHTML = 'soit seulement <span style="color:#4ade80;font-size:0.85rem">0,09€</span> / jour';
    if (pp) pp.textContent = '59,90€';
    if (pop) pop.textContent = '119,90€';
    if (pper) pper.innerHTML = '/ an · <span style="color:#4ade80;font-weight:700">-50%</span> · soit 4,99€/mois';
    if (ppd) ppd.innerHTML = 'soit seulement <span style="color:#4ade80;font-size:0.85rem">0,16€</span> / jour';
  } else {
    if (sp) sp.textContent = '2,99€';
    if (sop) sop.textContent = '5,99€';
    if (sper) sper.innerHTML = '/ mois · <span style="color:#4ade80;font-weight:700">-50%</span>';
    if (spd) spd.innerHTML = 'soit seulement <span style="color:#4ade80;font-size:0.85rem">0,09€</span> / jour';
    if (pp) pp.textContent = '4,99€';
    if (pop) pop.textContent = '9,99€';
    if (pper) pper.innerHTML = '/ mois · <span style="color:#4ade80;font-weight:700">-50%</span>';
    if (ppd) ppd.innerHTML = 'soit seulement <span style="color:#4ade80;font-size:0.85rem">0,16€</span> / jour';
  }
  var tsp = document.getElementById('pvTabStdPrice');
  var tpp = document.getElementById('pvTabPrmPrice');
  if (tsp) tsp.textContent = isAnnual ? '35,90€/an' : '2,99€/mois';
  if (tpp) tpp.textContent = isAnnual ? '59,90€/an' : '4,99€/mois';
};
window.pvSelectTier = function(tier) {
  var tiers = ['free', 'standard', 'premium'];
  tiers.forEach(function(t) {
    var tab = document.getElementById('pvTab' + t.charAt(0).toUpperCase() + t.slice(1));
    var panel = document.getElementById('pvPanel' + t.charAt(0).toUpperCase() + t.slice(1));
    if (tab) tab.classList.toggle('active', t === tier);
    if (panel) panel.classList.toggle('active', t === tier);
  });
};
window.pvOpenCompare = function() {
  var el = document.getElementById('pvCompareSheet');
  if (el) el.classList.add('open');
};
window.pvCloseCompare = function() {
  var el = document.getElementById('pvCompareSheet');
  if (el) el.classList.remove('open');
};"""

content = content[:k1] + NEW_JS + content[k2:]

old_switch = "document.getElementById('pricingView').style.display = view === 'pricing' ? 'block' : 'none';"
new_switch = old_switch + "\n    if (view === 'pricing' && window.pvSelectTier) { window.pvSelectTier(window.currentPlan === 'premium' ? 'premium' : (window.currentPlan === 'standard' ? 'standard' : 'free')); }"
if old_switch in content and new_switch not in content:
    content = content.replace(old_switch, new_switch)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("OK - vue abonnement v2 (onglets) appliquee dans app.html")
