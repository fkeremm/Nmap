# Başlangıç Tarihi -*- 13/11/2021 20:18 -*-
# Bitiş Tarihi -*- 13/11/2021 22:11 -*-
# Coding By Saep & Aser_Vant

import os
os.system("apt install tcptraceroute")
os.system("apt install traceroute")
os.system("apt install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet NMAP")
print("""
[~] Welcome to the Nmap practical use program [~]

[~] CODİNG BY SAEP & ASER_VANT [~]

1 [~] Short Scan
2 [~] Port scanning
3 [~] Aggressive scanning
4 [~] Private Browsing(mac address)
5 [~] Private Browsing (IP address)
6 [~] Learning the Target Operating System
7 [~] Learning Target Service Versions
8 [~] Target Filtering Detection
9 [~] Firewall Bypass
""")

choose = input("Please Choose ==> ")

if choose == "1":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap "+ target)

elif choose == "2":
	target = input("Please Enter Destination IP ==> ")	
	os.system("nmap -sS -sV "+target )
	
elif choose == "3":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -A "+target )

elif choose == "4":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap 10.0.2.15 --spoof-mac 00:0B:DB:82:58:C3 "+ target)

elif choose == "5":	
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -D 77.245.159.2 " + target)

elif choose == "6":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -sS "+ target)

elif choose == "7":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -sV "+ target)

elif choose == "8":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -sA "+ target)

elif choose == "9":
	target = input("Please Enter Destination IP ==> ")
	os.system("nmap -f -f "+ target)
else:
	print("Hatlı Seçim Yeniden Dene")

again = input("Do you want to scan again y/n ==> ")

if again == "y":
	os.system("python3 nmap.py")

elif again == "n":
	print("See you again")
else:
	print("Wrong Selection Program is Closed")
