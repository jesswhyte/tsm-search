#quick script to grab readable filename manifests for appraisers/researchers
#useful for appraisal reports, e.g. pre-acquisition
#run as python 3 
#may have to install django
import glob
import xml.etree.ElementTree
import sys
from django.utils.encoding import smart_str

target = sys.argv[1]
#grab the .xml files from the directory
filexmls = glob.iglob(target+'/**/*.xml', recursive=True)
#designate write file, named based on .xml file
f = open('00bigoldmanifest.txt', 'w')

for filexml in filexmls:
	f.write (filexml)
	f.write ("\n")
	#parse xml
	try:
		e = xml.etree.ElementTree.parse(filexml).getroot()
		#get the filenamennode and write to text file
		for filenamenode in e.findall('.//{http://www.forensicswiki.org/wiki/Category:Digital_Forensics_XML}filename'):
			filename = filenamenode.text
			filename = smart_str(filename)
			f.write (filename)
			f.write('\n')
	except: 
		f.write("PARSING ERROR")
		f.write('\n')

	f.write('\n')
##to do: expand to include prompts asking if they want to include tree, size, file type identification. 
