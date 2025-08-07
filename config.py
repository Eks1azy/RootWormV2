##  _________________________________________
##   |_______  authors: NoNamedExe  _______| 
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\                    
##  ___________________________________________
##  |                                          /\
##  |  github:https://github.com/NoNamedExe   / /
##  |                                        / / 
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/



###########################################################
API_TOKEN = '8237470674:AAGBEo7sfgiQFhxy88uAIUjor9YEHsOj8AI'  # TG API BOT TOKEN
ALLOWED_USER_ID = 950461095  # TG USER ID 
###########################################################



MAX_MESSAGE_LENGTH = 4000  # telegram limit – 4096 characters
MAX_ATTEMPTS = 1

destination_folder = r'C:\ProgramData\MediaTask'
directory = "C:/Users/Public/main"

from library import *

os.makedirs(destination_folder, exist_ok=True)
os.makedirs(directory, exist_ok=True)

file_ids = []

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
