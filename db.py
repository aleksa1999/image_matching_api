import pymssql
import json
import ast


class DatabaseProcess:
    def __init__(self, local=True):
        if local:
            self.conn = pymssql.connect(host='NS3013855\SQLSERVER_2016',
                                        user='sa',
                                        password='?ZE?[cUh{Br%58V[',
                                        database='Sample_NearestNeighbour')
        else:
            self.conn = pymssql.connect(host='145.239.254.185\SQLSERVER_2016',
                                        user='nikita',
                                        password='nikita',
                                        database='Sample_NearestNeighbour')

    def load_database(self, field_limit=0):
        print("Loading database ...")
        cursor = self.conn.cursor()
        cursor.execute('SELECT ID, Vector FROM Datafeed_100K')

        feature_dict = {}
        for row in cursor:
            try:
                field_id = row[0]
                field_feature = ast.literal_eval(row[1])
                feature_str = field_feature['result']['feature']
                feature = ast.literal_eval(feature_str)

                feature_dict[field_id] = feature

                if len(feature_dict) >= field_limit > 0:
                    break

            except Exception as e:
                pass
                # print(e)

        return feature_dict

    def find_id(self, field_id):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * FROM Datafeed_100K WHERE ID={field_id}')

        for row in cursor:
            result = {
                'ID': row[0],
                'merchant_name': row[1],
                'aw_deep_link': row[2],
                'brand_name': row[3],
                'product_name': row[4],
                'merchant_image_url': row[5],
                'Price': str(row[6]),
                'Status': row[7],
                'CheckSumProductName': row[8],
                'ImageName': row[9],
                'Vector': row[10]
            }
            return result


if __name__ == '__main__':
    class_db = DatabaseProcess(local=False)

    # features = class_db.load_database(field_limit=20)
    # print(len(features))

    ret_db = class_db.find_id(1503)
    print(json.dumps(ret_db, indent=4))
