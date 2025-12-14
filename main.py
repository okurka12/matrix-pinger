import logging

# Set the logging level to DEBUG/INFO to see all the connection attempts and errors
logging.basicConfig(level=logging.INFO)

import niobot
import config as cfg

# Initialize the bot
bot = niobot.NioBot(
    homeserver=cfg.homeserver,
    user_id=cfg.bot_user_id,
    device_id=cfg.device_id,
    owner_id=cfg.device_id,
    store_path=cfg.store_path,
    auto_join_rooms=cfg.auto_join_rooms,
    auto_read_messages=cfg.auto_read_messages,
    command_prefix="!",
    case_insensitive=True,
)

# Define a command
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
async def echo_command(ctx: niobot.Context, message):
    """repeats message"""
    await ctx.respond(str(message))


bot.run(password=cfg.password)
