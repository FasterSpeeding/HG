# -*- coding: utf-8 -*-
# Tanjun Examples - A collection of examples for a Hikari guide.
# Written in 2023 by Faster Speeding Lucina@lmbyrne.dev
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.

import alluka
import hikari
import tanjun
from yuyo import modals


class Modal(modals.Modal):
    async def callback(
        ctx: modals.ModalContext,
        name: str = modals.text_input(
            "name", placeholder="What is their name?", max_length=20
        ),
        reason: str = modals.text_input(
            "reason",
            default="Still likes harry potter.",
            style=hikari.TextInputStyle.PARAGRAPH,
        ),
    ) -> None:
        await ctx.respond(f"{name} is sussy because they {reason}")


async def command(
    ctx: tanjun.abc.AppCommandContext, client: alluka.Injected[modals.Client]
) -> None:
    modal = Modal()
    custom_id = str(ctx.interaction.id)
    client.register_modal(custom_id, modal)
    await ctx.create_modal_response(
        "Who's sussy?", custom_id, components=modal.rows
    )
