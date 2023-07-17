import logging
import shutil
from datetime import datetime


def log_setup():
    logging.basicConfig(
        filename="logs.txt",
        level=logging.INFO,
        format="[%(asctime)s] - %(message)s"
    )
def cp(source, dest):
    try:
        shutil.copy(source, dest)
        logging.info(f"{source} - copied successfully.")
        print("Файл успешно скопирован.")
    except Exception as e:
        logging.error(f"{source} - wasn't copied. Error: {e}")
        print("Ошибка при копировании файла!")


source_file_path = "C:/Users/Administrator/Desktop/По учёбе/Новая папка/src/file.txt"
destination_file_path = "C:/Users/Administrator/Desktop/По учёбе/Новая папка/dst"

log_setup()
cp(source_file_path, destination_file_path)