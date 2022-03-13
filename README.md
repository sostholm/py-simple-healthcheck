## Description

The py-simple-healthcheck module is designed to be a simple way to do simple python loop healthchecks.
By calling health_check(timeout=<normal_loop_time>) at the end of a python loop hosted in a docker it's possible to
detect if the application is no longer able to update the timestamp in the health check and using a docker healthcheck
subsequently restart the container.


## Usage

```python
from py_simple_healthcheck import health_check 

timeout = 20 #seconds

while True:
    do_stuff()
    health_check(timeout=timeout)
```

```docker
...
healthcheck:
  test: ["CMD", "python", "-c", "'import py_simple_healthcheck; py_simple_healthcheck.is_healthy();' || exit 1"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 40s

```