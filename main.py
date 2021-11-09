from PIL import Image
from pylibdmtx import pylibdmtx
import tkinter as tk
from tkinter import filedialog
import pandas

EXAMPLE_STRING = "Stegosaurus"
EXCEL_SHEET_NUM = 0
EXCEL_HEADER = 0
EXCEL_COL_NAME = "Sorszám"


def get_file_from_dialog():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()


def get_data_from_excel(file_path: str):
    data = pandas.read_excel(file_path, sheet_name=EXCEL_SHEET_NUM, header=EXCEL_HEADER)
    return data[EXCEL_COL_NAME].values.tolist()


def encode(text: str):
    return pylibdmtx.encode(text.encode('utf-8'))


def main():
    file_path = get_file_from_dialog()
    if file_path == '':
        return

    data = get_data_from_excel(file_path)

    # generate data matrices
    for i, element in enumerate(data):
        encoded_data = encode(element)
        img = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
        img.save(f'generated_{i}.png')


if __name__ == '__main__':
    main()
