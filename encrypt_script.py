##  _________________________________________
##   |_______  authors: Eks1azy     _______|
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##    \_\_\_|______  Tusay1  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\
##   ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy      / /
##  |                                        / /
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/

import os
import shutil
import subprocess

PROJECT_ENTRY = "RootWormV2.py"
OUTPUT_DIR = "dist"

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
    print("РЎС‚Р°СЂР°СЏ СЃР±РѕСЂРєР° СѓРґР°Р»РµРЅР°.")

print("РћР±С„СѓСЃРєР°С†РёСЏ РїСЂРѕРµРєС‚Р°...")
subprocess.run(["pyarmor", "gen", "-i", PROJECT_ENTRY, "-O", OUTPUT_DIR])

print("Р“РѕС‚РѕРІРѕ. Р¤Р°Р№Р»С‹ РІ РїР°РїРєРµ:", OUTPUT_DIR)
