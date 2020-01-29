<?php

//$locate=(dirname(__FILE__));
require_once dirname(__FILE__).'/DataTime.php';

$logArray = array();

class Debug
{
    private $debugStatus = 0;
    public function getDebugStatus(){
        return $this->debugStatus;
    }
    public function __construct($status = 0)
    {
        $this->debugStatus = $status;
    }
    public function console_log($tag, $debugtype, $str)
    {
        global $logArray;
        $item = array();
        array_push($item, $tag);
        array_push($item, $debugtype, $str);
        array_push($item, getFullTime());
        array_push($logArray, $item);
    }
    public function console_loge($tag, $str)
    {
        $this->console_log($tag, 'error', $str);
    }
    public function console_logd($tag, $str)
    {
        $this->console_log($tag, 'debug', $str);
    }
    public function getLogArray()
    {
        global $logArray;
        return $logArray;
    }
    public function getLogJson()
    {
        global $logArray;
        return json_encode($logArray);
    }
    // public function log($debugtype, $str)
    // {
    //     if ($this->debugStatus == 1) {
    //         print('<br>=============<br>');
    //         print("$debugtype > ");
    //         print_r($str);
    //         print('<br>=============<br>');
    //     }
    // }
    // public function loge($str)
    // {
    //     $this->log('error', $str);
    // }
    // public function logd($str)
    // {
    //     $this->log('debug', $str);
    // }
}




// $log = new Debug(1);
// $log->console_logd("bitch", "hello");

// echo $log->getLogJson();

// function addd()
// {
//     $log = new Debug(1);
//     $log->console_logd(__FUNCTION__, "hello");

//     $log->console_logd("her", "hello");
//     print_r($log->getLogArray());
//     echo $log->getLogJson();
//     echo __FUNCTION__;
// }

// addd();
