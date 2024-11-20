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
from yuyo import components


class LinkColumn(components.ActionColumnExecutor):
    @components.as_interactive_button(hikari.ButtonStyle.DANGER)
    async def on_button(self, ctx: components.Context) -> None:
        await ctx.respond("Button pressed")

    link_button = components.link_button("https://example.com/yee")


class SelectColumn(components.ActionColumnExecutor):
    @components.as_channel_menu
    async def on_channel_menu(self, ctx: components.Context) -> None:
        await ctx.respond(f"Selected {len(ctx.selected_channels)} channels")

    @components.with_option("borf", "dog")
    @components.with_option("meow", "cat")
    @components.with_option("label", "value")
    @components.as_text_menu(min_values=0, max_values=3)
    async def on_text_menu(self, ctx: components.Context) -> None:
        await ctx.respond("Animals: " + ", ".join(ctx.selected_texts))

    @components.as_role_menu
    async def on_role_menu(self, ctx: components.Context) -> None:
        roles = ", ".join(role.name for role in ctx.selected_roles.values())
        await ctx.respond(f"Selected roles: {roles}")

    @components.as_user_menu
    async def on_user_menu(self, ctx: components.Context) -> None:
        users = ", ".join(map(str, ctx.selected_users.values()))
        await ctx.respond(f"Selected users: {users}")

    @components.as_mentionable_menu
    async def on_mentionable_menu(self, ctx: components.Context) -> None:
        role_count = len(ctx.selected_roles)
        user_count = len(ctx.selected_users)
        await ctx.respond(f"Selected {user_count} users and {role_count} roles")


async def command(
    ctx: tanjun.abc.Context, client: alluka.Injected[components.Client]
) -> None:
    component = SelectColumn()
    message = await ctx.respond(
        "hello!", components=component.rows, ensure_result=True
    )
    client.register_executor(component, message=message)
