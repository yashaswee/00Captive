import subprocess
import os
import time
subprocess.call("ifconfig")
interface = input("interface > ") 
list = []
while True:
	f = input("enter range \nexmple:  1/24 or 100/124 >")
	a = f.split("/")
	if len(a) == 2:
		break
	else:
		print("exmple:  1/24 or 100/124")
for i in range(2):
	list.append(a[i])

with open('ips.txt',"w") as ip:
	for ips in range(int(list[0]),int(list[1])):
		address = ("192.168.1."+str(ips))
		ip.write(address+"\n")

os.system('gnome-terminal -- sudo python scan.py')
a = subprocess.call(["awk",'/MAC Address/ {print $3}','macs.txt'])
new_mac=input("?> ")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
print("check if you still on the network")
time.sleep(2)
subprocess.call(["ping","www.google.com","-c3"])

	
	
