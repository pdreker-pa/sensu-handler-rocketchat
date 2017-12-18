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

from sensu_plugin import SensuHandler
import pprint
import urllib2, json, os, sys, argparse

class RocketHandler(SensuHandler):
    def __init__(self):
        super(RocketHandler, self).__init__()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-c',
            '--config',
            required = False,
            default = "rockethandler",
            help = 'config section to use'
        )
        (self.options, self.remain) = self.parser.parse_known_args()

        self.config_space = vars(self.options)["config"]



    def handle(self):
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.settings)
        # print vars(self.options)
        # pp.pprint(self.remain)
        # sys.exit(0)


        message_payload = {}
        message_payload["channel"] = self.settings[self.config_space]["channel"]
        message_payload["username"] = self.settings[self.config_space]["nickname"]

        message_payload["attachment"] = {}
        message_payload["attachment"]["title"] = "%s (%s): %s" % (self.translate_status(self.event["check"]["status"]),
                                                                  self.event["check"]["name"],
                                                                  self.event["client"]["name"])
        message_payload["attachment"]["title_link"] = self.settings[self.config_space]["dashboard_url"]

        message_payload["attachment"]["pretext"] = self.settings[self.config_space]["pretext"]
        message_payload["attachment"]["color"] = self.status_to_color(self.event["check"]["status"])

        message_payload["attachment"]["ts"] = self.event["timestamp"]
        message_payload["attachment"]["fields"] = []

        for key,value in self.event["check"]["thresholds"].iteritems():
            message_payload["attachment"]["fields"].append({"title": key, "value": str(value), "short": True})

        message_payload["attachment"]["text"] = "%s\n%s" % (self.event["check"]["output"], thresholds)
        payload = json.dumps(mesage_payload)
        print payload
        sys.exit(0)

        req = urllib2.Request(self.settings[config_space]["hook_url"])
        req.add_header('Content-Type', 'application/json')
        payload = json.dumps(mesage_payload)

        response = urllib2.urlopen(req, payload)
        if response.getcode() is not 200:
        	print "Posting to Rocketchat failed!"


    def post_message(self, title, text, color):
        data['attachments'] = []
        attachment = {}
        attachment["title"] = title
        attachment["title_link"] = DASHBOARD_URL
        attachment["text"] = text
        attachment["color"] = color
        data['attachments'].append(attachment)



    def translate_status(self, status):
        return ["OK", "WARNING", "CRITICAL", "UNKNOWN"][status]

    def status_to_color(self, status):
        return ["#36a64f", "#FFCC00", "#FF0000", "#6600CC"][status]

if __name__ == "__main__":
  f = RocketHandler()
