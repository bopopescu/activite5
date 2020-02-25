import requests


class ApiOpenFoodFact:
    def __init__(self, element_search, page_size = 50):
        self.api_url = "https://world.openfoodfacts.org/cgi/search.pl"
        self.parameters = [("tagtype_0", "categories"),
                           ("countries", "France"),
                           ("tag_contains_0", "contains"),
                           ("tag_0", element_search),
                           ("search_simple", "1"),
                           ("action", "process"),
                           ("page_size", page_size),
                           ("page", "1"),
                           ("json", "1")]
        self.dbb_insert = ["nutriscore_grade",
                           "product_name", "generic_name_fr", "stores", "brands", "url"]
        self.valid_list = []
        self.dict_bdd = {}
        self.bdd_dict_list = []

    def get_food(self):
        response = requests.get(self.api_url, self.parameters)
        if response.status_code == 200:
            return response.json()["products"]
        else:
            return None

    def check_dict(self, dict_temp):
        for keys in dict_temp:
            if not dict_temp[keys]:
                return False
        return True


    def valid_results(self):
        test = self.get_food()
        for element in test:
            dict_temp = {}
            tata = True
            for keys in self.dbb_insert:
                try:
                    dict_temp[keys] = element[keys]
                except:
                    tata = False
                    continue
            if self.check_dict(dict_temp) and tata:
                self.bdd_dict_list.append(dict_temp)

        return self.bdd_dict_list



