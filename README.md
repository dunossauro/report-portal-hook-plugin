behave report portal hook plugin

## instalation
```
pip install git+https://github.com/dunossauro/report-portal-hook-plugin.git
```

## Usage

#### behave.ini file
```
[behave.userdata]
rp_endpoint = <report portal url>
rp_project  = <report portal project>
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
