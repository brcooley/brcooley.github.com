#!/usr/bin/env python3

import cmd
import sys
import json
import urllib.request

DEBUG = True

FULL_NAME = 'Brett Cooley'
REQUEST_URL = 'https://raw.github.com/brcooley/brcooley.github.com/resume/resume/resume.json'
COMPANY = 'Twilio'
TITLE_STR = '='*50 + '\n' + '='*16 + ' '*3 + FULL_NAME + ' '*3 + '='*16 + '\n' + '='*50 + '\n' + \
			'{:^50}\n'.format('Resume CLI') + \
'''
  Type "?" for list of commands
  To start, try "why"\n'''

### PRIVATE ###

def _docstr(*args):
	def wrapper(fn):
		fn.__doc__ = fn.__doc__.format(*args)
		return fn
	return wrapper

class QueryShell(cmd.Cmd):
	intro = TITLE_STR
	prompt = 'brc> '

	def __init__(self,**kwargs):
		super().__init__()
		self.events = kwargs['events']
		self.categories = set(x['cat'] for x in self.events)
		self.email = kwargs['email']
		self.phone = kwargs['phone']
		self.github = kwargs['github']
		self.stack_overflow = kwargs['stack']

	def do_work(self, args):
		'''Displays a summary of events in the work category'''
		self.do_show(['work','summary'])

	def do_skills(self, args):
		'''Displays a summary of events in the skills category'''
		self.do_show(['skills','summary'])

	def do_awards(self, args):
		'''Displays a summary of events in the awards category'''
		self.do_show(['awards','summary'])

	def do_edu(self, args):
		'''Displays a summary of events in the education category'''
		self.do_show(['edu','summary'])

	def do_proj(self, args):
		'''Displays a summary of events in the projects category'''
		self.do_show(['proj','summary'])

	def do_show(self, args):
		'''Displays info about a particular event or category of events'''

	def do_cat(self, args):
		print(self.categories)

	def do_event(self, args):
		print(self.events)

	@_docstr(FULL_NAME)
	def do_contact(self, args):
		'''Displays contact info for {}'''
		print('\n' + FULL_NAME)
		print('{:<20}\t{}'.format(self.email, self.github))
		print('{:<20}\t{}\n'.format(self.phone, self.stack_overflow))

	@_docstr(COMPANY)
	def do_why(self, args):
		'''Explains why I want to work for {}'''

	def do_exit(self, args):
		'''Exits the resume shell'''
		sys.exit()


def main():
	if DEBUG:
		with open('resume.json') as f:
			raw_data = json.load(f)
	else:
		with urllib.request.urlopen(REQUEST_URL) as f:
			raw_data = json.loads(f.readall().decode('utf-8'))

	_sh = QueryShell(**raw_data)
	# _sh = QueryShell()
	_sh.cmdloop()


if __name__ == '__main__':
	main()