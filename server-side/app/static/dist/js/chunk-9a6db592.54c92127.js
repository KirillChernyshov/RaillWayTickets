(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-9a6db592"],{"2fef":function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"form"},[a("b-form",{on:{submit:t.checkValid}},[t._l(t.form,(function(e){return a("b-form-group",{key:e.label,attrs:{label:e.label}},[a("b-form-input",{attrs:{placeholder:e.placeholder,state:e.valid,type:e.type,size:"sm"},on:{focus:function(t){e.valid=null}},model:{value:e.value,callback:function(a){t.$set(e,"value",a)},expression:"item.value"}})],1)})),a("b-button",{attrs:{type:"submit",variant:"primary",size:"sm"}},[t._v("Войти")]),a("span",[t._v(" или "),a("b-link",{attrs:{href:"/reg"}},[t._v("зарегистрироваться")])],1),t.waiting?a("b-spinner",{staticClass:"spiner",attrs:{variant:"success",small:"",type:"grow",label:"Spinning"}}):t._e(),a("div",{staticClass:"error"},[t._v(t._s(t.error))])],2)],1)},n=[],l=(a("b64b"),a("5530")),i=a("2f62"),s={name:"authorization",data:function(){return{form:{email:{label:"Эл. почта:",placeholder:"Введите адрес эл. почты",value:"",type:"email",valid:null},password:{label:"Пароль:",placeholder:"Введите пароль",value:"",type:"password",valid:null}}}},computed:Object(l["a"])({},Object(i["d"])({waiting:function(t){return t.auth.waiting},error:function(t){return t.auth.error}})),methods:{checkValid:function(t){t.preventDefault();for(var e={},a=0,r=Object.keys(this.form);a<r.length;a++){var n=r[a];e[n]=this.form[n].value}this.$store.dispatch("auth/authorization",e)}}},o=s,u=(a("fc85"),a("2877")),c=Object(u["a"])(o,r,n,!1,null,"305f53c1",null);e["default"]=c.exports},"8b2e":function(t,e,a){},fc85:function(t,e,a){"use strict";var r=a("8b2e"),n=a.n(r);n.a}}]);
//# sourceMappingURL=chunk-9a6db592.54c92127.js.map