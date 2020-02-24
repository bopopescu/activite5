from sql import SqlInject
from request_api import ApiOpenFoodFact
import mysql.connector
import os

#LIST OF PRODUCTS
product = ["jambon","chocolat","biscuit"]

#CHECK IF THE DATABASE EXIST
try:
    test = SqlInject([], 'chocolat')

except mysql.connector.errors.ProgrammingError:
    print("create de database first!!!")
    os.system("mysql < create-db2.sql")


#FILL THE DATABASE
for i in product:
    api = ApiOpenFoodFact(i)
    api.valid_results
    api_bdd=SqlInject(api.bdd_dict_list, i)
    api_bdd.inject_category()
    api_bdd.inject_product()
