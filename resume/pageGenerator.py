import os
import re
import sys
import shutil
import hashlib

COMPANY_LIST = [
	"Palantir",
	"SpiderOak",
	"FullContact",
	"Netflix",
	"Aglie Diagnosis",
	"WiFast",
	"Woven",
	"Counsyl",
	"Heroku",
	"Hipmunk",
	"Mixpanel",
	"Pinterest",
	"PubNub",
	"Twilio",
	"Spotify",
	"Opscode",
	"VMWare",
	"SumoLogic",
	"Nest",
	"Thumbtack",
	"Cloudera",
	"Cloudflare",
	"CloudScaling"
]

reasons = {
	"Palantir":"",
	"SpiderOak":"",
	"FullContact":"",
	"Netflix":"",
	"Aglie Diagnosis":"",
	"WiFast":"",
	"Woven":"",
	"Counsyl":"",
	"Heroku":"",
	"Hipmunk":"",
	"Mixpanel":"",
	"Pinterest":"",
	"PubNub":"",
	"Twilio":"",
	"Spotify":"",
	"Opscode":"",
	"VMWare":"",
	"SumoLogic":"",
	"Nest":"",
	"Thumbtack":"",
	"Cloudera":"",
	"Cloudflare":"",
	"CloudScaling":""
}

if os.path.basename(os.getcwd()) != 'resume':
	print("Must run from the resume directory, not {}".format(os.path.basename(os.getcwd())))
	sys.exit()

for company in COMPANY_LIST:
	chksum = hashlib.sha256(company.encode("utf-8")).hexdigest()[:6]
	os.mkdir(chksum)
	os.chdir(chksum)
	# print(chksum)
	shutil.copy2(os.path.join("..","index.html"),"index.html")
	with open("index.html","r") as f:
		fileContents = f.read()
	with open("index.html","w") as f:
		newF = re.sub(r'(?<=company: ).*',company,fileContents)
		newF = re.sub(r'',reasons[company],newF)
		print(newF,file=f)
	os.chdir('..')
