import logging

# Set the logging level to DEBUG/INFO to see all the connection attempts and errors
logging.basicConfig(level=logging.INFO)

import niobot

from nio.crypto.device import OlmDevice

import config as cfg

# Initialize the bot
bot = niobot.NioBot(
    homeserver=cfg.homeserver,
    user_id=cfg.bot_user_id,
    device_id=cfg.device_id,
    owner_id=cfg.owner_id,
    store_path=cfg.store_path,
    auto_join_rooms=cfg.auto_join_rooms,
    auto_read_messages=cfg.auto_read_messages,
    command_prefix="!",
    case_insensitive=True,
)

# responds to ping without exclamation mark
@bot.on_event("message")
async def on_message(room: niobot.MatrixRoom, event: niobot.RoomMessage):
    if event.sender == bot.user_id:
        return

    if bot.is_old(event):
        return

    if not isinstance(event, niobot.RoomMessageText):
        return

    if event.body == "ping":
        await bot.send_message(
            room=room,
            content="pong",
            reply_to=event
        )

@bot.command(name="ping")
async def ping_command(ctx: niobot.Context):
    """replies with 'pong'"""
    await ctx.respond("pong")

@bot.command(name="latency")
async def latency_command(ctx: niobot.Context):
    """replies with the event's latency in ms"""
    await ctx.respond(f"latency: {ctx.latency:.2f} ms")

@bot.command(name="info")
async def info_command(ctx: niobot.Context):
    """info about the bot"""
    await ctx.respond(
        "Matrix pinger bot: https://github.com/okurka12/matrix-pinger"
    )

@bot.command(name="echo")
async def echo_command(ctx: niobot.Context, message: str):
    """repeats message"""
    await ctx.respond(str(message))


def lookup_device(user_id: str, device_id: str) -> OlmDevice|None:
    for olmdevice in bot.device_store:
        conditions = [
            olmdevice.user_id == user_id,
            olmdevice.device_id == device_id
        ]
        if all(conditions):
            return olmdevice


@bot.command(name="list-devices")
async def list_devices_command(ctx: niobot.Context):
    """list all known devices (owner only)"""
    if not bot.is_owner(ctx.msg.sender):
        await ctx.respond("only owner can do this")
        return

    output = ""
    count = 0
    for olmdevice in bot.device_store:
        count += 1
        output += f"User ID: {olmdevice.user_id}\n"
        output += f"Device ID: {olmdevice.device_id}\n"
        output += f"Display name: {olmdevice.display_name}\n"
        output += f"Keys: {olmdevice.keys}\n"
        output += f"Deleted: {olmdevice.deleted}\n"
        output += f"Trust state: {olmdevice.trust_state}\n"
        output += "-------------------------------------\n"

    output += f"Total: {count}"

    await ctx.respond(output, content_type="plain")


@bot.command(name="verify-device")
async def verify_device_command(
    ctx: niobot.Context,
    user_id: str,
    device_id: str
):
    """verify a specific device key (owner only)"""
    if bot.is_owner(ctx.msg.sender):

        olmdevice = lookup_device(user_id, device_id)

        if olmdevice is None:
            await ctx.respond("couldn't find that device in my store")
        else:
            result = bot.verify_device(olmdevice)
            if result:
                await ctx.respond("successfuly verified")
            else:
                await ctx.respond("that device was already verified 🙄")
    else:
        await ctx.respond("only owner can do this")


@bot.command(name="blacklist-device")
async def blacklist_device_command(
    ctx: niobot.Context,
    user_id: str,
    device_id: str
):
    """blacklist a specific device key (owner only)"""
    if not bot.is_owner(ctx.msg.sender):
        await ctx.respond("only owner can do this")
        return
    olmdevice = lookup_device(user_id, device_id)

    if olmdevice is None:
        await ctx.respond("no such device in my store")
    else:
        result = bot.blacklist_device(olmdevice)
        if result:
            await ctx.respond("successfully blacklisted")
        else:
            await ctx.respond("it was on the blacklist already")


bot.run(password=cfg.password)
