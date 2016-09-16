#quick script to grab readable filename manifests for appraisers/researchers
#useful for appraisal reports, e.g. pre-acquisition
import glob
import xml.etree.ElementTree
import sys

target = sys.argv[1]
#grab the .xml files from the directory
filexmls = glob.glob(target+"*.xml")
#designate write file, named based on .xml file
f = open('arch_'+filexmls[0].split('/')[-1], 'w')
for filexml in filexmls:
	f.write (filexml)
	f.write ("\n")
	#parse xml
	e = xml.etree.ElementTree.parse(filexml).getroot()
	#get the filenamennode and write to text file
	for filenamenode in e.findall('.//{http://www.forensicswiki.org/wiki/Category:Digital_Forensics_XML}filename'):
		f.write (filenamenode.text)
		f.write('\n')
	f.write('\n')
##to do: expand to include prompts asking if they want to include tree, size, file type identification. 
