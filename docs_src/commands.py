# -*- coding: utf-8 -*-
# Tanjun Examples - A collection of examples for Tanjun.
# Written in 2023 by Lucina Lucina@lmbyrne.dev
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.
import hikari
import tanchan
import tanjun


def slash_command_example():
    @tanchan.doc_parse.with_annotated_args
    @tanchan.doc_parse.as_slash_command(
        default_to_ephemeral=True,
        dm_enabled=False,
        default_member_permissions=hikari.Permissions.BAN_MEMBERS,
    )
    async def ban_user(
        ctx: tanjun.abc.SlashContext,
        user: tanjun.annotations.User,
        reason: tanjun.annotations.Str | hikari.UndefinedType = hikari.UNDEFINED,
    ) -> None:
        """Ban a user.

        Parameters
        ----------
        user
            The user to ban.
        reason
            Why they're being banned.
        """
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
    slash_command_group = tanjun.slash_command_group("group", "description")

    @slash_command_group.as_sub_command("name", "description")
    async def sub_command(ctx: tanjun.abc.SlashContext) -> None:
        await ctx.respond("Called `group name` command")


def prefix_command_example():
    @tanjun.as_message_command("name")
    async def message_command(ctx: tanjun.abc.MessageContext) -> None:
        ...


def prefix_command_group_example():
    @tanjun.as_message_command_group("name")
    async def message_command_group(ctx: tanjun.abc.MessageContext) -> None:
        ...


def user_menu_example():
    @tanjun.as_user_menu("name")
    async def user_menu(
        ctx: tanjun.abc.MenuContext, user: hikari.InteractionMember
    ) -> None:
        ...


def context_menu_example():
    @tanjun.as_message_menu("name")
    async def message_menu(
        ctx: tanjun.abc.MenuContext, message: hikari.Message
    ) -> None:
        ...


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
