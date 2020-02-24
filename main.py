from request_api import ApiOpenFoodFact
from sql import SqlInject
from newgui import GuiFood

# Food we're going to work on
foods = ["chocolat", "purée", "biscuit","brioche"]

# Check if the database exist
# try:
#     test = SqlInject([], 'chocolat')
#
# except mysql.connector.errors.ProgrammingError:
#     print("create de database first!!!")
#     os.system("mysql < create-db2.sql")

for food in foods:
    api = ApiOpenFoodFact(food)
    api.valid_results()
    api_bdd = SqlInject(api.bdd_dict_list, food)
    check_dupplicate = api_bdd.existing_entry()
    if check_dupplicate:
        api_bdd.inject_category()
        api_bdd.inject_product()
    else:
        continue

if __name__ == '__main__':
    test = api_bdd.get_categorized_food("purée")
    print(test)
    app = GuiFood()
    app.mainloop()
