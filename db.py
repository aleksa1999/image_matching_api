import numpy as np
import pymssql
import json
import ast


class DatabaseProcess:
    def __init__(self, local=True):
        if local:
            self.conn = pymssql.connect(host='NS3013855\SQLSERVER_2016',
                                        user='sa',
                                        password='?ZE?[cUh{Br%58V[',
                                        database='Pricetracker')
        else:
            self.conn = pymssql.connect(host='145.239.254.185\SQLSERVER_2016',
                                        user='nikita_new',
                                        password='nikita_new',
                                        database='Pricetracker')

    def load_database(self, field_limit=0):
        print("Loading database ...")
        cursor = self.conn.cursor()
        cursor.execute('SELECT ID, ImageVector FROM KeywordData_Task_UserID')

        feature_dict = {}
        for row in cursor:
            try:
                field_id = row[0]
                field_feature = ast.literal_eval(row[1])
                feature_str = field_feature['result']['feature']
                feature = ast.literal_eval(feature_str)

                feature_dict[field_id] = np.array(feature)

                if len(feature_dict) >= field_limit > 0:
                    break

            except Exception as e:
                pass
                # print(e)

        return feature_dict

    def find_id(self, field_id):
        cursor = self.conn.cursor()
        # cursor.execute(f'SELECT * FROM KeywordData_Task_UserID WHERE ID={field_id}')
        cursor.execute(f'SELECT ID,Keyword,Product_ID,Title,UniqueProductID,ImageName,Gtin FROM KeywordData_Task_UserID WHERE ID={field_id}')

        for row in cursor:
            # result = {
            #     'ID': row[0],
            #     'Keyword': row[1],
            #     'Product_ID': row[2],
            #     'TotalResultReturned': row[3],
            #     'CreateDate': str(row[4]),
            #     'Title': row[5],
            #     'Details': str(row[6]),
            #     'Vote_Count': row[7],
            #     'PickedItemNumber': row[8],
            #     'Shopping_url': row[9],
            #     'UserID': row[10],
            #     'IsshoppingurlScrapped': row[11],
            #     'ImageLink': row[12],
            #     'ImageVector': row[13],
            #     'Brand': row[14],
            #     'Partnumbers': row[15],
            #     'Gtin': row[16],
            #     'Base64ImageString': row[17],
            #     'UniqueProductID': row[18],
            #     'ImageName': row[19]
            # }
            result = {
                'ID': row[0],
                'Keyword': row[1],
                'Product_ID': row[2],
                'Title': row[3],
                'UniqueProductID': row[4],
                'ImageName': row[5],
                'Gtin': str(row[6]),
            }
            return result


if __name__ == '__main__':
    class_db = DatabaseProcess(local=False)

    # features = class_db.load_database(field_limit=20)
    # print(len(features))

    ret_db = class_db.find_id(1503)
    print(json.dumps(ret_db, indent=4))
