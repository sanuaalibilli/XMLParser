import  xml.etree.ElementTree as ET
import csv
import sys
import os
from ParserUtil import *



#DEFINE INPUT AND OUTPUT FILES
xmlfileName="D:\\tempDir\\InputXML.xml"
csvfileName="D:\\tempDir\\OutputCSV.csv"

#Open Input File
openXml=open(xmlfileName,"r")

#Variable to Store Single <Account> Information
oneRecordXML=""

#Variable to detect Start of Account Information
recordStart = False
#Variable to detect End of Account Information
recordEnd = False
#Variable to hold Accounts Count
recordCount = 0

#Open Output file
openCSV = open(csvfileName,"a")

#Create Header and write it to CSV File
header = processRecord("")
print(header)
openCSV.write(header+"\n")

#Start Reading the XML file for accounts information
while True:
    line = openXml.readline()
    
    #Exit loop on EOF
    if not line: 
        break
    
    str = line.strip()
    
    #Detect Start of single account data 
    if(str.startswith("<account>")):
        recordStart = True

    #Detect End of single account data 
    if(str.endswith("</account>")):
        if(recordStart == True):
            recordEnd = True
    
    #If account info started append the data to oneRecordXML variable until End is reached       
    if(recordStart):
        oneRecordXML=oneRecordXML+str+"\n"
    
    #if End of Account Info Reached Process the single Record XML data to get the CSV Data
    if(recordEnd and recordStart):
        #send the single account info to processRecord() method which returns the parsed CSV formatted line.
        csvRecord=(processRecord(oneRecordXML.strip()))
        
        #write the record to the output file
        print(csvRecord)
        openCSV.write(csvRecord+"\n")
        
        #reset the start/stop flags and oneRecordXML variable
        recordStart = False
        recordEnd = False
        oneRecordXML = ""
        #increment the record Counter
        recordCount = recordCount+1
        
        
#print Total Records Processed:
print(recordCount, " Records Processed!!")

#close both the files 
openXml.close()
openCSV.close()
 