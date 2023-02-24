# Welcome

Hikari is a powerful Python library which lets you program bots to do all sorts of things on Discord.

Before using this guide to learn Hikari it's recommended that you make sure you
understand basic concepts and how they work in Python such as
[object-oriented](https://realpython.com/python3-object-oriented-programming/), and
[asynchronous](https://realpython.com/async-io-python/) programming. This knowledge is
really important for properly grasping libraries like Hikari.

If that all seems like a bit much for you and you don't really have a firm grasp on
Python yet then I recommend trying a basics course (like
[Real Python](https://realpython.com/learning-paths/python-basics/)) before using
Hikari as libraries like this can be challenging to use without that foundational knowledge.

First things we should work out what type of bot you want to create.

```py
bot = hikari.GatewayBot(bot_token)
```

Gateway bots are what you'll most likely want. These allow you to listen for generic
actions happening on Discord by listening for [events][]. All a gateway bot requires
to work is an internet connection which can reach Discord.

It comes with an in-memory [cache][]
intents
cache config
rest config

[hikari.GatewayBot][hikari.impl.bot.GatewayBot]


```py
bot = hikari.RESTBot(bot_token)
```

There's a bit more to the REST bot then may first meets the eye.

ports, needing to put it behind a reverse proxy with https which is best done in a contanorised setup with isolated n etworks

[hikari.RESTBot][hikari.impl.rest_bot.RESTBot]
