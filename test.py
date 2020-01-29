from sql import SqlInject
from request_api import ApiOpenFoodFact


test = ApiOpenFoodFact("chocolat")
test.check_valid_response()

toto = SqlInject(test.bdd_dict_list, 'chocolat')
toto.inject_category()
toto.InjectProduct()
tata=toto.GetProduct()
print(tata)
# tabler = PrettyTable(test.dbb_insert.insert(0,"Num"))
# for i in test.bdd_dict_list:
#     tabler.add_row(list(i.values()))


# cnx = mysql.connector.connect(user = 'toto', database = 'food', password = 'tata')
# cursor = cnx.cursor()
# tata = cursor.execute("SELECT idcategory from category WHERE name='jambon'")
# print(tata)




# from request_api import ApiOpenFoodFact

# toto = ApiOpenFoodFact("purée")
#
# toto.check_valid_response()
# list = toto.bdd_dict_list
#
#
#
#
#
#
#
# for dict in list:
#     placeholders = ', '.join(['%s'] * len(dict))
#     columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in dict.keys())
#     values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in dict.values())
#     sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('product', columns, values)
#     # print(sql)
#     f = open("test.sql", "a")
#     f.write(sql + '\n')
#     cursor.execute(sql)
#
# cursor.execute("INSERT INTO category (name) VALUES ('purée') ")
# cnx.commit()
