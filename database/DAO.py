from database.DB_connect import DBConnect
from model.Arco import Arco
from model.ordine import Ordine
from model.store import Store


class DAO():
    @staticmethod
    def getAllStore():

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query= """
                select distinct s.*
                from stores s 
                """

        cursor.execute(query)

        result=[]

        for row in cursor:
            result.append(Store(**row))

        return result

    @staticmethod
    def getAllNodes(idstore):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                    select distinct o.*
                    from stores s , orders o 
                    where s.store_id= %s
                    and s.store_id = o.store_id 
                    """

        cursor.execute(query, (idstore,))

        result = []

        for row in cursor:
            result.append(Ordine(**row))

        return result

    @staticmethod
    def getAllEdges(idmap,idstore,k):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
                        select  o.order_id as o1, o2.order_id as o2 , count(oi.item_id) as n
                        from orders o ,orders o2 , stores s ,order_items oi 
                        where s.store_id =%s
                        and s.store_id = o.store_id 
                        and s.store_id = o2.store_id 
                        and oi.order_id = o2.order_id 
                        and o.order_id < o2.order_id
                        and abs(datediff(o2.order_date,o.order_date)) <%s
                        and abs(datediff(o2.order_date,o.order_date)) >%s
                        group by o.order_id, o2.order_id  
                        
                        """

        cursor.execute(query, (idstore, k, 0))

        result = []

        for row in cursor:
            result.append((idmap[row["o1"]], idmap[row["o2"]], row["n"]))

        return result
