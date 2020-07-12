import sys
import  xml.etree.ElementTree as ET
import csv

def processRecord(oneRecord):
    recordCSVLine=""
    full = readColumnXPaths()
    columnNames = full[0]
    columnDefs = full[1]
    if(oneRecord==""):        
        for colname in (columnNames):
            if(recordCSVLine==""):
                recordCSVLine=colname
            else:
                recordCSVLine=recordCSVLine+"|"+colname.strip()
    
    else:       
        root = ET.fromstring(oneRecord)
        for columnDef in columnDefs:
            xpath=""
            if isAttrib(columnDef):
                xpath=getActualXPath(columnDef)
            else:
                xpath=columnDef
            elements = root.findall(xpath)
            csvEntry = ""
            if (len(elements) > 1):
                csvEntry=csvEntry+"["
                for ele in elements:
                    if isAttrib(columnDef):
                        csvEntry=csvEntry+(ele.get(getAttributeFromXPath(columnDef)))+","
                    else:
                        csvEntry=csvEntry+ele.text.strip()+","
                csvEntry=csvEntry.strip(",")+"]"
            else:
                if (len(elements) == 1):
                    for ele1 in elements:
                        csvEntry=ele1.text.strip()
                else:
                    csvEntry="NONE"
    
            recordCSVLine = recordCSVLine+csvEntry+"|"
        
        
                

    #print(recordCSVLine)
    return recordCSVLine.strip("|");


def isAttrib(columnDef):
    if "[@" in columnDef:
        return True
    else:
        return False

def getActualXPath(columnDef):
    return columnDef.split("[@")[0]
    
def getAttributeFromXPath(columnDef):
    return columnDef.split("[@")[1].strip("]")   
    
def readColumnXPaths():
    columnDef = open("ColumnDefinitions.properties",'r')
    columnNames = []
    columnDefs = []
    while True:
        line=  columnDef.readline()
        if not line:
            break
        
        str=line.strip()
        #print(str)
        columnNames.append(str.split("=")[0])
        columnDefs.append(str.split("=")[1])
    #print("Col Names ", columnNames)
    #print("Col Defs ", columnDefs)
    return columnNames,columnDefs   