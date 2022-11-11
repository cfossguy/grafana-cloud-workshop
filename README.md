# Grafana Cloud Workshop
You must have a valid Grafana Cloud account to complete this 
workshop as designed. You can obtain a free forever account 
[here](https://grafana.com/auth/sign-up/create-user?pg=hp&plcmt=hero-btn1&cta=create-free-account) 

This workshop is targeted to site reliability engineers that want to become 
Grafana literate with minimal effort. The breakouts should be completed
in sequence and can be used as handy references once you understand the 
key concepts.

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
TODO

6. [Loki Logs](todo): TODO
7. [Loki Logs](todo): TODO