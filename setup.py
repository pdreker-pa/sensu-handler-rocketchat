from distutils.core import setup

setup(
    name='sensu-plugin-rocketchat-handler',
    version='0.0.1',
    author='Patrick Dreker',
    author_email='patrick.dreker@proact.de',
    packages=['sensu_plugin_rocketchat_handler', 'sensu_plugin_rocketchat_handler.test'],
    scripts=[],
    url='http://www.proact.de',
    license='LICENSE.txt',
    description='A sensu plugin to send events to rocketchat.',
    long_description="""
    """,
    install_requires=[
        'argparse',
        'requests'
    ],
    tests_require=[
        'pep8',
        'pylint'
    ],
)
