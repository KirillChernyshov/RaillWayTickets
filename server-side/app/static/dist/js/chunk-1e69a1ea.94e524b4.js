(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1e69a1ea"],{"129f":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},"14c3":function(t,e,n){var i=n("c6b6"),r=n("9263");t.exports=function(t,e){var n=t.exec;if("function"===typeof n){var c=n.call(t,e);if("object"!==typeof c)throw TypeError("RegExp exec method returned something other than an Object or null");return c}if("RegExp"!==i(t))throw TypeError("RegExp#exec called on incompatible receiver");return r.call(t,e)}},"5c18":function(t,e,n){"use strict";var i=n("8319"),r=n.n(i);r.a},8319:function(t,e,n){},"841c":function(t,e,n){"use strict";var i=n("d784"),r=n("825a"),c=n("1d80"),a=n("129f"),o=n("14c3");i("search",1,(function(t,e,n){return[function(e){var n=c(this),i=void 0==e?void 0:e[t];return void 0!==i?i.call(e,n):new RegExp(e)[t](String(n))},function(t){var i=n(e,t,this);if(i.done)return i.value;var c=r(t),s=String(this),l=c.lastIndex;a(l,0)||(c.lastIndex=0);var u=o(c,s);return a(c.lastIndex,l)||(c.lastIndex=l),null===u?-1:u.index}]}))},9263:function(t,e,n){"use strict";var i=n("ad6d"),r=n("9f7f"),c=RegExp.prototype.exec,a=String.prototype.replace,o=c,s=function(){var t=/a/,e=/b*/g;return c.call(t,"a"),c.call(e,"a"),0!==t.lastIndex||0!==e.lastIndex}(),l=r.UNSUPPORTED_Y||r.BROKEN_CARET,u=void 0!==/()??/.exec("")[1],f=s||u||l;f&&(o=function(t){var e,n,r,o,f=this,d=l&&f.sticky,p=i.call(f),x=f.source,v=0,h=t;return d&&(p=p.replace("y",""),-1===p.indexOf("g")&&(p+="g"),h=String(t).slice(f.lastIndex),f.lastIndex>0&&(!f.multiline||f.multiline&&"\n"!==t[f.lastIndex-1])&&(x="(?: "+x+")",h=" "+h,v++),n=new RegExp("^(?:"+x+")",p)),u&&(n=new RegExp("^"+x+"$(?!\\s)",p)),s&&(e=f.lastIndex),r=c.call(d?n:f,h),d?r?(r.input=r.input.slice(v),r[0]=r[0].slice(v),r.index=f.lastIndex,f.lastIndex+=r[0].length):f.lastIndex=0:s&&r&&(f.lastIndex=f.global?r.index+r[0].length:e),u&&r&&r.length>1&&a.call(r[0],n,(function(){for(o=1;o<arguments.length-2;o++)void 0===arguments[o]&&(r[o]=void 0)})),r}),t.exports=o},"9f7f":function(t,e,n){"use strict";var i=n("d039");function r(t,e){return RegExp(t,e)}e.UNSUPPORTED_Y=i((function(){var t=r("a","y");return t.lastIndex=2,null!=t.exec("abcd")})),e.BROKEN_CARET=i((function(){var t=r("^r","gy");return t.lastIndex=2,null!=t.exec("str")}))},ac1f:function(t,e,n){"use strict";var i=n("23e7"),r=n("9263");i({target:"RegExp",proto:!0,forced:/./.exec!==r},{exec:r})},ad6d:function(t,e,n){"use strict";var i=n("825a");t.exports=function(){var t=i(this),e="";return t.global&&(e+="g"),t.ignoreCase&&(e+="i"),t.multiline&&(e+="m"),t.dotAll&&(e+="s"),t.unicode&&(e+="u"),t.sticky&&(e+="y"),e}},c513:function(t,e,n){"use strict";n.r(e);var i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"tickets"},[n("b-form",{staticClass:"search",attrs:{inline:""}},[n("b-form-group",{attrs:{label:"Станция отбытия"}},[n("b-form-input",{staticClass:"mb-2 mr-sm-2 mb-sm-0",model:{value:t.identificator,callback:function(e){t.identificator=e},expression:"identificator"}})],1),n("b-button",{staticClass:"btn",on:{click:function(e){return t.search()}}},[t._v("Поиск")])],1),t.tickets.length?n("b-table",{staticClass:"align-left",attrs:{"sticky-header":"",striped:"",hover:"",items:t.tickets,fields:t.fields},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return[e.item.is_booked?n("b-button",{staticClass:"mr-2",attrs:{size:"sm",variant:"info"},on:{click:function(n){return t.confirmReservation(e.item.ticket_id)}}},[t._v(" ✔ ")]):t._e(),n("b-button",{staticClass:"mr-2",attrs:{size:"sm"},on:{click:function(n){return t.cancelReservation(e.item.ticket_id)}}},[t._v(" ✘ ")])]}}],null,!1,2875554607)}):t._e()],1)},r=[],c=(n("c975"),n("ac1f"),n("841c"),n("5530")),a=n("2f62"),o={name:"confirmation",data:function(){return{identificator:"",fields:[{key:"ticket_id",label:"id"},{key:"dep_station_name",label:"Станция отбытия"},{key:"departure_time",label:"Время отбытия"},{key:"arr_station_name",label:"Станция прибытия"},{key:"arrival_time",label:"Время прибытия"},{key:"wagon_id",label:"Вагон"},{key:"place",label:"Место"},{key:"cost",label:"Цена"},{key:"actions",label:"Действия"}]}},computed:Object(c["a"])({},Object(a["d"])({tickets:function(t){return t.confirmationTickets.tickets}})),methods:{search:function(){if(this.identificator){var t={};-1==this.identificator.indexOf("@")?t.ticket_id=parseInt(this.identificator):t.usr_email=this.identificator,this.$store.dispatch("confirmationTickets/searchTickets",t)}},cancelReservation:function(t){var e=this;this.$store.dispatch("confirmationTickets/cancelReservation",t).then((function(){e.search()}))},confirmReservation:function(t){var e=this;this.$store.dispatch("confirmationTickets/confirmReservation",t).then((function(){e.search()}))}}},s=o,l=(n("5c18"),n("2877")),u=Object(l["a"])(s,i,r,!1,null,"a210e116",null);e["default"]=u.exports},c975:function(t,e,n){"use strict";var i=n("23e7"),r=n("4d64").indexOf,c=n("a640"),a=n("ae40"),o=[].indexOf,s=!!o&&1/[1].indexOf(1,-0)<0,l=c("indexOf"),u=a("indexOf",{ACCESSORS:!0,1:0});i({target:"Array",proto:!0,forced:s||!l||!u},{indexOf:function(t){return s?o.apply(this,arguments)||0:r(this,t,arguments.length>1?arguments[1]:void 0)}})},d784:function(t,e,n){"use strict";n("ac1f");var i=n("6eeb"),r=n("d039"),c=n("b622"),a=n("9263"),o=n("9112"),s=c("species"),l=!r((function(){var t=/./;return t.exec=function(){var t=[];return t.groups={a:"7"},t},"7"!=="".replace(t,"$<a>")})),u=function(){return"$0"==="a".replace(/./,"$0")}(),f=c("replace"),d=function(){return!!/./[f]&&""===/./[f]("a","$0")}(),p=!r((function(){var t=/(?:)/,e=t.exec;t.exec=function(){return e.apply(this,arguments)};var n="ab".split(t);return 2!==n.length||"a"!==n[0]||"b"!==n[1]}));t.exports=function(t,e,n,f){var x=c(t),v=!r((function(){var e={};return e[x]=function(){return 7},7!=""[t](e)})),h=v&&!r((function(){var e=!1,n=/a/;return"split"===t&&(n={},n.constructor={},n.constructor[s]=function(){return n},n.flags="",n[x]=/./[x]),n.exec=function(){return e=!0,null},n[x](""),!e}));if(!v||!h||"replace"===t&&(!l||!u||d)||"split"===t&&!p){var b=/./[x],m=n(x,""[t],(function(t,e,n,i,r){return e.exec===a?v&&!r?{done:!0,value:b.call(e,n,i)}:{done:!0,value:t.call(n,e,i)}:{done:!1}}),{REPLACE_KEEPS_$0:u,REGEXP_REPLACE_SUBSTITUTES_UNDEFINED_CAPTURE:d}),g=m[0],k=m[1];i(String.prototype,t,g),i(RegExp.prototype,x,2==e?function(t,e){return k.call(t,this,e)}:function(t){return k.call(t,this)})}f&&o(RegExp.prototype[x],"sham",!0)}}}]);
//# sourceMappingURL=chunk-1e69a1ea.94e524b4.js.map