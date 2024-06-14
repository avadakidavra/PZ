#  1) перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  2) перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  3) перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  4) перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().
#  5) удалить файл test.txt.

import os
import shutil

base_path = r"C:\Users\Elnur\Desktop\PZ\PZ"


# 1
def list_files_in_pz11():
    pz11_path = os.path.join(base_path, "PZ_11")
    files = [f for f in os.listdir(pz11_path) if os.path.isfile(os.path.join(pz11_path, f))]
    print("ФАЙЛЫ 11", files)


# 2
def create_and_move_files():
    test_path = os.path.join(base_path, "test")
    test1_path = os.path.join(test_path, "test1")
    pz6_path = os.path.join(base_path, "PZ_6")
    pz7_path = os.path.join(base_path, "PZ_7")

    os.makedirs(test1_path, exist_ok=True)
    shutil.move(os.path.join(pz6_path, "PZ_6_1.py"), os.path.join(test_path, "PZ_6_1.py"))
    shutil.move(os.path.join(pz6_path, "PZ_6_2.py"), os.path.join(test_path, "PZ_6_2.py"))
    shutil.move(os.path.join(pz7_path, "PZ_7_1.py"), os.path.join(test1_path, "test.txt"))

    for root, dirs, files in os.walk(test_path):
        for file in files:
            filepath = os.path.join(root, file)
            print(f"ФАЙЛ {file} РАЗМЕР {os.path.getsize(filepath)}")


# 3
def find_shortest_filename_in_pz11():
    pz11_path = os.path.join(base_path, "PZ_11")
    files = [f for f in os.listdir(pz11_path) if os.path.isfile(os.path.join(pz11_path, f))]
    shortest_name = min(files, key=lambda x: len(os.path.basename(x)))
    print("КОРОТКИЙ", os.path.basename(shortest_name))


# 4
try:
    pdf_report_path = r'C:\\Users\\Elnur\\Desktop\\PZ\\PZ\\Reports'
    os.startfile(pdf_report_path)
except FileNotFoundError:
    pass


# 5
def delete_test_txt():
    test_txt_path = os.path.join(base_path, "test", "test1", "test.txt")
    if os.path.exists(test_txt_path):
        os.remove(test_txt_path)
        print("УДАЛЕН")


if __name__ == "__main__":
    list_files_in_pz11()
    create_and_move_files()
    find_shortest_filename_in_pz11()
    delete_test_txt()
