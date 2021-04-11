
import os
os.system('pip install -U -r requirements.txt')

import discordbot
discordbot.start(os.getenv("TOKEN"))
