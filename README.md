# sensu-handler-rocketchat

This is a notification handler for Sensu written in Python. It should also work
with Slack and any other Chat service which uses Slack compatible WebHooks.

## Why this and not sensu-plugins-slack?
-------------------------------------
Because it was easier to rewrite this in Python than to figure out how to quote
and escape JSON in ERB in a JSON config file ;-). The orignal sensu plugin
identifies monitored hosts by their IP address, which is not helpful, when using
cloud setups, where IPs may repeat.

# Usage

Create a handler config for sensu:
```json
{
  "handlers": {
    "rockethandler": {
      "type": "pipe",
      "filters": [ "state_change_only" ],
      "command": "sensu-handler-rocketchat"
    }
  }
}
```

Refer to the [sensu documentation](https://sensuapp.org/docs/1.2/reference/handlers.html) for more info on how to write this.

Then create the config for this specific handler. The default config section is
"rockethandler", but this can be overridden on the commandline, to enable
handling multiple channels or Rocketchat servers.

```json
{
  "rockethandler": {
    "hook_url": "https://rocketchat.example.com/hooks/iPw6s7Ykseuhf88kkhf8s4fn0392cnfh83mcfnbsWCzxHTSK",
    "nickname": "sensu",
    "channel": "openstack-events",
    "dashboard_url": "http://10.43.8.4:3000",
    "pretext": ""
  }
}
```

## Parameters
* **hook_url**: (required) Full URL to the WebHook (incoming integration) you want to use.
* **nickname**: (optional) Nickname to use by the handler. Defaults to "RocketChat defined".
* **channel**: (optional) Channel name to deliver notification to. Defaults to "RocketChat defined".
* **dashboard_url**: (optional) URL to uchiwa or sensu dashboard (root URL). This is used to create a link in the title of every notification
* **pretext**: (optional) Text to prepend to each notification. Can be used e.g. for highlights.
