import os
from os import name, system
if name == 'nt':
    system("title Đậu Đậu")
    system("mode 160, 40")
os.system("cls" if os.name == "nt" else "clear")
jawbreaker = """
  ________  __         ______             __                                                       
 /        |/  |       /      \           /  |                                                      
 $$$$$$$$/ $$ |      /$$$$$$  |         _$$ |_    __    __  _______   _______    ______    ______  
    $$ |   $$ |      $$ \__$$/  ______ / $$   |  /  |  /  |/       \ /       \  /      \  /      \ 
    $$ |   $$ |      $$      \ /      |$$$$$$/   $$ |  $$ |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
    $$ |   $$ |       $$$$$$  |$$$$$$/   $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
    $$ |   $$ |_____ /  \__$$ |          $$ |/  |$$ \__$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$/ $$ |      
    $$ |   $$       |$$    $$/           $$  $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$       |$$ |      
    $$/    $$$$$$$$/  $$$$$$/             $$$$/   $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$$/ $$/       
"""
author = "                                   # # # {} # # #".format("  Đậu Đậu  ")
print(jawbreaker)
print(author)
host=input("  [+] Nhập URL Taget: ")
time=int(input("  [+] Nhập Time (s): "))
print("================================================")
os.system(f"node TLS.js {host} {time}")
input()
