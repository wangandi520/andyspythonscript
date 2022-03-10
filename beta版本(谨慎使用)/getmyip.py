import requests
import git
import time

url = 'https://ifconfig.me'

response = requests.get(url)
se = requests.Session()
if response.status_code == 200:
	newip = response.text

with open('/srv/git/getmyip/ip.txt', mode='r', encoding = 'UTF-8') as file:
	read = file.readlines()
	file.close()
	oldip = read[0]

if newip != oldip:
	newfile = open('/srv/git/getmyip/ip.txt', mode = 'w', encoding = 'UTF-8')
	newfile.writelines(newip)
	newfile.close()
	mygit = git.Git('/srv/git/getmyip')
	mygit.add('/srv/git/getmyip/ip.txt')
	mygit.commit('-m ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	mygit.push()
if newip == oldip:
	mygit = git.Git('/srv/git/getmyip')
	mygit.push()
