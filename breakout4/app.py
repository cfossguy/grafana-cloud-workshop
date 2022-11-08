from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route("/account")
def account():
    return 'ACCOUNT!'

@app.route("/payment")
def payment():
    return 'PAYMENT!'

@app.route("/login")
def login():
    return 'LOGIN!'

app.run(host='0.0.0.0', port=8080)