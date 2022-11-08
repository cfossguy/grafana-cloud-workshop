## Breakout 4: Prometheus Metrics

### What Good Looks Like
TODO

### Step #1
Start local instance of python API. This step requires a working python v3
local installation.

1. Open a terminal window
2. Create a file named `app.py` with executable permissions
3. Paste the contents of [app.py](./app.py) into your file
4. Install python API dependencies via this command `pip install Flask prometheus_flask_exporter`  
5. Start the API by running `python app.py`
6. Open a browser window to test the endpoint [http://localhost:8080]/payment](http://localhost:8080]/payment)
7. Open a browser window to test the prometheus metrics endpoint [http://localhost:8080]/metrics](http://localhost:8080]/metrics)

---
![alt text](python_api1.png) 

---
![alt text](python_api2.png) 

### Step #2 
Install and Setup a k6 OSS load test for the python API.

TODO

1. Download k6 client binary

### Step #3

Setup Hosted Prometheus Metrics Collector

TODO

```
metrics:
  global:
    [REMOTE_WRITE_CONFIG_COPY_PASTE]
    scrape_interval: 60s
    external_labels:
      app: python_app
  configs:
  - name: hosted-prometheus
    scrape_configs:
      - job_name: node
        static_configs:
        - targets: ['localhost:8080']
integrations:
  node_exporter:
    enabled: true
  agent:
    enabled: true
```

#### Useful References 
TODO