# !/usr/bin/python3
# @File: RSA_main.py.py
# --coding:utf-8--
# @Author:kinni
# @Time:  2019年06月05日 19:15:47
# 说明:  RSA加密算法主程序     自己写的
from RSA_file import *
from sys import exit
if __name__ =='__main__':
    display()
    while True:
        c = input(">>>")
        if c=='1':
            encrypt_file()
        if c=='2':
            decrypt_file()
        if c=='q':
            exit(0)
        display()

















