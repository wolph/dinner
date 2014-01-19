webshims.register("dom-extend",function(a,b,c,d,e){"use strict";var f=!("hrefNormalized"in a.support)||a.support.hrefNormalized,g=!("getSetAttribute"in a.support)||a.support.getSetAttribute,h=Object.prototype.hasOwnProperty;if(b.assumeARIA=g||Modernizr.canvas||Modernizr.video||Modernizr.boxsizing,("text"==a('<input type="email" />').attr("type")||""===a("<form />").attr("novalidate")||"required"in a("<input />")[0].attributes)&&b.error("IE browser modes are busted in IE10+. Please test your HTML/CSS/JS with a real IE version or at least IETester or similiar tools"),"debug"in b&&b.error('Use webshims.setOptions("debug", true||false||"noCombo"); to debug flag'),!b.cfg.no$Switch){var i=function(){if(!c.jQuery||c.$&&c.jQuery!=c.$||c.jQuery.webshims||(b.error("jQuery was included more than once. Make sure to include it only once or try the $.noConflict(extreme) feature! Webshims and other Plugins might not work properly. Or set webshims.cfg.no$Switch to 'true'."),c.$&&(c.$=b.$),c.jQuery=b.$),b.M!=Modernizr){b.error("Modernizr was included more than once. Make sure to include it only once! Webshims and other scripts might not work properly.");for(var a in Modernizr)a in b.M||(b.M[a]=Modernizr[a]);Modernizr=b.M}};i(),setTimeout(i,90),b.ready("DOM",i),a(i),b.ready("WINDOWLOAD",i)}var j=(b.modules,/\s*,\s*/),k={},l={},m={},n={},o={},p={},q=a.fn.val,r=function(b,c,d,e,f){return f?q.call(a(b)):q.call(a(b),d)};a.widget||!function(){var b=a.cleanData;a.cleanData=function(c){if(!a.widget)for(var d,e=0;null!=(d=c[e]);e++)try{a(d).triggerHandler("remove")}catch(f){}b(c)}}(),a.fn.val=function(b){var c=this[0];if(arguments.length&&null==b&&(b=""),!arguments.length)return c&&1===c.nodeType?a.prop(c,"value",b,"val",!0):q.call(this);if(a.isArray(b))return q.apply(this,arguments);var d=a.isFunction(b);return this.each(function(f){if(c=this,1===c.nodeType)if(d){var g=b.call(c,f,a.prop(c,"value",e,"val",!0));null==g&&(g=""),a.prop(c,"value",g,"val")}else a.prop(c,"value",b,"val")})},a.fn.onTrigger=function(a,b){return this.on(a,b).each(b)},a.fn.onWSOff=function(b,c,e,f){return f||(f=d),a(f)[e?"onTrigger":"on"](b,c),this.on("remove",function(d){d.originalEvent||a(f).off(b,c)}),this};var s="_webshimsLib"+Math.round(1e3*Math.random()),t=function(b,c,d){if(b=b.jquery?b[0]:b,!b)return d||{};var f=a.data(b,s);return d!==e&&(f||(f=a.data(b,s,{})),c&&(f[c]=d)),c?f&&f[c]:f};[{name:"getNativeElement",prop:"nativeElement"},{name:"getShadowElement",prop:"shadowElement"},{name:"getShadowFocusElement",prop:"shadowFocusElement"}].forEach(function(b){a.fn[b.name]=function(){var c=[];return this.each(function(){var d=t(this,"shadowData"),e=d&&d[b.prop]||this;-1==a.inArray(e,c)&&c.push(e)}),this.pushStack(c)}}),b.cfg.extendNative||b.cfg.noTriggerOverride||!function(b){a.event.trigger=function(c,d,e,f){if(!m[c]||f||!e||1!==e.nodeType)return b.apply(this,arguments);var g,i,j,k=e[c],l=a.prop(e,c),n=l&&k!=l;return n&&(j="__ws"+c,i=c in e&&h.call(e,c),e[c]=l,e[j]=k),g=b.apply(this,arguments),n&&(i?e[c]=k:delete e[c],delete e[j]),g}}(a.event.trigger),["removeAttr","prop","attr"].forEach(function(c){k[c]=a[c],a[c]=function(b,d,f,g,h){var i="val"==g,j=i?r:k[c];if(!b||!l[d]||1!==b.nodeType||!i&&g&&"attr"==c&&a.attrFn[d])return j(b,d,f,g,h);var m,o,q,s=(b.nodeName||"").toLowerCase(),t=n[s],u="attr"!=c||f!==!1&&null!==f?c:"removeAttr";if(t||(t=n["*"]),t&&(t=t[d]),t&&(m=t[u]),m){if("value"==d&&(o=m.isVal,m.isVal=i),"removeAttr"===u)return m.value.call(b);if(f===e)return m.get?m.get.call(b):m.value;m.set&&("attr"==c&&f===!0&&(f=d),q=m.set.call(b,f)),"value"==d&&(m.isVal=o)}else q=j(b,d,f,g,h);if((f!==e||"removeAttr"===u)&&p[s]&&p[s][d]){var v;v="removeAttr"==u?!1:"prop"==u?!!f:!0,p[s][d].forEach(function(a){(!a.only||(a.only="prop"&&"prop"==c)||"attr"==a.only&&"prop"!=c)&&a.call(b,f,v,i?"val":u,c)})}return q},o[c]=function(a,d,f){n[a]||(n[a]={}),n[a][d]||(n[a][d]={});var g=n[a][d][c],h=function(a,b,e){var g;return b&&b[a]?b[a]:e&&e[a]?e[a]:"prop"==c&&"value"==d?function(a){var b=this;return f.isVal?r(b,d,a,!1,0===arguments.length):k[c](b,d,a)}:"prop"==c&&"value"==a&&f.value.apply?(g="__ws"+d,m[d]=!0,function(){var a=this[g]||k[c](this,d);return a&&a.apply&&(a=a.apply(this,arguments)),a}):function(a){return k[c](this,d,a)}};n[a][d][c]=f,f.value===e&&(f.set||(f.set=f.writeable?h("set",f,g):b.cfg.useStrict&&"prop"==d?function(){throw d+" is readonly on "+a}:function(){b.info(d+" is readonly on "+a)}),f.get||(f.get=h("get",f,g))),["value","get","set"].forEach(function(a){f[a]&&(f["_sup"+a]=h(a,g))})}});var u=function(){var a=b.getPrototypeOf(d.createElement("foobar")),c=Modernizr.advancedObjectProperties&&Modernizr.objectAccessor;return function(e,f,g){var i,j;if(!(c&&(i=d.createElement(e))&&(j=b.getPrototypeOf(i))&&a!==j)||i[f]&&h.call(i,f))g._supvalue=function(){var a=t(this,"propValue");return a&&a[f]&&a[f].apply?a[f].apply(this,arguments):a&&a[f]},v.extendValue(e,f,g.value);else{var k=i[f];g._supvalue=function(){return k&&k.apply?k.apply(this,arguments):k},j[f]=g.value}g.value._supvalue=g._supvalue}}(),v=function(){var c={};b.addReady(function(d,e){var f={},g=function(b){f[b]||(f[b]=a(d.getElementsByTagName(b)),e[0]&&a.nodeName(e[0],b)&&(f[b]=f[b].add(e)))};a.each(c,function(a,c){return g(a),c&&c.forEach?(c.forEach(function(b){f[a].each(b)}),void 0):(b.warn("Error: with "+a+"-property. methods: "+c),void 0)}),f=null});var e,f=a([]),g=function(b,f){c[b]?c[b].push(f):c[b]=[f],a.isDOMReady&&(e||a(d.getElementsByTagName(b))).each(f)};return{createTmpCache:function(b){return a.isDOMReady&&(e=e||a(d.getElementsByTagName(b))),e||f},flushTmpCache:function(){e=null},content:function(b,c){g(b,function(){var b=a.attr(this,c);null!=b&&a.attr(this,c,b)})},createElement:function(a,b){g(a,b)},extendValue:function(b,c,d){g(b,function(){a(this).each(function(){var a=t(this,"propValue",{});a[c]=this[c],this[c]=d})})}}}(),w=function(a,b){a.defaultValue===e&&(a.defaultValue=""),a.removeAttr||(a.removeAttr={value:function(){a[b||"prop"].set.call(this,a.defaultValue),a.removeAttr._supvalue.call(this)}}),a.attr||(a.attr={})};a.extend(b,{getID:function(){var b=(new Date).getTime();return function(c){c=a(c);var d=c.prop("id");return d||(b++,d="ID-"+b,c.eq(0).prop("id",d)),d}}(),implement:function(a,c){var d=t(a,"implemented")||t(a,"implemented",{});return d[c]?(b.warn(c+" already implemented for element #"+a.id),!1):(d[c]=!0,!0)},extendUNDEFProp:function(b,c){a.each(c,function(a,c){a in b||(b[a]=c)})},createPropDefault:w,data:t,moveToFirstEvent:function(b,c,d){var e,f=(a._data(b,"events")||{})[c];f&&f.length>1&&(e=f.pop(),d||(d="bind"),"bind"==d&&f.delegateCount?f.splice(f.delegateCount,0,e):f.unshift(e)),b=null},addShadowDom:function(){var e,f,g,h={init:!1,runs:0,test:function(){var a=h.getHeight(),b=h.getWidth();a!=h.height||b!=h.width?(h.height=a,h.width=b,h.handler({type:"docresize"}),h.runs++,h.runs<9&&setTimeout(h.test,90)):h.runs=0},handler:function(b){clearTimeout(e),e=setTimeout(function(){if("resize"==b.type){var e=a(c).width(),i=a(c).width();if(i==f&&e==g)return;f=i,g=e,h.height=h.getHeight(),h.width=h.getWidth()}a(d).triggerHandler("updateshadowdom")},"resize"==b.type?50:9)},_create:function(){a.each({Height:"getHeight",Width:"getWidth"},function(a,b){var c=d.body,e=d.documentElement;h[b]=function(){return Math.max(c["scroll"+a],e["scroll"+a],c["offset"+a],e["offset"+a],e["client"+a])}})},start:function(){!this.init&&d.body&&(this.init=!0,this._create(),this.height=h.getHeight(),this.width=h.getWidth(),setInterval(this.test,600),a(this.test),b.ready("WINDOWLOAD",this.test),a(d).on("updatelayout",this.handler),a(c).on("resize",this.handler),function(){var b,c=a.fn.animate;a.fn.animate=function(){return clearTimeout(b),b=setTimeout(function(){h.test()},99),c.apply(this,arguments)}}())}};return b.docObserve=function(){b.ready("DOM",function(){h.start(),null==a.support.boxSizing&&a(function(){a.support.boxSizing&&h.handler({type:"boxsizing"})})})},function(c,d,e){if(c&&d){e=e||{},c.jquery&&(c=c[0]),d.jquery&&(d=d[0]);var f=a.data(c,s)||a.data(c,s,{}),g=a.data(d,s)||a.data(d,s,{}),h={};e.shadowFocusElement?e.shadowFocusElement&&(e.shadowFocusElement.jquery&&(e.shadowFocusElement=e.shadowFocusElement[0]),h=a.data(e.shadowFocusElement,s)||a.data(e.shadowFocusElement,s,h)):e.shadowFocusElement=d,a(c).on("remove",function(b){b.originalEvent||setTimeout(function(){a(d).remove()},4)}),f.hasShadow=d,h.nativeElement=g.nativeElement=c,h.shadowData=g.shadowData=f.shadowData={nativeElement:c,shadowElement:d,shadowFocusElement:e.shadowFocusElement},e.shadowChilds&&e.shadowChilds.each(function(){t(this,"shadowData",g.shadowData)}),e.data&&(h.shadowData.data=g.shadowData.data=f.shadowData.data=e.data),e=null}b.docObserve()}}(),propTypes:{standard:function(a){w(a),a.prop||(a.prop={set:function(b){a.attr.set.call(this,""+b)},get:function(){return a.attr.get.call(this)||a.defaultValue}})},"boolean":function(a){w(a),a.prop||(a.prop={set:function(b){b?a.attr.set.call(this,""):a.removeAttr.value.call(this)},get:function(){return null!=a.attr.get.call(this)}})},src:function(){var b=d.createElement("a");return b.style.display="none",function(c,d){w(c),c.prop||(c.prop={set:function(a){c.attr.set.call(this,a)},get:function(){var c,e=this.getAttribute(d);if(null==e)return"";if(b.setAttribute("href",e+""),!f){try{a(b).insertAfter(this),c=b.getAttribute("href",4)}catch(g){c=b.getAttribute("href",4)}a(b).detach()}return c||b.href}})}}(),enumarated:function(a){w(a),a.prop||(a.prop={set:function(b){a.attr.set.call(this,b)},get:function(){var b=(a.attr.get.call(this)||"").toLowerCase();return b&&-1!=a.limitedTo.indexOf(b)||(b=a.defaultValue),b}})}},reflectProperties:function(c,d){"string"==typeof d&&(d=d.split(j)),d.forEach(function(d){b.defineNodeNamesProperty(c,d,{prop:{set:function(b){a.attr(this,d,b)},get:function(){return a.attr(this,d)||""}}})})},defineNodeNameProperty:function(c,d,e){return l[d]=!0,e.reflect&&(e.propType&&!b.propTypes[e.propType]?b.error("could not finde propType "+e.propType):b.propTypes[e.propType||"standard"](e,d)),["prop","attr","removeAttr"].forEach(function(f){var g=e[f];g&&(g="prop"===f?a.extend({writeable:!0},g):a.extend({},g,{writeable:!0}),o[f](c,d,g),"*"!=c&&b.cfg.extendNative&&"prop"==f&&g.value&&a.isFunction(g.value)&&u(c,d,g),e[f]=g)}),e.initAttr&&v.content(c,d),e},defineNodeNameProperties:function(a,c,d,e){for(var f in c)!e&&c[f].initAttr&&v.createTmpCache(a),d&&(c[f][d]||(c[f][d]={},["value","set","get"].forEach(function(a){a in c[f]&&(c[f][d][a]=c[f][a],delete c[f][a])}))),c[f]=b.defineNodeNameProperty(a,f,c[f]);return e||v.flushTmpCache(),c},createElement:function(c,d,e){var f;return a.isFunction(d)&&(d={after:d}),v.createTmpCache(c),d.before&&v.createElement(c,d.before),e&&(f=b.defineNodeNameProperties(c,e,!1,!0)),d.after&&v.createElement(c,d.after),v.flushTmpCache(),f},onNodeNamesPropertyModify:function(b,c,d,e){"string"==typeof b&&(b=b.split(j)),a.isFunction(d)&&(d={set:d}),b.forEach(function(a){p[a]||(p[a]={}),"string"==typeof c&&(c=c.split(j)),d.initAttr&&v.createTmpCache(a),c.forEach(function(b){p[a][b]||(p[a][b]=[],l[b]=!0),d.set&&(e&&(d.set.only=e),p[a][b].push(d.set)),d.initAttr&&v.content(a,b)}),v.flushTmpCache()})},defineNodeNamesBooleanProperty:function(c,d,f){f||(f={}),a.isFunction(f)&&(f.set=f),b.defineNodeNamesProperty(c,d,{attr:{set:function(a){this.setAttribute(d,a),f.set&&f.set.call(this,!0)},get:function(){var a=this.getAttribute(d);return null==a?e:d}},removeAttr:{value:function(){this.removeAttribute(d),f.set&&f.set.call(this,!1)}},reflect:!0,propType:"boolean",initAttr:f.initAttr||!1})},contentAttr:function(a,b,c){if(a.nodeName){var d;return c===e?(d=a.attributes[b]||{},c=d.specified?d.value:null,null==c?e:c):("boolean"==typeof c?c?a.setAttribute(b,b):a.removeAttribute(b):a.setAttribute(b,c),void 0)}},activeLang:function(){var c=[],d=[],e={},f=function(d,f,h){f._isLoading=!0,e[d]?e[d].push(f):(e[d]=[f],b.loader.loadScript(d,function(){h==c.join()&&a.each(e[d],function(a,b){g(b)}),delete e[d]}))},g=function(b){var d=b.__active,e=function(a,d){return b._isLoading=!1,b[d]||-1!=b.availableLangs.indexOf(d)?(b[d]?b.__active=b[d]:f(b.langSrc+d,b,c.join()),!1):void 0};a.each(c,e),b.__active||(b.__active=b[""]),d!=b.__active&&a(b).trigger("change")};return function(a){var b;if("string"==typeof a)c[0]!=a&&(c=[a],b=c[0].split("-")[0],b&&b!=a&&c.push(b),d.forEach(g));else if("object"==typeof a)return a.__active||(d.push(a),g(a)),a.__active;return c[0]}}()}),a.each({defineNodeNamesProperty:"defineNodeNameProperty",defineNodeNamesProperties:"defineNodeNameProperties",createElements:"createElement"},function(a,c){b[a]=function(a,d,e,f){"string"==typeof a&&(a=a.split(j));var g={};return a.forEach(function(a){g[a]=b[c](a,d,e,f)}),g}}),b.isReady("webshimLocalization",!0)}),function(a,b){if(!(!a.webshims.assumeARIA||"content"in b.createElement("template")||(a(function(){var b=a("main").attr({role:"main"});b.length>1?webshims.error("only one main element allowed in document"):b.is("article *, section *")&&webshims.error("main not allowed inside of article/section elements")}),"hidden"in b.createElement("a")))){var c={article:"article",aside:"complementary",section:"region",nav:"navigation",address:"contentinfo"},d=function(a,b){var c=a.getAttribute("role");c||a.setAttribute("role",b)};a.webshims.addReady(function(e,f){if(a.each(c,function(b,c){for(var g=a(b,e).add(f.filter(b)),h=0,i=g.length;i>h;h++)d(g[h],c)}),e===b){var g=b.getElementsByTagName("header")[0],h=b.getElementsByTagName("footer"),i=h.length;if(g&&!a(g).closest("section, article")[0]&&d(g,"banner"),!i)return;var j=h[i-1];a(j).closest("section, article")[0]||d(j,"contentinfo")}})}}(webshims.$,document),webshims.register("filereader",function(a,b){"use strict";!function(){var c=window.swfmini||window.swfobject,d=a.Callbacks("once unique memory"),e=0,f=null;if(window.FileReader)return a.fn.fileReader=function(){return this},void 0;a.fn.fileReader=function(b){if(this.length){b=a.extend(a.fn.fileReader.defaults,b);var c=this;d.add(function(){return g(c,b)}),a.isFunction(b.callback)&&d.add(b.callback),FileAPIProxy.ready||FileAPIProxy.init(b)}return this},a.fn.fileReader.defaults={id:"fileReaderSWFObject",multiple:null,accept:null,label:null,extensions:null,filereader:"files/filereader.swf",expressInstall:null,debugMode:!1,callback:!1};var g=function(b,c){return b.each(function(b,d){d=a(d);var g,h,i,j=d.attr("id");j||(j="flashFileInput"+e,d.attr("id",j),e++),g=d.prop("multiple"),h=d.data("swfaccept")||d.prop("accept")||c.accept,i=d.jProp("labels").map(function(){return a(this).text()}).get().join(" ")||d.data("swflabel")||c.label,FileAPIProxy.inputs[j]=d,FileAPIProxy.swfObject.add(j,g,h,i,c.extensions),d.css("z-index",0).mouseover(function(a){j!==f&&(a=a||window.event,f=j,FileAPIProxy.swfObject.mouseover(j),FileAPIProxy.container.height(d.outerHeight()).width(d.outerWidth()).css(d.offset()))}).click(function(a){return a.preventDefault(),a.stopPropagation(),a.stopImmediatePropagation(),!1})})};window.FileAPIProxy={ready:!1,_inititalized:!1,init:function(b){var e=this;this.debugMode=b.debugMode,this.container||(this.container=a("<div>").attr("id",b.id).wrap("<div>").parent().css({position:"fixed",width:"1px",height:"1px",display:"inline-block",background:"transparent","z-index":99999}).on("mouseover mouseout mousedown mouseup",function(b){f&&a("#"+f).trigger(b.type)}).appendTo("body"),c.embedSWF(b.filereader,b.id,"100%","100%","10",b.expressInstall,{debugMode:b.debugMode?!0:""},{wmode:"transparent",allowScriptAccess:"sameDomain"},{},function(b){e.swfObject=b.ref,a(e.swfObject).css({display:"block",outline:0}).attr("tabindex",0),e.ready=b.success&&"function"==typeof b.ref.add,e.ready&&d.fire()}))},swfObject:null,container:null,inputs:{},readers:{},onFileInputEvent:function(a){if(this.debugMode&&console.info("FileInput Event ",a.type,a),a.target in this.inputs){var c=this.inputs[a.target];a.target=c[0],"change"===a.type&&b.data(a.target,"fileList",new FileList(a.files)),c.trigger(a)}window.focus()},onFileReaderEvent:function(a){if(this.debugMode&&console.info("FileReader Event ",a.type,a,a.target in this.readers),a.target in this.readers){var b=this.readers[a.target];a.target=b,b._handleFlashEvent.call(b,a)}},onFileReaderError:function(a){this.debugMode&&console.log(a)},onSWFReady:function(){return this.container.css({position:"absolute"}),this.ready="function"==typeof this.swfObject.add,this.ready&&d.fire(),!0}},window.FileReader=function(){this.EMPTY=0,this.LOADING=1,this.DONE=2,this.readyState=0,this.result=null,this.error=null,this.onloadstart=null,this.onprogress=null,this.onload=null,this.onabort=null,this.onerror=null,this.onloadend=null,this._callbacks={loadstart:a.Callbacks("unique"),progress:a.Callbacks("unique"),abort:a.Callbacks("unique"),error:a.Callbacks("unique"),load:a.Callbacks("unique"),loadend:a.Callbacks("unique")},this._id=null},window.FileReader.prototype={readAsBinaryString:function(a){this._start(a),FileAPIProxy.swfObject.read(a.input,a.name,"readAsBinaryString")},readAsText:function(a){this._start(a),FileAPIProxy.swfObject.read(a.input,a.name,"readAsText")},readAsDataURL:function(a){this._start(a),FileAPIProxy.swfObject.read(a.input,a.name,"readAsDataURL")},readAsArrayBuffer:function(){throw"Whoops FileReader.readAsArrayBuffer is unimplemented"},abort:function(){this.result=null,this.readyState!==this.EMPTY&&this.readyState!==this.DONE&&FileAPIProxy.swfObject.abort(this._id)},addEventListener:function(a,b){a in this._callbacks&&this._callbacks[a].add(b)},removeEventListener:function(a,b){a in this._callbacks&&this._callbacks[a].remove(b)},dispatchEvent:function(b){if(b.target=this,b.type in this._callbacks){var c=this["on"+b.type];a.isFunction(c)&&c(b),this._callbacks[b.type].fire(b)}return!0},_register:function(a){this._id=a.input+"."+a.name,FileAPIProxy.readers[this._id]=this},_start:function(a){if(this._register(a),this.readyState===this.LOADING)throw{type:"InvalidStateError",code:11,message:"The object is in an invalid state."}},_handleFlashEvent:function(a){switch(a.type){case"loadstart":this.readyState=this.LOADING;break;case"loadend":this.readyState=this.DONE;break;case"load":this.readyState=this.DONE,this.result=FileAPIProxy.swfObject.result(this._id);break;case"error":this.result=null,this.error={name:"NotReadableError",message:"The File cannot be read!"}}this.dispatchEvent(new FileReaderEvent(a))}},window.FileReaderEvent=function(a){this.initEvent(a)},window.FileReaderEvent.prototype={initEvent:function(b){a.extend(this,{type:null,target:null,currentTarget:null,eventPhase:2,bubbles:!1,cancelable:!1,defaultPrevented:!1,isTrusted:!1,timeStamp:(new Date).getTime()},b)},stopPropagation:function(){},stopImmediatePropagation:function(){},preventDefault:function(){}},window.FileList=function(a){if(a){for(var b=0;b<a.length;b++)this[b]=a[b];this.length=a.length}else this.length=0},window.FileList.prototype={item:function(a){return a in this?this[a]:null}}}(),b.defineNodeNameProperty("input","files",{prop:{writeable:!1,get:function(){return"file"!=this.type?null:(a(this).is(".ws-filereader")||b.error("please add the 'ws-filereader' class to your input[type='file'] to implement files-property"),b.data(this,"fileList")||b.data(this,"fileList",new FileList))}}}),b.defineNodeNamesBooleanProperty("input","multiple"),a.fn.fileReader.defaults.filereader=b.cfg.basePath+"swf/filereader.swf";var c=["DOM"];b.modules["form-core"].loaded&&c.push("forms"),b.ready(c,function(){b.addReady(function(b){a('input[type="file"].ws-filereader',b).fileReader()})})});