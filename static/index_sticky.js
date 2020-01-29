let getFormatedDateTime = function () {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    if (month < 10) {
        month = "0" + month;
    }
    var day = date.getDate();
    if (day < 10) {
        day = "0" + day;
    }
    var hour = date.getHours();
    if (hour < 10) {
        hour = "0" + hour;
    }
    var min = date.getMinutes();
    if (min < 10) {
        min = "0" + min;
    }
    var sec = date.getSeconds();
    if (sec < 10) {
        sec = "0" + sec;
    }
    return `${year}-${month}-${day} ${hour}:${min}:${sec}`;
}

let input_panel = new Vue({
    el: "#sticky_panel",
    data: {
        title: "Default Title",
        con: "",
        time: "",
        devName: "",
        ip: "",
        sticky_list: []
    },
    methods: {
        onBtnSubmitClick() {
            localStorage.setItem('devName', this.devName);
            let that = this;
            axios({
                method: "put",
                url: "/v2/Sticky/add",
                params: {
                    title: that.title,
                    con: that.con,
                    time: that.time,
                    devName: that.devName,
                    ip: that.ip
                }
            }).then(function (response) {
                console.log(response.data);
                that.getData();
            }).catch(function (err) {
                console.log(err);
            });
        },
        getData() {
            that = this;
            axios({
                method: 'get',
                url: "/v2/Sticky/get"
            }).then(function (response) {
                that.sticky_list = response.data;
            }).catch(function (err) {
                console.log(err);
            });
        }
    },
    created() {
        this.time = getFormatedDateTime();
        this.devName = localStorage.getItem('devName');
        this.getData();
    },
    mounted() {
        this.getData();
    }
});