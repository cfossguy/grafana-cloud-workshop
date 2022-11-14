# Grafana Cloud Workshop
This workshop is targeted to site reliability engineers that want to become 
Grafana literate with minimal effort. The breakouts should be completed
in sequence and can be used as handy references once you understand the 
key concepts.

Most SREs are comfortable running go binaries and IaC via Python. You will *NOT* need to edit
python or go code, but you will:

1. Hand edit a YAML configuration file
2. Execute a pre-built python/flask REST API locally
3. Execute pre-built go binaries(k6 and grafana agent)

## System Requirements
1. A valid [Grafana Cloud](https://grafana.com/auth/sign-up/create-user?pg=hp&plcmt=hero-btn1&cta=create-free-account) account
2. Ability to download and run go binaries. You will *NOT* need to compile go code from source.
3. A fully functional [Python 3](https://www.python.org/downloads/) installation with pip package manager.

## Grafana Dashboards
**User Story** - As an SRE, I want to build a new RED dashboard so that the application team has a customized view of 
key application and system metrics. 

**For every resource, monitor:**

1. Rate (the number of requests per second)
2. Errors (the number of those requests that are failing)
3. Duration (the amount of time those requests take)

### Key Concepts
* Panels 
* Queries
* Expressions
* Hot Keys
* Transformations
* Dashboard Settings
* Alerts
* Annotations
* Variables

### Breakouts
1. [Grafana Dashboard](breakout1/README.md): RED dashboard with test data - PART 1
2. [Grafana Dashboard](breakout2/README.md): RED dashboard with test data - PART 2
3. [Grafana Dashboard](todo): TODO

## Grafana Cloud Metrics(Prometheus)
**User Story** - As an SRE, I want to explore infrastructure metrics and response time metrics for a cloud native, 
REST API. I also want to configure metrics recording rules and alerts rules. 

### Key Concepts
* Prometheus node_exporters
* Hosted Prometheus Metrics Collector
* k6 load test for REST API
* PromQL builder in Grafana
* Prometheus recording rules
* Prometheus alerting rules

4. [Prometheus Metrics](breakout4/README.md): REST API with metrics, recording rules, and alert rules - PART 1
5. [Prometheus Metrics](breakout5/README.md): REST API with metrics, recording rules, and alert rules - PART 2

## Grafana Cloud Logs(Loki)
**User Story** - As an SRE, I want to explore application logs for a cloud native, 
REST API. I also want to configure logs -> metrics recording rules and alerts rules. 

6. [Loki Logs](breakout6/README.md): REST API with logs, recording rules, and alert rules - PART 1
7. [Loki Logs](todo): TODO

### Key Concepts
* Hosted Loki Logs Collector
* LogQL builder in Grafana