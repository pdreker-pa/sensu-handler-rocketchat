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

import os
from distutils.core import setup

long_description = 'Notification handler to deliver events to rocketchat from sensu written in python'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name='sensu-handler-rocketchat',
    version='0.1.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat',
        'Topic :: System :: Monitoring'
    ],
    author='Patrick Dreker',
    author_email='patrick@dreker.de',
    packages=['sensu_handler_rocketchat'],
    scripts=[],
    url='https://github.com/pdreker/sensu-handler-rocketchat',
    license='LICENSE',
    description='A sensu plugin to send events to rocketchat.',
    long_description=long_description,
    install_requires=[
        'argparse',
        'requests',
        'sensu_plugin'
    ],
    entry_points = { 'console_scripts': ['sensu_handler_rocketchat=sensu_handler_rocketchat.__main__:main']},
)
