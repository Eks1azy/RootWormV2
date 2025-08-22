##  _________________________________________
##   |_______  authors: Eks1azy  _______| 
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\                    
##  ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy   / /
##  |                                        / / 
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/


from aiogram import Bot, Dispatcher
import os 


############################################################
API_TOKEN = '123123123123123213'   # TG API BOT TOKEN
ALLOWED_USER_ID = 123123123        # TG USER ID
############################################################


MAX_MESSAGE_LENGTH = 4000  # telegram limit – 4096 characters
MAX_ATTEMPTS = 1

destination_folder = r'C:\ProgramData\MediaTask'
directory = "C:/Users/Public/main"

os.makedirs(destination_folder, exist_ok=True)
os.makedirs(directory, exist_ok=True)

file_ids = []

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
