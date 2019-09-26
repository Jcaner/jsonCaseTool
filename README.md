# jsonTool
自动生成测试所需要的json容错用例.
## 用例生成规则
按照用例的目录层级进行生成，即，修改一级层级的所有key对应value值，修改二级层级的所有key对应value值....<br>
最多修改到四级，如有更多级别需要请自行修改代码CreateJson.createjson方法.
## 运行步骤
1.存放需要容错的json到jsondata.txt <br>
2.直接运行在项目目录下执行cmd命令： python runnerjson.py
## 查看生成的用例
用例位于jsondata文件夹中，每一条为一个文件.
## TODO
1.生成的文件格式调整，可以输出多个txt文件，或生成单个文件.<br>
   目的： 多个TXT文件有利于使用Fiddler进行测试;<br>
         单个可以使用jmeter进行测试，当然多个文件jmeter接口测试也可以;<br>
2.容错case的完善.<br>
3.过滤必填项，类似code:0或success:0 这种在某些场景下不可改变值的.<br>
