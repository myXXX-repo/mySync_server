<?php

require_once dirname(__FILE__) . '/DebugCtrl.php';

class FileConCtrl
{
    private $filePath;
    private $data = '';
    public function __construct($filePath)
    {
        $this->filePath = $filePath;
        if (file_exists($filePath)) {
            $this->data = file_get_contents($filePath);
            if ($this->data == null) {
                $this->data = '';
            }
            $log = new Debug();
            $log->console_logd(__CLASS__, "File $filePath is exist");
            $log->console_logd(__CLASS__, $this->data);
        } else {
            $log = new Debug();
            $log->console_loge(__CLASS__, "File $filePath is not exist");
            file_put_contents($this->filePath, '');
        }
    }
    public function __destruct()
    {
        file_put_contents($this->filePath, $this->data);
        $log = new Debug();
        $log->console_logd(__CLASS__, __METHOD__ . ' __destruct');
    }
    public function putDataToFile()
    {
        file_put_contents($this->filePath, $this->data);
        $log = new Debug();
        $log->console_logd(__METHOD__, $this->data);
    }
    public function getFilePath()
    {
        return $this->filePath;
    }
    public function setData($array)
    {
        $this->data = json_encode($array);
        $this->putDataToFile();
    }
    public function delItem($id)
    { //这里的id是指key值
        $dataArray = json_decode($this->data);
        unset($dataArray[$id]);
        $dataArray = array_values($dataArray);
        $this->data = json_encode($dataArray);
        $this->putDataToFile();
    }
    public function addItemToEnd($item)
    {
        $dataArray = json_decode($this->data);
        $dataArray[] = $item;
        $this->data = json_encode($dataArray);
        $this->putDataToFile();
    }

    //new function may be buggy
    public function addItemsToEnd($array){
        if($this->data!=null&&$this->data!='null'&&$this->data!='0'&&$this->data!=''){
            $dataArray = json_decode($this->data);
            $this->data = json_encode(array_merge($dataArray,$array));
        }else{
            $this->data = json_encode($array);
        }
        $this->putDataToFile();
    }
    public function clearData()
    {
        $this->data = '';
        $this->putDataToFile();
    }
    public function modifyItem($id, $item)
    {
        $dataArray = json_decode($this->data);
        array_fill($dataArray, $id, $item);
        $this->data = json_encode($dataArray);
        $this->putDataToFile();
    }
    public function getItem($id)
    {
        $dataArray = json_decode($this->data);
        if (array_key_exists($id, $dataArray)) {
            return $dataArray[$id];
        } else {
            $log = new Debug();
            $log->console_loge(__CLASS__, "Filed to find this item id=$id");
        }
    }
    public function getLastItem()
    {
        $dataArray = json_decode($this->data);
        $len = sizeof($dataArray);
        return $dataArray[$len - 1];
    }
    public function getAllJson()
    {
        return $this->data;
    }
    public function getAllArray()
    {
        return json_decode($this->data);
    }
}
