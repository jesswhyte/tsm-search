import csv
import sys

f = open('tfrbl-csv.csv','rb')
xml = open('ls.csv','rb')
csvreader = csv.reader(f)
xmlreader = csv.reader(xml)
ofile = open('test.csv','wb')
writer = csv.writer (ofile, delimiter=",")

for row in csvreader:
	namecolumn = [0]
	for row in xmlreader:
		if namecolumn in row[0]:
			print ("found it, bitch")
		else:
			print ("no dice, sucka")



f.close()
ofile.close()
xml.close()
