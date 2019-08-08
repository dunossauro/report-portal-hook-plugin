from setuptools import setup

setup(
    name='report-portal-hook-plugin',
    version='0.0.2',
    description='behave report portal hook plugin',
    url='https://github.com/dunossauro/report-portal-hook-plugin',
    author='Eduardo Mendes',
    author_email='mendesxeduardo@gmail.com',
    license='MIT',
    packages=['report_portal'],
    keywords=['testing', 'reporting', 'reportportal', 'hook_plug', 'behave'],
    install_requires=[
        'reportportal-client',
        'hook_plug @ https://github.com/dunossauro/hook_plug/tarball/master#egg=hook_plug'
    ],
    dependency_links=[
        'https://github.com/dunossauro/hook_plug/tarball/master#egg=hook_plug'
    ],
    zip_safe=False,
)
