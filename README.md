# XML-CSV
Convert XML JSON files to CSV

Scripts to convert JSON files to CSV

GET: “/all” -> Retrieves all the entries in the DB
GET: “/all/search/(UPC)” -> Gets all the records that match the UPC provided
GET: “/all/(ASIN)” -> Gets all the records that match the ASIN number
POST: “/todo” -> Insert into database as a new record. Must provide as x-wwww-form-urlencoded: the data to be inputed, along with the correct column names)
PUT: “/todo” -> Update a record with task_id (the ASIN number to be assigned), task (the value of the column to be edited and column (the name of the column to be changed).Must provide as x-wwww-form-urlencoded
DELETE: /todo/(ASIN) -> Delete an entry. Provide the ASIN number

To see code, look in https://github.com/eyalabadi98/XML-CSV/blob/master/RestAPI/server.js
