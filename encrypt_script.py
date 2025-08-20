import os
import shutil
import subprocess

PROJECT_ENTRY = "RootWormV2.py"
OUTPUT_DIR = "dist"

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
    print("Старая сборка удалена.")

print("Обфускация проекта...")
subprocess.run(["pyarmor", "gen", "-i", PROJECT_ENTRY, "-O", OUTPUT_DIR])

print("Готово. Файлы в папке:", OUTPUT_DIR)
