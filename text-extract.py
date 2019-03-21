import os
import re
 
directory = os.fsencode('CdE/text_AR-tez/') # directory with individual text files
pattern = r'(?:[^ ]+ ){0,3}\w+er|ir|ar\b(?: [^ ]+){0,3}'#pattern we're after as a regular expression, see https://regex101.com/r/pB3eW0/1

for file in os.listdir(directory):

	filename = os.fsdecode(file)
	with open(os.fsdecode(directory)+filename, 'r') as f:
		result = re.findall(pattern, f.read())
		print(result)