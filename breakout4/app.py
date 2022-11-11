from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import logging
import time
import random
import traceback
from logfmter import Logfmter

formatter = Logfmter(keys=["ts", "level"],mapping={"ts": "asctime", "level": "levelname"})
#formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler_stream = logging.StreamHandler()
handler_stream.setFormatter(formatter)

handler_file = logging.FileHandler(filename='app.log')
handler_file.setFormatter(formatter)

logging.basicConfig(handlers=[handler_stream,handler_file])

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')

users = ['John', 'Matthew', 'Luke', 'Mary', 'Joseph']

start_time = time.time()

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route("/login")
def login():
    time.sleep(delay_interval(1))
    user = random.randint(0, 4)
    logging.info(f"{users[user]} has logged in")
    return f"{users[user]} has logged in"

@app.route("/account")
def account():
    time.sleep(delay_interval(2))
    user = random.randint(0, 4)
    balance = round(random.uniform(10.00,100000.00),2)
    logging.info(f"{users[user]} has account balance of: ${balance}")
    return f"Account balance is: {balance}"

@app.route("/payment")
def payment():
    time.sleep(delay_interval(3))
    random_nbr = random.randint(1, 6)
    try:
        if random_nbr == 6:
            raise Exception("A random error occurred")
        user = random.randint(0, 4)
        payment = round(random.uniform(10.00, 10000.00), 2)
        logging.warning(f"{users[user]} made a payment for: ${payment}")
        return f"{users[user]} made a payment for: ${payment}"
    except Exception as e:
        logging.error(traceback.format_exc())
        return str(e), 500

def delay_interval(sleep_time):
    elapsed_time = time.time() - start_time
    new_delay_interval = (sleep_time / 10) * (elapsed_time % 10)

    logging.debug(f"Delay interval increased to: {new_delay_interval}")
    return new_delay_interval

app.run(host='0.0.0.0', port=8080)
