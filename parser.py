import json
import xml.etree.cElementTree as ET
import csv

index = 0

tree = ET.parse("file.xml")
root = tree.getroot()

# open a file for writing

data = open('data.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(data)


# Functions
def search(attribute):
    tbl = []
    for child in root.findall('.//Product//'+attribute):
        tbl.append(child.text)
    return tbl
def singleAttr(indexofChild, attribute):
    result = ""
    vari = False
    indexofColumn = 0
    # print "Index of Child ", indexofChild
    result = root[indexofChild].find('.//'+ attribute)
        #If result cannot be found, break
    result1 = {}
    for ind,ite in enumerate(root[indexofChild].findall('.//'+ attribute)):
        if ite.tag == "Feature":
            print "\n"
            print "Multiple: ", ite.text
            result1[ind] = ite.text
            vari = True
    if vari:
        return result1
    if (result is None):
        return None
    result = result.text
    print "-> ",attribute, ": ", result
    indexofColumn+=1
    return result



count = 0

print "root is " , root
#print "root child" , root.findall('.//Product//Title')
print "\n"
columns = {"id", "ASIN", "UPC", "Binding", "Brand", "Color", "Feature", "Height","Model", "ItemDimensions//Length", "ItemDimensions//Width", "ItemDimensions//Weight", "Amount", "Material", "Model", "PackageDimensions//Height", "PackageDimensions//Length", "PackageDimensions//Width", "PackageDimensions//Weight", "PartNumber", "ProductGroup", "ProductTypeName", "URL", "Title", "ProductCategoryId"}
columns1 = {"Title", "Number"}
print "--- Starting --- \n"
numberofProducts = len(root.getchildren())
print "Number of products: ", numberofProducts
index = 0

# dic = {}

# dic[0] = columns
# dic[1] = columns1

# print "dic: ", dic


it = 0
table = {}
overall = []
duplic = 0
for index,entries in enumerate(root.getchildren()):
    print "Index is ", index
    print '\n'
    for x,colm in enumerate(columns):
        resp = singleAttr(index, colm)
        if type(resp) == dict:  
            duplic+=1
            #print "has duplicate: ", resp
            print "\n"
            for dupl in resp:
                print "dupl", resp[dupl]
                table[colm+""+str(dupl)] = resp[dupl]
            continue
        duplic = 0
        table[colm] = resp
    print "table so far is", table
    it+=1
    print "Insert ", it
    overall.append(table.copy())
    table = {}
print "Inside overall: ", overall
# print "\n"
# print "Creating new entry" ,overall

# print "\n \n"
print "Table size is ", len(overall)
# print singleAttr(index, "Brand")
# print search("Color")

print "\n"
print "--- End ---"


data.close()


