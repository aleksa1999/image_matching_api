import pymssql
import ast


class DatabaseProcess:
    def __init__(self, local=True, field_limit=0):
        self.features = self.load_database(local, field_limit)

    @staticmethod
    def load_database(local=True, field_limit=0):
        print("Loading database ...")
        if local:
            conn = pymssql.connect(host='NS3013855\SQLSERVER_2016',
                                   user='sa',
                                   password='?ZE?[cUh{Br%58V[',
                                   database='Sample_NearestNeighbour')
        else:
            conn = pymssql.connect(host='145.239.254.185\SQLSERVER_2016',
                                   user='nikita',
                                   password='nikita',
                                   database='Sample_NearestNeighbour')

        cursor = conn.cursor()
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
                print(e)

        return feature_dict


if __name__ == '__main__':
    # class_db = DatabaseProcess(local=False, field_limit=20)
    class_db = DatabaseProcess(local=True)
    print(class_db.features)
