import pandas as pd
import numpy as np

def generate_metadata(path_to_file):
	df = pd.read_csv(path_to_file, sep='\t', encoding = "ISO-8859-1")
	#delete columns that are created from malformatting and have no data in them
	df = df.drop(columns='url')
	df = df.drop(columns='Unnamed: 8')
	df = df.drop(columns='title')
	df = df.drop([0], axis=0)
	df.columns = ['textID', '#words', 'genre', 'country', 'website', 'url', 'title']
	np.savetxt('../cde.meta', df, delimiter='\t', fmt='%s', header= 'textID\t#words\tgenre\tcountry\twebsite\turl\ttitle')

generate_metadata('../span_sources.txt')
