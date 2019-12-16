import requests

class ApiOpenFoodFact:
    def __init__(self, element_search):
        self.api_url="https://world.openfoodfacts.org/cgi/search.pl"
        self.parameters = [("tagtype_0","categories"),
                     ("countries","France"),
                     ("tag_contains_0","contains"),
                     ("tag_0",element_search),
                     ("search_simple","1"),
                     ("action","process"),
                     ("page_size","1"),
                     ("page","1"),
                     ("json","1")]
        self.dbb_insert = ["nutriscore_score",
                    "product_name","generic_name_fr","stores","brands","url"]
        self.valid_list = []
        self.dict_bdd = {}
        self.bdd_dict_list = []


    def get_food(self):
        response = requests.get(self.api_url,self.parameters)
        if response.status_code == 200:
            return response.json()["products"]
        else:
            return None

    def check_valid_response(self):
        for element in self.get_food():
            if all (values in element for values in self.dbb_insert):
                for keys in self.dbb_insert:
                    self.dict_bdd[keys] = element[keys]
                    self.bdd_dict_list.append(self.dict_bdd)
            else:
                continue
        return self.bdd_dict_list


if __name__ == "__main__":
    test = ApiOpenFoodFact("chocolat")
    test.check_valid_response()
    # print("#################################################################")
    # print(test.get_food())
    # print("#################################################################")
    # print(test.valid_list)
    print("#################################################################")
    print(test.bdd_dict_list)

creation class mysql
    mysql.connector
commenter les class
