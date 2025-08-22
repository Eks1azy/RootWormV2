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
import python_minifier

# РџСѓС‚СЊ Рє РёСЃС…РѕРґРЅРѕРјСѓ РїСЂРѕРµРєС‚Сѓ Рё РєСѓРґР° РєРѕРїРёСЂРѕРІР°С‚СЊ РјРёРЅРёС„РёС†РёСЂРѕРІР°РЅРЅСѓСЋ РІРµСЂСЃРёСЋ

#########################################################
source_dir = r"D:\Vs_code\Rat\RootWormV2"        # Папка с исходными файлами проекта ( Ваш )
output_dir = r"D:\Vs_code\Rat\Manify_RootWormV2"  # Папка для минифицированных файлов ( Ваш )
#########################################################

def minify_file(source_path, target_path):
    try:
        with open(source_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print(f"[ERROR] РќРµ СѓРґР°Р»РѕСЃСЊ РїСЂРѕС‡РёС‚Р°С‚СЊ {source_path}: {e}")
        return

    try:
        minified = python_minifier.minify(
            code,
            remove_literal_statements=True,   # СѓРґР°Р»СЏРµС‚ РґРѕРєСЃС‚СЂРёРЅРіРё/Р»РёС‚РµСЂР°Р»С‹ РґРѕРєСѓРјРµРЅС‚Р°С†РёРё
            rename_locals=True,               # РїРµСЂРµРёРјРµРЅРѕРІР°РЅРёРµ Р»РѕРєР°Р»СЊРЅС‹С… РїРµСЂРµРјРµРЅРЅС‹С… вЂ” Р±РµР·РѕРїР°СЃРЅРѕ
            rename_globals=False              # Р’РђР–РќРћ: РќР• РїРµСЂРµРёРјРµРЅРѕРІС‹РІР°С‚СЊ РіР»РѕР±Р°Р»С‹, С‡С‚РѕР±С‹ РёРјРїРѕСЂС‚С‹ СЂР°Р±РѕС‚Р°Р»Рё
        )
    except Exception as e:
        print(f"[ERROR] РћС€РёР±РєР° РјРёРЅРёС„РёРєР°С†РёРё {source_path}: {e}")
        return

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(minified)
        print(f"[GOOD] РњРёРЅРёС„РёС†РёСЂРѕРІР°РЅ: {source_path} -> {target_path}")
    except Exception as e:
        print(f"[ERROR] РќРµ СѓРґР°Р»РѕСЃСЊ Р·Р°РїРёСЃР°С‚СЊ {target_path}: {e}")

def minify_project(src_dir, out_dir):
    src_dir = os.path.abspath(src_dir)
    out_dir = os.path.abspath(out_dir)
    print(f"РњРёРЅРёС„РёРєР°С†РёСЏ: {src_dir} -> {out_dir}")
    for root, dirs, files in os.walk(src_dir):
        # РЅРµ РѕР±СЂР°Р±Р°С‚С‹РІР°С‚СЊ РїР°РїРєСѓ РІС‹РІРѕРґР°, РµСЃР»Рё РѕРЅР° РІРЅСѓС‚СЂРё РёСЃС…РѕРґРЅРѕР№
        if os.path.commonpath([os.path.abspath(root), out_dir]) == out_dir:
            continue
        for file in files:
            if file.endswith(".py"):
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, src_dir)
                target_path = os.path.join(out_dir, relative_path)
                minify_file(src_path, target_path)
    print("Р“РѕС‚РѕРІРѕ")

if __name__ == "__main__":
    # Р РµРєРѕРјРµРЅРґСѓРµС‚СЃСЏ СЃРґРµР»Р°С‚СЊ СЂРµР·РµСЂРІРЅСѓСЋ РєРѕРїРёСЋ РёСЃС…РѕРґРЅРѕР№ РїР°РїРєРё РїРµСЂРµРґ Р·Р°РїСѓСЃРєРѕРј
    minify_project(source_dir, output_dir)
