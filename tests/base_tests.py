from hook_plug import environment_hooks, register_hooks
from report_portal import ReportPortalPlugin

rp_endpoint = ""
rp_project = ""
rp_token = ""

register_hooks(ReportPortalPlugin())


class FakeContext:
    class config:
        ...
    config = config


context = FakeContext()
context.config.userdata = dict(
    rp_endpoint=rp_endpoint,
    rp_project=rp_project,
    rp_token=rp_token
)

environment_hooks.hook.before_all(context=context)
environment_hooks.hook.after_all(context=context)
