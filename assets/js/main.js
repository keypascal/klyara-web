/* Klyara v3 motion. Vanilla, dependency-free, reduced-motion safe. */
(function(){
"use strict";
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var touch=matchMedia('(pointer: coarse)').matches;

/* veil preloader (first visit per session) */
var veil=document.getElementById('veil');
if(veil){
  if(reduce||sessionStorage.getItem('k3')){veil.classList.add('sweep');veil.classList.add('off');}
  else{setTimeout(function(){veil.classList.add('off');sessionStorage.setItem('k3','1');},420);}
  window.__veilSweep=function(cb){
    if(reduce){cb();return}
    veil.classList.add('sweep');veil.classList.remove('off');veil.style.transformOrigin='bottom';
    setTimeout(function(){cb();veil.style.transformOrigin='top';veil.classList.add('off');},340);
  };
}

/* inertia smooth scroll (desktop only — explicit touch guard) */
var isTouchDevice = matchMedia('(pointer: coarse)').matches || 'ontouchstart' in window || navigator.maxTouchPoints > 0;
var isNarrow = matchMedia('(max-width: 1060px)').matches;
if(!reduce && !isTouchDevice && !isNarrow){
  var target=window.scrollY, current=target, raf=null;
  var max=function(){return document.documentElement.scrollHeight-innerHeight};
  addEventListener('wheel',function(e){
    if(e.ctrlKey) return;
    e.preventDefault();
    target=Math.max(0,Math.min(max(),target+e.deltaY));
    if(!raf) raf=requestAnimationFrame(step);
  },{passive:false});
  function step(){
    current+=(target-current)*0.11;
    if(Math.abs(target-current)<0.5){current=target;raf=null}
    else raf=requestAnimationFrame(step);
    scrollTo(0,current);
  }
  addEventListener('scroll',function(){ if(!raf){target=current=window.scrollY} },{passive:true});
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="#"]'); if(!a) return;
    var id=a.getAttribute('href'); if(id.indexOf('#/')===0) return;
    var el=document.querySelector(id); if(!el) return;
    e.preventDefault();
    target=el.getBoundingClientRect().top+window.scrollY-86;
    if(!raf) raf=requestAnimationFrame(step);
    history.pushState(null,'',id);
  });
}

/* progress + header hide/show */
var prog=document.getElementById('progress'), hdr=document.querySelector('.hdr'), lastY=0;
addEventListener('scroll',function(){
  var y=window.scrollY, h=document.documentElement.scrollHeight-innerHeight;
  if(prog) prog.style.width=(h>0? (y/h*100):0)+'%';
  if(hdr){ hdr.classList.toggle('hide', y>150 && y>lastY && !document.body.classList.contains('nav-open')); lastY=y; }
},{passive:true});

/* burger */
var burger=document.querySelector('.burger');
if(burger){ burger.addEventListener('click',function(){ document.body.classList.toggle('nav-open');
  burger.setAttribute('aria-expanded',document.body.classList.contains('nav-open')); });
  document.querySelectorAll('.nav a').forEach(function(a){a.addEventListener('click',function(){
    if(a.classList.contains('mega-t')) return;  /* accordion parents handled separately */
    document.body.classList.remove('nav-open');
  })});
}

/* reveal system (one config) */
function watch(sel,cb,thr){ var io=new IntersectionObserver(function(es){es.forEach(function(e){ if(e.isIntersecting){cb(e.target); io.unobserve(e.target);} })},{threshold:thr||0.16,rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll(sel).forEach(function(el){io.observe(el)}); return io; }
if('IntersectionObserver' in window && !reduce){
  watch('[data-reveal],[data-stagger],.diag,.ticks',function(el){el.classList.add('in')});
  watch('.ws,.cs',function(el){el.classList.add('go')},0.3);
  watch('.brandfill',function(el){el.classList.add('in')},0.05);
}else{
  document.querySelectorAll('[data-reveal],[data-stagger],.diag,.ticks,.brandfill').forEach(function(el){el.classList.add('in')});
  document.querySelectorAll('.ws,.cs').forEach(function(el){el.classList.add('go')});
}

/* word-split */
document.querySelectorAll('.ws[data-split]:not([data-done])').forEach(function(h){h.setAttribute('data-done','1');
  var delay=0;
  h.innerHTML=h.textContent.trim().split(/\s+/).map(function(w){
    return '<span class="w"><i style="transition-delay:'+(delay+=0.055)+'s">'+w+'</i></span>';
  }).join(' ');
});
/* char-split */
document.querySelectorAll('.cs[data-chars]:not([data-done])').forEach(function(h){h.setAttribute('data-done','1');
  var d=0;
  h.innerHTML=h.textContent.trim().split(/\s+/).map(function(w){
    var chars=w.split('').map(function(ch){
      d+=0.024;
      return '<span class="c"><i style="transition-delay:'+d.toFixed(3)+'s">'+ch+'</i></span>';
    }).join('');
    return '<span style="white-space:nowrap">'+chars+'</span>';
  }).join(' ');
});
setTimeout(function(){document.querySelectorAll('.hero .ws,.hero .cs').forEach(function(h){h.classList.add('go')})},120);

/* horizontal pan */
(function(){
  var hp=document.querySelector('.hpan'); if(!hp) return;
  var track=hp.querySelector('.hpan-track');
  function setup(){
    if(matchMedia('(max-width:860px)').matches||reduce){hp.style.height='';track.style.transform='';return}
    var extra=track.scrollWidth-innerWidth;
    hp.style.height=(extra+innerHeight)+'px';
  }
  function onScroll(){
    if(matchMedia('(max-width:860px)').matches||reduce) return;
    var r=hp.getBoundingClientRect();
    var extra=track.scrollWidth-innerWidth;
    var prog=Math.max(0,Math.min(1,(-r.top)/(r.height-innerHeight)));
    track.style.transform='translateX('+(-prog*extra)+'px)';
  }
  setup(); addEventListener('resize',setup);
  addEventListener('scroll',onScroll,{passive:true}); onScroll();
})();

/* marquee dup */
document.querySelectorAll('.mq-track').forEach(function(t){t.innerHTML+=t.innerHTML});

/* countdown */
document.querySelectorAll('[data-countdown]').forEach(function(el){
  var tgt=new Date(el.getAttribute('data-countdown')+'T00:00:00');
  var q=function(k){return el.querySelector('[data-c="'+k+'"]')};
  function tick(){ var d=Math.max(0,tgt-new Date());
    var dd=Math.floor(d/864e5),hh=Math.floor(d%864e5/36e5),mm=Math.floor(d%36e5/6e4),ss=Math.floor(d%6e4/1e3);
    if(q('d'))q('d').textContent=dd; if(q('h'))q('h').textContent=String(hh).padStart(2,'0');
    if(q('m'))q('m').textContent=String(mm).padStart(2,'0'); if(q('s'))q('s').textContent=String(ss).padStart(2,'0');
  } tick(); setInterval(tick,1000);
});

/* count-up */
if('IntersectionObserver' in window){
  var cio=new IntersectionObserver(function(es){es.forEach(function(e){ if(!e.isIntersecting)return;
    var el=e.target,end=parseFloat(el.getAttribute('data-count')),suf=el.getAttribute('data-suffix')||'',t0=null;
    if(reduce){el.textContent=end+suf;cio.unobserve(el);return}
    (function f(ts){ if(!t0)t0=ts; var p=Math.min((ts-t0)/1100,1),e2=1-Math.pow(1-p,3);
      el.textContent=Math.round(end*e2)+suf; if(p<1)requestAnimationFrame(f); })(performance.now());
    cio.unobserve(el);
  })},{threshold:.6});
  document.querySelectorAll('[data-count]').forEach(function(el){cio.observe(el)});
}

/* MTD checker */
var ck=document.querySelector('[data-checker]');
if(ck){
  var out=ck.querySelector('.cout'),verdict=ck.querySelector('.verdict'),detail=ck.querySelector('.detail');
  var ans={type:null,income:null};
  var copy={
    under:{v:'You are <em>not in MTD yet</em>, but the net is closing.',d:'Below \u00a320,000 qualifying income you are outside Making Tax Digital for now. HMRC has signalled the direction of travel, and clean digital records already speed up CIS refunds. Getting ahead while it is optional is the cheap way to do it.'},
    b2028:{v:'You join MTD in <em>April 2028</em>.',d:'Between \u00a320,000 and \u00a330,000 qualifying income you will keep digital records and file quarterly updates from April 2028. Lock a founding Solo rate now and the switch becomes a non-event.'},
    b2027:{v:'You join MTD in <em>April 2027</em>. That is the next wave.',d:'Between \u00a330,000 and \u00a350,000 you are in the April 2027 intake: digital records, four quarterly updates and a final declaration, every year. Remember it counts gross income before CIS deductions, so most working subbies clear \u00a330k. Join the Solo waitlist and your first quarter files itself.'},
    live:{v:'You are in MTD <em>right now</em>.',d:'Over \u00a350,000 qualifying income means Making Tax Digital for Income Tax has applied to you since April 2026. If you are not filing quarterly through recognised software, penalty points are a live risk. Book a call this week. Catch-up is our specialty.'},
    ltd:{v:'Limited company? <em>MTD for Income Tax is not your fight.</em> CIS and VAT are.',d:'MTD for Income Tax targets sole traders and landlords. As a Ltd construction firm your battles are CIS returns, the VAT domestic reverse charge and monthly figures, exactly what Start, Trade and Pro handle. Your sole-trader subbies are in scope though. Send them our way.'}
  };
  function judge(){ if(!ans.type||!ans.income) return; var k;
    if(ans.type==='ltd')k='ltd'; else if(ans.income==='u20')k='under'; else if(ans.income==='20-30')k='b2028';
    else if(ans.income==='30-50')k='b2027'; else k='live';
    verdict.innerHTML=copy[k].v; detail.textContent=copy[k].d; out.classList.add('show');
  }
  ck.querySelectorAll('.chp').forEach(function(c){ c.addEventListener('click',function(){
    var g=c.getAttribute('data-g'); ans[g]=c.getAttribute('data-v');
    ck.querySelectorAll('.chp[data-g="'+g+'"]').forEach(function(x){x.classList.remove('sel')});
    c.classList.add('sel'); judge();
  })});
}

/* portal tabs + auto-cycle */
document.querySelectorAll('.portal').forEach(function(p){
  var tabs=p.querySelectorAll('.ptab'),views=p.querySelectorAll('.pv'),idx=0,user=false;
  function go(i){ idx=i;
    tabs.forEach(function(x,j){x.setAttribute('aria-selected',j===i?'true':'false')});
    views.forEach(function(v,j){v.classList.toggle('on',j===i)});
  }
  tabs.forEach(function(t,i){ t.addEventListener('click',function(){user=true;go(i)}) });
  if(!reduce && tabs.length>1){
    var vis=true;
    if('IntersectionObserver' in window){
      new IntersectionObserver(function(es){es.forEach(function(e){vis=e.isIntersecting})},{threshold:.2}).observe(p);
    }
    var hov=false;
    p.addEventListener('pointerenter',function(){hov=true});
    p.addEventListener('pointerleave',function(){hov=false});
    setInterval(function(){ if(!user && !hov && vis && !document.hidden) go((idx+1)%tabs.length); },3800);
  }
});

/* scrollytelling steps */
var stps=document.querySelectorAll('.stp');
if(stps.length && 'IntersectionObserver' in window){
  var bar=document.querySelector('.railbar>i');
  var sio=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){ stps.forEach(function(s){s.classList.remove('on')});
      e.target.classList.add('on');
      var idx=[].indexOf.call(stps,e.target);
      if(bar)bar.style.transform='scaleX('+((idx+1)/stps.length)+')';
    }
  })},{rootMargin:'-42% 0px -42% 0px'});
  stps.forEach(function(s){sio.observe(s)});
}

/* magnetic buttons (desktop) */
if(!reduce && !isTouchDevice){
  document.querySelectorAll('.btn-solid,.btn-lg').forEach(function(b){
    b.addEventListener('pointermove',function(e){
      var r=b.getBoundingClientRect(),x=(e.clientX-r.left-r.width/2)/r.width,y=(e.clientY-r.top-r.height/2)/r.height;
      b.style.transform='translate('+x*7+'px,'+y*6+'px)';
    });
    b.addEventListener('pointerleave',function(){b.style.transform=''});
  });
}

/* forms: demo mode until Brevo action wired */
document.querySelectorAll('form[data-demo]').forEach(function(f){
  f.addEventListener('submit',function(ev){ ev.preventDefault();
    var em=f.querySelector('input[type="email"]');
    if(em && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value)){em.focus();em.style.borderColor='#A6592E';return}
    for(var i=0;i<f.elements.length;i++)f.elements[i].disabled=true;
    var ok=f.querySelector('.okmsg'); if(ok)ok.classList.add('show');
    var dl=f.getAttribute('data-download'); if(dl)setTimeout(function(){location.href=dl},900);
  });
});

/* v4: sliders */
document.querySelectorAll('[data-slider]:not([data-w])').forEach(function(sl){sl.setAttribute('data-w','1');
  var slides=sl.querySelectorAll('.slide'),dots=sl.querySelectorAll('.sl-dot'),i=0,t=null,hov=false,vis=true;
  function go(n){ i=(n+slides.length)%slides.length;
    slides.forEach(function(s,j){s.classList.toggle('on',j===i)});
    dots.forEach(function(d,j){d.classList.remove('on'); if(j===i){void d.offsetWidth; d.classList.add('on');}});
  }
  function arm(){ clearInterval(t); if(reduce||slides.length<2)return;
    t=setInterval(function(){ if(!hov&&vis&&!document.hidden) go(i+1); },5000); }
  sl.querySelectorAll('[data-next]').forEach(function(b){b.addEventListener('click',function(){go(i+1);arm()})});
  sl.querySelectorAll('[data-prev]').forEach(function(b){b.addEventListener('click',function(){go(i-1);arm()})});
  dots.forEach(function(d,j){d.addEventListener('click',function(){go(j);arm()})});
  sl.addEventListener('pointerenter',function(){hov=true});
  sl.addEventListener('pointerleave',function(){hov=false});
  if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){vis=e.isIntersecting})},{threshold:.2}).observe(sl);}
  go(0); arm();
});
/* v4: card tilt */
if(!reduce && !isTouchDevice){
  document.querySelectorAll('.tilt').forEach(function(c){
    c.addEventListener('pointermove',function(e){
      var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
      c.style.transform='perspective(900px) rotateY('+x*5+'deg) rotateX('+(-y*5)+'deg) translateY(-4px)';
    });
    c.addEventListener('pointerleave',function(){c.style.transform=''});
  });
}
/* v4: mega menu */
(function(){
  var t=document.querySelector('.mega-t'), m=document.querySelector('.mega');
  var isMobile=function(){ return matchMedia('(max-width:1060px)').matches; };
  var open=false, hideT=null;
  function set(o){ open=o; if(m){m.classList.toggle('open',o);} if(t){t.classList.toggle('open',o);} }

  /* Desktop: hover + click for the Services mega panel */
  if(t && m){
    t.addEventListener('click',function(e){ if(isMobile()) return; e.preventDefault(); set(!open); });
    [t,m].forEach(function(el){
      el.addEventListener('pointerenter',function(){ if(isMobile())return; clearTimeout(hideT); set(true); });
      el.addEventListener('pointerleave',function(){ if(isMobile())return; hideT=setTimeout(function(){set(false)},260); });
    });
    document.addEventListener('click',function(e){ if(open && !m.contains(e.target) && !t.contains(e.target)) set(false); });
    m.addEventListener('click',function(e){ if(e.target.closest('a')) set(false); });
  }

  /* Mobile: pull the Services mega panel inline so it can expand as an accordion.
     (On desktop it is position:fixed, so moving it in the DOM is invisible there.) */
  var nav=document.querySelector('.nav');
  function repositionMega(){
    if(!nav || !m || !t) return;
    if(isMobile()){
      if(m.parentElement !== nav){ t.after(m); }
    } else {
      var hdr=document.querySelector('.hdr');
      if(hdr && m.parentElement === nav){ hdr.appendChild(m); }
    }
  }
  repositionMega();
  addEventListener('resize',repositionMega);

  /* Mobile accordion: Services + Tools + Resources toggle inline */
  document.querySelectorAll('.nav .mega-t').forEach(function(link){
    link.addEventListener('click',function(e){
      if(!isMobile()) return;
      e.preventDefault();
      var parent=link.parentElement;
      var drop=parent.classList.contains('ndrop') ? parent : m;
      var was=drop.classList.contains('open');
      document.querySelectorAll('.nav .ndrop.open, .nav .mega.open, .nav .mega-t.open').forEach(function(d){ d.classList.remove('open'); });
      if(!was){ drop.classList.add('open'); link.classList.add('open'); }
    });
  });

  /* Close accordions when tapping outside the nav */
  document.addEventListener('click',function(e){
    if(!isMobile()) return;
    if(!e.target.closest('.nav')){
      document.querySelectorAll('.nav .ndrop.open, .nav .mega.open, .nav .mega-t.open').forEach(function(d){ d.classList.remove('open'); });
    }
  });
})();
/* v6: animated headers */
(function(){var hs=document.querySelectorAll('h1.h1,h2.h1');
 hs.forEach(function(h){ if(h.dataset.aw) return; h.dataset.aw='1';
   (function walk(n){ Array.prototype.slice.call(n.childNodes).forEach(function(c){
     if(c.nodeType===3 && c.textContent.trim()){
       var frag=document.createDocumentFragment();
       c.textContent.split(/(\s+)/).forEach(function(w){
         if(!w.trim()){frag.appendChild(document.createTextNode(w));return;}
         var o=document.createElement('span');o.className='aw';
         var i=document.createElement('span');i.textContent=w;o.appendChild(i);frag.appendChild(o);
       }); n.replaceChild(frag,c);
     } else if(c.nodeType===1 && c.tagName!=='BR') walk(c);
   });})(h);
   var sp=h.querySelectorAll('.aw>span');sp.forEach(function(s,i){s.style.transitionDelay=(i*55)+'ms'});
 });
 if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('hin');io.unobserve(e.target)}})},{threshold:.35});
  hs.forEach(function(h){io.observe(h)});} else hs.forEach(function(h){h.classList.add('hin')});
})();
/* v6: count-up numbers */
(function(){var els=document.querySelectorAll('[data-count]'); if(!els.length) return;
 function run(el){var end=parseFloat(el.dataset.count),suf=el.dataset.suffix||'',pre=el.dataset.prefix||'',t0=null,dur=1200;
   function step(t){ if(!t0)t0=t; var p=Math.min((t-t0)/dur,1); p=1-Math.pow(1-p,3);
     el.textContent=pre+Math.round(end*p)+suf; if(p<1) requestAnimationFrame(step);}
   requestAnimationFrame(step);}
 if(reduce){els.forEach(function(e){e.textContent=(e.dataset.prefix||'')+e.dataset.count+(e.dataset.suffix||'')});return;}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target)}})},{threshold:.6});
 els.forEach(function(e){io.observe(e)});
})();
/* v7: mark reveals for anim pack */
(function(){ if(!('IntersectionObserver' in window)) return;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.3});
 document.querySelectorAll('[data-reveal],[data-stagger],.plate,.kicker,section.sec').forEach(function(el){io.observe(el)});
})();
/* v6: accordions */

/* v8: charts */
(function(){var cs=document.querySelectorAll('.chart'); if(!cs.length)return;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.4});
 cs.forEach(function(c){io.observe(c)});})();
/* v6: mtd waves */
(function(){var ws=document.querySelectorAll('.wave'); if(!ws.length)return;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.5});
 ws.forEach(function(w){io.observe(w)});})();
/* v5: app demo cycler */
document.querySelectorAll('[data-cycle]:not([data-w])').forEach(function(dm){dm.setAttribute('data-w','1');
  var steps=dm.querySelectorAll('.dstep'),dots=dm.querySelectorAll('.dm-dot'),i=0,vis=true;
  function go(n){ i=n%steps.length;
    steps.forEach(function(s,j){s.classList.toggle('on',j===i)});
    dots.forEach(function(d,j){d.classList.remove('on'); if(j===i){void d.offsetWidth; d.classList.add('on');}});
    steps[i].querySelectorAll('.dbar i').forEach(function(b){b.style.animation='none';void b.offsetWidth;b.style.animation=''});
  }
  var tabs=document.createElement('div');tabs.className='dm-tabs';
  steps.forEach(function(s,j){var t=document.createElement('button');t.className='dm-tab'+(j===0?' on':'');
    var h=s.querySelector('.h6d,h6,.h5,h5,.dm-h');var lab=h?h.textContent.replace(/\s*[·].*$/,'').trim():'';
    if(!lab){var d=s.querySelector('.dr span');lab=d?d.textContent.trim():''}
    if(lab.length>22){var cut=lab.slice(0,22);var sp=cut.lastIndexOf(' ');lab=(sp>8?cut.slice(0,sp):cut).replace(/[,&:;-]+$/,'').trim()}
    t.textContent=lab||'Overview';
    t.addEventListener('click',function(ev){ev.stopPropagation();go(j)});tabs.appendChild(t);});
  dm.insertBefore(tabs, dm.querySelector('.dm-body'));
  var tbs=tabs.querySelectorAll('.dm-tab');
  var _go=go; go=function(n){_go(n);tbs.forEach(function(t,j){t.classList.toggle('on',j===i)});};
  if(!reduce){ setInterval(function(){ if(vis&&!document.hidden) go(i+1); },4200); }
  if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){vis=e.isIntersecting})},{threshold:.25}).observe(dm);}
  dm.addEventListener('click',function(){go(i+1)});
});
/* v5: swipe for sliders */
document.querySelectorAll('[data-slider]').forEach(function(sl){
  var x0=null;
  sl.addEventListener('pointerdown',function(e){x0=e.clientX});
  sl.addEventListener('pointerup',function(e){ if(x0===null)return; var dx=e.clientX-x0; x0=null;
    if(Math.abs(dx)>42){ var b=sl.querySelector(dx<0?'[data-next]':'[data-prev]'); if(b) b.click(); }});
});
document.querySelectorAll('[data-year]').forEach(function(el){el.textContent=new Date().getFullYear()});
})();

/* v12: topbar rotation */
(function(){var ms=[].slice.call(document.querySelectorAll('.tb-m')); if(ms.length<2) return;
 if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
 var i=0; setInterval(function(){ms[i].classList.remove('on'); i=(i+1)%ms.length; ms[i].classList.add('on')},4200);})();
/* v12: FAQ + accordion delegation (fixes dead arrows) */
document.addEventListener('click',function(e){
  var q=e.target.closest('.fx-q');
  if(q){var it=q.closest('.fx-i'); var open=it.classList.toggle('open'); q.setAttribute('aria-expanded',open?'true':'false'); return}
  var h=e.target.closest('.acc-h');
  if(h){var g=h.closest('.acc-g'); var was=g.classList.contains('open');
    var wrap=g.parentElement;
    [].forEach.call(wrap.children,function(x){if(x.classList&&x.classList.contains('acc-g'))x.classList.remove('open')});
    if(!was){g.classList.add('open')}
  }
});

/* v14: open accordion category from hash / TOC */
(function(){
  function openHash(){
    var id=location.hash.slice(1); if(!id) return;
    var g=document.getElementById(id);
    if(g && g.classList.contains('acc-g')){
      [].forEach.call(g.parentElement.children,function(x){if(x.classList&&x.classList.contains('acc-g'))x.classList.remove('open')});
      g.classList.add('open');
    }
  }
  addEventListener('hashchange',openHash); openHash();
})();

(function(){var h=document.querySelector('.hdr');if(!h)return;
function m(){document.documentElement.style.setProperty('--menutop', h.getBoundingClientRect().bottom+'px')}
m();addEventListener('resize',m,{passive:true});addEventListener('scroll',m,{passive:true});})();

(function(){document.querySelectorAll('.dm-tabs').forEach(function(tabs){
  var obs=new MutationObserver(function(){var on=tabs.querySelector('.dm-tab.on');
    if(on&&tabs.scrollWidth>tabs.clientWidth){var l=on.offsetLeft-(tabs.clientWidth-on.offsetWidth)/2;
      tabs.scrollTo({left:Math.max(0,l),behavior:'smooth'})}});
  obs.observe(tabs,{attributes:true,subtree:true,attributeFilter:['class']});});})();
