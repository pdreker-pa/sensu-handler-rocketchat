# Copyright 2017 Patrick Dreker <patrick@dreker.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
