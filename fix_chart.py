with open('/workspaces/nutricare-frontend/app.html', 'r') as f:
    content = f.read()

old = "function renderHealthChart(logs) {\n  const canvas = document.getElementById('healthChart');\n  if (!canvas || !logs.length) return;\n  const existing = Chart.getChart(canvas);\n  if (existing) existing.destroy();\n  const labels = logs.map(l => new Date(l.date).toLocaleDateString('fr-FR', { day:'numeric', month:'short' }));\n  new Chart(canvas, {\n    type: 'line',\n    data: {\n      labels,\n      datasets: [\n        { label: 'Poids (kg)', data: logs.map(l => l.weight), borderColor: '#378ADD', backgroundColor: 'rgba(55,138,221,0.08)', tension: 0.4, fill: true, yAxisID: 'y' },\n        { label: 'Énergie (/10)', data: logs.map(l => l.energy_level), borderColor: '#C9A84C', backgroundColor: 'rgba(201,168,76,0.08)', tension: 0.4, fill: false, yAxisID: 'y2' },\n        { label: 'Sommeil (h)', data: logs.map(l => l.sleep_hours), borderColor: '#845EC2', backgroundColor: 'rgba(132,94,194,0.08)', tension: 0.4, fill: false, yAxisID: 'y2' },\n        { label: 'Hydratation (L)', data: logs.map(l => l.hydration_liters), borderColor: '#00C9A7', backgroundColor: 'rgba(0,201,167,0.08)', tension: 0.4, fill: false, yAxisID: 'y2' },\n        { label: 'Glycémie (mmol/L)', data: logs.map(l => l.glycemia), borderColor: '#FF6B6B', backgroundColor: 'rgba(255,107,107,0.08)', tension: 0.4, fill: false, yAxisID: 'y2' }\n      ]\n    },\n    options: {\n      responsive: true,\n      interaction: { mode: 'index', intersect: false },\n      plugins: { legend: { position: 'bottom', labels: { boxWidth: 12, font: { size: 11 } } } },\n      scales: {\n        y: { type: 'linear', position: 'left', title: { display: true, text: 'Poids (kg)', font: { size: 10 } }, beginAtZero: false },\n        y2: { type: 'linear', position: 'right', title: { display: true, text: 'Autres', font: { size: 10 } }, beginAtZero: true, grid: { drawOnChartArea: false } }\n      }\n    }\n  });\n}"

new = '''function renderHealthChart(logs) {
  const canvas = document.getElementById('healthChart');
  if (!canvas || !logs.length) return;
  const labels = logs.map(l => new Date(l.date).toLocaleDateString('fr-FR', { day:'numeric', month:'short' }));
  const metrics = [
    {key:'weight', label:'Poids (kg)', color:'#378ADD'},
    {key:'energy_level', label:'Énergie (/10)', color:'#C9A84C'},
    {key:'sleep_hours', label:'Sommeil (h)', color:'#845EC2'},
    {key:'hydration_liters', label:'Hydratation (L)', color:'#00C9A7'},
    {key:'glycemia', label:'Glycémie', color:'#FF6B6B'}
  ];
  let activeKey = 'weight';
  const wrap = canvas.parentElement;
  if (!wrap.querySelector('.chart-selector')) {
    const sel = document.createElement('div');
    sel.className = 'chart-selector';
    sel.style.cssText = 'display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px';
    metrics.forEach(function(m) {
      const btn = document.createElement('button');
      btn.textContent = m.label;
      btn.dataset.key = m.key;
      btn.style.cssText = 'padding:4px 10px;border-radius:20px;border:none;font-size:0.72rem;font-weight:600;cursor:pointer;font-family:DM Sans,sans-serif;transition:all 0.2s;background:' + (m.key===activeKey ? m.color : '#F0F0F0') + ';color:' + (m.key===activeKey ? 'white' : '#666');
      btn.onclick = function() {
        activeKey = m.key;
        sel.querySelectorAll('button').forEach(function(b) {
          const mm = metrics.find(x=>x.key===b.dataset.key);
          b.style.background = b.dataset.key===activeKey ? mm.color : '#F0F0F0';
          b.style.color = b.dataset.key===activeKey ? 'white' : '#666';
        });
        drawHealthChart(activeKey);
      };
      sel.appendChild(btn);
    });
    wrap.insertBefore(sel, canvas);
  }
  function drawHealthChart(key) {
    const ex = Chart.getChart(canvas);
    if (ex) ex.destroy();
    const m = metrics.find(x=>x.key===key);
    new Chart(canvas, {
      type: 'line',
      data: { labels, datasets: [{ label: m.label, data: logs.map(function(l){return l[key];}), borderColor: m.color, backgroundColor: m.color+'22', tension: 0.4, fill: true, pointRadius: 3, pointHoverRadius: 5 }] },
      options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: false, grid: { color: 'rgba(0,0,0,0.04)' } }, x: { grid: { display: false }, ticks: { font: { size: 10 }, maxRotation: 45 } } } }
    });
  }
  drawHealthChart(activeKey);
}'''

if old in content:
    content = content.replace(old, new)
    print('done')
else:
    print('NOT FOUND - trying line by line match')
    print(repr(content[content.find('function renderHealthChart'):content.find('function renderHealthChart')+100]))

with open('/workspaces/nutricare-frontend/app.html', 'w') as f:
    f.write(content)
