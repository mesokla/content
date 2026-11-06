// Fills [data-f="key"] elements from URL params: ?title=...&kicker=...  Use "|" for line breaks inside a value.
const q=new URLSearchParams(location.search);
for(const el of document.querySelectorAll('[data-f]')){
  const v=q.get(el.dataset.f); if(v===null) continue;
  if(el.tagName==='IMG') el.src=v; else el.innerHTML=v.split('|').map(s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])).replace(/\*(.+?)\*/g,'<em>$1</em>')).join('<br>');
}
for(const el of document.querySelectorAll('[data-hide-empty]')) if(!el.textContent.trim()) el.style.display='none';
const t=q.get('theme'); if(t) document.body.dataset.theme=t;
