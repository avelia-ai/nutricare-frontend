window.rechercherPathologie = async function() {
  var input = document.getElementById('pathoSearchInput');
  var loading = document.getElementById('pathoLoading');
  var result = document.getElementById('pathoResult');
  if (!input) return;
  var query = input.value.trim();
  if (!query) return;
  loading.style.display = 'block';
  result.style.display = 'none';
  result.innerHTML = '';
  var token = localStorage.getItem('nutricare_token');
  try {
    var res = await fetch('https://nutricare-backend-production.up.railway.app/api/chat/message', {
      method: 'POST',
      headers: {'Content-Type':'application/json','Authorization':'Bearer '+token},
      body: JSON.stringify({message: 'Fiche complete sur la pathologie: "' + query + '". Reponds avec ces sections separees par ###: Description, Causes, Symptomes, Aliments recommandes, Aliments a eviter, Conseils Mirella, Quand consulter.', context: 'pathologie'})
    });
    var data = await res.json();
    var text = data.reply || data.response || '';
    loading.style.display = 'none';
    result.style.display = 'block';
    var icons = {'Description':'📋','Causes':'🔬','Symptomes':'🩺','Aliments recommandes':'🥗','Aliments a eviter':'❌','Conseils Mirella':'💡','Quand consulter':'👨‍⚕️'};
    var bgs = {'Description':'#E6F1FB','Causes':'#EEEDFE','Symptomes':'#FFF5E6','Aliments recommandes':'#EAF3DE','Aliments a eviter':'#FEF2F2','Conseils Mirella':'#FFF0EC','Quand consulter':'#FBEAF0'};
    var colors = {'Description':'#185FA5','Causes':'#534AB7','Symptomes':'#FF9A3C','Aliments recommandes':'#3B6D11','Aliments a eviter':'#ef4444','Conseils Mirella':'#FF6B6B','Quand consulter':'#993556'};
    var html = '<div style="font-size:0.95rem;font-weight:700;color:#1a1a1a;margin-bottom:12px">' + query.charAt(0).toUpperCase() + query.slice(1) + '</div>';
    var parts = text.split('###');
    parts.forEach(function(part) {
      var trimmed = part.trim();
      if (!trimmed) return;
      var lines = trimmed.split('\n');
      var title = lines[0].replace(/^#+\s*/, '').trim();
      var body = lines.slice(1).join(' ').trim();
      if (!body) return;
      var bg = bgs[title] || '#FFF0EC';
      var color = colors[title] || '#FF6B6B';
      var icon = icons[title] || '📌';
      html += '<div style="background:' + bg + ';border-radius:12px;padding:12px;margin-bottom:8px">';
      html += '<div style="font-size:0.65rem;font-weight:700;text-transform:uppercase;color:' + color + ';margin-bottom:6px">' + icon + ' ' + title + '</div>';
      html += '<div style="font-size:0.82rem;color:#333;line-height:1.6">' + body + '</div>';
      html += '</div>';
    });
    result.innerHTML = html;
  } catch(ex) {
    loading.style.display = 'none';
    result.style.display = 'block';
    result.innerHTML = '<div style="color:#ef4444;font-size:0.82rem">Erreur: ' + ex.message + '</div>';
  }
};

document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('pathoBtn');
  var input = document.getElementById('pathoSearchInput');
  if (btn) btn.addEventListener('click', window.rechercherPathologie);
  if (input) input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') window.rechercherPathologie();
  });
});
