接口地址：

获取省份：http://www.weather.com.cn/data/city3jdata/china.html
获取区域：http://weather.com.cn/data/city3jdata/provshi/10101.html
获取县市：http://weather.com.cn/data/city3jdata/station/1010100.html
获取当天：http://weather.com.cn/data/cityinfo/101010100.html
实时信息：http://weather.com.cn/data/sk/101210101.html

规则：
直辖市：北京、上海、天津、重庆，比较特殊，从station到cityinfo的步骤是在00前5位后加入县市的id然后再加00

可以参照这里：
http://blog.csdn.net/gaojinshan/article/details/27665741
http://blog.csdn.net/gaojinshan/article/details/25891809

还有：
http://m.weather.com.cn/data/101280601.html


