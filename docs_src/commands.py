# -*- coding: utf-8 -*-
# Tanjun Examples - A collection of examples for a Hikari guide.
# Written in 2023 by Faster SpeedingLucina@lmbyrne.dev
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.
import typing

import hikari
import tanchan
import tanjun
from tanjun import annotations


def slash_command_example():
    @tanchan.doc_parse.with_annotated_args
    @tanchan.doc_parse.as_slash_command(
        default_to_ephemeral=True,
        dm_enabled=False,
        default_member_permissions=hikari.Permissions.BAN_MEMBERS,
    )
    async def ban_user(
        ctx: tanjun.abc.SlashContext,
        user: annotations.User,
        reason: annotations.Str | hikari.UndefinedType = hikari.UNDEFINED,
    ) -> None:
        """Ban a user.

        Parameters
        ----------
        user
            The user to ban.
        reason
            Why they're being banned.
        """
        # guild_id should never be None thanks to dm_enabled=False
        assert ctx.guild_id is not None

        try:
            await ctx.rest.ban_member(ctx.guild_id, user, reason=reason)

        except hikari.NotFoundError:
            await ctx.respond("User doesn't exist!!!")

        except hikari.ForbiddenError:
            await ctx.respond("I Cannot do that!!!")

        else:
            await ctx.respond(f"Successfully banned {user}")


def slash_command_group_example():
    slash_command_group = tanchan.doc_parse.slash_command_group(
        "group", "description"
    )

    @slash_command_group.as_sub_command()
    async def name(ctx: tanjun.abc.SlashContext) -> None:
        """`group name` command."""
        await ctx.respond("Called `group name` command")


def message_command_example():
    @tanjun.annotations.with_annotated_args
    @tanjun.as_message_command("meow")
    async def message_command(
        ctx: tanjun.abc.MessageContext, weebish: tanjun.annotations.Bool = False
    ) -> None:
        ...


def message_command_group_example():
    @tanjun.as_message_command_group("uwu group")
    async def message_command_group(ctx: tanjun.abc.MessageContext) -> None:
        ...

    @tanjun.annotations.with_annotated_args
    @message_command_group.as_sub_command("echo")
    async def sub_command(
        ctx: tanjun.abc.MessageContext,
        content: typing.Annotated[annotations.Str, annotations.Greedy()],
    ) -> None:
        ...


def user_menu_example():
    @tanjun.as_user_menu("Yeet user")
    async def user_menu(
        ctx: tanjun.abc.MenuContext, user: hikari.InteractionMember
    ) -> None:
        # ... Yetting logic
        await ctx.respond(f"{user} got yeeted!", delete_after=30)


def message_menu_example():
    @tanjun.as_message_menu("Archive", dm_enabled=False)
    async def message_menu(
        ctx: tanjun.abc.MenuContext, message: hikari.Message
    ) -> None:
        # ... Archive logic
        try:
            await ctx.rest.delete_message(ctx.channel_id, message)

        except hikari.NotFoundError:
            pass

        except hikari.ForbiddenError:
            await ctx.respond("Couldn't delete message", delete_after=30)
            return

        await ctx.respond("Archived message", delete_after=30)


def muti_command_example():
    @tanchan.doc_parse.with_annotated_args(follow_wrapped=True)
    @tanchan.doc_parse.as_slash_command()
    @tanjun.as_message_command("meow command")
    @tanjun.as_user_menu("meow command")
    async def command(ctx: tanjun.abc.Context, user: annotations.User) -> None:
        """Do a thing to a user.

        Parameters
        ----------
        user
            The user to do the thing to.
        """
        # ... Thing logic
        await ctx.respond(f"Thing done to {user}")


def load_from_scope():
    @tanjun.as_slash_command("name", "description")
    async def slash_command(ctx: tanjun.abc.SlashContext) -> None:
        ...

    component = tanjun.Component().load_from_scope()


def load_with_command():
    component = tanjun.Component()

    @component.with_command(follow_wrapped=True)
    @tanjun.as_slash_command("name", "description")
    @tanjun.as_message_command("name")
    async def command(ctx: tanjun.abc.Context) -> None:
        ...

    @tanjun.as_slash_command("name", "description")
    async def other_command(ctx: tanjun.abc.Context) -> None:
        ...

    component.add_command(other_command)


def make_loader():
    component = tanjun.Component()

    # ...

    loaders = component.make_loader()


def tanjun_client():
    bot = hikari.GatewayBot("Token")
    (
        tanjun.Client.from_gateway_bot(bot, declare_global_commands=True)
        .load_directory("./components", namespace="bot.components")
        .load_modules("bot.admin")
    )

    bot.run()


def hot_reloader():
    bot = hikari.GatewayBot("Token")
    client = tanjun.Client.from_gateway_bot(bot)

    (
        tanjun.dependencies.HotReloader()
        .add_directory("./components", namespace="bot.components")
        .add_modules("bot.admin")
        .add_to_client(client)
    )

    bot.run()
