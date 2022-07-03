#Importing modules
import glob
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from path import Path
import imageio

#Function to convert Images to GIF
def convertToGIF():
    path = direc.get() #Get the path of the folder entered by the user
    ext=extension.get() #Get the extension png or jpeg 
    path_in =path+'/*.'+ext #Creating the final path of the images
    path_out = path+"/MyGif.gif" #Creating the path for GIF in the same folder as the images
     
    imgs=[] #list to store all the images
    try:
        file = glob.glob(path_in, recursive = True) #Recursively getting the paths of all the images in the folder
        for im in file:
            imgs.append(imageio.imread(im)) #Reading all the images

        imageio.mimsave(path_out, imgs) #Converting the images to GIF and saving it
        #Showing the message box on saving the gif
        messagebox.showinfo("DataFlair GIF Generator","GIF is saved successfully in the folder with Images!")
    except: 
        #Showing a message if not able to collect the images or convert them to gif
        messagebox.showinfo("Error occured!","Please check the path of the folder or the extension of images.")

#Creating the window 
wn = Tk() 
wn.title("DataFlair GIF Creator")
wn.geometry('500x300')
wn.config(bg='azure')

#Creating the variables to get the path of folder and the extension of images
extension = StringVar(wn)
direc=StringVar(wn)

#The main label
Label(wn, text='DataFlair GIF Creator',bg='azure',
  fg='black', font=('Times', 20,'bold')).place(x=60, y=10)

#Getting the extension of the image as either png or jpeg
Label(wn, text='Please select the extension of the images',bg='azure2', anchor="e", justify=LEFT).place(x=20, y=70)

Radiobutton(wn, text='png',bg='azure2', variable=extension, value='png').place(x=50,y=100) 
Radiobutton(wn, text='jpeg',bg='azure2',variable=extension, value='jpeg').place(x=150,y=100) 

#Getting the path of the folder with the images
Label(wn, text='Please enter the folder location where images exist',bg='azure2', anchor="e", justify=LEFT).place(x=20, y=130)

Entry(wn,textvariable=direc, width=35, font=('calibre',10,'normal')).place(x=200,y=160)

#Button to convert the images into GIF and save the GIF
Label(wn, text='Please click the button to get the GIF', bg='azure2',anchor="e", justify=LEFT).place(x=20, y=190)

Button(wn, text="Click Me", bg='ivory3',font=('calibre', 13),
   command=convertToGIF).place(x=230, y=220)

#Runs the window till it is closed by the user
wn.mainloop()
