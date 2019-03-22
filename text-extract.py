import os
import re

window_size = 3

#directory = os.fsencode('CdE/text_AR-tez/') # directory with individual text files
with open('CdE/text_AR-tez/AR-B-00.txt') as f:
	with open('CdE/text_output/text_data.txt', mode = 'w') as h:
		for line in f:
			words = line.split()
			for i in range(len(words)):
				if words[i][-2:] in ['ar', 'er', 'ir']:
					if i > 0:
						if words[i][0].islower() or words[i-1][-1] == '.':
							if i < window_size: 
								left_window = i-1
							else:
								left_window = i-window_size
							if len(words) < i+window_size:
								right_window = len(words)
							else:
								right_window = i+window_size+1
							h.write('%s\n' % ' '.join(words[left_window:right_window]))

# for file in os.listdir(directory):

# 	filename = os.fsdecode(file)
# 	with open(os.fsdecode(directory)+filename, 'r') as f:
# 		result = re.findall(pattern, f.read())
# 		print(result)