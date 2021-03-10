import pymssql
import ast


def save_text(filename, text):
    file1 = open(filename, 'w')
    file1.write(text)
    file1.close()


def load_database():
    conn = pymssql.connect(
        host='145.239.254.185\SQLSERVER_2016',
        user='nikita',
        password='nikita',
        database='Sample_NearestNeighbour')

    cursor = conn.cursor()
    cursor.execute('SELECT ID, Vector FROM Datafeed_100K')

    store_size = 10
    index = 0
    data_list = ''
    for row in cursor:
        try:
            field_id = row[0]
            field_feature = ast.literal_eval(row[1])
            feature_str = field_feature['result']['feature']
            feature = ast.literal_eval(feature_str)
            data = f'{field_id},{feature_str}'
            data_list += data + '\n'
            index += 1
            if index % store_size == 0:
                save_text(f'db/{str(int(index/store_size))}.txt', data_list)
                data_list = ''

            print(field_id)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    load_database()
