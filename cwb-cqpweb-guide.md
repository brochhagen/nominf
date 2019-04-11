---
output:
  html_document: default
  pdf_document: default
---
# CQP(web) installation @ corptedig-glif

This is a rough guideline to install corpora on the corptedig-glif [CQPweb interface](http://corptedig-glif.upf.edu/cqpweb/), written by [Thomas Brochhagen](http://brochhagen.github.io). 

Most of the (active) time will likely be spent cleaning the data and putting it into the right format prior to indexing. This guide is supposed to offer some orientation for what comes after. Particularly to not get confused with what goes where on the server. 

The content below on data formats and indexing is better covered by online documentation. I added a brief sketch just for the sake of concreteness.   

Always double-check if the steps make sense to you in view of your data! 

## What you need
  * The latest *CWB main package* as well as the *Perl API & Support packages* from the [IMS Open Corpus Workbench](http://cwb.sourceforge.net/). The latter is optional but recommended.

* Access to the server that hosts CQPweb in order to upload files and set things up. Its located at `corptedig-glif.s.upf.edu` 

* An admin account with full privleges for the [corptedig-glif CQPweb interface](http://corptedig-glif.upf.edu/cqpweb/)


## Local setup


### Data format
For POS-tagged data, the cwb tools expect: one or multiple tab-separated vertical files (`.vrt`-files). Except for the XML-markup (see below), each row in a `vrt`-file contains a word followed by any additional information for it (its POS-tag, lemma, e.g.).

Each `vrt`-file needs to begin (and end) with at least one  `<text>`-tag. In general, the tools do a good job at recognizing XML information if you tell them to expect it. A minimal example of a ready to be processed `vrt`-file would look as follows:

| | | |
|:-|:-|:-|
| \<text>   &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; |  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; | |
| She  | PRP  | she |
| sells  | VRZ  | sell | 
| seashells  |  NNS | seashell |
| \</text> | | |
| &nbsp; &nbsp; &nbsp; | | |


You may want to at least add an `id`-attribute to the tags. The more information the merrier.
The file could look like this:

| | | |
|:-|:-|:-|
| \<text id='tales_of_sales_by_the_sea' year='2019'>  | &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  | |
| She  | PRP  | she |
| sells  | VRZ  | sell |   
| seashells  |  NNS | seashell |
| \</text> | | | 
| &nbsp; &nbsp; &nbsp; | | |

As noted above, if you have no information to add, a single `<text>`-tag enclosing all the text will do.

### Indexing
Let's call our corpus `SEA`. Assume that all its vertical files are in `/corpus/vrt/`. Create a folder to store the indexed corpus:

```
mkdir corpus/data
```
Assuming the second, richer, `vrt`-format, including an `id` and a `year` tag, build the corpus:
```
cwb-encode -c utf8 -d corpus/data -F corpus/vrt -R corpus/sea -xsB -P pos -P lemma -S text:0+id+year
```
In the order in which the flags appear, this tells CWB to encode the corpus as utf8; to store its output at `corpus/data`; to take its input from `corpus/vrt`; to store the corpus' registry as `corpus/sea`; to parse the XML; to expect, after the first column, reserved for words, a POS tag and a lemma; and to parse `<text>`-tags with their information appropriately. Further XML-markup needs to be added with more `-S` flags.

Next, index and compress the corpus:
```
cwb-make -r corpus/ -V SEA
```
Skip the `-V` flag if your corpus is large as it may take too long.

### Testing
See whether if everything works locally. E.g., 
```
cqp -r corpus/
show corpora;
SEA;
"seashells";
```
### Server-side
The main challenge is understanding how the directories are set up so that everything is read correctly.

First, upload the registry:
```
scp corpus/SEA/sea YOUR-USERNAME@corptedig-glif.s.upf.edu:../../mnt/vmdata/corptedig-glif/corpora/cqp/registry/sea
```
Make a directory to save the data (you'll need root privileges)

```
sudo mkdir ../../mnt/vmdata/corptedig-glif/corpora/data/sea
```

Move your data (everything in `corpus/data` in our example) to this folder. 

Next, change the `user:group` of the files.

```
sudo su -
sudo chown -R www-data:cqpweb /mnt/vmdata/corptedig-glif/corpora/cqp/data/sea
sudo chown www-data:cqpweb /mnt/vmdata/corptedig-glif/corpora/cqp/registry/sea
```

Next, change the registry at `mnt/vmdata/corptedig-glif/corpora/cqp/registry/sea` to indicate the correct path to its data: `/mnt/vmdata/corptedig-glif/corpora/cqp/data/sea`. 


### Graphical interface (CQPweb) + server
Log in to the graphical interface of CQPweb. 

Go to the `admin control panel`, then to `install nex corpus`, then to `Click here to install a corpus you have already indexed in CWB.`

Enter the information and press the button at the bottom. If everything is where it should be on the server, then you will move on to the next window. 

At this point, if you press on, you will prompted with an error. The reason is that CQPweb did not generate the necessary subpages to go with the corpus you just installed. Generate them yourself by copying them from a different corpus. For instance from `adkintuwe`:

```
mkdir mnt/vmdata/corptedig-glif/cqpweb/sea
cp -a mnt/vmdata/corptedig-glif/cqpweb/adkintuwe/. mnt/vmdata/corptedig-glif/cqpweb/sea
```

If you do this before installing the corpus the system might complain. If you delete the corpus you need to do this again.

## Metadata
Setting up the corpus' metadata is required for it to be queryable. If you have metadata, you need to upload it to `/mnt/vmdata/corptedig-glif/corpora/cqp/uploads/`. Uploading files through the graphical interface does **not** seem to work. If the upload folder does not exist: create it first. 

Youŕe done! Congratulations. Move on to configure the remaining settings of the corpus.

I hope this helps. Good luck!