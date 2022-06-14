from tkinter import *
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
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
root.icon_size = ''

def remove_frame_elements():
    for element in active_frame_elements:
        element.forget()


def main_menu_frame():
    global desc_Label
    global resize_Btn
    global create_icon_Btn
    global icon_size

    root.filename = ''
    root.icon_size = ''
    icon_size.set('')

    remove_frame_elements()


    active_frame_elements.append(desc_Label)
    active_frame_elements.append(resize_Btn)
    active_frame_elements.append(create_icon_Btn)

    desc_Label.pack()
    resize_Btn.pack()
    create_icon_Btn.pack()


def select_image():
    root.filename = filedialog.askopenfilename(initialdir=BASE_DIR, title='Select File', filetypes=(
        ('JPEG, JPG', '*.jpg'), ('PNG Files', '*.png')
    ))

def resize_frame():
    # global title_Label
    remove_frame_elements()
    global desc_Label
    global resize_Btn


    global resize_cancel_Btn
    global resize_accept_Btn
    global menu_Btn
    global select_image_Btn
    global image_label
    global resize_image

    desc_Label.forget()
    resize_Btn.forget()

    select_image_Btn = Button(root, text='Select File', comman=resize_image)


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


def resize_image():
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
    select_image()
    

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
            
            img = Image.open(root.filename).copy()
            dimensions = (img_width, img_width)
            img.thumbnail(dimensions)

            destination = Path() / root.filedirectory / Path(root.filename).absolute().name
            temp = destination
            count = 0
            dest_exists = True
            while dest_exists:
                if count != 0:
                    temp = destination.parent / f"{destination.stem}{count}{destination.suffix}"


                if temp.exists():
                    count += 1
                else:
                    destination = temp
                    dest_exists = False

            print(destination)
            img.save(destination)   

            img.close()

        else:
            img_height = int(height_entry.get())

            img = Image.open(root.filename)
            dimensions = (img_width, img_height)
            img = img.resize(dimensions)

            destination = Path() / root.filedirectory / Path(root.filename).absolute().name
            temp = destination
            count = 0

            dest_exists = True
            while dest_exists:
                if count != 0:
                    temp  = destination.parent / f"{destination.stem}{count}{destination.suffix}"

                if temp.exists():
                    count += 1
                else:
                    destination = temp
                    dest_exists = False
                
            # print(img.width,img.height)
            img.save(destination)
            img.close()

    root.filename = ''
    messagebox.showinfo('Success!', 'Picture Changed Succesfuly!')
    main_menu_frame()


def select_convert_image():
    global convert_frame

    select_image()
    convert_frame()


def convert_icon():
    global convert_frame

    sizes = (root.icon_size,root.icon_size)
    # print(root.filename)
    img = Image.open(root.filename).copy()
    img.thumbnail(sizes)

    messagebox.showinfo('Select Save Location',
        'Please select the saving location.'
    )

    root.filedirectory = filedialog.askdirectory(initialdir=BASE_DIR)

    if root.filedirectory:

        destination = Path() / root.filedirectory / f'{Path(root.filename).absolute().stem}.ico'
        temp = destination 
        count = 0
        dest_exist = True

        while dest_exist:

            if count != 0:
                temp = destination.parent / f'{destination.stem}{count}{destination.suffix}'

            if temp.exists():
                count += 1
            else:
                destination = temp
                dest_exist = False


        print(destination)        
        img.save(destination, format='ICO')
        messagebox.showinfo('Success!', 'Icon generated Succesfully!')
        main_menu_frame()
        


def convert_frame():
    global create_icon_Btn
    global select_image_Btn
    global image_label
    global convert_cancel_Btn
    global convert_accept_Btn
    global icon_sizes_options
    global icon_sizes_label

    remove_frame_elements()

    select_image_Btn = Button(root, text='Select File', command=select_convert_image)


    if not root.filename:
        image_label = Label(root, text='No image Selected!')
    else:
        image_label = Label(root, text=f'Selected Image:{root.filename}')

    if root.filename and root.icon_size:
        convert_accept_Btn = Button(root, text='Convert', command=convert_icon)
    else:
        convert_accept_Btn = Button(root, text='Convert', state=DISABLED)


    active_frame_elements.clear()
    # active_frame_elements.append(create_icon_Btn)
    active_frame_elements.append(convert_cancel_Btn)
    active_frame_elements.append(convert_accept_Btn)
    active_frame_elements.append(image_label)
    active_frame_elements.append(icon_sizes_options)
    active_frame_elements.append(icon_sizes_label)
    active_frame_elements.append(select_image_Btn)


    # create_icon_Btn.pack()
    icon_sizes_label.pack()
    icon_sizes_options.pack()
    image_label.pack()
    select_image_Btn.pack()
    convert_accept_Btn.pack()
    convert_cancel_Btn.pack()



def select_convert_size(value):
    size = int(str(value).split('x')[0])

    root.icon_size = size
    # print(root.icon_size)
    convert_frame()




# Main Menu elements
title_Label = Label(root, text='KOKOA')
desc_Label = Label(root, text='Here you can convert images and transform them.')
menu_Btn = Button(root, text='Menu', command=main_menu_frame)


# Resizing
image_label = Label(root, text='No image Selected')
image_showing_label = Label()


sp = IntVar()
width_label = Label(root, text='Width:')
width_entry = Entry(root)
height_label = Label(root, text='Height:')
height_entry = Entry(root)
equality_checkbox = Checkbutton(root, text='Same Width and Height', variable=sp, command=resize_same_proportions)


select_image_Btn = Button(root, text='Select File')

resize_Btn = Button(root, text='Resize', command=resize_frame)
resize_cancel_Btn = Button(root, text='Cancel', command=main_menu_frame)
resize_accept_Btn = Button(root, text='Accept', state=DISABLED, command=resize_accept)



# Convert button
create_icon_Btn = Button(root, text='Icon', command=convert_frame)
convert_cancel_Btn = Button(root, text='Cancel', command=main_menu_frame)
convert_accept_Btn = Button(root, text='Convert', state=DISABLED)

icon_size = StringVar()
# icon_size.set('128x128')
sizes = ['256x256',"128x128", '64x64', '32x32', '16x16']
icon_sizes_label = Label(root, text='Sizes:')
icon_sizes_options = OptionMenu(root, icon_size, *sizes, command=select_convert_size)



title_Label.pack()
desc_Label.pack()
resize_Btn.pack()
create_icon_Btn.pack()


active_frame_elements.append(desc_Label)
active_frame_elements.append(resize_Btn)
active_frame_elements.append(create_icon_Btn)


root.mainloop()
