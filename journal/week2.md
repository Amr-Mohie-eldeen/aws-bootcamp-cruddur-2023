# Week 2 — Distributed Tracing

Learnt the concept of tracing for webapps and tried diffrent solutions to achieve this in Crudder.

## Honeycomb

- Configured honeycomb with open telementary to generate traces for the backend requests.

<img src='_assets/Honeycombio.png' width='700'>

---

## AWS X-ray
Configured tracing using AWS X-ray and created a segment for the notifications_activities endpoint

#### Service Maps

<img src='_assets/Week2_Service_map.png' width='700'>

#### Traces

<img src='_assets/Week2_xray_traces.png' width='700'>

---
## Rollbar
Configured Rollbar and tested conectivity using the test endpoint
<img src='_assets/Week2_rollbar.png' width='700'>
---

## Cloudwatch logs
Configure logger to stream logs to CW.

<img src='_assets/Week2_cwlogs.png' width='700'>

```
I have disabled Xray & Cloudwatch logs for spend control
```
