import mysql.connector
from matrix import Matrix


def analyze(table_name):
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="wital1999",
        database="twitter"
    )
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM " + table_name + " ORDER BY id;")
    my_result = my_cursor.fetchall()
    b = []
    max_sum = []
    coefficients = []
    for day in my_result:
        day_coefficients = []
        day_res = 0
        for thing in day:
            if type(thing) is float:
                day_coefficients.append(thing)
                day_res += thing
        coefficients.append(day_coefficients)
        max_sum.append(sum(day_coefficients))
    m = Matrix()
    for i in range(len(coefficients)):
        b.append(max(max_sum)*2)
    result = m.gauss_solve(coefficients, b)
    return result


def analyze_all():
    def coef_to_name(coef_index):
        if coef_index == 0:
            return 1
        else:
            return (coef_index * 2) + 1
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="wital1999",
        database="twitter"
    )
    list_of_analized = []
    my_cursor = my_db.cursor()
    my_cursor.execute("SHOW TABLES;")
    my_result = my_cursor.fetchall()
    for i in my_result:
        my_cursor.execute("SELECT * FROM {}".format(i[0]))
        res = my_cursor.fetchall()
        if not res:
            my_cursor.execute("DROP TABLE {}".format(i[0]))
    for i in my_result:
        try:
            analized_table = []
            my_cursor.execute("SELECT * FROM {}".format(i[0]))
            res = my_cursor.fetchall()
            columns = int((len(res[0]) - 1) / 2)
            rows = len(res)
            if rows == columns:
                coeficients = analyze(i[0])
                for k in range(len(coeficients)):
                    analized_table.append([res[0][coef_to_name(k)], coeficients[k]])
            list_of_analized.append(analized_table)
        except:
            pass
    for i in list_of_analized:
        i.sort(key=lambda row: row[1])
    for i in list_of_analized:
        for j in i:
            j.pop(1)
    for i in range(len(list_of_analized)):
        for j in range(len(list_of_analized[i])):
            list_of_analized[i][j] = str(list_of_analized[i][j])[2:len(str(j))-3]
    dict_of_analzed = dict()
    for i in range(len(my_result)):
        try:
            dict_of_analzed[my_result[i][0]] = list_of_analized[i]
        except:
            pass
    return dict_of_analzed
