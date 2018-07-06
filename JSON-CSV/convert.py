import json
from pprint import pprint
import csv



# data = open('json.csv', 'w')

# create the csv writer object

data = {}
iter = 0
with open('Prod_data3.json') as json_data:
    d = json.load(json_data)
    length = len(d)
    print "Length is: ", length

    for row in d:
        #print row
        data[iter] = row["RawResponse"]
        iter = iter+1
    with open('json.csv', 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, data.keys())
        w.writeheader()
        w.writerow(data)
    #print data    
f.close()
#csv_file.close()
json_data.close()
#     data = json.load(f)
#     #print data["RawResponse"]
#     with open("json.csv", "wb") as csv_file:
#         writer = csv.writer(csv_file, delimiter=' ')
#         it = 0
#         for line in data:
#             if it >5:
#                 break
#             it = it +1
#             writer.writerow(line["RawResponse"])
#     ## Python will convert \n to os.linesep
#     f.close()