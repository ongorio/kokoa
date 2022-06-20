from struct import pack
from textwrap import fill
from tkinter import *
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image


BASE_DIR = Path(__name__).absolute().parent
BITMAP = BASE_DIR / 'logo.ico'

# print(str(BITMAP.absolute()))

root = Tk()
root.geometry("600x600")
root.title('KOKOA')
root.iconbitmap(str(BITMAP))

active_frame_elements = []

root.filename = ''
root.icon_size = ''


def remove_frame_elements():
    """
    Removes elements that are not use in all frames and that are active.
    """
    for element in active_frame_elements:
        element.forget()
        element.grid_forget()


def main_menu_frame():
    """
    Main window

    Contains the main menu and is the frame show when the program starts.
    It resets all values from variables.
    """
    
    global menu_label
    global resize_Btn
    global create_icon_Btn
    global icon_size

    # Clear all variables
    root.filename = ''
    root.icon_size = ''
    icon_size.set('')

    remove_frame_elements()


    active_frame_elements.append(menu_label)
    active_frame_elements.append(resize_Btn)
    active_frame_elements.append(create_icon_Btn)

    menu_label.pack()
    resize_Btn.pack()
    create_icon_Btn.pack()


def select_image():
    """
    When call opens a new window to select an image and saves it to the filename attribute in root.
    """
    root.filename = filedialog.askopenfilename(initialdir=BASE_DIR, title='Select File', filetypes=(
        ('JPEG, JPG', '*.jpg'), ('PNG Files', '*.png')
    ))

def resize_frame():
    """
    Resize frame

    Use to resize images
    """
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
    global resize_label
    global resize_lbframe
    global image_showing_label


    select_image_Btn = Button(resize_lbframe, text='Select File', comman=resize_image)


    if root.filename:
        img = Image.open(root.filename)
        img.thumbnail((100,100))
        img = ImageTk.PhotoImage(img)


        image_showing_label = Label(resize_lbframe, image=img, width=100, height=100)
        image_showing_label.img = img

        image_label = Label(resize_lbframe, text=f'Selected Image: {root.filename}', pady=5)
        resize_accept_Btn = Button(resize_lbframe, text='Accept', command=resize_accept)
        image_showing_label.grid(column=0, row=2, columnspan=2, sticky='')
    else:
        resize_accept_Btn = Button(resize_lbframe, text='Accept', state=DISABLED)
        image_label = Label(resize_lbframe, text='No Image Selected', pady=5)
        image_showing_label.grid_forget()

    

    resize_lbframe.pack(fill='both')

    resize_label.grid(column=0, row=0, columnspan=2, sticky='', padx=270)
    select_image_Btn.grid(column=0, row=1, sticky='', columnspan=2)
    image_label.grid(column=0, row=3, sticky='', columnspan=2)

    resize_accept_Btn.grid(column=0, row=7)
    resize_cancel_Btn.grid(column=1, row=7)



    
    active_frame_elements.clear()
    active_frame_elements.append(resize_lbframe)
    active_frame_elements.append(resize_accept_Btn)
    active_frame_elements.append(resize_cancel_Btn)
    active_frame_elements.append(menu_Btn)
    active_frame_elements.append(select_image_Btn)
    active_frame_elements.append(image_label)
    active_frame_elements.append(resize_label)


def resize_image():
    """
    After image is selected if valid enable resize button and
    adds the entries for height and width.
    """
    global width_label
    global width_entry
    global height_label
    global height_entry
    global equality_checkbox

    select_image()
    resize_frame()


    width_label.grid(column=0, row=4, sticky='E')
    width_entry.grid(column=1, row=4, sticky='W')
    height_label.grid(column=0, row=5, sticky='E')
    height_entry.grid(column=1, row=5, sticky='W')
    equality_checkbox.grid(column=0, row=6, columnspan=2)



    active_frame_elements.append(width_label)
    active_frame_elements.append(width_entry)
    active_frame_elements.append(height_entry)
    active_frame_elements.append(height_label)
    active_frame_elements.append(equality_checkbox)


def resize_same_proportions():
    """
    If same proportion is checked, disables height entry.
    """

    global sp
    global height_label
    global height_entry
    global width_label
    global resize_lbframe

    width_label.grid_forget()

    if sp.get() == 1:
        height_label.grid_forget()
        height_entry.grid_forget()
        width_label = Label(resize_lbframe,text='Size:')
    else:
        width_label = Label(resize_lbframe, text='Width:')
        height_label.grid(column=0, row=5, sticky='E')
        height_entry.grid(column=1, row=5, sticky='W')

    width_label.grid(column=0, row=4, sticky='E')


def resize_accept():
    """
    First calls a new windows to select the saving location.

    Then saves the image with the new size or sizes.

    Finally returns to the main menu.
    """
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
    """
    Calls the select image window and reloads the page.
    """
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
    """
    Frame to convert images to ICO format
    """
    global create_icon_Btn
    global select_image_Btn
    global image_label
    global convert_cancel_Btn
    global convert_accept_Btn
    global icon_sizes_options
    global icon_sizes_label
    global icon_frame
    global icon_label

    remove_frame_elements()


    select_image_Btn = Button(icon_frame, text='Select File', command=select_convert_image)


    if not root.filename:
        image_label = Label(icon_frame, text='No image Selected!')
    else:
        image_label = Label(icon_frame, text=f'Selected Image:{root.filename}')

    if root.filename and root.icon_size:
        convert_accept_Btn = Button(icon_frame, text='Convert', command=convert_icon)
    else:
        convert_accept_Btn = Button(icon_frame, text='Convert', state=DISABLED)

    icon_frame.pack(fill='both')


    icon_label.grid(column=0, row=0, padx=250, sticky='', columnspan=2)
    select_image_Btn.grid(column=0, row=1, columnspan=2, sticky='')
    image_label.grid(column=0, row=3, columnspan=2, sticky='')
    icon_sizes_label.grid(column=0, row=4, sticky='E')
    icon_sizes_options.grid(column=1, row=4, sticky='W')
    convert_accept_Btn.grid(column=0, row=5)
    convert_cancel_Btn.grid(column=1, row=5)
    # create_icon_Btn.pack()
    # select_image_Btn.pack()
    # image_label.pack()
    # icon_sizes_label.pack()
    # icon_sizes_options.pack()
    # convert_accept_Btn.pack()
    # convert_cancel_Btn.pack()


    active_frame_elements.clear()
    # active_frame_elements.append(create_icon_Btn)
    active_frame_elements.append(icon_frame)
    active_frame_elements.append(convert_cancel_Btn)
    active_frame_elements.append(convert_accept_Btn)
    active_frame_elements.append(image_label)
    active_frame_elements.append(icon_sizes_options)
    active_frame_elements.append(icon_sizes_label)
    active_frame_elements.append(select_image_Btn)



def select_convert_size(value):
    """
    Function to be call when size option is change.

    The value is added to the icon_size values.
    """
    size = int(str(value).split('x')[0])

    root.icon_size = size
    # print(root.icon_size)
    convert_frame()


head_frame = LabelFrame(root,height= 50, bg='#d17210', bd=0)
head_frame.pack(fill='x', side='top', pady=(0, 10))



# Main Menu elements
title_Label = Label(head_frame, text='KOKOA', bg='#d17210', fg='white', font=50)
desc_Label = Label(head_frame, text='Change and Transform images!', bg='#d17210', fg='white')

title_Label.pack(pady=4)
desc_Label.pack(pady=2)


menu_label = Label(root, text='Main Menu')
menu_Btn = Button(root, text='Menu', command=main_menu_frame)


# Resizing
resize_Btn = Button(root, text='Resize', command=resize_frame, width=15)
resize_lbframe = LabelFrame(root, width=600)

resize_label = Label(resize_lbframe, text='Resize', font=25, pady=10)
image_label = Label(resize_lbframe, text='No image Selected')
image_showing_label = Label(resize_lbframe)


sp = IntVar()
width_label = Label(resize_lbframe, text='Width:')
width_entry = Entry(resize_lbframe)
height_label = Label(resize_lbframe, text='Height:')
height_entry = Entry(resize_lbframe)
equality_checkbox = Checkbutton(resize_lbframe, text='Same Width and Height', variable=sp, command=resize_same_proportions)


select_image_Btn = Button(root, text='Select File')

resize_cancel_Btn = Button(resize_lbframe, text='Cancel', command=main_menu_frame)
resize_accept_Btn = Button(resize_lbframe, text='Accept', state=DISABLED, command=resize_accept)



# Convert button
create_icon_Btn = Button(root, text='Icon', command=convert_frame, width=15)
icon_frame = LabelFrame(root, width=600)

icon_label = Label(icon_frame, text='Convert 2 Icon', font=25, pady=10)

convert_cancel_Btn = Button(icon_frame, text='Cancel', command=main_menu_frame)
convert_accept_Btn = Button(icon_frame, text='Convert', state=DISABLED)

icon_size = StringVar()
# icon_size.set('128x128')
sizes = ['256x256',"128x128", '64x64', '32x32', '16x16']
icon_sizes_label = Label(icon_frame, text='Sizes:')
icon_sizes_options = OptionMenu(icon_frame, icon_size, *sizes, command=select_convert_size)





menu_label.pack(pady=(0, 10))
resize_Btn.pack()
create_icon_Btn.pack()



# active_frame_elements.append(desc_Label)
active_frame_elements.append(menu_label)
active_frame_elements.append(resize_Btn)
active_frame_elements.append(create_icon_Btn)


root.mainloop()
