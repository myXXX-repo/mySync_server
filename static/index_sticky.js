let getFormatedDateTime = function(){
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    if(month<10){
        month="0"+month;
    }
    var day = date.getDate();
    if(day<10){
        day="0"+day;
    }
    var hour = date.getHours();
    if(hour<10){
        hour="0"+hour;
    }
    var min = date.getMinutes();
    if(min<10){
        min="0"+min;
    }
    var sec = date.getSeconds();
    if(sec<10){
        sec="0"+sec;
    }
    return `${year}-${month}-${day} ${hour}:${min}:${sec}`;
}

new Vue({
    el:"#input_panel",
    data:{
        title:"Default Title",
        con:"",
        time:"",
        devName:"",
        ip:""
    },
    methods:{
        onBtnSubmitClick(){
            console.log("123");
            localStorage.setItem('devName',this.devName);
            that=this
            axios.post("/v2/Sticky/add",{
                title:that.title,
                con:that.con,
                time:that.time,
                devName:that.devName,
                ip:that.ip
            }).then(function(response){
                console.log(response.data)
            },function(err){
                console.log(err)
            });
        }
    },
    created(){
        that = this
        this.time = getFormatedDateTime();
        this.devName = localStorage.getItem('devName');
        axios.get("/getip").then(function(request){
            that.ip = request.data;
        });
    },
});