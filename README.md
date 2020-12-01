# weiboNER-pretreatment
weibo命名实体识别数据集的预处理。weiboNER pretreatment

# 说明
网上没有weibo数据集bio-->bmes标注格式转换的程序，所以自己就写了一个。因为在处理过程中发现golden-horse那个项目上传的数据其实还是有标注错误的，比如实体开头为I，为了给其他同学创建便利，便把自己的项目传了上来。使用时，将golden-horse项目下weibo2的数据复制到本项目的根目录，执行两个处理脚本，就可以在result文件夹得到相应数据。
