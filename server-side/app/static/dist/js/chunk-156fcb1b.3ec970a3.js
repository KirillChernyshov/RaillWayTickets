(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-156fcb1b"],{"2ca8":function(e,t,a){"use strict";var i=a("7178"),s=a.n(i);s.a},7178:function(e,t,a){},c66d:function(e,t,a){"use strict";a.r(t);var i=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"profile"},[a("div",[a("b-avatar",{attrs:{variant:"primary",text:e.avatar,size:"100px"}}),a("div",{staticClass:"info"},[a("div",{staticClass:"name"},[e._v(e._s(e.firstname)+" "+e._s(e.lastname))]),a("div",[e._v(e._s(e.email))]),a("div",[e._v(e._s(e.dRole))])])],1),e.tickets.length?a("b-table",{staticClass:"align-left",attrs:{"sticky-header":"",striped:"",hover:"",items:e.tickets,fields:e.fields},scopedSlots:e._u([{key:"cell(actions)",fn:function(t){return[t.item.is_booked?a("b-button",{staticClass:"mr-2",attrs:{size:"sm"},on:{click:function(a){return e.cancelReservation(t.item.ticket_id)}}},[e._v(" ✘ ")]):e._e()]}}],null,!1,1980892489)}):e._e(),"manager"==e.role||e.tickets.length?e._e():a("div",[e._v("Здесь будет отображаться список Ваших билетов")])],1)},s=[],n=a("5530"),r=a("2f62"),l={name:"user-profile",data:function(){return{fields:[{key:"ticket_id",label:"id"},{key:"dep_station_name",label:"Станция отбытия"},{key:"departure_time",label:"Время отбытия"},{key:"arr_station_name",label:"Станция прибытия"},{key:"arrival_time",label:"Время прибытия"},{key:"wagon_id",label:"Вагон"},{key:"place",label:"Место"},{key:"cost",label:"Цена"},{key:"is_booked",label:"Статус"},{key:"actions",label:"Отмена"}]}},computed:Object(n["a"])(Object(n["a"])({},Object(r["d"])({firstname:function(e){return e.user.local.firstname},lastname:function(e){return e.user.local.lastname},role:function(e){return e.user.local.role},tickets:function(e){return e.user.tickets},email:function(e){return e.user.email}})),{},{avatar:function(){return this.firstname[0]+this.lastname[0]},dRole:function(){var e={client:"пользователь",manager:"менеджер"};return e[this.role]}}),methods:{cancelReservation:function(e){var t=this;this.$store.dispatch("confirmationTickets/cancelReservation",e).then((function(){t.$store.dispatch("user/getUserTickets")}))}},created:function(){this.$store.dispatch("user/getProfile"),this.$store.dispatch("user/getUserTickets")}},c=l,o=(a("2ca8"),a("2877")),u=Object(o["a"])(c,i,s,!1,null,"f58ae820",null);t["default"]=u.exports}}]);
//# sourceMappingURL=chunk-156fcb1b.3ec970a3.js.map