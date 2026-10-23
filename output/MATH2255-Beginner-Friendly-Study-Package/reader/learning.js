/* Progressive mathematical walkthroughs preserve the original DOM states. */
function initLearning(root){
  let serial=0;
  for(const first of [...root.querySelectorAll('.row-step')]){
    if(first.dataset.stepped)continue;
    const steps=[first];let next=first.nextElementSibling;
    while(next?.classList.contains('row-step')){steps.push(next);next=next.nextElementSibling;}
    if(steps.length<2){first.dataset.stepped='true';continue;}
    serial++;const wrap=document.createElement('section');wrap.className='math-stepper example-walkthrough';wrap.setAttribute('aria-label','Mathematical walkthrough '+serial);wrap.dataset.stepCount=steps.length;
    const head=document.createElement('div');head.className='walkthrough-head';head.innerHTML='<span class="component-label">MATHEMATICAL WALKTHROUGH</span><h3>One operation at a time</h3><p class="step-status" aria-live="polite" aria-atomic="true" tabindex="0"></p><div class="step-controls"><button type="button" data-step="prev">← Previous Step</button><button type="button" data-step="next">Next Step →</button><button type="button" class="all-steps" data-step="all" aria-pressed="false">Show All Steps</button></div>';
    first.before(wrap);wrap.append(head);const body=document.createElement('div');body.className='walkthrough-steps';wrap.append(body);
    for(const step of steps){step.dataset.stepped='true';body.append(step);}
    let current=0,all=false;const status=head.querySelector('.step-status');const prev=head.querySelector('[data-step="prev"]'),forward=head.querySelector('[data-step="next"]'),allButton=head.querySelector('[data-step="all"]');
    function update(){
      const operation=steps[current].querySelector('strong')?.textContent||'';
      const purpose=operation.includes('↔')?'Swap the rows to place a nonzero pivot':operation.includes('+')?'Use the pivot row to clear a target entry':'Scale the pivot row so its leading entry becomes 1';
      status.textContent=all?'All '+steps.length+' verified operations · complete overview':'Step '+(current+1)+' of '+steps.length+' · '+purpose;
      steps.forEach((s,i)=>{s.hidden=!all&&i!==current;s.setAttribute('aria-label','Row operation '+(i+1)+' of '+steps.length);});
      prev.disabled=current===0&&!all;forward.disabled=current===steps.length-1&&!all;allButton.textContent=all?'Focus on One Step':'Show All Steps';allButton.setAttribute('aria-pressed',String(all));wrap.dataset.view=all?'all':'guided';markOverflow();
    }
    prev.addEventListener('click',()=>{all=false;current=Math.max(0,current-1);update();});
    forward.addEventListener('click',()=>{all=false;current=Math.min(steps.length-1,current+1);update();});
    allButton.addEventListener('click',()=>{all=!all;update();});
    head.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();forward.click();}if(e.key==='ArrowLeft'){e.preventDefault();prev.click();}});
    update();
  }
  for(const a of root.querySelectorAll('[data-pdf-download],[data-pdf-view]')){
    a.href=sheetURL();if(a.hasAttribute('data-pdf-download'))a.download=DATA.cheatSheet.name;
  }
  for(const img of root.querySelectorAll('[data-sheet-side]'))img.src=DATA.cheatSheet.previews[Number(img.dataset.sheetSide)-1];
}
function sheetURL(){
 if(!sheetURL.cached){const bytes=Uint8Array.from(atob(DATA.cheatSheet.pdf),c=>c.charCodeAt(0));sheetURL.cached=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));}
 return sheetURL.cached;
}
function sheetActions(){return '<div class="sheet-actions"><a class="button-primary" href="#cheat-sheet">View Cheat Sheet</a><a class="button-secondary" href="#cheat-sheet" data-pdf-download>Download PDF ↓</a></div>';}
function cheatSheetPage(){return `<article class="page cheat-sheet-page">${crumbs([['Reference','#reference'],['Cheat Sheet']])}${heading('YOUR TWO-SIDED STUDY REFERENCE','The essentials, within reach.','One US Letter sheet, front and back. A compact companion to the complete explanations.')}<p class="sheet-qualification"><strong>Printable study reference.</strong> The supplied course documents do not establish whether this format is permitted in the examination. It is not described as exam-approved.</p><div class="sheet-actions"><a class="button-primary" href="#cheat-sheet" data-pdf-view target="_blank" rel="noopener">View PDF ↗</a><a class="button-secondary" href="#cheat-sheet" data-pdf-download>Download PDF ↓</a></div><p class="screen-note">Two PDF pages · 8.5 × 11 inches each · Print at actual size (100%) · Duplex, flip on the long edge.</p><div class="sheet-previews">${[1,2].map(i=>`<figure><figcaption>Side ${i} of 2</figcaption><img data-sheet-side="${i}" alt="Printable study reference, side ${i}; use View PDF for selectable text and full-resolution mathematics."></figure>`).join('')}</div></article>`;}
let printDetails=[];
window.addEventListener('beforeprint',()=>{printDetails=[...main.querySelectorAll('details.solution,details.worked-solution,details.proof-detail')].map(d=>[d,d.open]);for(const [d] of printDetails)d.open=true;});
window.addEventListener('afterprint',()=>{for(const [d,open] of printDetails)d.open=open;printDetails=[];});
