# Corpus analysis

Following the lead of Grimm & McNally (2015), we want to take a quantitative look at the empirical distribution of Spanish nominalized infinitives. In the following, we summarize our approach

### Collection
* Corpus: [Corpus del Español](https://www.corpusdelespanol.org/web-dial/)
* Extract utterances with endings *-ir*, *-ar*, or *er*
	* Without POS-tagging
	* With POS-tagging
* Context window of 200 words


### Cleaning
* Exclude false infinitives **is there a syntactic criterion we could use for filtering? Otherwise use RAE or similar as criterion for lexicalization**


#### Plain text

* I would not remove the special symbol: "@". As far as I can see, it:
	* Indicates a new fragment in the corpus when its doubled and followed by a digit, e.g. *@@1100*
	* Indicates that trailing text is missing, e.g. *and then the doctor said @ @ @ @ @ @ @ @ @ Jane was content.* Removing these markers could cause confusion by assuming that the text continues where it doesn't.


### Categorization


### Analysis  