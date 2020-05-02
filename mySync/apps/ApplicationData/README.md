
### ApplicationData 保存用户app的全部数据 以key_value组成的json数组字符串 形式保存
* GET /app/ApplicationData/v1.0/test 测试服务器连接
    * 正常则返回 200 和 server is fine

* GET /app/ApplicationData/v1.0 获取该server_app下的全部数据 即获取全部用户app的数据
    * 正常则返回 200 和一个json数组的字符串

* DELETE /app/ApplicationData/v1.0 删除全部数据
    * 正常则返回 200 和 del all done



* GET /app/ApplicationData/v1.0/<string:app_name> 获取指定app的全部数据
    * 正常则返回 200 和一个json数组的字符串

* POST /app/ApplicationData/v1.0/<string:app_name> 上传某app的全部数据
    * 正常则返回 200 和 update data 或者 add data

* DELETE /app/ApplicationData/v1.0/<string:app_name>/delete 删除某app下的全部数据
    * 正常则返回 200 和
