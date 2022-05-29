from importlib.resources import path
from tkinter import *
from pathlib import Path


BASE_DIR = Path(__name__).absolute().parent
BITMAP = BASE_DIR / 'logo.ico'

# print(str(BITMAP.absolute()))

root = Tk()
root.geometry("400x400")
root.title('KOKOA')
root.iconbitmap(str(BITMAP))


title_Label = Label(root, text='KOKOA')
desc_Label = Label(root, text='Here you can convert images and transform them.')

resize_Btn = Button(root, text='Rezise')
resize_cancel_Btn = Button(root, text='Cancel')
resize_accept_Btn = Button(root, text='Accept', state=DISABLED)


title_Label.pack()
desc_Label.pack()
resize_Btn.pack()



root.mainloop()
