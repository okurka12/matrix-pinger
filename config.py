import password as password_module

homeserver = "https://matrix.vitapavlik.cz"
bot_user_id = "@test-user-xx:matrix.vitapavlik.cz"
auto_join_rooms = True
auto_read_messages = True

# you can set pretty much anything here but keep it consistent so your bot
# doesn't create a milion device keys
device_id = "my-device-1234"

# the device keys are stored here
store_path = "./store"

# only useful for owner-only commands
owner_id = "@vita:matrix.vitapavlik.cz"

password = password_module.password
