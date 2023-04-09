# -*- coding: utf-8 -*-
# Tanjun Examples - A collection of examples for a Hikari guide.
# Written in 2023 by Lucina Lucina@lmbyrne.dev
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.
# pyright: reportUnknownMemberType=none
# pyright: reportUnknownVariableType=none
import os

import agraffe  # type: ignore  # TODO: add py.typed to agraffe
import fastapi
import tanjun
import yuyo


def fastapi_mount():
    bot = yuyo.AsgiBot(os.environ["TOKEN"].strip(), asgi_managed=False)
    tanjun.Client.from_rest_bot(bot, bot_managed=True)

    # ... Other bot setup.

    app = fastapi.FastAPI(on_startup=[bot.start], on_shutdown=[bot.close])

    app.mount("/bot", bot)


def serverless():
    bot = yuyo.AsgiBot(os.environ["TOKEN"].strip(), "Bot")

    # ... Setup bot

    entry_point = agraffe.Agraffe(bot)
