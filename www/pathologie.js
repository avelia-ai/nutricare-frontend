window.rechercherPathologie = async function() {
  var input = document.getElementById('pathoSearchInput');
  var loading = document.getElementById('pathoLoading');
  var result = document.getElementById('pathoResult');
  if (!input || !input.value.trim()) return;
  var query = input.value.trim();
  loading.style.display = 'block';
  result.style.display = 'none';
  var token = localStorage.getItem('nutricare_token');
  var res = await fetch('https://nutricare-backend-production.up.railway.app/api/pathologie/info', {
    method: 'POST',
    headers: {'Content-Type':'application/json','Authorization':'Bearer '+token},
    body: JSON.stringify({pathologie: query})
  }).catch(function(e) { return null; });
  loading.style.display = 'none';
  result.style.display = 'block';
  if (!res || !res.ok) { result.innerHTML = '<p style="color:#ef4444">Erreur de connexion</p>'; return; }
  var d = await res.json();
  var h = '<div style="font-size:1rem;font-weight:700;color:#1a1a1a;margin-bottom:12px">' + (d.titre || query) + '</div>';
  h += '<div style="background:#E6F1FB;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#185FA5;margin-bottom:6px">📋 DESCRIPTION</div><div style="font-size:0.82rem;color:#333;line-height:1.6">' + (d.description||'') + '</div></div>';
  if (d.causes && d.causes.length) { h += '<div style="background:#EEEDFE;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#534AB7;margin-bottom:6px">🔬 CAUSES</div><ul style="margin:0;padding-left:16px">'; d.causes.forEach(function(c){h+='<li style="font-size:0.82rem;color:#333;margin-bottom:4px">'+c+'</li>';}); h+='</ul></div>'; }
  if (d.symptomes && d.symptomes.length) { h += '<div style="background:#FFF5E6;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#FF9A3C;margin-bottom:6px">🩺 SYMPTÔMES</div><ul style="margin:0;padding-left:16px">'; d.symptomes.forEach(function(c){h+='<li style="font-size:0.82rem;color:#333;margin-bottom:4px">'+c+'</li>';}); h+='</ul></div>'; }
  if (d.aliments_recommandes && d.aliments_recommandes.length) { h += '<div style="background:#EAF3DE;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#3B6D11;margin-bottom:6px">🥗 ALIMENTS RECOMMANDÉS</div><ul style="margin:0;padding-left:16px">'; d.aliments_recommandes.forEach(function(c){h+='<li style="font-size:0.82rem;color:#333;margin-bottom:4px">'+c+'</li>';}); h+='</ul></div>'; }
  if (d.aliments_eviter && d.aliments_eviter.length) { h += '<div style="background:#FEF2F2;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#ef4444;margin-bottom:6px">❌ ALIMENTS À ÉVITER</div><ul style="margin:0;padding-left:16px">'; d.aliments_eviter.forEach(function(c){h+='<li style="font-size:0.82rem;color:#333;margin-bottom:4px">'+c+'</li>';}); h+='</ul></div>'; }
  if (d.conseils && d.conseils.length) { h += '<div style="background:#FFF0EC;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#FF6B6B;margin-bottom:6px">💡 CONSEILS MIRELLA</div><ul style="margin:0;padding-left:16px">'; d.conseils.forEach(function(c){h+='<li style="font-size:0.82rem;color:#333;margin-bottom:4px">'+c+'</li>';}); h+='</ul></div>'; }
  if (d.quand_consulter) { h += '<div style="background:#FBEAF0;border-radius:12px;padding:12px;margin-bottom:8px"><div style="font-size:0.65rem;font-weight:700;color:#993556;margin-bottom:6px">👨‍⚕️ QUAND CONSULTER</div><div style="font-size:0.82rem;color:#333;line-height:1.6">' + d.quand_consulter + '</div></div>'; }
  result.innerHTML = h;
};

document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('pathoBtn');
  var input = document.getElementById('pathoSearchInput');
  if (btn) btn.addEventListener('click', window.rechercherPathologie);
  if (input) input.addEventListener('keydown', function(e) { if (e.key === 'Enter') window.rechercherPathologie(); });
});
