import mysql.connector


class SqlInject(object):
    def __init__(self, list_product, category):
        self.connect = mysql.connector.connect(
            user='toto', database='food', password='tata')
        self.cursor = self.connect.cursor(buffered=True)
        self.list_product = list_product
        self.category = category
        self.id_substitute = 0
        self.id_product = 0

    def inject_category(self):
        self.cursor.execute(
            "INSERT INTO category (name) VALUES ('%s');" % self.category)

    def InjectProduct(self):
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
    def GetProduct(self):
        self.cursor.execute("SELECT * FROM product;")
        test = self.cursor.fetchall()
        return test
    # 
    # def SaveSubstitute(self, self.id_product, self.id_substitute):
    #     self.product = product
    #     self.substitute = substitute
    #     sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (
    #         'substitute', self.product, self.substitute)
