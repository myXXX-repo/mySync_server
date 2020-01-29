<?php

$responseBody=array(
    // 'debugStatus'=>NULL,
    // 'requestIp'=>NULL,
    // 'responseIp'=>NULL,
    // 'operate'=>NULL,//操作
    // 'operate_data'=>NULL,//收到的操作数据
    // 'operate_response'=>NULL,//操作返回
    // 'log'=>NULL
);

function addItemToResponseBody($key,$data){
    global $responseBody;
    $responseBody[$key]=$data;
}

function response_debugStatus($item){
    addItemToResponseBody('debugStatus',$item);
}

function response_requestIp($item){
    addItemToResponseBody('requestIp',$item);
}

function response_responseIp($item){
    addItemToResponseBody('responseIp',$item);
}

function response_operate($item){
    addItemToResponseBody('operate',$item);
}

function response_operate_data($item){
    addItemToResponseBody('operate_data',$item);
}

function response_operate_response($item){
    addItemToResponseBody('operate_response',$item);
}

function response_log($item){
    addItemToResponseBody('log',$item);
}

function getResponseBodyArray(){
    global $responseBody;
    return $responseBody;
}

function sendResponseBody(){
    global $responseBody;
    //return $responseBody;
    echo(json_encode($responseBody));
}