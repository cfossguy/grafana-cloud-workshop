## Breakout 3: RED dashboard with test data - PART 3
 
### What Good Looks Like
Image Placeholder
 
### Step #1
Create an Alert Rule 
 
1. In the Grafana menu, hover over the Alerting icon to open the Alerting menu, listing alerting options. 
2. Click *New alert rule* at the bottom of the menu. The new alerting rule page opens where the Grafana managed alerts option is selected by default.
3. Add 1 *TestData DB* datasource queries to the panel
4. Select *Scenario -> CSV Metric Values*
5. Set A *String Input* = `659,414,925,1121,970,962,721,796,787,686` and *Alias* = `latency`
6. Click *+ Expression* button and set *Operation* to `Classic Condition` and set *Conditions* to when `Max` of `A` is above `750`
6. Click Run queries to verify that the query is successful.
7. Set the frequency of evaluation to *Evaluate Every* `5m` *for* `1h`.
8. Configure *no data and error handling*.
Set *Alert state if no data or all values are null* -> `No Data`
Set *Alert state if execution error or timeout* -> `Alerting`
8. Click *Preview alerts* to check the result of running the query at this moment. Note:Preview excludes no data and error handling.
9. In *Add details for your alert* name your alert `Alerting` and save it in the folder *Grafana Cloud*. 
10. Set the rule group to `RED`.
10. Click *Save*

---

