接口地址：   

获取省份：http://www.weather.com.cn/data/city3jdata/china.html   
获取区域：http://weather.com.cn/data/city3jdata/provshi/10101.html   
获取县市：http://weather.com.cn/data/city3jdata/station/1010100.html   
获取当天：http://weather.com.cn/data/cityinfo/101010100.html   
实时信息：http://weather.com.cn/data/sk/101010100.html   
六天信息：http://m.weather.com.cn/data/101010100.html
七天信息：http://mobile.weather.com.cn/data/forecast/101010100.html

获取省份：   
`{
10101: "北京",
10102: "上海",
10103: "天津",
10104: "重庆",
10105: "黑龙江",
10106: "吉林",
10107: "辽宁",
10108: "内蒙古",
10109: "河北",
10110: "山西",
10111: "陕西",
10112: "山东",
10113: "新疆",
10114: "西藏",
10115: "青海",
10116: "甘肃",
10117: "宁夏",
10118: "河南",
10119: "江苏",
10120: "湖北",
10121: "浙江",
10122: "安徽",
10123: "福建",
10124: "江西",
10125: "湖南",
10126: "贵州",
10127: "四川",
10128: "广东",
10129: "云南",
10130: "广西",
10131: "海南",
10132: "香港",
10133: "澳门",
10134: "台湾"
`}

获取区域：   
`{
00: "北京"
`}

获取县市：   
`{
10: "石景山",
11: "大兴",
12: "房山",
13: "密云",
14: "门头沟",
15: "平谷",
01: "北京",
02: "海淀",
03: "朝阳",
04: "顺义",
05: "怀柔",
06: "通州",
07: "昌平",
08: "延庆",
09: "丰台"
`}

获取当天：   
`{
weatherinfo: {
city: "北京",
cityid: "101010100",
temp1: "1℃",
temp2: "-5℃",
weather: "多云转阴",
img1: "d1.gif",
img2: "n2.gif",
ptime: "11:00"
}
`}

实时信息：   
`{
weatherinfo: {
city: "北京",
cityid: "101010100",
temp: "0",
WD: "东北风",
WS: "2级",
SD: "21%",
WSE: "2",
time: "11:25",
isRadar: "1",
Radar: "JC_RADAR_AZ9010_JB",
njd: "暂无实况",
qy: "1030"
}
`}


规则：   
直辖市：北京、上海、天津、重庆，比较特殊，从station到cityinfo的步骤是在00前5位后加入县市的id然后再加00

可以参照这里：   
http://blog.csdn.net/gaojinshan/article/details/27665741   
http://blog.csdn.net/gaojinshan/article/details/25891809   

还有：   
http://m.weather.com.cn/data/101280601.html   

https://blog.alphatr.com/weather-jsonp-api.html   
http://www.weather.com.cn/m2/i/icon_weather/29x20/d01.gif   
http://www.cnblogs.com/technology/p/3488176.html   
http://www.cnblogs.com/waddell/p/3391137.html   
http://blog.csdn.net/hmt20130412/article/details/25657879   
http://blog.mynook.info/post/weather-com-cn-api   
