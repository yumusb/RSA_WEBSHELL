&nbsp;&nbsp;&nbsp;&nbsp;首先看到这个想法是在`学蚁致用`公众号 原文在这里[https://mp.weixin.qq.com/s/uITAIt-jj3-CYKwXQqFzMw](https://mp.weixin.qq.com/s/uITAIt-jj3-CYKwXQqFzMw)，这样不就给我这种蹭分狗断了活路了！于是，俺也想研究一下。。
&nbsp;&nbsp;&nbsp;&nbsp;虽然蚁剑中这个功能已经很好用，但是好像没办法批量操作。。 而 先知里面的原文是用php实现的，这样。。总感觉还是有一些不对劲。于是乎就想自己研究一下。找了几个RSA模块好像都是只能通过公钥加密，私钥解密。或者是使用私钥签名。但是不符合我们的要求哈，然后找到了`M2Crypto`，不过安装时候好像有点麻烦，我找的的解决办法是先apt/yum安装swig，然后直接`pip3 install M2Crypto`可以完美解决，如果使用过程中有问题，请多在网上搜寻答案（因为，我觉得这个模块好像靠运气成分比较大。。） 

程序逻辑: 生成公私钥对，使用公钥生成webshell,然后通过私钥对其进行传参  

目前已经完成的: 
- 自动生成公私钥 
- 自动生成webshell(demo.php为模板) 
- 直接传递RSA加密后的参数到SHELL 
- 直接传递RSA加密后的参数以交互  

未完成:
- 批量 
- 返回结果加密 

用法: 
1. python3 RsaWebShell.py create yourpwd(指定密码生成shell)
2. python3 RsaWebShell.py con shellurl yourpwd payload(指定SHELL地址 密码 执行payload)
3. python3 RsaWebShell.py con shellurl yourpwd(指定SHELL地址 密码 直接交互)

由于使用了f-string 所以需要python版本为3.6或者以上。

[BLOG](http://huai.pub/2019/07/17/%E5%9C%A8WebShell%E4%B8%AD%E4%BD%BF%E7%94%A8RSA%E5%8A%A0%E5%AF%86/)