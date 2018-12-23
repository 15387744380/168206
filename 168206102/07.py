# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:20:54 2018

@author: 刘莹莹
"""
print("A：我没有偷钻石。")


 
print("B：D就是罪犯。")


 
print("C：B是盗窃这块钻石的罪犯。")


 
print("D：B有意诬陷我。")

def find():  
    thief = 0
    for thief in ["A","B","C","D"]:
       # thief = 64+i
        if((thief != "A") + (thief == "D") + (thief=="B") + (thief != "D") == 1):
            print("小偷是：")
            print(thief)
find()
