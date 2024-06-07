import sqlite3
from flask import Flask, render_template, redirect
from werkzeug.exceptions import abort
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('../pythonProject4/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return redirect("/contracts")

# Контракты 

@app.route('/contracts')
def contracts():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM contracts, trainings, clients
    WHERE contracts.training_id = trainings.id_training and contracts.client_id = clients.id_client
    """).fetchall()
    conn.close()
    return render_template('contracts.html', contracts=pos)

def get_contract(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM contracts, trainings, clients
    WHERE contracts.training_id = trainings.id_training and contracts.client_id = clients.id_client and contracts.id_contract = ?
                        """, (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

@app.route('/contract/<int:contract_id>')
def contract(contract_id):
    pos = get_contract(contract_id)
    return render_template('contract.html', contract=pos)

# Квартиры 

@app.route('/trainings')
def training():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM contracts, trainings, clients
    WHERE contracts.training_id = trainings.id_training and contracts.client_id = clients.id_client
    """).fetchall()
    conn.close()
    return render_template('trainings.html', training=pos)

def get_training(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM contracts, trainings, clients
    WHERE contracts.training_id = trainings.id_training and contracts.client_id = clients.id_client and trainings.id_training = ?
                        """, (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

'''@app.route('/training/<int:training_id>')
def training(training_id):
    pos = get_training(training_id)
    return render_template('training.html', training=pos)
'''
#/contract/<int:contract_id>

@app.route('/clients')
def clients():
    abort(404)

@app.route('/reports')
def reports():
    abort(404)

@app.route('/employees')
def employees():
    abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()