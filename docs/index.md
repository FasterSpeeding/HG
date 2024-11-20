# Getting started

Hikari is a powerful Python library which lets you program bots to do all sorts of things on Discord.

Before using this guide to learn Hikari it's recommended that you make sure you
understand basic concepts and how they work in Python such as
[object-oriented](https://realpython.com/python3-object-oriented-programming/),
[asynchronous](https://realpython.com/async-io-python/) programming, and
[exceptions](https://realpython.com/python-exceptions/). This knowledge is
really important for properly grasping libraries like Hikari.

If that all seems like a bit much for you and you don't really have a firm grasp on
Python yet then I recommend trying a basics course (like
[Real Python](https://realpython.com/learning-paths/python-basics/)) before using
Hikari as libraries like this can be challenging to use without that foundational knowledge.

### Making a bot

So to start off we should work out what type of bot you want to use.

##### Gateway bots

```py
--8<-- "./docs_src/index.py:23:38"
```

Gateway bots are what you'll most likely want. These allow you to listen for actions happening
on Discord by subscribing to [events][]. All a gateway bot needs to work is a bot token, and
an internet connection which can reach Discord and maintain a persistent connection.

The example above shows how you'd initiate and the [standard gateway bot implementation][hikari.impl.gateway_bot.GatewayBot],
it should be noted that the only required argument here is the token (first argument). The
other arguments configure what entities this should cache in-process and the [intents][] which
indicate what events the bot wants to receive, more information on these can be found in [events][].

##### REST server bots

```py
--8<-- "./docs_src/index.py:17:19"
```

While there's a lot less direct configuration to RESTBots than Gateway bot, there's a bit
more to getting it working than with Gateway bot. The RESTBot runs a REST server which
is meant to receive interaction requests from Discord; this limits it to only knowing when
users actively interact with the bot through using components, slash commands, and context
menus but means that before this can work you need to have the network setup to allow
Discord to connect to your bot.

The example above shows how you'd initiate the [standard REST bot implementation][hikari.impl.rest_bot.RESTBot],
it should be noted that the only requirement arguments here are the token (first argument) and the
token type (second argument). Before this this'll work though you'll need to have that pesky
networking setup; this means having a domain name with ssl support which points towards the IP the
RESTBot is behind (Discord won't accept a raw IP address). You should keep the RESTBot behind a
reverse proxy with ssl enabled locally instead of exposing it straight to the public internet to
keep the payloads encrypted in-transit.

![interaction_url](./images/interaction_url.png)

Once you've got the networking setup and the bot running you'll want to enter the bot's web address
here to tell Discord to start sending interaction requests to the bot. You should see a failed ping
request and a successful one in the logs as Discord validates the endpoint (these may be received
either way around).
