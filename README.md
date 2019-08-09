# hook plug plugin to report portal.

hp_report_portal is a [hook_plug](https://github.com/dunossauro/hook_plug) plugin based to report [Behave](https://github.com/behave/behave) executions on [Report Portal](reportportal.io).

## installation
```
pip install hp-report-portal
```

## Usage

To use this plugin you need to create the variables in the behave configuration file. You can also pass the parameters using the `-D` flag.

#### behave.ini file
```
[behave.userdata]
rp_project  = <report portal project>
rp_endpoint = <report portal url>
rp_launch   = <report portal laucher>
rp_token    = <report portal api token>
```

> An important thing to say is that not necessarily behave will use `behave.ini`, in some cases it may be in `tox.ini`

#### environment.py file

Simple example using only `all` hooks. But should be used on all hooks

```python
from hook_plug import environment_hooks, register_hooks
from hp_report_portal import ReportPortalPlugin

register_hooks(ReportPortalPlugin())

def before_all(context):
    environment_hooks.hook.before_all(context=context)


def after_all(context):
    environment_hooks.hook.after_all(context=context)
```
