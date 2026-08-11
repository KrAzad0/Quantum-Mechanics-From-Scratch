(()=>{
const P=window.QM_PAPERS,E=window.QM_ERAS,$=s=>document.querySelector(s),state={q:"",era:"All eras",essential:false,order:1,read:new Set(JSON.parse(localStorage.getItem("qm-read")||"[]"))};
const grid=$("#paperGrid"),filters=$("#filters"),search=$("#search"),dialog=$("#dialog"),body=$("#dialogBody");
const esc=s=>String(s).replace(/[&<>'"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"})[c]);
function save(){localStorage.setItem("qm-read",JSON.stringify([...state.read]))}
function progress(){const n=state.read.size,p=Math.round(n/P.length*100);$("#readCount").textContent=n;$("#heroProgress").textContent=p+"%";$("#progressFill").style.width=p+"%"}
function renderFilters(){filters.innerHTML=["All eras",...E].map(e=>`<button class="${state.era===e?"active":""}" data-era="${esc(e)}">${esc(e)}</button>`).join("")}
function visible(){const q=state.q.trim().toLowerCase();return P.filter(p=>state.era==="All eras"||p.era===state.era).filter(p=>!state.essential||p.essential).filter(p=>!q||[p.title,p.authors,p.year,p.era,p.summary,p.equation].join(" ").toLowerCase().includes(q)).sort((a,b)=>(a.year-b.year||a.id-b.id)*state.order)}
function card(p){const done=state.read.has(p.id);return `<article class="card" id="paper-${p.id}"><div class="topline"><span>Paper ${String(p.id).padStart(2,"0")} · ${p.year}</span>${p.essential?'<span class="star">★ Essential</span>':""}</div><div class="art"><i class="orb"></i><span class="equation">${esc(p.equation)}</span></div><h3>${esc(p.title)}</h3><p class="meta">${esc(p.era)}</p><p class="summary">${esc(p.summary)}</p><p class="authors">${esc(p.authors)}</p><div class="card-actions"><button data-open="${p.id}">Read overview ↗</button><button class="study ${done?"done":""}" data-read="${p.id}" aria-label="Mark as studied">${done?"✓":"○"}</button></div></article>`}
function render(){const v=visible();grid.innerHTML=v.map(card).join("");grid.hidden=!v.length;$("#empty").hidden=!!v.length;$("#results").textContent=`${v.length} of ${P.length} entries shown${state.essential?" · essential path":""}${state.era!=="All eras"?" · "+state.era:""}`;progress()}
function toggle(id){state.read.has(id)?state.read.delete(id):state.read.add(id);save();render();if(dialog.open&&+body.dataset.id===id)open(id)}
function open(id){const p=P.find(x=>x.id===id);if(!p)return;body.dataset.id=id;body.innerHTML=`<div class="dialog-body"><p>PAPER ${String(p.id).padStart(2,"0")} / ${P.length} · ${p.year} · ${esc(p.era)}</p><h2>${esc(p.title)}</h2><p class="authors">${esc(p.authors)}</p><div class="dialog-equation">${esc(p.equation)}</div><section><h3>Abstract overview</h3><p>${esc(p.summary)}</p></section><section><h3>Research prompt</h3><p>Recover the problem this work answered, reconstruct its central derivation in modern notation, and reproduce one consequence analytically or computationally.</p></section><div class="dialog-actions"><a href="${esc(p.link)}" target="_blank" rel="noreferrer">Open original source ↗</a><button data-dialog-read="${p.id}">${state.read.has(id)?"✓ Studied":"○ Mark studied"}</button></div><section><h3>Editorial note</h3><p>This is an original educational summary, not copied publisher abstract text.</p></section></div>`;if(!dialog.open)dialog.showModal();history.replaceState(null,"",`#paper-${id}`)}
grid.addEventListener("click",e=>{const o=e.target.closest("[data-open]"),r=e.target.closest("[data-read]");if(o)open(+o.dataset.open);if(r)toggle(+r.dataset.read)});
filters.addEventListener("click",e=>{const b=e.target.closest("[data-era]");if(b){state.era=b.dataset.era;renderFilters();render()}});
search.addEventListener("input",()=>{state.q=search.value;render()});
$("#essential").onclick=()=>{state.essential=!state.essential;$("#essential").setAttribute("aria-pressed",state.essential);render()};
$("#sort").onclick=()=>{state.order*=-1;$("#sort").textContent=state.order===1?"Oldest first ↓":"Newest first ↑";render()};
$("#reset").onclick=()=>{state.q="";state.era="All eras";state.essential=false;search.value="";$("#essential").setAttribute("aria-pressed","false");renderFilters();render()};
$(".close").onclick=()=>dialog.close();dialog.addEventListener("click",e=>{if(e.target===dialog)dialog.close();const r=e.target.closest("[data-dialog-read]");if(r)toggle(+r.dataset.dialogRead)});dialog.addEventListener("close",()=>history.replaceState(null,"","#archive"));
$("#continue").onclick=()=>open((P.find(p=>!state.read.has(p.id))||P[0]).id);
$("#theme").onclick=()=>{const d=document.documentElement,n=d.dataset.theme==="dark"?"light":"dark";d.dataset.theme=n;localStorage.setItem("qm-theme",n)};
document.querySelectorAll(".chain [data-era]").forEach(b=>b.onclick=()=>{state.era=b.dataset.era;renderFilters();render();$("#archive").scrollIntoView()});
document.querySelector("[data-paper='1']").onclick=()=>open(1);
document.addEventListener("keydown",e=>{if(e.key==="/"&&document.activeElement!==search&&!dialog.open){e.preventDefault();search.focus()}});
document.documentElement.dataset.theme=localStorage.getItem("qm-theme")||"dark";renderFilters();render();const m=location.hash.match(/^#paper-(\d+)$/);if(m)setTimeout(()=>open(+m[1]),50);
})();
