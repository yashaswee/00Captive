import subprocess 
with open("macs.txt","w") as mac:
	subprocess.call(["sudo", "nmap", "-sP","-iL","ips.txt"],stdout=mac)
