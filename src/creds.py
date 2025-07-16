from pathlib import Path
from jproperties import Properties

project_dir = Path(__file__).resolve().parent.parent


configs = Properties()
with open(project_dir / 'config/app-config.properties', 'rb') as config_file:
    configs.load(config_file)

# web driver
use_web_driver = True if configs.get('use_web_driver').data == "True" else False
local_debugger_address = configs.get('local_debugger_address').data
wait_web_driver = int(configs.get('wait_web_driver').data)
remote_web_driver = configs.get('remote_web_driver').data
driver_version = configs.get('driver_version').data or None

# ais.usvisa-info.com credentials

username = configs.get('username').data
password = configs.get('password').data

# Number id in the url (e.g.: https://ais.usvisa-info.com/en-ca/niv/schedule/41231513)
url_id = configs.get('url_id').data

# Country code in the url
country_code = configs.get('country_code').data

facility_name = configs.get('facility_name').data

latest_notification_date = configs.get('latest_notification_date').data

seconds_between_checks = int(configs.get('seconds_between_checks').data)

# Telegram bot token and chat
telegram_bot_token = configs.get('telegram_bot_token').data
telegram_chat_id = configs.get('telegram_chat_id').data
