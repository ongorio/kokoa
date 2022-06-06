from re import L
from tkinter import *
from pathlib import Path
from tkinter import filedialog
from PIL import ImageTk, Image


BASE_DIR = Path(__name__).absolute().parent
BITMAP = BASE_DIR / 'logo.ico'

# print(str(BITMAP.absolute()))

root = Tk()
root.geometry("1280x720")
root.title('KOKOA')
root.iconbitmap(str(BITMAP))

active_frame_elements = []

root.filename = ''
def remove_frame_elements():
    for element in active_frame_elements:
        element.forget()


def main_menu_frame():
    global desc_Label
    global resize_Btn

    root.filename = ''

    remove_frame_elements()

    desc_Label.pack()
    resize_Btn.pack()




def resize_frame():
    # global title_Label
    global desc_Label
    global resize_Btn


    global resize_cancel_Btn
    global resize_accept_Btn
    global menu_Btn
    global select_image_Btn
    global image_label

    desc_Label.forget()
    resize_Btn.forget()


    if not root.filename:
        image_label = Label(root, text='No Image Selected!')

    menu_Btn.pack()
    image_label.pack()
    resize_cancel_Btn.pack()
    resize_accept_Btn.pack()
    select_image_Btn.pack()

    

    active_frame_elements.clear()
    active_frame_elements.append(resize_accept_Btn)
    active_frame_elements.append(resize_cancel_Btn)
    active_frame_elements.append(menu_Btn)
    active_frame_elements.append(select_image_Btn)
    active_frame_elements.append(image_label)


def select_image():
    global image_label
    global resize_accept_Btn
    global width_label
    global width_entry
    global height_label
    global height_entry
    global equality_checkbox
    global resize_accept

    resize_accept_Btn.forget()
    image_label.forget()
    root.filename = filedialog.askopenfilename(initialdir=BASE_DIR, title='Select File', filetypes=(
            ('JPEG Files', '*.jpg'),('PNG Files', '*.png')
        ))
    

    if root.filename:
        # print('selected')
        # img = ImageTk.PhotoImage(Image.open(root.filename))
        image_label = Label(root, text=f"Selected Image: {root.filename}")
        resize_accept_Btn = Button(root, text='Accept', command=resize_accept)
        # print()
    else:
        resize_accept_Btn = Button(root, text='Accept', state=DISABLED)
        image_label = Label(root, text='No Image Selected')

    # image_label.pack()
    resize_frame()

    width_label.pack()
    width_entry.pack()
    height_label.pack()
    height_entry.pack()
    equality_checkbox.pack()


    active_frame_elements.append(width_label)
    active_frame_elements.append(width_entry)
    active_frame_elements.append(height_entry)
    active_frame_elements.append(height_label)
    active_frame_elements.append(equality_checkbox)


def resize_same_proportions():
    global sp
    global height_label
    global height_entry

    height_label.forget()
    height_entry.forget()
    # print('hge')
    if sp.get() == 1:
        height_entry = Entry(root, state=DISABLED)
    else:
        height_entry = Entry(root)

    height_label.pack()
    height_entry.pack()


def resize_accept():
    global width_entry
    global height_entry
    global sp
    
    root.filedirectory = filedialog.askdirectory(initialdir=BASE_DIR)

    img_width = int(width_entry.get())

    if root.filedirectory:
        if sp.get() == 1:
            
            img = Image.open(root.filename)
            dimensions = (img_width, img_width)
            img.thumbnail(dimensions)

            destination = Path() / root.filedirectory / Path(root.filename).absolute().name
            count = 1
            dest_exists = True
            while dest_exists:
                if destination.exists():
                    destination = destination.parent / f"{destination.stem}{count}{destination.suffix}" 
                    count += 1
                else:
                    dest_exists = False

            print(destination)
            img.save(destination)   
        else:
            img_height = int(height_entry.get())

            img = Image.open(root.filename)
            dimensions = (img_width, img_height)
            img.thumbnail(dimensions)

            destination = Path() / root.filedirectory / Path(root.filename).absolute().name
            count = 1

            dest_exists = True
            while dest_exists:
                if destination.exists():
                    destination = destination.parent / f'{destination.stem}{count}{destination.suffix}'
                    count += 1
                else:
                    dest_exists = False
                
                print(destination)
                img.save(destination)



# Main Menu elements
title_Label = Label(root, text='KOKOA')
desc_Label = Label(root, text='Here you can convert images and transform them.')
menu_Btn = Button(root, text='Menu', command=main_menu_frame)


# img = ImageTk.PhotoImage(Image.open(BASE_DIR/"orb.jpg"))


# Resizing
image_label = Label(root, text='No image Selected')
image_showing_label = Label()


sp = IntVar()
width_label = Label(root, text='Width:')
width_entry = Entry(root)
height_label = Label(root, text='Height:')
height_entry = Entry(root)
equality_checkbox = Checkbutton(root, text='Same Width and Height', variable=sp, command=resize_same_proportions)


select_image_Btn = Button(root, text='Select File', command=select_image)

resize_Btn = Button(root, text='Resize', command=resize_frame)
resize_cancel_Btn = Button(root, text='Cancel', command=main_menu_frame)
resize_accept_Btn = Button(root, text='Accept', state=DISABLED, command=resize_accept)


title_Label.pack()
desc_Label.pack()
resize_Btn.pack()



root.mainloop()
