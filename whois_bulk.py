import time
import subprocess

f = open("whois_ip_list.txt","r")

for ip in f.readlines():
	time.sleep(1)
	test = subprocess.Popen(["whois", ip.rstrip()], stdout=subprocess.PIPE)
	output = test.communicate()[0]
	list_output =  (output.splitlines())
	for x in list_output:
		if ("OrgName") in x:
			print ip.rstrip() + "   "+ x
