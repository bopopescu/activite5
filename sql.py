import mysql.connector


class SqlInject(object):
    """
    Exchange with the database

    Parameters
    ----------
    list_product : list
        Contains all the data on the food sought

    category : str
        Name of the food category

    """
    def __init__(self, list_product = [], category = 'None'):
        self.connect = mysql.connector.connect(
            user='toto', database='food', password='tata')
        self.cursor = self.connect.cursor(buffered=True)
        self.list_product = list_product
        self.category = category
        self.id_substitute = 0
        self.id_product = 0

    def existing_entry(self):
        """Check that there are no duplicates in the database

        Returns
        -------
        test : bool
            If the product already exist inside the database
        """
        self.cursor.execute(
            "SELECT name from category WHERE name= '%s' " % (self.category))
        check = self.cursor.fetchall()
        print(check)
        if check == []:
            test = True
            return test
        else:
            test = False
            return test

    def inject_category(self):
        """ Filled the category table """
        self.cursor.execute(
            "INSERT INTO category (name) VALUES ('%s');" % self.category)

    def inject_product(self):
        """ Filled the product table """
        self.cursor.execute(
            "SELECT idcategory from category WHERE name= '%s' " % (self.category))
        category_id = self.cursor.fetchone()
        for dict in self.list_product:
            dict["category_id"] = category_id[0]
            columns = ', '.join(str(x) for x in dict.keys())
            values = ', '.join(
                "'" + str(x).replace("'", "_") + "'" for x in dict.values())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (
                'product', columns, values)
            self.cursor.execute(sql)
            self.connect.commit()
    #
    def get_data_product(self, column = "id", search ="1"):
        self.cursor.execute("SELECT * FROM product WHERE %s= '%s';" % (column, search))
        data_product = self.cursor.fetchall()
        return data_product
    def get_category(self):
        self.cursor.execute("SELECT name FROM category")
        raw_category = self.cursor.fetchall()
        category = []
        for i in raw_category:
            category.append(i[0])
        return category
    def get_food_info(self, category = "chocolat"):
        self.cursor.execute("SELECT id_category FROM category WHERE name = '%s';" % (category))

    # def SaveSubstitute(self, self.id_product, self.id_substitute):
    #     self.product = product
    #     self.substitute = substitute
    #     sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (
    #         'substitute', self.product, self.substitute)
