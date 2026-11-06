// Fills [data-f="key"] elements from URL params: ?title=...  "|" = line break, *word* = highlight.
const q=new URLSearchParams(location.search);
const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const fmt=v=>v.split('|').map(s=>esc(s).replace(/\*(.+?)\*/g,'<em>$1</em>')).join('<br>');
for(const el of document.querySelectorAll('[data-f]')){const v=q.get(el.dataset.f); if(v!==null) el.innerHTML=fmt(v);}
for(const el of document.querySelectorAll('[data-list]')){
  const v=(q.get(el.dataset.list)??el.dataset.default).split('|');
  el.innerHTML=v.map(s=>'<li><span>'+esc(s.trim()).replace(/\*(.+?)\*/g,'<em>$1</em>')+'</span></li>').join('');
}
const t=q.get('theme'); if(t) document.body.dataset.theme=t;
