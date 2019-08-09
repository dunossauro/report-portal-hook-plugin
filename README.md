behave report portal hook plugin

## installation
```
pip install hp-report-portal
```

## Usage

#### behave.ini file
```
[behave.userdata]
rp_project  = <report portal project>
rp_endpoint = <report portal url>
rp_launch   = <report portal project>
rp_token    = <report portal api token>
```


#### environment.py file

Simple example using only `all` hooks. But should be used on all hooks

```python
from hook_plug import environment_hooks, register_hooks
from report_portal import ReportPortalPlugin

register_hooks(ReportPortalPlugin())

def before_all(context):
    environment_hooks.hook.before_all(context=context)


def after_all(context):
    environment_hooks.hook.after_all(context=context)
```
