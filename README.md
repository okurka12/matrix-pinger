# Matrix pinger

An always-online fellow that responds `pong` to your `!ping`

## Quick guide for docker installation

- `mkdir store` (your bot's device key is going to be stored here, outside of
  the container)
- edit `config.py` to match your configuration
- create `password.py` with line `password = "mypassword123"` (change
  `mypassword123` to your actual password)
- `docker compose up -d`

## How to set up

- `mkdir venv`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `mkdir store`
- `nano config.py` - edit your homeserver and bot configuration here
- `nano password.py` - enter `password = "123"` here

## Run one time

- `source venv/bin/activate`
- `python3 main.py`

## Install as a service

- `nano matrix-pinger.service` - edit your user and directory
- `sudo cp matrix-pinger.service /usr/local/lib/systemd/system/`
 - you may need to `mkdir -p /usr/local/lib/systemd/system/`
- `sudo systemctl enable matrix-pinger`
- `sudo systemctl start matrix-pinger`

## Credits

Creation of this bot was possible thanks to
[`nio-bot`](https://pypi.org/project/nio-bot/1.1.0a2/). Go give them a star on
[github](https://github.com/nexy7574/nio-bot)!
