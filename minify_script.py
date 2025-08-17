import os
import python_minifier

# Путь к исходному проекту и куда копировать минифицированную версию

#########################################################
source_dir = r"D:\Vs_code\Rat\RootWormV2"
output_dir = r"D:\Vs_code\Rat\minify_RAT"
#########################################################

def minify_file(source_path, target_path):
    try:
        with open(source_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print(f"[ERROR] Не удалось прочитать {source_path}: {e}")
        return

    try:
        minified = python_minifier.minify(
            code,
            remove_literal_statements=True,   # удаляет докстринги/литералы документации
            rename_locals=True,               # переименование локальных переменных — безопасно
            rename_globals=False              # ВАЖНО: НЕ переименовывать глобалы, чтобы импорты работали
        )
    except Exception as e:
        print(f"[ERROR] Ошибка минификации {source_path}: {e}")
        return

    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(minified)
        print(f"[GOOD] Минифицирован: {source_path} -> {target_path}")
    except Exception as e:
        print(f"[ERROR] Не удалось записать {target_path}: {e}")

def minify_project(src_dir, out_dir):
    src_dir = os.path.abspath(src_dir)
    out_dir = os.path.abspath(out_dir)
    print(f"Минификация: {src_dir} -> {out_dir}")
    for root, dirs, files in os.walk(src_dir):
        # не обрабатывать папку вывода, если она внутри исходной
        if os.path.commonpath([os.path.abspath(root), out_dir]) == out_dir:
            continue
        for file in files:
            if file.endswith(".py"):
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, src_dir)
                target_path = os.path.join(out_dir, relative_path)
                minify_file(src_path, target_path)
    print("Готово")

if __name__ == "__main__":
    # Рекомендуется сделать резервную копию исходной папки перед запуском
    minify_project(source_dir, output_dir)