from flask import Flask, render_template

application = app = Flask(__name__)

@app.route("/index.html")
def index_page():
    return render_template('index.html')

@app.route("/Job Status.html")
def jobstatus_page():
    return render_template('Job Status.html')

@app.route("/Operations.html")
def operations_page():
    return render_template('Operations.html')

@app.route("/Engineering.html")
def engineering_page():
    return render_template('Engineering.html')

@app.route("/Electronics.html")
def electronics_page():
    return render_template('Electronics.html')

@app.route("/Maintenance.html")
def maintenance_page():
    return render_template('Maintenance.html')

@app.route("/Accounting.html")
def accounting_page():
    return render_template('Accounting.html')

@app.route("/Overdue Parts.html")
def Parts_page():
    return render_template('Overdue Parts.html')

@app.route("/Test.html")
def Test_page():
    return render_template('Test.html')

