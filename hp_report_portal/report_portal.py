"""reportportal.io plugin to hook_plug."""
from time import time
from traceback import print_exc, format_tb
from hook_plug import tag_behavior
from reportportal_client import ReportPortalServiceAsync


class ReportPortalPlugin:
    """reportportal.io plugin to hook_plug.

    behave propertys:behave.readthedocs.io/en/latest/context_attributes.html
    """
    @staticmethod
    def error(exc_info):
        print_exc(*exc_info)

    @staticmethod
    def step_table(step):
        if step.table:
            rows = '|\n|'.join(['|'.join(row) for row in step.table.rows])
            return '|{}|'.format(rows)
        return None

    @staticmethod
    def step_text(step):
        if hasattr(step, 'text'):
            return step.text
        return None

    @staticmethod
    def timestamp():
        return str(int(time() * 1000))

    @staticmethod
    def check_context(context):
        if not hasattr(context, 'config'):
            raise EnvironmentError(
                'Please, check if context is a behave context'
            )
        try:
            context.config.userdata['rp_project']
            context.config.userdata['rp_endpoint']
            context.config.userdata['rp_launch']
            context.config.userdata['rp_token']
        except KeyError:
            raise EnvironmentError(
                'Please, check yout behave.ini file'
            )
        return True

    @tag_behavior
    def before_all(self, context):
        """
        TODO: get data from behave.userdata

            endpoint: archteture/SO/Browser
            token: user report portal api token
            project: project name or label
        """
        self._rp = ReportPortalServiceAsync(
            endpoint=context.config.userdata.get('rp_endpoint', None),
            project=context.config.userdata.get('rp_project', None),
            token=context.config.userdata.get('rp_token', None),
            error_handler=self.error,
        )
        self._rp.start_launch(
            name=context.config.userdata.get('rp_launch', None),
            start_time=self.timestamp(),
        )

    @tag_behavior
    def before_feature(self, context, feature):
        self._rp.start_test_item(
            name=feature.name,
            start_time=self.timestamp(),
            description=' '.join(feature.description),
            tags=feature.tags,
            item_type='STORY'
        )

    @tag_behavior
    def before_scenario(self, context, scenario):
        self._rp.start_test_item(
            name=scenario.name,
            start_time=self.timestamp(),
            description=' '.join(scenario.description),
            tags=scenario.tags,
            item_type='Scenario'
        )

    @tag_behavior
    def before_step(self, context, step):
        """NOTE: step doesn't has tag"""
        self._rp.start_test_item(
            name=step.name,
            start_time=self.timestamp(),
            description=self.step_table(step) or self.step_text(step),
            tags=None,
            item_type='step'
        )

    @tag_behavior
    def after_all(self, context):
        self._rp.finish_launch(end_time=self.timestamp())
        self._rp.terminate()

    @tag_behavior
    def after_feature(self, context, feature):
        self._rp.finish_test_item(
            end_time=self.timestamp(),
            status=feature.status.name,
        )

    @tag_behavior
    def after_scenario(self, context, scenario):
        self._rp.finish_test_item(
            end_time=self.timestamp(),
            status=scenario.status.name,
        )

    @tag_behavior
    def after_step(self, context, step):
        if step.status.name == 'failed':
            self._rp.log(
                time=self.timestamp(),
                message=''.join(format_tb(step.exc_traceback)),
                level='ERROR',
            )
        self._rp.finish_test_item(
            end_time=self.timestamp(),
            status=step.status.name,
        )
