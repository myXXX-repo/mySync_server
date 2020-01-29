<?php

if (!file_exists(dirname(__FILE__) . '/libs/RouterCtrl.php')) {
    goto EXT;
}
if (!file_exists(dirname(__FILE__) . '/libs/FileConCtrl.php')) {
    goto EXT;
}
if (!file_exists(dirname(__FILE__) . '/libs/ResponseBody.php')) {
    goto EXT;
}
if (!file_exists(dirname(__FILE__) . '/libs/DataTime.php')) {
    goto EXT;
}
if (!file_exists(dirname(__FILE__) . '/libs/DebugCtrl.php')) {
    goto EXT;
}

require_once dirname(__FILE__) . '/libs/RouterCtrl.php';
require_once dirname(__FILE__) . '/libs/FileConCtrl.php';
require_once dirname(__FILE__) . '/libs/ResponseBody.php';
require_once dirname(__FILE__) . '/libs/DataTime.php';
require_once dirname(__FILE__) . '/libs/DebugCtrl.php';


$dataPath = dirname(__FILE__) . '/data';
if (!is_dir(dirname(__FILE__) . '/data')) {
    mkdir($dataPath, '0777');
}

$debugStatus = 0;
$verification = 0;
$log = new Debug($debugStatus);
$log->console_logd('MAIN>', 'log');
$log->console_logd('POST>', json_encode($_POST));

$jsonFilePath = array(
    "tabJson" => dirname(__FILE__) . '/data/tabjson.json',
    "stickyJson" => dirname(__FILE__) . '/data/sticky.json',
    "configJson" => dirname(__FILE__) . '/data/config.json'
);

$routerCtrl = new RouterCtrl($_SERVER);

$routePath = $routerCtrl->getRoutePath(1);
if (sizeof($routePath) != 1) {
    goto END;
}
$operate = $routePath[0];

$allowedOperate = array(
    'addOneTab',
    'clearTabs',
    'delOneTab',
    'getLastTab',
    'getAllTabs',
    'addTabs',

    'addOneSticky',
    'delOneSticky',
    'getAllStickies',

    'v2',
    'test'
);
if (!in_array($operate, $allowedOperate)) {
    $debugStatus = 1;
    $log->console_loge($operate, 'error: wrong operate>' . $operate);
    goto END;
}

$AllowedKey = array(
    'asdf'
);
if (!in_array($_POST['key'], $AllowedKey) && $verification) {
    $debugStatus = 1;
    $log->console_loge($_POST['key'], 'error: wrong key>' . $_POST['key']);
    goto END;
}

$AllowedDev = array(
    'WolfSurface',
    'WolfPC'
);
if (!in_array($_POST['devname'], $AllowedDev) && $verification) {
    $debugStatus = 1;
    $log->console_loge($_POST['devname'], 'error: wrong devname>' . $_POST['devname']);
    goto END;
}

response_operate($operate);
switch ($operate) {
    case "addOneTab": {
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $fileCtrl->addItemToEnd(json_decode($_POST['data']));
            response_operate_response($operate);
            break;
        }
    case "addTabs": {
            $dataArray = json_decode($_POST['data']);
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $fileCtrl->addItemsToEnd($dataArray);
            response_operate_response($operate);
            break;
        }
    case "clearTabs": {
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $fileCtrl->clearData();
            response_operate_response($operate);
            break;
        }
    case "delOneTab": {
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $fileCtrl->delItem($_POST['data']);
            response_operate_response($operate);
            break;
        }
    case "getLastTab": {
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $item = $fileCtrl->getLastItem();
            response_operate_response($item);
            break;
        }
    case "getAllTabs": {
            $fileCtrl = new FileConCtrl($jsonFilePath['tabJson']);
            $fileCon = $fileCtrl->getAllArray();
            response_operate_response($fileCon);
            break;
        }
    case "v2": {
            goto V2PART;
        }
    case "test": {
            break;
        }
    case "addOneSticky": {
            $fileCtrl = new FileConCtrl($jsonFilePath['stickyJson']);
            $tmp_new_sticky=json_decode($_POST['data']);
            if($tmp_new_sticky==""){
                $log->console_loge("addOneSticky","new sticky is blank");
                goto END;
            }
            $fileCtrl->addItemToEnd($tmp_new_sticky);
            response_operate_response($operate);
            break;
        }
    case "delOneSticky": {
            $fileCtrl = new FileConCtrl($jsonFilePath['stickyJson']);
            $fileCtrl->delItem($_POST['data']);
            response_operate_response($operate);
            break;
        }
    case "getAllStickies": {
            $fileCtrl = new FileConCtrl($jsonFilePath['stickyJson']);
            $fileCon = $fileCtrl->getAllArray();
            response_operate_response($fileCon);
            break;
        }
}

V2PART:
//for api version 2
$appArray = array(
    'sticky',
    'tab',
    'file'
);

$app = $routePath[1];

switch ($app) {
    case "sticky": {
            break;
        }
    case "tab": {
            break;
        }
    case "file": {
            break;
        }
}


END:
//end
if ($debugStatus) {
    response_debugStatus($debugStatus);
    response_log($log->getLogArray());
}
sendResponseBody();
// print_r(getResponseBodyArray());

exit(0);

EXT: echo "error: require file not exist";
exit(-1);
