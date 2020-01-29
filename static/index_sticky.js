let ensure_2 = function (num) {
    if (num < 10) {
        num = "0" + num;
    }
    return num;
}

let getFormatedDateTime = function () {
    var date = new Date();
    var year = date.getFullYear();
    var month = ensure_2(date.getMonth() + 1);
    var day = ensure_2(date.getDate());
    var hour = ensure_2(date.getHours());
    var min = ensure_2(date.getMinutes());
    var sec = ensure_2(date.getSeconds());
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
            this.time = getFormatedDateTime();
            let that = this;
            axios({
                method: "post",
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
        onBtnResetClick() {
            let that = this;
            this.title = "Default Title";
            this.con = "";
            this.time = getFormatedDateTime();
            this.devName = localStorage.getItem('devName');
            axios({
                method: 'get',
                url: "/getip"
            }).then(function (response) {
                that.ip = response.data;
                that.onBtnResetClick();
            });
        },
        onBtnClearClick() {
            let that = this;
            axios({
                method: "get",
                url: "/v2/Sticky/clear"
            }).then(function (response) {
                that.getData();
            }).catch(function (err) {
                console.log(err);
            });
        },
        // onCtrlKeyUp() {
        //     let that = this;
        //     document.onkeydown = function (e) {
        //         // let keyNum=window.event ? e.keyCode : e.which;
        //         if ((keyNum = window.event ? e.keyCode : e.which) == 13) {
        //             that.onBtnSubmitClick();
        //         }
        //     }
        // },
        delstickybyid(id) {
            let that = this;
            axios({
                method: "get",
                url: "/v2/Sticky/del",
                params: {
                    'id': id
                }
            }).then(function (response) {
                console.log(response.data);
                that.getData();
            }).catch(function (e) {
                console.log(e);
            });
        },
        getData() {
            let that = this;
            axios({
                method: 'get',
                url: "/v2/Sticky/get"
            }).then(function (response) {
                that.sticky_list = response.data;
            }).catch(function (err) {
                console.log(err);
            });
            axios({
                method: 'get',
                url: "/getip"
            }).then(function (response) {
                that.ip = response.data;
            });
        },
    },
    created() {
        this.time = getFormatedDateTime();
        this.devName = localStorage.getItem('devName');
        this.getData();
    },
    mounted() {
        this.getData();
        $('#con').focus();
    }
});
