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
// --- moth signature + decorative element ---
(function(){
  const NAME={'rgb(226, 9, 66)':'crimson','rgb(166, 184, 160)':'leaf','rgb(139, 114, 156)':'violet'};
  const theme=document.body.dataset.theme||'leaf';
  if(q.get('sig')!=='plain') document.querySelectorAll('.sig').forEach(s=>{
    const c=NAME[getComputedStyle(s).color]||'crimson';
    const i=document.createElement('img'); i.className='sig-moth'; i.alt=''; i.src='../moth/moth-front-'+c+'.svg'; s.prepend(i);
  });
  const el=q.get('el'); if(!el||el==='none') return;
  const shape={leaf:'violet',violet:'crimson',crimson:'violet'}[theme];   // filled shapes
  const line={leaf:'crimson',violet:'leaf',crimson:'leaf'}[theme];        // line art
  const img=document.createElement('img'); img.className='deco el-'+el; img.alt='';
  img.src=el==='moth'?'../moth/moth-flight-'+line+'.svg':'../elements/'+el+'-'+shape+'.svg';
  (document.querySelector('.canvas')).prepend(img); document.body.classList.add('has-deco'); if(['wing','wings','contour','lens'].includes(el)) document.body.classList.add('deco-corner');
})();
