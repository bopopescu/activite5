import mysql.connector


class SqlInject(object):
    def __init__(self, list_product, category):
        self.connect = mysql.connector.connect(
            user='toto', database='food', password='tata')
        self.cursor = self.connect.cursor(buffered=True)
        self.list_product = list_product
        self.category = category

    def inject_category(self):
        self.cursor.execute(
            "INSERT INTO category (name) VALUES ('%s');" % self.category)

    def InjectProduct(self):
        self.cursor.execute(
            "SELECT idcategory from category WHERE name= '%s' " % (self.category))
        category_id = self.cursor.fetchone()
        for dict in self.list_product:
            dict["category_id"] = category_id[0]
            placeholders = ', '.join(['%s'] * len(dict))
            columns = ', '.join(str(x) for x in dict.keys())
            values = ', '.join(
                "'" + str(x).replace("'", "_") + "'" for x in dict.values())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (
                'product', columns, values)
            print(sql)
            f = open("test.sql", "a")
            f.write(sql + '\n')
            self.cursor.execute(sql)
            self.connect.commit()
