var swfmini=function(){function a(){if(!B){try{var a=v.getElementsByTagName("body")[0].appendChild(l("span"));a.parentNode.removeChild(a)}catch(b){return}B=!0;for(var c=y.length,d=0;c>d;d++)y[d]()}}function b(a){B?a():y[y.length]=a}function c(){}function d(){x&&e()}function e(){var a=v.getElementsByTagName("body")[0],b=l(p);b.setAttribute("type",t);var c=a.appendChild(b);if(c){var d=0;!function(){if(typeof c.GetVariable!=o){var e=c.GetVariable("$version");e&&(e=e.split(" ")[1].split(","),D.pv=[parseInt(e[0],10),parseInt(e[1],10),parseInt(e[2],10)])}else if(10>d)return d++,setTimeout(arguments.callee,10),void 0;a.removeChild(b),c=null}()}}function f(a){var b=null,c=k(a);if(c&&"OBJECT"==c.nodeName)if(typeof c.SetVariable!=o)b=c;else{var d=c.getElementsByTagName(p)[0];d&&(b=d)}return b}function g(a,b,c){var d,e=k(c);if(D.wk&&D.wk<312)return d;if(e)if(typeof a.id==o&&(a.id=c),D.ie&&D.win){var f="";for(var g in a)a[g]!=Object.prototype[g]&&("data"==g.toLowerCase()?b.movie=a[g]:"styleclass"==g.toLowerCase()?f+=' class="'+a[g]+'"':"classid"!=g.toLowerCase()&&(f+=" "+g+'="'+a[g]+'"'));var i="";for(var j in b)b[j]!=Object.prototype[j]&&(i+='<param name="'+j+'" value="'+b[j]+'" />');e.outerHTML='<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"'+f+">"+i+"</object>",z[z.length]=a.id,d=k(a.id)}else{var m=l(p);m.setAttribute("type",t);for(var n in a)a[n]!=Object.prototype[n]&&("styleclass"==n.toLowerCase()?m.setAttribute("class",a[n]):"classid"!=n.toLowerCase()&&m.setAttribute(n,a[n]));for(var q in b)b[q]!=Object.prototype[q]&&"movie"!=q.toLowerCase()&&h(m,q,b[q]);e.parentNode.replaceChild(m,e),d=m}return d}function h(a,b,c){var d=l("param");d.setAttribute("name",b),d.setAttribute("value",c),a.appendChild(d)}function i(a){var b=k(a);b&&"OBJECT"==b.nodeName&&(D.ie&&D.win?(b.style.display="none",function(){4==b.readyState?j(a):setTimeout(arguments.callee,10)}()):b.parentNode.removeChild(b))}function j(a){var b=k(a);if(b){for(var c in b)"function"==typeof b[c]&&(b[c]=null);b.parentNode.removeChild(b)}}function k(a){var b=null;try{b=v.getElementById(a)}catch(c){}return b}function l(a){return v.createElement(a)}function m(a){var b=D.pv,c=a.split(".");return c[0]=parseInt(c[0],10),c[1]=parseInt(c[1],10)||0,c[2]=parseInt(c[2],10)||0,b[0]>c[0]||b[0]==c[0]&&b[1]>c[1]||b[0]==c[0]&&b[1]==c[1]&&b[2]>=c[2]?!0:!1}function n(a,b){if(C){var c,d=b?"visible":"hidden";B&&c&&k(a)&&(k(a).style.visibility=d)}}{var o="undefined",p="object",q=window.webshims,r="Shockwave Flash",s="ShockwaveFlash.ShockwaveFlash",t="application/x-shockwave-flash",u=window,v=document,w=navigator,x=!1,y=[d],z=[],A=[],B=!1,C=!0,D=function(){var a=typeof v.getElementById!=o&&typeof v.getElementsByTagName!=o&&typeof v.createElement!=o,b=w.userAgent.toLowerCase(),c=w.platform.toLowerCase(),d=c?/win/.test(c):/win/.test(b),e=c?/mac/.test(c):/mac/.test(b),f=/webkit/.test(b)?parseFloat(b.replace(/^.*webkit\/(\d+(\.\d+)?).*$/,"$1")):!1,g=!1,h=[0,0,0],i=null;if(typeof w.plugins!=o&&typeof w.plugins[r]==p)i=w.plugins[r].description,!i||typeof w.mimeTypes!=o&&w.mimeTypes[t]&&!w.mimeTypes[t].enabledPlugin||(x=!0,g=!1,i=i.replace(/^.*\s+(\S+\s+\S+$)/,"$1"),h[0]=parseInt(i.replace(/^(.*)\..*$/,"$1"),10),h[1]=parseInt(i.replace(/^.*\.(.*)\s.*$/,"$1"),10),h[2]=/[a-zA-Z]/.test(i)?parseInt(i.replace(/^.*[a-zA-Z]+(.*)$/,"$1"),10):0);else if(typeof u.ActiveXObject!=o)try{var j=new ActiveXObject(s);j&&(i=j.GetVariable("$version"),i&&(g=!0,i=i.split(" ")[1].split(","),h=[parseInt(i[0],10),parseInt(i[1],10),parseInt(i[2],10)]))}catch(k){}return{w3:a,pv:h,wk:f,ie:g,win:d,mac:e}}();!function(){D.ie&&D.win&&window.attachEvent&&window.attachEvent("onunload",function(){for(var a=A.length,b=0;a>b;b++)A[b][0].detachEvent(A[b][1],A[b][2]);for(var c=z.length,d=0;c>d;d++)i(z[d]);for(var e in D)D[e]=null;D=null;for(var f in swfmini)swfmini[f]=null;swfmini=null})}()}return q.ready("DOM",a),{registerObject:function(){},getObjectById:function(a){return D.w3?f(a):void 0},embedSWF:function(a,c,d,e,f,h,i,j,k,l){var q={success:!1,id:c};D.w3&&!(D.wk&&D.wk<312)&&a&&c&&d&&e&&f?(n(c,!1),b(function(){d+="",e+="";var b={};if(k&&typeof k===p)for(var h in k)b[h]=k[h];b.data=a,b.width=d,b.height=e;var r={};if(j&&typeof j===p)for(var s in j)r[s]=j[s];if(i&&typeof i===p)for(var t in i)typeof r.flashvars!=o?r.flashvars+="&"+t+"="+i[t]:r.flashvars=t+"="+i[t];if(m(f)){var u=g(b,r,c);b.id==c&&n(c,!0),q.success=!0,q.ref=u}else n(c,!0);l&&l(q)})):l&&l(q)},switchOffAutoHideShow:function(){C=!1},ua:D,getFlashPlayerVersion:function(){return{major:D.pv[0],minor:D.pv[1],release:D.pv[2]}},hasFlashPlayerVersion:m,createSWF:function(a,b,c){return D.w3?g(a,b,c):void 0},showExpressInstall:function(){},removeSWF:function(a){D.w3&&i(a)},createCSS:function(){},addDomLoadEvent:b,addLoadEvent:c,expressInstallCallback:function(){}}}();webshims.register("dom-extend",function(a,b,c,d,e){"use strict";var f=!("hrefNormalized"in a.support)||a.support.hrefNormalized,g=!("getSetAttribute"in a.support)||a.support.getSetAttribute,h=Object.prototype.hasOwnProperty;if(b.assumeARIA=g||Modernizr.canvas||Modernizr.video||Modernizr.boxsizing,("text"==a('<input type="email" />').attr("type")||""===a("<form />").attr("novalidate")||"required"in a("<input />")[0].attributes)&&b.error("IE browser modes are busted in IE10+. Please test your HTML/CSS/JS with a real IE version or at least IETester or similiar tools"),"debug"in b&&b.error('Use webshims.setOptions("debug", true||false||"noCombo"); to debug flag'),!b.cfg.no$Switch){var i=function(){if(!c.jQuery||c.$&&c.jQuery!=c.$||c.jQuery.webshims||(b.error("jQuery was included more than once. Make sure to include it only once or try the $.noConflict(extreme) feature! Webshims and other Plugins might not work properly. Or set webshims.cfg.no$Switch to 'true'."),c.$&&(c.$=b.$),c.jQuery=b.$),b.M!=Modernizr){b.error("Modernizr was included more than once. Make sure to include it only once! Webshims and other scripts might not work properly.");for(var a in Modernizr)a in b.M||(b.M[a]=Modernizr[a]);Modernizr=b.M}};i(),setTimeout(i,90),b.ready("DOM",i),a(i),b.ready("WINDOWLOAD",i)}var j=(b.modules,/\s*,\s*/),k={},l={},m={},n={},o={},p={},q=a.fn.val,r=function(b,c,d,e,f){return f?q.call(a(b)):q.call(a(b),d)};a.widget||!function(){var b=a.cleanData;a.cleanData=function(c){if(!a.widget)for(var d,e=0;null!=(d=c[e]);e++)try{a(d).triggerHandler("remove")}catch(f){}b(c)}}(),a.fn.val=function(b){var c=this[0];if(arguments.length&&null==b&&(b=""),!arguments.length)return c&&1===c.nodeType?a.prop(c,"value",b,"val",!0):q.call(this);if(a.isArray(b))return q.apply(this,arguments);var d=a.isFunction(b);return this.each(function(f){if(c=this,1===c.nodeType)if(d){var g=b.call(c,f,a.prop(c,"value",e,"val",!0));null==g&&(g=""),a.prop(c,"value",g,"val")}else a.prop(c,"value",b,"val")})},a.fn.onTrigger=function(a,b){return this.on(a,b).each(b)},a.fn.onWSOff=function(b,c,e,f){return f||(f=d),a(f)[e?"onTrigger":"on"](b,c),this.on("remove",function(d){d.originalEvent||a(f).off(b,c)}),this};var s="_webshimsLib"+Math.round(1e3*Math.random()),t=function(b,c,d){if(b=b.jquery?b[0]:b,!b)return d||{};var f=a.data(b,s);return d!==e&&(f||(f=a.data(b,s,{})),c&&(f[c]=d)),c?f&&f[c]:f};[{name:"getNativeElement",prop:"nativeElement"},{name:"getShadowElement",prop:"shadowElement"},{name:"getShadowFocusElement",prop:"shadowFocusElement"}].forEach(function(b){a.fn[b.name]=function(){var c=[];return this.each(function(){var d=t(this,"shadowData"),e=d&&d[b.prop]||this;-1==a.inArray(e,c)&&c.push(e)}),this.pushStack(c)}}),b.cfg.extendNative||b.cfg.noTriggerOverride||!function(b){a.event.trigger=function(c,d,e,f){if(!m[c]||f||!e||1!==e.nodeType)return b.apply(this,arguments);var g,i,j,k=e[c],l=a.prop(e,c),n=l&&k!=l;return n&&(j="__ws"+c,i=c in e&&h.call(e,c),e[c]=l,e[j]=k),g=b.apply(this,arguments),n&&(i?e[c]=k:delete e[c],delete e[j]),g}}(a.event.trigger),["removeAttr","prop","attr"].forEach(function(c){k[c]=a[c],a[c]=function(b,d,f,g,h){var i="val"==g,j=i?r:k[c];if(!b||!l[d]||1!==b.nodeType||!i&&g&&"attr"==c&&a.attrFn[d])return j(b,d,f,g,h);var m,o,q,s=(b.nodeName||"").toLowerCase(),t=n[s],u="attr"!=c||f!==!1&&null!==f?c:"removeAttr";if(t||(t=n["*"]),t&&(t=t[d]),t&&(m=t[u]),m){if("value"==d&&(o=m.isVal,m.isVal=i),"removeAttr"===u)return m.value.call(b);if(f===e)return m.get?m.get.call(b):m.value;m.set&&("attr"==c&&f===!0&&(f=d),q=m.set.call(b,f)),"value"==d&&(m.isVal=o)}else q=j(b,d,f,g,h);if((f!==e||"removeAttr"===u)&&p[s]&&p[s][d]){var v;v="removeAttr"==u?!1:"prop"==u?!!f:!0,p[s][d].forEach(function(a){(!a.only||(a.only="prop"&&"prop"==c)||"attr"==a.only&&"prop"!=c)&&a.call(b,f,v,i?"val":u,c)})}return q},o[c]=function(a,d,f){n[a]||(n[a]={}),n[a][d]||(n[a][d]={});var g=n[a][d][c],h=function(a,b,e){var g;return b&&b[a]?b[a]:e&&e[a]?e[a]:"prop"==c&&"value"==d?function(a){var b=this;return f.isVal?r(b,d,a,!1,0===arguments.length):k[c](b,d,a)}:"prop"==c&&"value"==a&&f.value.apply?(g="__ws"+d,m[d]=!0,function(){var a=this[g]||k[c](this,d);return a&&a.apply&&(a=a.apply(this,arguments)),a}):function(a){return k[c](this,d,a)}};n[a][d][c]=f,f.value===e&&(f.set||(f.set=f.writeable?h("set",f,g):b.cfg.useStrict&&"prop"==d?function(){throw d+" is readonly on "+a}:function(){b.info(d+" is readonly on "+a)}),f.get||(f.get=h("get",f,g))),["value","get","set"].forEach(function(a){f[a]&&(f["_sup"+a]=h(a,g))})}});var u=function(){var a=b.getPrototypeOf(d.createElement("foobar")),c=Modernizr.advancedObjectProperties&&Modernizr.objectAccessor;return function(e,f,g){var i,j;if(!(c&&(i=d.createElement(e))&&(j=b.getPrototypeOf(i))&&a!==j)||i[f]&&h.call(i,f))g._supvalue=function(){var a=t(this,"propValue");return a&&a[f]&&a[f].apply?a[f].apply(this,arguments):a&&a[f]},v.extendValue(e,f,g.value);else{var k=i[f];g._supvalue=function(){return k&&k.apply?k.apply(this,arguments):k},j[f]=g.value}g.value._supvalue=g._supvalue}}(),v=function(){var c={};b.addReady(function(d,e){var f={},g=function(b){f[b]||(f[b]=a(d.getElementsByTagName(b)),e[0]&&a.nodeName(e[0],b)&&(f[b]=f[b].add(e)))};a.each(c,function(a,c){return g(a),c&&c.forEach?(c.forEach(function(b){f[a].each(b)}),void 0):(b.warn("Error: with "+a+"-property. methods: "+c),void 0)}),f=null});var e,f=a([]),g=function(b,f){c[b]?c[b].push(f):c[b]=[f],a.isDOMReady&&(e||a(d.getElementsByTagName(b))).each(f)};return{createTmpCache:function(b){return a.isDOMReady&&(e=e||a(d.getElementsByTagName(b))),e||f},flushTmpCache:function(){e=null},content:function(b,c){g(b,function(){var b=a.attr(this,c);null!=b&&a.attr(this,c,b)})},createElement:function(a,b){g(a,b)},extendValue:function(b,c,d){g(b,function(){a(this).each(function(){var a=t(this,"propValue",{});a[c]=this[c],this[c]=d})})}}}(),w=function(a,b){a.defaultValue===e&&(a.defaultValue=""),a.removeAttr||(a.removeAttr={value:function(){a[b||"prop"].set.call(this,a.defaultValue),a.removeAttr._supvalue.call(this)}}),a.attr||(a.attr={})};a.extend(b,{getID:function(){var b=(new Date).getTime();return function(c){c=a(c);var d=c.prop("id");return d||(b++,d="ID-"+b,c.eq(0).prop("id",d)),d}}(),implement:function(a,c){var d=t(a,"implemented")||t(a,"implemented",{});return d[c]?(b.warn(c+" already implemented for element #"+a.id),!1):(d[c]=!0,!0)},extendUNDEFProp:function(b,c){a.each(c,function(a,c){a in b||(b[a]=c)})},createPropDefault:w,data:t,moveToFirstEvent:function(b,c,d){var e,f=(a._data(b,"events")||{})[c];f&&f.length>1&&(e=f.pop(),d||(d="bind"),"bind"==d&&f.delegateCount?f.splice(f.delegateCount,0,e):f.unshift(e)),b=null},addShadowDom:function(){var e,f,g,h={init:!1,runs:0,test:function(){var a=h.getHeight(),b=h.getWidth();a!=h.height||b!=h.width?(h.height=a,h.width=b,h.handler({type:"docresize"}),h.runs++,h.runs<9&&setTimeout(h.test,90)):h.runs=0},handler:function(b){clearTimeout(e),e=setTimeout(function(){if("resize"==b.type){var e=a(c).width(),i=a(c).width();if(i==f&&e==g)return;f=i,g=e,h.height=h.getHeight(),h.width=h.getWidth()}a(d).triggerHandler("updateshadowdom")},"resize"==b.type?50:9)},_create:function(){a.each({Height:"getHeight",Width:"getWidth"},function(a,b){var c=d.body,e=d.documentElement;h[b]=function(){return Math.max(c["scroll"+a],e["scroll"+a],c["offset"+a],e["offset"+a],e["client"+a])}})},start:function(){!this.init&&d.body&&(this.init=!0,this._create(),this.height=h.getHeight(),this.width=h.getWidth(),setInterval(this.test,600),a(this.test),b.ready("WINDOWLOAD",this.test),a(d).on("updatelayout",this.handler),a(c).on("resize",this.handler),function(){var b,c=a.fn.animate;a.fn.animate=function(){return clearTimeout(b),b=setTimeout(function(){h.test()},99),c.apply(this,arguments)}}())}};return b.docObserve=function(){b.ready("DOM",function(){h.start(),null==a.support.boxSizing&&a(function(){a.support.boxSizing&&h.handler({type:"boxsizing"})})})},function(c,d,e){if(c&&d){e=e||{},c.jquery&&(c=c[0]),d.jquery&&(d=d[0]);var f=a.data(c,s)||a.data(c,s,{}),g=a.data(d,s)||a.data(d,s,{}),h={};e.shadowFocusElement?e.shadowFocusElement&&(e.shadowFocusElement.jquery&&(e.shadowFocusElement=e.shadowFocusElement[0]),h=a.data(e.shadowFocusElement,s)||a.data(e.shadowFocusElement,s,h)):e.shadowFocusElement=d,a(c).on("remove",function(b){b.originalEvent||setTimeout(function(){a(d).remove()},4)}),f.hasShadow=d,h.nativeElement=g.nativeElement=c,h.shadowData=g.shadowData=f.shadowData={nativeElement:c,shadowElement:d,shadowFocusElement:e.shadowFocusElement},e.shadowChilds&&e.shadowChilds.each(function(){t(this,"shadowData",g.shadowData)}),e.data&&(h.shadowData.data=g.shadowData.data=f.shadowData.data=e.data),e=null}b.docObserve()}}(),propTypes:{standard:function(a){w(a),a.prop||(a.prop={set:function(b){a.attr.set.call(this,""+b)},get:function(){return a.attr.get.call(this)||a.defaultValue}})},"boolean":function(a){w(a),a.prop||(a.prop={set:function(b){b?a.attr.set.call(this,""):a.removeAttr.value.call(this)},get:function(){return null!=a.attr.get.call(this)}})},src:function(){var b=d.createElement("a");return b.style.display="none",function(c,d){w(c),c.prop||(c.prop={set:function(a){c.attr.set.call(this,a)},get:function(){var c,e=this.getAttribute(d);if(null==e)return"";if(b.setAttribute("href",e+""),!f){try{a(b).insertAfter(this),c=b.getAttribute("href",4)}catch(g){c=b.getAttribute("href",4)}a(b).detach()}return c||b.href}})}}(),enumarated:function(a){w(a),a.prop||(a.prop={set:function(b){a.attr.set.call(this,b)},get:function(){var b=(a.attr.get.call(this)||"").toLowerCase();return b&&-1!=a.limitedTo.indexOf(b)||(b=a.defaultValue),b}})}},reflectProperties:function(c,d){"string"==typeof d&&(d=d.split(j)),d.forEach(function(d){b.defineNodeNamesProperty(c,d,{prop:{set:function(b){a.attr(this,d,b)},get:function(){return a.attr(this,d)||""}}})})},defineNodeNameProperty:function(c,d,e){return l[d]=!0,e.reflect&&(e.propType&&!b.propTypes[e.propType]?b.error("could not finde propType "+e.propType):b.propTypes[e.propType||"standard"](e,d)),["prop","attr","removeAttr"].forEach(function(f){var g=e[f];g&&(g="prop"===f?a.extend({writeable:!0},g):a.extend({},g,{writeable:!0}),o[f](c,d,g),"*"!=c&&b.cfg.extendNative&&"prop"==f&&g.value&&a.isFunction(g.value)&&u(c,d,g),e[f]=g)}),e.initAttr&&v.content(c,d),e},defineNodeNameProperties:function(a,c,d,e){for(var f in c)!e&&c[f].initAttr&&v.createTmpCache(a),d&&(c[f][d]||(c[f][d]={},["value","set","get"].forEach(function(a){a in c[f]&&(c[f][d][a]=c[f][a],delete c[f][a])}))),c[f]=b.defineNodeNameProperty(a,f,c[f]);return e||v.flushTmpCache(),c},createElement:function(c,d,e){var f;return a.isFunction(d)&&(d={after:d}),v.createTmpCache(c),d.before&&v.createElement(c,d.before),e&&(f=b.defineNodeNameProperties(c,e,!1,!0)),d.after&&v.createElement(c,d.after),v.flushTmpCache(),f},onNodeNamesPropertyModify:function(b,c,d,e){"string"==typeof b&&(b=b.split(j)),a.isFunction(d)&&(d={set:d}),b.forEach(function(a){p[a]||(p[a]={}),"string"==typeof c&&(c=c.split(j)),d.initAttr&&v.createTmpCache(a),c.forEach(function(b){p[a][b]||(p[a][b]=[],l[b]=!0),d.set&&(e&&(d.set.only=e),p[a][b].push(d.set)),d.initAttr&&v.content(a,b)}),v.flushTmpCache()})},defineNodeNamesBooleanProperty:function(c,d,f){f||(f={}),a.isFunction(f)&&(f.set=f),b.defineNodeNamesProperty(c,d,{attr:{set:function(a){this.setAttribute(d,a),f.set&&f.set.call(this,!0)},get:function(){var a=this.getAttribute(d);return null==a?e:d}},removeAttr:{value:function(){this.removeAttribute(d),f.set&&f.set.call(this,!1)}},reflect:!0,propType:"boolean",initAttr:f.initAttr||!1})},contentAttr:function(a,b,c){if(a.nodeName){var d;return c===e?(d=a.attributes[b]||{},c=d.specified?d.value:null,null==c?e:c):("boolean"==typeof c?c?a.setAttribute(b,b):a.removeAttribute(b):a.setAttribute(b,c),void 0)}},activeLang:function(){var c=[],d=[],e={},f=function(d,f,h){f._isLoading=!0,e[d]?e[d].push(f):(e[d]=[f],b.loader.loadScript(d,function(){h==c.join()&&a.each(e[d],function(a,b){g(b)}),delete e[d]}))},g=function(b){var d=b.__active,e=function(a,d){return b._isLoading=!1,b[d]||-1!=b.availableLangs.indexOf(d)?(b[d]?b.__active=b[d]:f(b.langSrc+d,b,c.join()),!1):void 0};a.each(c,e),b.__active||(b.__active=b[""]),d!=b.__active&&a(b).trigger("change")};return function(a){var b;if("string"==typeof a)c[0]!=a&&(c=[a],b=c[0].split("-")[0],b&&b!=a&&c.push(b),d.forEach(g));else if("object"==typeof a)return a.__active||(d.push(a),g(a)),a.__active;return c[0]}}()}),a.each({defineNodeNamesProperty:"defineNodeNameProperty",defineNodeNamesProperties:"defineNodeNameProperties",createElements:"createElement"},function(a,c){b[a]=function(a,d,e,f){"string"==typeof a&&(a=a.split(j));var g={};return a.forEach(function(a){g[a]=b[c](a,d,e,f)}),g}}),b.isReady("webshimLocalization",!0)}),function(a,b){if(!(!a.webshims.assumeARIA||"content"in b.createElement("template")||(a(function(){var b=a("main").attr({role:"main"});b.length>1?webshims.error("only one main element allowed in document"):b.is("article *, section *")&&webshims.error("main not allowed inside of article/section elements")}),"hidden"in b.createElement("a")))){var c={article:"article",aside:"complementary",section:"region",nav:"navigation",address:"contentinfo"},d=function(a,b){var c=a.getAttribute("role");c||a.setAttribute("role",b)};a.webshims.addReady(function(e,f){if(a.each(c,function(b,c){for(var g=a(b,e).add(f.filter(b)),h=0,i=g.length;i>h;h++)d(g[h],c)}),e===b){var g=b.getElementsByTagName("header")[0],h=b.getElementsByTagName("footer"),i=h.length;if(g&&!a(g).closest("section, article")[0]&&d(g,"banner"),!i)return;var j=h[i-1];a(j).closest("section, article")[0]||d(j,"contentinfo")}})}}(webshims.$,document),webshims.register("form-core",function(a,b,c,d,e,f){"use strict";b.capturingEventPrevented=function(b){if(!b._isPolyfilled){var c=b.isDefaultPrevented,d=b.preventDefault;b.preventDefault=function(){return clearTimeout(a.data(b.target,b.type+"DefaultPrevented")),a.data(b.target,b.type+"DefaultPrevented",setTimeout(function(){a.removeData(b.target,b.type+"DefaultPrevented")},30)),d.apply(this,arguments)},b.isDefaultPrevented=function(){return!(!c.apply(this,arguments)&&!a.data(b.target,b.type+"DefaultPrevented"))},b._isPolyfilled=!0}},Modernizr.formvalidation&&!b.bugs.bustedValidity&&b.capturingEvents(["invalid"],!0);var g=function(b){return(a.prop(b,"validity")||{valid:1}).valid},h=function(){var c=["form-validation"];f.lazyCustomMessages&&(f.customMessages=!0,c.push("form-message")),f.customDatalist&&(f.fD=!0,c.push("form-datalist")),f.addValidators&&c.push("form-validators"),b.reTest(c),a(d).off(".lazyloadvalidation")},i=/^(?:form|fieldset)$/i,j=function(b){var c=!1;return a(b).jProp("elements").each(function(){return!i.test(b.nodeName||"")&&(c=a(this).is(":invalid"))?!1:void 0}),c},k=function(){if(a.extend(a.expr[":"],{"valid-element":function(b){return i.test(b.nodeName||"")?!j(b):!(!a.prop(b,"willValidate")||!g(b))},"invalid-element":function(b){return i.test(b.nodeName||"")?j(b):!(!a.prop(b,"willValidate")||g(b))},"required-element":function(b){return!(!a.prop(b,"willValidate")||!a.prop(b,"required"))},"user-error":function(b){return a.prop(b,"willValidate")&&a(b).hasClass("user-error")},"optional-element":function(b){return!(!a.prop(b,"willValidate")||a.prop(b,"required")!==!1)}}),["valid","invalid","required","optional"].forEach(function(b){a.expr[":"][b]=a.expr[":"][b+"-element"]}),"unknown"==typeof d.activeElement){var c=a.expr[":"].focus;a.expr[":"].focus=function(){try{return c.apply(this,arguments)}catch(a){b.error(a)}return!1}}};a.expr.filters?k():b.ready("sizzle",k),b.triggerInlineForm=function(b,c){a(b).trigger(c)};var l=function(a,c,d){h(),b.ready("form-validation",function(){a[c].apply(a,d)})},m="transitionDelay"in d.documentElement.style?"":" no-transition",n=b.cfg.wspopover;n.position||n.position===!1||(n.position={at:"left bottom",my:"left top",collision:"fit flip"}),b.wsPopover={id:0,_create:function(){this.options=a.extend(!0,{},n,this.options),this.id=b.wsPopover.id++,this.eventns=".wsoverlay"+this.id,this.timers={},this.element=a('<div class="ws-popover'+m+'" tabindex="-1"><div class="ws-po-outerbox"><div class="ws-po-arrow"><div class="ws-po-arrowbox" /></div><div class="ws-po-box" /></div></div>'),this.contentElement=a(".ws-po-box",this.element),this.lastElement=a([]),this.bindElement(),this.element.data("wspopover",this)},options:{},content:function(a){this.contentElement.html(a)},bindElement:function(){var a=this,b=function(){a.stopBlur=!1};this.preventBlur=function(){a.stopBlur=!0,clearTimeout(a.timers.stopBlur),a.timers.stopBlur=setTimeout(b,9)},this.element.on({mousedown:this.preventBlur})},show:function(){l(this,"show",arguments)}},b.validityAlert={showFor:function(){l(this,"showFor",arguments)}},b.getContentValidationMessage=function(c,d,e){b.errorbox&&b.errorbox.initIvalContentMessage&&b.errorbox.initIvalContentMessage(c);var f=a(c).data("errormessage")||c.getAttribute("x-moz-errormessage")||"";return e&&f[e]?f=f[e]:f&&(d=d||a.prop(c,"validity")||{valid:1},d.valid&&(f="")),"object"==typeof f&&(d=d||a.prop(c,"validity")||{valid:1},d.valid||(a.each(d,function(a,b){return b&&"valid"!=a&&f[a]?(f=f[a],!1):void 0}),"object"==typeof f&&(d.typeMismatch&&f.badInput&&(f=f.badInput),d.badInput&&f.typeMismatch&&(f=f.typeMismatch)))),"object"==typeof f&&(f=f.defaultMessage),f||""},a.fn.getErrorMessage=function(c){var d="",e=this[0];return e&&(d=b.getContentValidationMessage(e,!1,c)||a.prop(e,"customValidationMessage")||a.prop(e,"validationMessage")),d},a(d).on("focusin.lazyloadvalidation",function(a){"form"in a.target&&h()}),b.ready("WINDOWLOAD",h)}),webshims.register("form-datalist",function(a,b,c,d,e,f){"use strict";var g=function(a){a&&"string"==typeof a||(a="DOM"),g[a+"Loaded"]||(g[a+"Loaded"]=!0,b.ready(a,function(){b.loader.loadList(["form-datalist-lazy"])}))},h={submit:1,button:1,reset:1,hidden:1,range:1,date:1,month:1};b.modules["form-number-date-ui"].loaded&&a.extend(h,{number:1,time:1}),b.propTypes.element=function(c,e){b.createPropDefault(c,"attr"),c.prop||(c.prop={get:function(){var b=a.attr(this,e);return b&&(b=d.getElementById(b),b&&c.propNodeName&&!a.nodeName(b,c.propNodeName)&&(b=null)),b||null},writeable:!1})},function(){var i=a.webshims.cfg.forms,j=Modernizr.input.list;if(!j||i.customDatalist){var k=function(){var c=function(){var b;!a.data(this,"datalistWidgetData")&&(b=a.prop(this,"id"))?a('input[list="'+b+'"], input[data-wslist="'+b+'"]').eq(0).attr("list",b):a(this).triggerHandler("updateDatalist")},d={autocomplete:{attr:{get:function(){var b=this,c=a.data(b,"datalistWidget");return c?c._autocomplete:"autocomplete"in b?b.autocomplete:b.getAttribute("autocomplete")},set:function(b){var c=this,d=a.data(c,"datalistWidget");d?(d._autocomplete=b,"off"==b&&d.hideList()):"autocomplete"in c?c.autocomplete=b:c.setAttribute("autocomplete",b)}}}};j?((a("<datalist><select><option></option></select></datalist>").prop("options")||[]).length||b.defineNodeNameProperty("datalist","options",{prop:{writeable:!1,get:function(){var b=this.options||[];if(!b.length){var c=this,d=a("select",c);d[0]&&d[0].options&&d[0].options.length&&(b=d[0].options)}return b}}}),d.list={attr:{get:function(){var c=b.contentAttr(this,"list");return null!=c?(a.data(this,"datalistListAttr",c),h[a.prop(this,"type")]||h[a.attr(this,"type")]||this.removeAttribute("list")):c=a.data(this,"datalistListAttr"),null==c?e:c},set:function(c){var d=this;a.data(d,"datalistListAttr",c),h[a.prop(this,"type")]||h[a.attr(this,"type")]?d.setAttribute("list",c):(b.objectCreate(l,e,{input:d,id:c,datalist:a.prop(d,"list")}),d.setAttribute("data-wslist",c)),a(d).triggerHandler("listdatalistchange")}},initAttr:!0,reflect:!0,propType:"element",propNodeName:"datalist"}):b.defineNodeNameProperties("input",{list:{attr:{get:function(){var a=b.contentAttr(this,"list");return null==a?e:a},set:function(c){var d=this;b.contentAttr(d,"list",c),b.objectCreate(f.shadowListProto,e,{input:d,id:c,datalist:a.prop(d,"list")}),a(d).triggerHandler("listdatalistchange")}},initAttr:!0,reflect:!0,propType:"element",propNodeName:"datalist"}}),b.defineNodeNameProperties("input",d),b.addReady(function(a,b){b.filter("datalist > select, datalist, datalist > option, datalist > select > option").closest("datalist").each(c)})},l={_create:function(c){if(!h[a.prop(c.input,"type")]&&!h[a.attr(c.input,"type")]){var d=c.datalist,e=a.data(c.input,"datalistWidget"),f=this;return d&&e&&e.datalist!==d?(e.datalist=d,e.id=c.id,a(e.datalist).off("updateDatalist.datalistWidget").on("updateDatalist.datalistWidget",a.proxy(e,"_resetListCached")),e._resetListCached(),void 0):d?(e&&e.datalist===d||(this.datalist=d,this.id=c.id,this.hasViewableData=!0,this._autocomplete=a.attr(c.input,"autocomplete"),a.data(c.input,"datalistWidget",this),a.data(d,"datalistWidgetData",this),g("WINDOWLOAD"),b.isReady("form-datalist-lazy")?this._lazyCreate(c):(a(c.input).one("focus",g),b.ready("form-datalist-lazy",function(){f._destroyed||f._lazyCreate(c)}))),void 0):(e&&e.destroy(),void 0)}},destroy:function(b){var f,g=a.attr(this.input,"autocomplete");a(this.input).off(".datalistWidget").removeData("datalistWidget"),this.shadowList.remove(),a(d).off(".datalist"+this.id),a(c).off(".datalist"+this.id),this.input.form&&this.input.id&&a(this.input.form).off("submit.datalistWidget"+this.input.id),this.input.removeAttribute("aria-haspopup"),g===e?this.input.removeAttribute("autocomplete"):a(this.input).attr("autocomplete",g),b&&"beforeunload"==b.type&&(f=this.input,setTimeout(function(){a.attr(f,"list",a.attr(f,"list"))},9)),this._destroyed=!0}};b.loader.addModule("form-datalist-lazy",{noAutoCallback:!0,options:a.extend(f,{shadowListProto:l})}),f.list||(f.list={}),k()}}()}),function(a,b){"use strict";var c,d,e=b.$,f=a.audio&&a.video,g=!1,h=b.bugs,i="mediaelement-jaris",j=function(){b.ready(i,function(){b.mediaelement.createSWF||(b.mediaelement.loadSwf=!0,b.reTest([i],f))})},k=b.cfg,l=k.mediaelement;if(!l)return b.error("mediaelement wasn't implemented but loaded"),void 0;if(f){var m=document.createElement("video");if(a.videoBuffered="buffered"in m,a.mediaDefaultMuted="defaultMuted"in m,g="loop"in m,b.capturingEvents(["play","playing","waiting","paused","ended","durationchange","loadedmetadata","canplay","volumechange"]),a.videoBuffered||(b.addPolyfill("mediaelement-native-fix",{d:["dom-support"]}),b.loader.loadList(["mediaelement-native-fix"])),!l.preferFlash){var n={1:1},o=function(a){var c,f,g;!l.preferFlash&&(e(a.target).is("audio, video")||(g=a.target.parentNode)&&e("source",g).last()[0]==a.target)&&(c=e(a.target).closest("audio, video"))&&(f=c.prop("error"))&&!n[f.code]&&e(function(){d&&!l.preferFlash?(j(),b.ready("WINDOWLOAD "+i,function(){setTimeout(function(){l.preferFlash||!b.mediaelement.createSWF||c.is(".nonnative-api-active")||(l.preferFlash=!0,document.removeEventListener("error",o,!0),e("audio, video").each(function(){b.mediaelement.selectSource(this)}),b.error("switching mediaelements option to 'preferFlash', due to an error with native player: "+a.target.src+" Mediaerror: "+c.prop("error")+"first error: "+f))},9)})):document.removeEventListener("error",o,!0)})};document.addEventListener("error",o,!0),e("audio, video").each(function(){var a=e.prop(this,"error");return a&&!n[a]?(o({target:this}),!1):void 0})}}a.track&&!h.track&&!function(){if(h.track||(h.track="number"!=typeof e("<track />")[0].readyState),!h.track)try{new TextTrackCue(2,3,"")}catch(a){h.track=!0}}(),c=a.track&&!h.track,b.register("mediaelement-core",function(b,e,h,k,l,m){d=swfmini.hasFlashPlayerVersion("9.0.115"),b("html").addClass(d?"swf":"no-swf");var n=e.mediaelement;n.parseRtmp=function(a){var b,c,d,f=a.src.split("://"),g=f[1].split("/");for(a.server=f[0]+"://"+g[0]+"/",a.streamId=[],b=1,c=g.length;c>b;b++)d||-1===g[b].indexOf(":")||(g[b]=g[b].split(":")[1],d=!0),d?a.streamId.push(g[b]):a.server+=g[b]+"/";a.streamId.length||e.error("Could not parse rtmp url"),a.streamId=a.streamId.join("/")};var o=function(a,c){a=b(a);var d,e={src:a.attr("src")||"",elem:a,srcProp:a.prop("src")};return e.src?(d=a.attr("data-server"),null!=d&&(e.server=d),d=a.attr("type")||a.attr("data-type"),d?(e.type=d,e.container=b.trim(d.split(";")[0])):(c||(c=a[0].nodeName.toLowerCase(),"source"==c&&(c=(a.closest("video, audio")[0]||{nodeName:"video"}).nodeName.toLowerCase())),e.server?(e.type=c+"/rtmp",e.container=c+"/rtmp"):(d=n.getTypeForSrc(e.src,c,e),d&&(e.type=d,e.container=d))),e.container||b(a).attr("data-wsrecheckmimetype",""),d=a.attr("media"),d&&(e.media=d),("audio/rtmp"==e.type||"video/rtmp"==e.type)&&(e.server?e.streamId=e.src:n.parseRtmp(e)),e):e},p=!d&&"postMessage"in h&&f,q=function(){q.loaded||(q.loaded=!0,m.noAutoTrack||e.ready("WINDOWLOAD",function(){s(),e.loader.loadList(["track-ui"])}))},r=function(){var a;return function(){!a&&p&&(a=!0,e.loader.loadScript("https://www.youtube.com/player_api"),b(function(){e._polyfill(["mediaelement-yt"])}))}}(),s=function(){d?j():r()};e.addPolyfill("mediaelement-yt",{test:!p,d:["dom-support"]}),n.mimeTypes={audio:{"audio/ogg":["ogg","oga","ogm"],'audio/ogg;codecs="opus"':"opus","audio/mpeg":["mp2","mp3","mpga","mpega"],"audio/mp4":["mp4","mpg4","m4r","m4a","m4p","m4b","aac"],"audio/wav":["wav"],"audio/3gpp":["3gp","3gpp"],"audio/webm":["webm"],"audio/fla":["flv","f4a","fla"],"application/x-mpegURL":["m3u8","m3u"]},video:{"video/ogg":["ogg","ogv","ogm"],"video/mpeg":["mpg","mpeg","mpe"],"video/mp4":["mp4","mpg4","m4v"],"video/quicktime":["mov","qt"],"video/x-msvideo":["avi"],"video/x-ms-asf":["asf","asx"],"video/flv":["flv","f4v"],"video/3gpp":["3gp","3gpp"],"video/webm":["webm"],"application/x-mpegURL":["m3u8","m3u"],"video/MP2T":["ts"]}},n.mimeTypes.source=b.extend({},n.mimeTypes.audio,n.mimeTypes.video),n.getTypeForSrc=function(a,c){if(-1!=a.indexOf("youtube.com/watch?")||-1!=a.indexOf("youtube.com/v/"))return"video/youtube";if(0===a.indexOf("rtmp"))return c+"/rtmp";a=a.split("?")[0].split("#")[0].split("."),a=a[a.length-1];var d;return b.each(n.mimeTypes[c],function(b,c){return-1!==c.indexOf(a)?(d=b,!1):void 0}),d},n.srces=function(a,c){if(a=b(a),!c){c=[];var d=a[0].nodeName.toLowerCase(),e=o(a,d);return e.src?c.push(e):b("source",a).each(function(){e=o(this,d),e.src&&c.push(e)}),c}a.removeAttr("src").removeAttr("type").find("source").remove(),b.isArray(c)||(c=[c]),c.forEach(function(c){"string"==typeof c&&(c={src:c}),a.append(b(k.createElement("source")).attr(c))})},b.fn.loadMediaSrc=function(a,c){return this.each(function(){c!==l&&(b(this).removeAttr("poster"),c&&b.attr(this,"poster",c)),n.srces(this,a),b(this).mediaLoad()})},n.swfMimeTypes=["video/3gpp","video/x-msvideo","video/quicktime","video/x-m4v","video/mp4","video/m4p","video/x-flv","video/flv","audio/mpeg","audio/aac","audio/mp4","audio/x-m4a","audio/m4a","audio/mp3","audio/x-fla","audio/fla","youtube/flv","video/jarisplayer","jarisplayer/jarisplayer","video/youtube","video/rtmp","audio/rtmp"],n.canThirdPlaySrces=function(a,c){var e="";return(d||p)&&(a=b(a),c=c||n.srces(a),b.each(c,function(a,b){return b.container&&b.src&&(d&&-1!=n.swfMimeTypes.indexOf(b.container)||p&&"video/youtube"==b.container)?(e=b,!1):void 0})),e};var t={};n.canNativePlaySrces=function(a,c){var d="";if(f){a=b(a);var e=(a[0].nodeName||"").toLowerCase(),g=(t[e]||{prop:{_supvalue:!1}}).prop._supvalue||a[0].canPlayType;
if(!g)return d;c=c||n.srces(a),b.each(c,function(b,c){return c.type&&g.call(a[0],c.type)?(d=c,!1):void 0})}return d};var u=/^\s*application\/octet\-stream\s*$/i,v=function(){var a=u.test(b.attr(this,"type")||"");return a&&b(this).removeAttr("type"),a};n.setError=function(a,c){if(b("source",a).filter(v).length){e.error('"application/octet-stream" is a useless mimetype for audio/video. Please change this attribute.');try{b(a).mediaLoad()}catch(d){}}else c||(c="can't play sources"),b(a).pause().data("mediaerror",c),e.error("mediaelementError: "+c),setTimeout(function(){b(a).data("mediaerror")&&b(a).addClass("media-error").trigger("mediaerror")},1)};var w=function(){var a,c=d?i:"mediaelement-yt";return function(d,f,g){e.ready(c,function(){n.createSWF&&b(d).parent()[0]?n.createSWF(d,f,g):a||(a=!0,s(),w(d,f,g))}),a||!p||n.createSWF||r()}}(),x=function(a,b,c,d,e){var f;c||c!==!1&&b&&"third"==b.isActive?(f=n.canThirdPlaySrces(a,d),f?w(a,f,b):e?n.setError(a,!1):x(a,b,!1,d,!0)):(f=n.canNativePlaySrces(a,d),f?b&&"third"==b.isActive&&n.setActive(a,"html5",b):e?(n.setError(a,!1),b&&"third"==b.isActive&&n.setActive(a,"html5",b)):x(a,b,!0,d,!0))},y=/^(?:embed|object|datalist)$/i,z=function(a,c){var d=e.data(a,"mediaelementBase")||e.data(a,"mediaelementBase",{}),f=n.srces(a),g=a.parentNode;clearTimeout(d.loadTimer),b(a).removeClass("media-error"),b.data(a,"mediaerror",!1),f.length&&g&&1==g.nodeType&&!y.test(g.nodeName||"")&&(c=c||e.data(a,"mediaelement"),n.sortMedia&&f.sort(n.sortMedia),x(a,c,m.preferFlash||l,f))};n.selectSource=z,b(k).on("ended",function(a){var c=e.data(a.target,"mediaelement");(!g||c&&"html5"!=c.isActive||b.prop(a.target,"loop"))&&setTimeout(function(){!b.prop(a.target,"paused")&&b.prop(a.target,"loop")&&b(a.target).prop("currentTime",0).play()},1)});var A=!1,B=function(){var c=function(){if(e.implement(this,"mediaelement")&&(z(this),a.mediaDefaultMuted||null==b.attr(this,"muted")||b.prop(this,"muted",!0),f&&(!g||"ActiveXObject"in h))){var c,d,i=this,j=function(){var a=b.prop(i,"buffered");if(a){for(var c="",d=0,e=a.length;e>d;d++)c+=a.end(d);return c}},k=function(){var a=j();a!=d&&(d=a,e.info("needed to trigger progress manually"),b(i).triggerHandler("progress"))};b(this).on({"play loadstart progress":function(a){"progress"==a.type&&(d=j()),clearTimeout(c),c=setTimeout(k,400)},"emptied stalled mediaerror abort suspend":function(a){"emptied"==a.type&&(d=!1),clearTimeout(c)}}),"ActiveXObject"in h&&b.prop(this,"paused")&&!b.prop(this,"readyState")&&b(this).is('audio[preload="none"][controls]:not([autoplay],.nonnative-api-active)')&&b(this).prop("preload","metadata").mediaLoad()}};e.ready("dom-support",function(){A=!0,g||e.defineNodeNamesBooleanProperty(["audio","video"],"loop"),["audio","video"].forEach(function(a){var c;c=e.defineNodeNameProperty(a,"load",{prop:{value:function(){var a=e.data(this,"mediaelement");z(this,a),!f||a&&"html5"!=a.isActive||!c.prop._supvalue||c.prop._supvalue.apply(this,arguments)}}}),t[a]=e.defineNodeNameProperty(a,"canPlayType",{prop:{value:function(c){var e="";return f&&t[a].prop._supvalue&&(e=t[a].prop._supvalue.call(this,c),"no"==e&&(e="")),!e&&d&&(c=b.trim((c||"").split(";")[0]),-1!=n.swfMimeTypes.indexOf(c)&&(e="maybe")),e}}})}),e.onNodeNamesPropertyModify(["audio","video"],["src","poster"],{set:function(){var a=this,b=e.data(a,"mediaelementBase")||e.data(a,"mediaelementBase",{});clearTimeout(b.loadTimer),b.loadTimer=setTimeout(function(){z(a),a=null},9)}}),e.addReady(function(a,d){var e=b("video, audio",a).add(d.filter("video, audio")).each(c);!q.loaded&&b("track",e).length&&q(),e=null})}),f&&!A&&e.addReady(function(a,c){A||b("video, audio",a).add(c.filter("video, audio")).each(function(){return n.canNativePlaySrces(this)?void 0:(s(),A=!0,!1)})})};c&&e.defineProperty(TextTrack.prototype,"shimActiveCues",{get:function(){return this._shimActiveCues||this.activeCues}}),f?(e.isReady("mediaelement-core",!0),B(),e.ready("WINDOWLOAD mediaelement",s)):e.ready(i,B),e.ready("track",q)})}(Modernizr,webshims);