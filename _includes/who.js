<script type="text/javascript">
	// format function taken from Stack Overflow (http://stackoverflow.com/a/4673436/950912)
	String.prototype.format = function() {
	  var args = arguments;
	  return this.replace(/{(\d+)}/g, function(match, number) { 
	    return typeof args[number] != 'undefined'? args[number] : match;
	  });
	};

	var fullStack = "I enjoy working on the full stack, diving into everything from the kernel to CSS. I'm not afraid of jumping into other people's code, fixing bugs, and submitting them back upstream";
	var network = "Multiple of my past projects have been working with level 2-4 networking. I enjoy fully understanding complex routing and networking algorithms";
	var distributed = "I enjoy designing and implementing distributed systems. That includes everything from architecting fault-tolerant, asynchronous services to researching the latest in lock-free data structures";
	var craft = "I have a passion for software, and view developing it as a craft. I strongly believe in meritocracy, and will debate anything to find the best ideas";
	var general = "I am driven by a desire to design, implement, test, and scale elegant and effective code.  This is something that applies to every project, regardless of language or size";
	var measure = "I like to test code in the truest sense of the word.  Not only should it be correct, but it should be efficient and robust.  Automated tests make fast iterations that consistently improve software possible";
	var api = "API design is my tech drug.  I live by the ideals of REST and making complex tasks simple.  API's should be like good wine: simple and fun to the inexperienced with hidden subtly and power(ful flavors) for the expert";
	var automation = 'If I had a motto, "Automate everything" would be a serious contender.  {0} is the kind of company that fully embraces this idea, and is aligned with how I think about software';
	var world = "I want to change the world using software.  {0} is a place where I can try to do just that full-time, bettering the lives of millions of people along the way";
	var tools = "I live for embracing and extending the tools that other developers use to build awesome software. {0} gives me the opportunity to effect thousands of engineers in a real and tangible way";
	var tech = "New and emerging technology always excites me.  {0} is pushing the boundaries of what is possible, and would give me an amazing chance to change the world";

	var reasons = {
		'1720d8': {
			'name': 'Github',
			'reasons': [fullStack, distributed, tools.format('Github')]
		},
		'd722b1': {
			'name': 'Twilio',
			'reasons': [api, distributed, tools.format('Twilio')]
		},
		'26f9a1': {
			'name': 'Cloudera',
			'reasons': [distributed, tools.format('Cloudera'), craft]
		},
		'f09f14': {
			'name': 'Netflix',
			'reasons': [measure, distributed, automation.format('Netflix')]
		},
		'daa4f9': {
			'name': 'Heroku',
			'reasons': [distributed, network, tools.format('Heroku')]
		},
		'099137': {
			'name': 'Mozilla',
			'reasons': [craft, network, world.format('Mozilla')]
		},
		'afd623': {
			'name': 'SpaceX',
			'reasons': [fullStack, measure, tech.format('SpaceX')]
		},
		'f89f85': {
			'name': 'Tesla',
			'reasons': [general, craft, tech.format('Tesla')]
		},
		'0fe8e0': {
			'name': 'IFTTT',
			'reasons': [fullStack, automation.format('IFTTT'), craft]
		},
		'c11092': {
			'name': 'Square',
			'reasons': [distributed, tech.format('Square'), craft]
		},
		'bb0347': {
			'name': 'you',
			'reasons': [general, craft, fullStack]
		}
	}

	var hash = window.location.href.split('#')[1] || 'default';
	if (!reasons[hash]) {
		hash = 'bb0347';
	}
	// get reasons from json
	var company_name = reasons[hash]['name'];
	var reason_text = ['<ul>'];
	for (var i = reasons[hash]['reasons'].length - 1; i >= 0; i--) {
		reason_text.push('<li>' + reasons[hash]['reasons'][i] + '</li>');
	};
	reason_text.push('</ul>');
	reason_text = reason_text.join('');

	document.getElementById('company-name').insertAdjacentHTML('afterbegin', company_name);
	document.getElementById('pitch').insertAdjacentHTML('afterbegin', reason_text);
</script>