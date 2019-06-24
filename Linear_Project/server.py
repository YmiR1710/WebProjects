from data import get_info, database_insert, update, update_all
from analysis import analyze, analyze_all
from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
import datetime

update_date = [11]
app = Flask(__name__)
new_table = [0, []]

# my_db = mysql.connector.connect(
#     host="yaroslavboiko.mysql.pythonanywhere-services.com",
#     user="yaroslavboiko",
#     passwd="wital1999",
#     database="yaroslavboiko$twitter"
# )
@app.route("/", methods=['GET', 'POST'])
def main_func():
    try:
        if datetime.datetime.now().day != update_date[-1]:
            update_date.append(datetime.datetime.now().day)
            update_all()
    except IndexError:
        update_date.append(datetime.datetime.now().day)
        update_all()
    finish = False
    name = request.form.get("table", False)
    if name not in new_table and name:
        new_table[0] = name
    user = request.form.get("user", False)
    if user not in new_table and user:
        new_table[1].append(user)
    if not user:
        finish = True
    if not new_table[0] or len(new_table[1]) < 1:
        finish = False
    if finish:
        database_insert(new_table[0], get_info(new_table[1], len(new_table[1])))
        for u in reversed(range(len(new_table[1]) - 1)):
            update(new_table[0], u)
        new_table.pop(0)
        new_table.pop(0)
        new_table.append(0)
        new_table.append([])
    data_dict = analyze_all()
    return render_template("index.html", data=data_dict, id=1)


if __name__ == "__main__":
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
