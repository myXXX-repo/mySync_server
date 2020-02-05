let getCurrentAddress = function () {
    return window.location.protocol + '//' + window.location.host;
};
let toBool = function (str) {
    if (str == 'true') {
        return true;
    } else {
        return false;
    }
};
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

new Vue({
    el: "#api_panel",
    data: {
        this_address: getCurrentAddress(),
        api_list: [{
            title: "Sticky",
            show_list: toBool(localStorage.getItem('api_list_show_Sticky')),
            list: [{
                api_name: "index",
                method: "GET",
                routes: "/v2/Sticky",
                details: "have no upload data display index page"
            },
                {
                    api_name: "get sticky",
                    method: "GET",
                    routes: "/v2/Sticky/get",
                    details: "send request:<br>GET: ?id=1&id=2<br>POST: json array string [1,2]<br>auth: header with AuthKey and DevName<br>return: json array string<br>for one or multilines"
                },
                {
                    api_name: "add sticky",
                    method: "POST",
                    routes: "/v2/Sticky/add",
                    details: "send request:<br>GET: ?title=TITLE&con=CON for one line<br>POST: json string [['title','con'],['title','con']] for multilines<br>auth: header with AuthKey and DevName<br>return: 1 or 0"
                },
                {
                    api_name: "del sticky",
                    method: "GET",
                    routes: "/v2/Sticky/del",
                    details: "send request:<br>GET: ?id=1&id=2&id=3<br>post json array string: [1,2,3]<br>auth: header with AuthKey and DevName"
                },
                {
                    api_name: "clear sticky",
                    method: "GET",
                    routes: "/v2/Sticky/clear",
                    details: ""
                }
            ]
        },
            {
                title: "statistics",
                show_list: toBool(localStorage.getItem('api_list_show_statistics')),
                list: [{
                    api_name: "statistics",
                    method: "GET",
                    routes: "/statistics",
                    details: ""
                },]
            }
        ]
    },
    methods: {
        hide_toggle(i) {
            this.api_list[i].show_list = !this.api_list[i].show_list;
            localStorage.setItem('api_list_show_' + this.api_list[i].title, this.api_list[i].show_list);
        }
    }
});

// new Vue({
//     el: "#Statistics_panel",
//     data: {
//         this_address: getCurrentAddress(),
//         title: "Api Call Statistics",
//         th: ['App Name', 'Api Name', 'Methods', 'Number Of Calls', 'Last Call Time', 'Operation'],
//         apis: []
//     },
//     methods: {
//         initStatisticsData() {
//             this.apis = [];
//             let that = this;
//             axios.get('/statistics').then(function (response) {
//                 console.log(response.data);
//                 response.data.forEach(app => {
//                     app.apis.forEach(api => {
//                         var tmp = {};
//                         tmp.appname = app.appname;
//                         tmp.apiname = api.apiname;
//                         tmp.method = api.method;
//                         tmp.NumOfCall = api.NumOfCall;
//                         tmp.LastCallTime = api.LastCallTime;
//
//                         that.apis.push(tmp);
//                     });
//                 });
//             });
//         },
//     },
//     mounted: function () {
//         this.apis = [];
//         let that = this;
//         axios.get('/statistics').then(function (response) {
//             console.log(response.data);
//             response.data.forEach(app => {
//                 app.apis.forEach(api => {
//                     var tmp = {};
//                     tmp.appname = app.appname;
//                     tmp.apiname = api.apiname;
//                     tmp.method = api.method;
//                     tmp.NumOfCall = api.NumOfCall;
//                     tmp.LastCallTime = api.LastCallTime;
//
//                     that.apis.push(tmp);
//                 });
//             });
//         });
//     }
// });
