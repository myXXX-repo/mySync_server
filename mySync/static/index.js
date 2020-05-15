// let getCurrgetAllAppDataentAddress = function () {
//     return window.location.protocol + '//' + window.location.host;
// };
// let toBool = function (str) {
//     return str === 'true';
// };
let init = function () {
    if (localStorage.getItem('inited') !== 1) {
        localStorage.setItem('inited', 1);
        localStorage.setItem('debug', 0);
        localStorage.setItem('api_list_show_Sticky', 'true');
        localStorage.setItem('api_list_show_tabSync', 'true');
        localStorage.setItem('api_list_show_toDoList', 'true');
        localStorage.setItem('api_list_show_statistics', 'true')
    }
};
init();

// new Vue({
//     el: "#api_panel",
//     data: {
//         this_address: getCurrentAddress(),
//         api_list: [{
//             title: "Sticky",
//             show_list: toBool(localStorage.getItem('api_list_show_Sticky')),
//             list: [{
//                 api_name: "index",
//                 method: "GET",
//                 routes: "/StickyIndex",
//                 details: "have no upload data display index page"
//             },
//                 {
//                     api_name: "get sticky",
//                     method: "GET",
//                     routes: "/v2.1/Sticky",
//                     details: ""
//                 },
//                 {
//                     api_name: "post sticky",
//                     method: "POST",
//                     routes: "/v2.1/Sticky",
//                     details: ""
//                 },
//                 {
//                     api_name: "del all sticky",
//                     method: "DELETE",
//                     routes: "/v2.1/Sticky",
//                     details: "must set auth"
//                 },
//                 {
//                     api_name: "get aimed sticky",
//                     method: "GET",
//                     routes: "/v2.1/Sticky/int:resid",
//                     details: ""
//                 },
//                 {
//                     api_name: "update/cover aimed sticky",
//                     method: "PUT PATH",
//                     routes: "/v2.1/Sticky/int:resid",
//                     details: ""
//                 },
//                 {
//                     api_name: "delete aimed sticky",
//                     method: "DELETE",
//                     routes: "/v2.1/Sticky/int:resid",
//                     details: ""
//                 }
//             ]
//         },
//             // {
//             //     title: "statistics",
//             //     show_list: toBool(localStorage.getItem('api_list_show_statistics')),
//             //     list: [{
//             //         api_name: "statistics",
//             //         method: "GET",
//             //         routes: "/statistics",
//             //         details: ""
//             //     },]
//             // }
//         ]
//     },
//     methods: {
//         hide_toggle(i) {
//             this.api_list[i].show_list = !this.api_list[i].show_list;
//             localStorage.setItem('api_list_show_' + this.api_list[i].title, this.api_list[i].show_list);
//         }
//     }
// });

new Vue({
    el: "#route_list",
    data: {
        routes: ["a", "b", "c"]
    },
    mounted() {
        console.log("mounted");
        let that = this;
        axios({
            url:"/getroutes",
            method: 'get'
        }).then(function (response) {
            that.routes = response.data
        }).catch(function (err) {
            console.log(err);
        });
    }
});
