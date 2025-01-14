from flask import Flask, request
from flask import render_template
import psycopg2

app = Flask("myApi")

class sqlProvider:
    def __init__(self):
        print(1)

    def getCursor(self):
        self.conn = psycopg2.connect(dbname='go-crud', user='postgres', host='localhost', password='RjirfLeyz')
        cur =  self.conn.cursor()
        return cur

    def commit(self):
        self.conn.commit()

provider = sqlProvider()

@app.route('/debts')
def get_debts():
    cur = provider.getCursor()
    cur.execute("SELECT id, name, status FROM debts")
    rows = cur.fetchall()
    return rows

@app.route('/debts', methods=['POST'])
def create_debt():
    id = request.json["id"]
    name = request.json["name"]
    status = request.json["status"]

    cur = provider.getCursor()
    cur.execute("INSERT INTO public.debts (id, name, status) VALUES (%s, %s, %s)", (id, name, status))
    provider.commit()
    return "inserted successfully"

@app.route('/debts/<id>', methods=['DELETE'])
def delete_debt(id):
    cur = provider.getCursor()
    print(id)
    cur.execute("DELETE FROM public.debts WHERE id = " + str(int(id)))
    provider.commit()
    return "delete successfully"

#@app.route('/debts/{id}', methods=['DELETE'])
#def delete_debt(id):
#    return 'success bratik' + id

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return '<body><b>This is the about page</b></body>'

@app.route('/user/<username>')
def show_user_profile(username):
    print(username)
    return f'User {username}'

@app.route('/main/<name>')
def hello(name):
  return render_template('main.html', name=name)

print('hello')

app.run(debug=True, port=4545)