# - 小狼毫如何导入自定义的词库

小狼毫导入自定义的词库。有点类似于ananconda，不同的环境下可以使用不同的库或包。可以在搜狗词库https://pinyin.sogou.com/dict/ 中下载自己感兴趣的词库，下载为scel格式文件，然后利用“深蓝词库转换工具”，将其
转换为txt文件，存在本地。接下来的任务可以运行程序完成，具体流程如下。

然后在RIME的用户文件夹下，新建一个luna_pinyin_simp.custom.yaml文件，里面的内容是<br>
patch:<br>
  'translator/dictionary': luna_pinyin.extended<br>
  
然后新建一个luna_pinyin.extended.dict.yaml文件，输入的内容如下
---
name: luna_pinyin.extended
version: "2021.01.01"
sort: by_wight
use_preset_vocabulary: true

import_tables:
    - luna_pinyin	\#这个是默认使用的明月拼音，没事别删
    - luna_pinyin.quanxue   \#这个是词库的文件名，以后别的词库也要这样输入进来才有效
    - luna_pinyin.history   
    - luna_pinyin.laozi
    - luna_pinyin.programmer
    - luna_pinyin.wenyanwen
