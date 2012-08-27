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
	"Agile Diagnosis",
	"WiFast",
	"Woven",
	"Counsyl",
	"Heroku",
	"Hipmunk",
	"Mixpanel",
	"Pinterest",
	# "PubNub",
	# "Twilio",
	# "Spotify",
	# "Opscode",
	# "VMWare",
	# "SumoLogic",
	# "Nest",
	# "Thumbtack",
	# "Cloudera",
	# "Cloudflare",
	# "CloudScaling",
	"You"
]

# Could add about sysadmining/hardware, all OSs
fullStack = "I enjoy working on the full stack, diving into everything from the kernel to CSS. I'm not afraid of jumping into other people's code, fixing bugs, and submitting them back upstream"
network = "Multiple of my past projects have been working with level 2-4 networking. I enjoy fully understanding complex routing and networking algorithms"
distributed = "I enjoy designing and implementing distributed systems. That includes everything from architecting fault-tolerant, asynchronous services to researching the latest in lock-free data structures"
craft = "I have a passion for software, and view developing it as a craft. I strongly believe in meritocracy, and will debate anything to find the best ideas"
general = "I am driven by a desire to design, implement, test, and scale elegant and effective code.  This is something that applies to every project, regardless of language or size"
measure = "I like to test code in the truest sense of the word.  Not only should it be correct, but it should be efficient and robust.  Automated tests make fast iterations that consistently improve software possible"
api = "API design is my tech drug.  I live by the ideals of REST and making complex tasks simple.  API's should be like good wine: simple and fun to the inexperienced with hidden subtly and power(ful flavors) for the expert"

automation = 'If I had a motto, "Automate everything" would be a serious contender.  {} is the kind of company that fully embraces this idea, and is aligned with how I think about software'
world = "I want to change the world using software.  {} is a place where I can try to do just that full-time, bettering the lives of millions of people along the way"
tools = "I live for embracing and extending the tools that other developers use to build awesome software. {} gives me the opportunity to effect thousands of engineers in a real and tangible way"

reasons = { 
	"Palantir": 		[craft,fullStack,world.format("Palantir")],
	"SpiderOak": 		[craft,distributed,network],
	"FullContact": 		[craft,api,"Colorado is my true home, and getting the chance to be a part of the budding tech scene in Denver would be a dream come true"],
	"Netflix": 			[measure,distributed,automation.format("Netflix")],
	"Agile Diagnosis": 	[measure,api,world.format("Agile Diagnosis")],
	"WiFast": 			[fullStack,network,craft],
	"Woven": 			[craft,fullStack,automation.format("Woven")],
	"Counsyl": 			[fullStack,craft,measure],
	"Heroku": 			[distributed,network,tools.format("Heroku")],
	"Hipmunk": 			[craft,fullStack,distributed],
	"Mixpanel": 		[distributed,api,network],
	"Pinterest": 		[craft,api,distributed],
	# "PubNub": 			["","",""],
	# "Twilio": 			["","",""],
	# "Spotify": 			["","",""],
	# "Opscode": 			["","",""],
	# "VMWare": 			["","",""],
	# "SumoLogic": 		["","",""],
	# "Nest": 			["","",""],
	# "Thumbtack": 		["","",""],
	# "Cloudera": 		["","",""],
	# "Cloudflare": 		["","",""],
	# "CloudScaling": 	["","",""],
	"You": 				[general, craft,fullStack]
}

pages = ["index","edu","work","code"] #,"print"]


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

	for company in COMPANY_LIST:
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
