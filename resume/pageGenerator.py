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

# Could add about sysadmining/hardware, all OSs
fullStack = "I enjoy working on the full stack, diving into everything from the kernel to CSS. I'm not afraid of jumping into other people's code, fixing bugs, and submitting them back upstream"
network = "Multiple of my past projects have been working with level 2-4 networking. I enjoy fully understanding complex routing and network algorithms"
distributed = "I enjoy designing and implementing distributed systems. That includes architecting fault-tolerant, asynchronous services and researching the latest in lock-free data structures"
craft = "I have a passion for software, and view developing it as a craft. I strongly believe in meritocracy, and will debate anything to find the best ideas"
passion = ""

reasons = { 
	"Palantir": [fullStack,"",""],
	"SpiderOak": ["","",""],
	"FullContact": ["","",""],
	"Netflix": ["","",distributed],
	"Aglie Diagnosis": ["","",""],
	"WiFast": ["","",""],
	"Woven": ["","",""],
	"Counsyl": ["","",""],
	"Heroku": ["",network,""],
	"Hipmunk": ["","",""],
	"Mixpanel": ["","",""],
	"Pinterest": ["","",""],
	"PubNub": ["","",""],
	"Twilio": ["","",""],
	"Spotify": ["","",""],
	"Opscode": ["","",""],
	"VMWare": ["","",""],
	"SumoLogic": ["","",""],
	"Nest": ["","",""],
	"Thumbtack": ["","",""],
	"Cloudera": ["","",""],
	"Cloudflare": ["","",""],
	"CloudScaling": ["","",""]
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
		newF = re.sub(r'(?<=company: ).*',company,fileContents) # Should be \w or similar
		newF = re.sub(r'(?<=reason1: )<<REASON1>>',reasons[company][0],newF)
		newF = re.sub(r'(?<=reason2: )<<REASON2>>',reasons[company][1],newF)
		newF = re.sub(r'(?<=reason3: )<<REASON3>>',reasons[company][2],newF)
		print(newF,file=f)
	os.chdir('..')
