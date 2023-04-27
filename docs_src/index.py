# -*- coding: utf-8 -*-
# Tanjun Examples - A collection of examples for a Hikari guide.
# Written in 2023 by Faster Lucina@lmbyrne.dev
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.
import os

import hikari


def make_rest_bot():
    bot = hikari.RESTBot(os.environ["TOKEN"].strip(), "Bot")

    bot.run(path="192.168.1.102", port=8000)


def make_gateway_bot():
    cache_components = (
        hikari.api.CacheComponents.GUILD_CHANNELS
        | hikari.api.CacheComponents.ROLES
        | hikari.api.CacheComponents.GUILDS
        | hikari.api.CacheComponents.MEMBERS
    )
    bot = hikari.GatewayBot(
        os.environ["TOKEN"].strip(),
        cache_settings=hikari.impl.CacheSettings(components=cache_components),
        intents=hikari.Intents.ALL_UNPRIVILEGED,
    )

    activity = hikari.Activity(
        name="Hello world!", type=hikari.ActivityType.LISTENING
    )
    bot.run(activity=activity)
