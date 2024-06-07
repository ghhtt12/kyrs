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
def trainings():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM trainings""").fetchall()
    conn.close()
    return render_template('trainings.html', trainings=pos)

def get_training(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM trainings WHERE id_training = ?""", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

@app.route('/training/<int:training_id>')
def training(training_id):
    pos = get_training(training_id)
    return render_template('training.html', training=pos)


@app.route('/clients')
def clients():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM clients""").fetchall()
    conn.close()
    return render_template('clients.html', clients=pos)

def get_client(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM clients WHERE id_client = ?""", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

@app.route('/client/<int:client_id>')
def client(client_id):
    pos = get_client(client_id)
    return render_template('client.html', client=pos)



@app.route('/reports')
def reports():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM reports""").fetchall()
    conn.close()
    return render_template('reports.html', reports=pos)

def get_report(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM reports WHERE id_report = ?""", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

@app.route('/report/<int:report_id>')
def report(report_id):
    pos = get_report(report_id)
    return render_template('report.html', report=pos)


@app.route('/employees')
def employees():
    conn = get_db_connection()
    pos = conn.execute("""SELECT * FROM employees""").fetchall()
    conn.close()
    return render_template('employees.html', employees=pos)

def get_employee(item_id):
    conn = get_db_connection()
    item = conn.execute("""SELECT * FROM employees WHERE id_employee = ?""", (item_id,)).fetchone()
    conn.close()
    if item is None:
        abort(404)
    return item

@app.route('/employee/<int:employee_id>')
def employee(employee_id):
    pos = get_employee(employee_id)
    return render_template('employee.html', employee=pos)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()