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
distributed = "I enjoy designing and implementing distributed systems. That includes architecting fault-tolerant, asynchronous services to researching the latest in lock-free data structures"
craft = "I have a passion for software, and view developing it as a craft. I strongly believe in meritocracy, and will debate anything to find the best ideas"
world = "I want to change the world using software.  {} is a place where I can try to do just that full-time, bettering the lives of millions of people along the way"

reasons = { 
	"Palantir": [craft,fullStack,world.format("Palantir")],
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

pages = ["index","edu","work","skills","print"]


def populate(companyData):
	with open("index.html","r") as f:
		newF = f.read()
		varList = re.findall(r'<<.*>>', newF)

	with open("index.html","w") as f:
		for var in varList:
			newF = re.sub(var, companyData[var.strip('<>')], newF)

		print(newF, file=f)


def main():
	if os.path.basename(os.getcwd()) != 'resume':
		print("Must run from the resume directory, not {}".format(os.path.basename(os.getcwd())))
		sys.exit()

	for company in COMPANY_LIST[:1]:
		chksum = hashlib.sha256(company.encode("utf-8")).hexdigest()[:6]
		try:
			shutil.rmtree(chksum)
		except OSError:
			pass

		os.mkdir(chksum)
		os.chdir(chksum)

		companyData = {
			'COMPANY': company,
			'HASH': chksum,
			'REASON1': reasons[company][0],
			'REASON2': reasons[company][1],
			'REASON3': reasons[company][2]
		}

		for page in pages:
			shutil.copy(os.path.join("..",page + ".html"),page + ".html")
			if page != "index":
				os.mkdir(page)
				shutil.move(page + ".html", os.path.join(page,"index.html"))
				os.chdir(page)

			populate(companyData)

			if page != "index":
				os.chdir("..")

		os.chdir("..")


if __name__ == '__main__':
	main()
