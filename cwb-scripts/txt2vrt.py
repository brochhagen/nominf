import os
from glob import glob

def cda_postxt2_vert(file_path):
	'''Transforms a POS-tagged txt-file from the Corpus del Espanol into an encodable vrt-file''' 
	print('Transforming txt to vrt')
	lst = []
	with open(file_path, encoding ='ISO-8859-1') as f:
		line = f.readline()
		while line:
			messy_line = line.strip()
			#strip everything before the 2nd tab, inclusive
			cleaner_line = messy_line[messy_line.find('\t')+1:]
			cleaner_line = cleaner_line[cleaner_line.find('\t')+1:]
			lst.append(cleaner_line)
			line = f.readline()

	return(lst)

def get_file_paths(PATH, EXT):
	'''Get all files that end in EXT from all children of PATH'''
	return [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]	


def get_vrt(PATH, EXT):
	paths = get_file_paths(PATH, EXT)
	for i in range(len(paths)):
		print('Processing txt %d/%d' % (i, len(paths)))
		lst = cda_postxt2_vert(paths[i])
		file_id = paths[i][paths[i].find('wlp'):-4]
		with open('./pos.vrt', 'a') as outfile:
			for j in lst:
				if j[:2] == '@@':
					text_id = j[2:j.find('\t')]
					outfile.write('<text id=\"%s\">\n' % text_id)
				else:
					outfile.write('%s\n' % j)
			outfile.write('</text>\n')	