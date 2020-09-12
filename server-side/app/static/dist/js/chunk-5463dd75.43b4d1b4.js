(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5463dd75"],{"5efa":function(t,e,a){},6738:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"timetable"},[a("b-form",{staticClass:"search",attrs:{inline:""}},[a("b-form-group",{attrs:{label:"Станция отбытия"}},[a("b-form-select",{staticClass:"mb-2 mr-sm-2 mb-sm-0",attrs:{options:t.cities},model:{value:t.dep_station_name,callback:function(e){t.dep_station_name=e},expression:"dep_station_name"}})],1),a("b-form-group",{attrs:{label:"Станция прибытия"}},[a("b-form-select",{staticClass:"mb-2 mr-sm-2 mb-sm-0",attrs:{options:t.cities},model:{value:t.arr_station_name,callback:function(e){t.arr_station_name=e},expression:"arr_station_name"}})],1),a("b-form-group",{attrs:{label:"Дата прибытия"}},[a("b-form-datepicker",{staticClass:"mb-2 mr-sm-2 mb-sm-0",model:{value:t.date,callback:function(e){t.date=e},expression:"date"}})],1),a("b-form-group",{attrs:{label:"Время прибытия"}},[a("b-form-timepicker",{staticClass:"mb-2 mr-sm-2 mb-sm-0",model:{value:t.time,callback:function(e){t.time=e},expression:"time"}})],1),a("b-button",{staticClass:"btn",on:{click:function(e){return t.search()}}},[t._v("Поиск")])],1),a("b-table",{staticClass:"align-left routes",attrs:{busy:t.load,"sticky-header":"",striped:"",hover:"",items:t.routes,fields:t.fields},scopedSlots:t._u([{key:"cell(actions)",fn:function(e){return["client"==t.role?a("b-button",{staticClass:"mr-2",attrs:{size:"sm",variant:"info"},on:{click:function(a){return t.showBookTicket(e.item)}}},[t._v(" Бронировать билет ")]):t._e(),"manager"==t.role?a("b-button",{staticClass:"mr-2",attrs:{size:"sm",variant:"info"},on:{click:function(a){return t.showIssueTicket(e.item)}}},[t._v(" Оформить билет ")]):t._e()]}},{key:"table-busy",fn:function(){return[a("div",{staticClass:"text-center text-info my-2"},[a("b-spinner",{staticClass:"align-middle"}),a("strong",[t._v(" Загрузка...")])],1)]},proxy:!0}])}),a("BookTicket",t._b({on:{search:t.search}},"BookTicket",t.bookTicket,!1)),a("IssueTicket",t._b({on:{search:t.search}},"IssueTicket",t.bookTicket,!1))],1)},o=[],i=a("5530"),n=a("2f62"),c=a("c1df"),r=a.n(c),u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("b-modal",{attrs:{id:"book_ticket",title:"Бронирование билета","ok-only":""},on:{hidden:t.hideBookTicket,ok:t.bookTicket}},[t._l(t.dataList,(function(e,s){return a("div",{key:s},[a("span",[t._v(t._s(e.header)+":")]),t._v(" "+t._s(e.value)+" ")])})),a("div",[a("span",[t._v("Цена:")]),t._v(" "+t._s(t.seat.cost)+" ")]),a("b-row",[a("b-col",{attrs:{sm:"2"}},[a("span",[t._v("Место:")])]),a("b-col",{attrs:{sm:"8"}},[a("b-select",{attrs:{size:"sm",options:t.seats},model:{value:t.seat,callback:function(e){t.seat=e},expression:"seat"}})],1)],1),a("b-form")],2)},l=[],d=(a("99af"),a("4160"),a("159b"),{name:"BookTicket",data:function(){return{seat:{}}},computed:Object(i["a"])(Object(i["a"])({},Object(n["d"])({firstname:function(t){return t.user.local.firstname},lastname:function(t){return t.user.local.lastname},show:function(t){return t.bookTicket.show},bookData:function(t){return t.bookTicket.data},wagon_seats_info:function(t){return t.bookTicket.wagon_seats_info}})),{},{dataList:function(){return{route:{header:"Маршрут",value:this.bookData.route_name},trainNum:{header:"Номер поезда",value:this.bookData.schedule_id},dep:{header:"Станция и время отбытия",value:"".concat(this.bookData.dep_station_name," / ").concat(this.bookData.departure_time)},arr:{header:"Станция и время прибытия",value:"".concat(this.bookData.arr_station_name," / ").concat(this.bookData.arrival_time)}}},seats:function(){if(this.wagon_seats_info&&!this.wagon_seats_info.length)return[];var t=[];return this.wagon_seats_info.forEach((function(e){e.empty_places.forEach((function(a){t.push({value:{cost:e.cost,wagon_id:e.wagon_num,place:a},text:"Вагон: ".concat(e.wagon_num," | Место: ").concat(a," | Тип: ").concat(e.type_name)})}))})),t}}),methods:Object(i["a"])(Object(i["a"])({},Object(n["c"])("bookTicket",["hideBookTicket"])),{},{bookTicket:function(){this.$store.dispatch("bookTicket/bookTicket",{cost:this.seat.cost,place:this.seat.place,wagon_id:this.seat.wagon_id,schedule_id:this.bookData.schedule_id,arrival_stop_id:this.bookData.arr_stop_id,departure_stop_id:this.bookData.dep_stop_id}),this.$emit("search")}}),watch:{show:function(t){t?(this.$bvModal.show("book_ticket"),this.$store.dispatch("bookTicket/getRouteInfo",{arr_stop_id:this.bookData.arr_stop_id,dep_stop_id:this.bookData.dep_stop_id,schedule_id:this.bookData.schedule_id})):this.$bvModal.hide("book_ticket")},seats:function(t){t.length&&(this.seat=t[0].value)}}}),_=d,b=(a("d615"),a("2877")),h=Object(b["a"])(_,u,l,!1,null,"682a1db2",null),m=h.exports,k=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("b-modal",{attrs:{id:"issue_ticket",title:"Оформление билета","ok-only":""},on:{hidden:t.hideIssueTicket,ok:t.issueTicket}},[t._l(t.dataList,(function(e,s){return a("div",{key:s},[a("span",[t._v(t._s(e.header)+":")]),t._v(" "+t._s(e.value)+" ")])})),a("div",[a("span",[t._v("Цена:")]),t._v(" "+t._s(t.seat.cost)+" ")]),a("b-row",[a("b-col",{attrs:{sm:"2"}},[a("span",[t._v("Место:")])]),a("b-col",{attrs:{sm:"8"}},[a("b-select",{attrs:{size:"sm",options:t.seats},model:{value:t.seat,callback:function(e){t.seat=e},expression:"seat"}})],1)],1)],2)},f=[],p={name:"BookTicket",data:function(){return{seat:{},firstname:"",lastname:""}},computed:Object(i["a"])(Object(i["a"])({},Object(n["d"])({show:function(t){return t.bookTicket.showIssue},bookData:function(t){return t.bookTicket.data},wagon_seats_info:function(t){return t.bookTicket.wagon_seats_info}})),{},{dataList:function(){return{route:{header:"Маршрут",value:this.bookData.route_name},trainNum:{header:"Номер поезда",value:this.bookData.schedule_id},dep:{header:"Станция и время отбытия",value:"".concat(this.bookData.dep_station_name," / ").concat(this.bookData.departure_time)},arr:{header:"Станция и время прибытия",value:"".concat(this.bookData.arr_station_name," / ").concat(this.bookData.arrival_time)}}},seats:function(){if(this.wagon_seats_info&&!this.wagon_seats_info.length)return[];var t=[];return this.wagon_seats_info.forEach((function(e){e.empty_places.forEach((function(a){t.push({value:{cost:e.cost,wagon_id:e.wagon_num,place:a},text:"Вагон: ".concat(e.wagon_num," | Место: ").concat(a," | Тип: ").concat(e.type_name)})}))})),t}}),methods:Object(i["a"])(Object(i["a"])({},Object(n["c"])("bookTicket",["hideIssueTicket"])),{},{issueTicket:function(){this.$store.dispatch("bookTicket/issueTicket",{cost:this.seat.cost,place:this.seat.place,wagon_id:this.seat.wagon_id,schedule_id:this.bookData.schedule_id,arrival_stop_id:this.bookData.arr_stop_id,departure_stop_id:this.bookData.dep_stop_id}),this.$emit("search")}}),watch:{show:function(t){t?(this.$bvModal.show("issue_ticket"),this.$store.dispatch("bookTicket/getRouteInfo",{arr_stop_id:this.bookData.arr_stop_id,dep_stop_id:this.bookData.dep_stop_id,schedule_id:this.bookData.schedule_id})):this.$bvModal.hide("issue_ticket")},seats:function(t){t.length&&(this.seat=t[0].value)}}},v=p,w=(a("a6c2"),Object(b["a"])(v,k,f,!1,null,"f9584bb4",null)),T=w.exports,g={name:"timetable",data:function(){return{arr_station_name:null,dep_station_name:null,date:r()().add(1,"day").format("YYYY-MM-DD"),time:r()().format("HH:mm:ss"),bookTicket:{}}},computed:Object(i["a"])(Object(i["a"])({},Object(n["d"])({cities:function(t){return t.timetable.cities},load:function(t){return t.timetable.load},routes:function(t){return t.timetable.routes},role:function(t){return t.user.local.role}})),{},{rDate:function(){return r()(this.date).add(this.time).format()},fields:function(){return[{key:"dep_station_name",label:"Станция отбытия"},{key:"departure_time",label:"Время отбытия"},{key:"arr_station_name",label:"Станция прибытия"},{key:"arrival_time",label:"Время прибытия"},{key:"route_name",label:"Маршрут"},{key:"places",label:"Места"},this.role?{key:"actions",label:"Действия"}:{}]}}),methods:Object(i["a"])({search:function(){this.$store.dispatch("timetable/searchRoutes",{arrival_date:this.rDate,arrival_province_name:this.arr_station_name,departure_province_name:this.dep_station_name})}},Object(n["c"])("bookTicket",["showBookTicket","showIssueTicket"])),watch:{cities:function(t){t.length<2||(this.arr_station_name=t[0],this.dep_station_name=t[1])}},components:{BookTicket:m,IssueTicket:T},created:function(){this.$store.dispatch("timetable/getCitiesList")}},D=g,y=(a("a3c3"),Object(b["a"])(D,s,o,!1,null,"9855d7e8",null));e["default"]=y.exports},a3c3:function(t,e,a){"use strict";var s=a("cdc0"),o=a.n(s);o.a},a6c2:function(t,e,a){"use strict";var s=a("c3b3"),o=a.n(s);o.a},c3b3:function(t,e,a){},cdc0:function(t,e,a){},d615:function(t,e,a){"use strict";var s=a("5efa"),o=a.n(s);o.a}}]);
//# sourceMappingURL=chunk-5463dd75.43b4d1b4.js.map