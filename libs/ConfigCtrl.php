<?php

class ConfigCtrl{
	public $configArray = array(
		'debugStatus'=>'0',
		'verification'=>'0',
		'trans_data_encode'=>'0',
		'trans_data_encode_type'=>'md5',
		'allowed_key'=>array('asdf'),
		'allowed_devname'=>array('WolfSurface','WolfPC'),
		'data_store_mathod'=>'.json',
		'data_path'=>'./data',
		'ctrler'=>array(
			'tabSync',
			'sticky',
			'configure'
		);
	);
	public function __construct(){
		
	}

}