import json
import xml.etree.cElementTree as ET
import csv

index = 0

tree = ET.parse("final.xml")
root = tree.getroot()

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
        if ite.tag == "Feature" or ite.tag == "MaterialType":
            print "\n"
            # print "Multiple: ", ite.text
            result1[ind] = ite.text
            vari = True
    if vari:
        return result1
    if (result is None):
        return None
    result = result.text
    # print "-> ",attribute, ": ", result
    indexofColumn+=1
    return result



count = 0

print "root is " , root
#print "root child" , root.findall('.//Product//Title')
print "\n"
columns = {"id", "ASIN", "UPC", "Binding", "Brand", "Color", "Feature", "Height","Model", "ItemDimensions//Length", "ItemDimensions//Width", "ItemDimensions//Weight", "Amount", "MaterialType", "Model", "PackageDimensions//Height", "PackageDimensions//Length", "PackageDimensions//Width", "PackageDimensions//Weight", "PartNumber", "ProductGroup", "ProductTypeName", "URL", "Title", "ProductCategoryId"}
columns1 = {"Title", "Number"}
# print "--- Starting --- \n"
numberofProducts = len(root.getchildren())
# print "Number of products: ", numberofProducts
index = 0


it = 0
table = {"MaterialType0": "", "MaterialType1": "", "Feature6": "", "Feature5":"", "Feature7":"", "Feature8":"", "Feature9":"", "Feature": "", 'Feature15':"", 'Feature14':"", 'Feature10':"", 'Feature11':"", 'Feature12':"", 'Feature13':"", "Feature16":"", 'MaterialType2':"", "MaterialType3": "", "MaterialType4": "", 'MaterialType8':"", 'MaterialType5':"", 'MaterialType6':"", 'MaterialType7':"", 'Feature18':"", 'Feature17':"", 'Feature29':"", 'Feature28':"", 'Feature25':"", 'Feature24':"", 'Feature27':"", 'Feature26':"", 'Feature21':"", 'Feature20':"", 'Feature23':"", 'Feature22':"", 'Feature19':"", 'Feature30':"", 'Feature31':"", 'MaterialType9':"", 'MaterialType85':"",'MaterialType84':"",'MaterialType87':"",'MaterialType86':"",'MaterialType81':"",'MaterialType80':"",'MaterialType83':"",'MaterialType82':"",'MaterialType28':"",'MaterialType89':"",'MaterialType88':"",'MaterialType41':"",'MaterialType40':"",'MaterialType43':"",'MaterialType42':"",'MaterialType45':"",'MaterialType44':"",'MaterialType47':"",'MaterialType46':"",'MaterialType49':"",'MaterialType48':"",'MaterialType61':"",'MaterialType78':"",'MaterialType79':"",'MaterialType74':"",'MaterialType75':"",'MaterialType76':"",'MaterialType77':"",'MaterialType70':"",'MaterialType71':"",'MaterialType72':"",'MaterialType73':"",'MaterialType38':"",'MaterialType39':"",'MaterialType54':"",'MaterialType31':"",'MaterialType32':"",'MaterialType33':"",'MaterialType35':"",'MaterialType36':"",'MaterialType30':"",'MaterialType20':"",'MaterialType37':"",'MaterialType58':"",'MaterialType59':"",'MaterialType34':"",'MaterialType69':"",'MaterialType68':"",'MaterialType63':"",'MaterialType62':"",'MaterialType60':"",'MaterialType67':"",'MaterialType66':"",'MaterialType65':"",'MaterialType64':"",'MaterialType27':"",'MaterialType25':"",'MaterialType24':"",'MaterialType22':"",'MaterialType21':"",'MaterialType29':"",'MaterialType55':"",'MaterialType26':"",'MaterialType96':"",'MaterialType97':"",'MaterialType94':"",'MaterialType95':"",'MaterialType92':"",'MaterialType93':"",'MaterialType90':"",'MaterialType91':"",'MaterialType23':"",'MaterialType98':"",'MaterialType99':"",'MaterialType52':"",'MaterialType53':"",'MaterialType50':"",'MaterialType51':"",'MaterialType56':"",'MaterialType57':"",'MaterialType18':"",'MaterialType19':"",'MaterialType16':"",'MaterialType17':"",'MaterialType14':"",'MaterialType15':"",'MaterialType12':"",'MaterialType13':"",'MaterialType10':"",'MaterialType11':""}

overall = []
duplic = 0
for index,entries in enumerate(root.getchildren()):
    print "Adding",
    print '\n'
    for x,colm in enumerate(columns):
        resp = singleAttr(index, colm)
        if type(resp) == dict:  
            duplic+=1
            #print "has duplicate: ", resp
            # print "\n"
            for dupl in resp:
                # print "dupl", resp[dupl] 
                table[colm+""+str(dupl)] = resp[dupl]
            continue
        duplic = 0
        table[colm] = resp
    # print "table so far is", table
    it+=1
    print "Insert ", it
    overall.append(table.copy())
    table = {}
# print "Inside overall: ", overall
# print "\n"
# print "Creating new entry" ,overall

# print "\n \n"
print "Table size is ", len(overall)
# print singleAttr(index, "Brand")
# print search("Color")
print "\n"
print "--- End ---"




keys = overall[0].keys()
with open('data.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(overall)

