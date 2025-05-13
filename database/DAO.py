from database.DB_connect import DBConnect
from model.Product import Product


class DAO():
    @staticmethod
    def getAllColors():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)

        query = """select distinct gp.Product_color 
                    from go_products gp 
                    order by gp.Product_color"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProduct():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select *
                    from  go_products gp"""
        cursor.execute(query)

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(color):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select gds.Product_number, gds2.Product_number , count(*) as weight
                from go_daily_sales gds ,go_products gp ,go_daily_sales gds2 
                where gds.Product_number <> gds2.Product_number
                and gds.Product_number = gp.Product_number
                and gds.Retailer_code = gds2.Retailer_code 
                and gp.Product_color =  %s
                and gds.`Date` = gds2.`Date` 
                group by gds.Product_number,gds2.Product_number """
        cursor.execute(query,(color,))

        for row in cursor:
            result.append((row["p1"],row["p2"], row["peso"]))
        cursor.close()
        conn.close()
        return result
