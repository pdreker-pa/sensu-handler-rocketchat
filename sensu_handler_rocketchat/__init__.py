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
        super(RocketHandler, self).__init__()

    def handle(self):
        message_payload = {}
        if "channel" in self.settings[self.config_space]:
            message_payload["channel"] = self.settings[self.config_space]["channel"]

        if "nickname" in self.settings[self.config_space]:
            message_payload["username"] = self.settings[self.config_space]["nickname"]

        message_payload["attachments"] = []
        att = {}
        att["title"] = "%s (%s): %s" % (self.translate_status(self.event["check"]["status"]),
                                        self.event["check"]["name"],
                                        self.event["client"]["name"])
        if "dashboard_url" in self.settings[self.config_space]:
            att["title_link"] = self.settings[self.config_space]["dashboard_url"]

        if "pretext" in self.settings[self.config_space]:
            att["pretext"] = self.settings[self.config_space]["pretext"]

        att["color"] = self.status_to_color(self.event["check"]["status"])

        att["ts"] = self.event["timestamp"]
        att_fields = []

        if "thresholds" in self.event["check"]:
            for key,value in self.event["check"]["thresholds"].iteritems():
                att_fields.append({"title": key, "value": str(value), "short": True})
            att["fields"] = att_fields

        att["text"] = self.event["check"]["output"]

        message_payload["attachments"].append(att)

        req = urllib2.Request(self.settings[self.config_space]["hook_url"])
        req.add_header('Content-Type', 'application/json')
        payload = json.dumps(message_payload)

        response = urllib2.urlopen(req, payload)
        if response.getcode() is not 200:
        	print "Posting to Rocketchat failed!"

    def translate_status(self, status):
        return ["OK", "WARNING", "CRITICAL", "UNKNOWN"][status]

    def status_to_color(self, status):
        return ["#36a64f", "#FFCC00", "#FF0000", "#6600CC"][status]

if __name__ == "__main__":
  f = RocketHandler()
