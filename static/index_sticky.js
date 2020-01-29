let ensure_2 = function(num) {
    if (num < 10) {
        num = "0" + num;
    }
    return num;
}

let getFormatedDateTime = function() {
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
            }).then(function(response) {
                console.log(response.data);
                that.getData();
            }).catch(function(err) {
                console.log(err);
            });
        },
        getData() {
            that = this;
            axios({
                method: 'get',
                url: "/v2/Sticky/get"
            }).then(function(response) {
                that.sticky_list = response.data;
            }).catch(function(err) {
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
