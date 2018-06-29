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
def singleAttr(index, attribute):
    for attr in root[index].findall('.//'+ attribute):
        result = attr.text
    index = index + 1
    return result



count = 0

print "root is " , root
#print "root child" , root.findall('.//Product//Title')
print "\n"
columns = {"id", "AISN", "UPC", "Binding", "Brand", "Color", "Feature", "Item_Height", "Item_Length", "Item_Width", "Item_Weight", "Amount", "Material", "Model", "Package_Height", "Package_Length", "Package_Width", "Package_Weight", "PartNumber", "ProductGroup", "ProductTypeName", "SmallImage", "Title", "ProductCategoryId"}
columns1 = {"Title", "Number"}
print "--- Starting --- \n"
numberofProducts = len(root.getchildren())
print "Number of products: ", numberofProducts
index = 0


table = {}
table[0] = "Eyal"
print "Table: ",table

print singleAttr(index, "Brand")
print search("Color")

print "\n"
print "--- End ---"


data.close()


