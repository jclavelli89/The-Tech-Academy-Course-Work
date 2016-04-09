##
## Python GUI Development with Tkinter
##

##
## 1. Getting Started with Tkinter
##

##
## Saying hello to Tkinter
##


# from tkinter import *

# root = Tk()                                #Calls TK constructor method to create a new, top-level widgit
# Label(root, text="Hello, Tkinter!").pack() # create a Label with the text Hello Tkinter with the .pack() geometry management method 
# root.mainloop()                            # run the mainloop() method for the root window 

##
## 2. Tkinter Concepts
##

##
## Tk and Tkinter background 
##

# Open source toolkit used to develop Graphical User Interfaces. Provides a library
# of interactive widgits commonly used in desktop apps, like buttons, etc.

##
## Creating and configuring widgets 
##

# Widgits are controls you see that you can use to interact with a program like buttons
# and text entry fieds. They can also be used to display information to a user, like
# simple text or a complex graphic. They're define as a class in TKinter.
# You create individual objects for each widget. Widgets have parents in a hierarchy
# The parent widgit is the geography manager. 

# >>> from tkinter import *                                 #The * inputs all functions/variables from Tkinter package
# >>> from tkinter import ttk                               #Imports the themed widgits from TTK
# >>> root = Tk()                                           # Instantiates the TK class
# >>> button = ttk.Button(root, text = 'Click Me')          # button saved in a button variable, root is the parent, text of the button is next. 
# >>> button.pack()                                         # In order to add a created (it was created above) widgit into a window, you need to use pack()
# >>> button['text']                                        # using butt['text'] returns the text value of that button which in this case is Click me
# 'Click Me'
# >>> button['text'] = 'Press Me'                           # Can also be used in this manner to change the text name 
# >>> button.config(text = 'Push Me')                       # config allows you to modify an object in general, you then specify the property you'd like to change 
# >>> button.config()                                       # config method is using keyword arguments, which are stored in a dictionary within the widgit object, to modify properties of that object, by just hitting config on that object like was done here, you see all of the items in that dictionary that you can change  
# {'width': ('width', 'width', 'Width', '', ''), 'takefocus':
#  ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'),
#  'image': ('image', 'image', 'Image', '', ''), 'style':
#  ('style', 'style', 'Style', '', ''), 'padding':
#  ('padding', 'padding', 'Pad', '', ''), 'state':
#  ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>),
#  'text': ('text', 'text', 'Text', '', 'Push Me'), 'default':
#  ('default', 'default', 'Default', <index object: 'normal'>,
#   <index object: 'normal'>), 'command':
#  ('command', 'command', 'Command',
#   <bytecode object: ''>, <bytecode object: ''>),
#  'underline': ('underline', 'underline', 'Underline', -1, -1),
#  'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
#  'class': ('class', '', '', '', ''), 'cursor':
#  ('cursor', 'cursor', 'Cursor', '', ''), 'compound':
#  ('compound', 'compound', 'Compound', <index object: 'none'>,
#   <index object: 'none'>)}
# >>> str(button)                                           # Gives a unique integer assigned to that unique button
# '.50993872'
# >>> str(root)                                             # root is always given a special default name of '.'
# '.'
# >>> ttk.Label(root, text = 'Hello, Tkinter!').pack()      #ttk.Label means you're labeling a widgit, but without a variable you have no reference and thus can't change it.  
# >>> 

##
## Managing Widgit placement
##

# Geometry is very important because your windows need to be organized appropriately
# Three geography managers involved in Tk.
# Pack Geometry Manager, define edge of parent, good for simple problems: on top of each other, or side by side orientation
# Grid Geometry Manager, divides the master widgits area into a two dimensional table and places slave widgits into rows and columns
# Place Geometry Manager, explicitly set the position of a widgit using relative or absolute terms in the x and y direction
# Best suited for laying out widgits in very specific way that is not well suited to pack. or grid geometry mangers
# One geometry manager within a particular master, however, you can use more then one in a program

##
## Handling User Events
##

# Uses event handling to handle functions received from the mouse, keyboard, etc.
# For each event a handler method needs to be defined, the button pressing needs to be bind and sent to the handler function
# The mainloop() brings the program into the Event Loop which waits for an event to occur, which executes the appropriate handler code
# Only one event can occur at a time, otherwise events are on a que, keep your handler code short and quick!
# Configuring event handlers: Command callbacks via command property, tells what function to write when the command is pressed

##
## Revisiting Hello, Tkinter!
##



# from tkinter import *
# from tkinter import ttk

# class HelloApp:             #Writing the application as a Class, common practice 

#     def __init__(self, master):  # All of the Tk widgit objects for the gui are created in the init constructor method, the init method takes the master parameter  
                                 # All handler methods are self contained within the class 
#         self.label = ttk.Label(master, text = "Hello, Tkinter!")  #First widgit we create is a label, child of master, stored in a class variable so it can be accessed later so that we can change its text   
#         self.label.grid(row = 0, column = 0, columnspan = 2)      #put into place using the grid command, puttin it where it belongs in the window
        
#         ttk.Button(master, text = "Texas",
#                    command = self.texas_hello).grid(row = 1, column = 0) # Makes the Texas button and puts it in its proper place with the grid manager

#         ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1) # Makes the Hawaii button and puts it in its proper place with the grid manager
# In the bove you see that if the event is clicked it kicks in the below methods 
#     def texas_hello(self):
#         self.label.config(text = 'Howdy, Tkinter!')

#     def hawaii_hello(self):
#         self.label.config(text = 'Aloha, Tkinter!')

            
# def main():                         #This is the function that gets called by the program, this references the application      
    
#     root = Tk()                     # Tk Constructor method to make top level tk method
#     app = HelloApp(root)            # Master level
#     root.mainloop()                 # Mainloop brings on the event loop
    
# if __name__ == "__main__": main()   # Can be used by another Python program 


##
## 3. Basic Widgits
##

##
## Displaying text and images with labels  
##

# >>> from tkinter import *                        
# >>> from tkinter import ttk
# >>> root = Tk()                         #This activated the window, root is the name of the instance of ttk, technically can be named anything but root makes sense because it identifies it as the root element 
# >>> label = ttk.Label(root, text = "Hello, Tkinter!")   # the label is basically labeling the root 
# >>> label.pack()                                        #pack() gives it a space in geometry
# >>> label.config(text = "Howdy, Tkinter!")              # changes the text 
# >>> label.config(text = "Howdy, Tkinter! It\'s been a while since we last met. Great to see you again!")
# >>> label.config(wraplength = 150)                      #adjusts the size
# >>> label.config(justify = CENTER)                      # centers 
# >>> label.config(foreground = 'blue', background = 'yellow')    #font 
# >>> label.config(font = ( 'Courier', 18, 'bold'))               #font 
# >>> label.config(text = "Howdy,, Tkinter!")                   #change text 
# >>> PhotoImage(file = 'C:\\Users\\James Clavelli\\Desktop\\Ex_Files_Python_Tkinter\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch03\\python_logo.gif')
# <tkinter.PhotoImage object at 0x03325810> #adds image 
# >>> logo = PhotoImage(file = 'C:\\Users\\James Clavelli\\Desktop\\Ex_Files_Python_Tkinter\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch03\\python_logo.gif') #puts the image in a variable for more functionality 
# >>> label.config(image = logo)
# >>> label.config(compound = 'text')
# >>> label.config(compound = 'center')  #compound allows you to move the image and text so they both appear 
# >>> label.config(compound = 'left')
# >>> label.img = logo
# >>> label.config(image = label.img)

##
## Capturing input with buttons
##

# Labels are for show, buttons give the users interaction

# >>> from tkinter import ttk
# >>> root = Tk()
# >>> 
# >>> button = ttk.Button(root, text = "Click Me")
# >>> button.pack()
# >>> def callback():
# 	print('Clicked')

	
# >>> button.config(command = callback)
# >>> Clicked
# Clicked
# Clicked
# Clicked
# Clicked

# >>> button.invoke()
# Clicked
# 'None'
# >>> button.state(['disabled'])
# ('!disabled',)
# >>> button.instate(['disabled'])
# True
# >>> button.state(['!disabled'])
# ('disabled',)
# >>> Clicked
# Clicked
# Clicked
# Clicked
# Clicked
# Clicked

 
# >>> button.instate(['!disabled'])
# True
# >>> 
# >>> logo = PhotoImage(file = 'C:\\Users\\James Clavelli\\Desktop\\Ex_Files_Python_Tkinter\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch03\\python_logo.gif')
# >>> button.config(image = logo, compound = LEFT)
# >>> Clicked
# Clicked
# Clicked
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     Clicked
# NameError: name 'Clicked' is not defined
# >>> small_logo = logo.subsample(5, 5)
# >>> button.config(image = small_logo)
# >>> 

# In this section we learned, state, instate, invoke, config and subsample

##
## Presenting Choices with check buttons and radio buttons
##

# check button: slightly more advanced version of the basic button, can store binary value which makes them ideal for selecting or not selecting options from a series of choices (2 choices)
# radio button: similar because they maintain a value, but not limited to two choices, user can make one selection from a series of mutually exclusive options

# Tkinter Variable Classes that include change monitoring
# BooleanVar
# DoubleVar
# IntVar
# StringVar

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> checkbutton = ttk.Checkbutton(root, text = 'SPAM?' )
# >>> checkbutton.pack()
# >>> spam = StringVar()
# >>> spam.set('SPAM!')
# >>> spam.get()
# 'SPAM!'
# >>> checkbutton.config(variable = spam, onvalue = 'SPAM Please!', offvalue = 'Boo SPAM')
# >>> spam.get()
# 'SPAM Please!'
# >>> spam.get()
# 'Boo SPAM'
# >>> breakfast = StringVar()
# >>> ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
# >>> ttk.Radiobutton(root, text = 'Eggs', variable = breakfast, value = 'Eggs').pack()
# >>> ttk.Radiobutton(root, text = 'Sausage', variable = breakfast, value = 'Sausage').pack()
# >>> ttk.Radiobutton(root, text = 'SPAM', variable = breakfast, value = 'SPAM').pack()
# >>> 
# >>> breakfast.get()
# 'Sausage'
# >>> breakfast.get()
# 'SPAM'
# >>> checkbutton.config(textvariable = breakfast)
# >>>

# New methods:
# Checkbutton(), .set(), Radiobutton(),

##
## Entering Single-Line text with the Entry widget 
##

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> entry = ttk.Entry(root, width = 30)
# >>> entry.pack()
# >>> entry.get()
# 'Hello, Tkinter'
# >>> entry.delete(0, 1)
# >>> entry.delete(0, END)
# >>> entry.insert(0, 'Enter your password')
# >>> entry.config(show = '*')
# >>> entry.get()
# 'Enter your password'
# >>> entry.state(['disabled'])
# ('!disabled',)
# >>> entry.state(['!disabled'])
# ('disabled',)
# >>> entry.state(['readonly'])
# ('!readonly',)

# New methods:
# Entry(), get(), delete(), insert()

##
## Making selections with the combo box and spin box 
##

# When options increase use the combo and spin box
# combo box widgit: A basic drop down selection tool with lots of options and a drop down box.
# useful when your choices don't have a clear and rational order
# sping box: See one option at a time and cycle through avail options with arros.
# useful when you have a known order, link numbers in a row.

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> month = StringVar()
# >>> combobox = ttk.Combobox(root, textvariable = month)
# >>> combobox.pack()
# >>> combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
# 			      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# >>> month.get()
# 'Sep'
# >>> month.set('Mar')
# >>> month.set('Not a month')
# >>> month.get()
# 'Not a month'
# >>> month.get()
# 'Whatever they want to'
# >>> year = StringVar()
# >>> Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
# >>> year.get()
# '1993'
# >>> 

# New methods:
# Spingbox(), Combobox

##
## Inputting values and displaying status with the Scale and Progressbar widgets
##

# Provide feedback to user with progress bar

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
# >>> progressbar.pack()
# >>> progressbar.config(mode = 'indeterminate')
# >>> progressbar.start()
# >>> progressbar.stop()
# >>> progressbar.start()
# >>> progressbar.stop()
# >>> progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
# >>> progressbar.config(value = 8.0)
# >>> progressbar.step()
# >>> progressbar.step(5)
# >>> value = DoubleVar()
# >>> progressbar.config(variable = value)
# >>> scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)
# >>> scale.pack()
# >>> scale.set(4.2)
# >>> scale.get()
# 4.2
 
# New methods:
# Progressbar(), start(), stop(), Doublevar(), Scale()

##
## 4. Organizational Widgits 
##

##
## Organizing widgets with frames
##

# Framers are fundamental widgits for organizing a Tkinter GUI
# Frames act as parent and geometry manager to hold and organize other widgits
# Used to organize a large gui into small, more manageable sub regions.
# One frame for nav, one for user controls, one for displaying output
# Frame border: 6 different types of frame relief.
# Flat is default, raised (elevated or depressed), sunken, Solid, Ridge, Groove
# Added like this: frame.config(relief = RIDGE)
# When working with frames, make frame the parent, not root.
# Geometry management: pack() is the basic, when frame is in pack()
# when working WITHIN the frame, you can use grid() for more specific management

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> frame = ttk.Frame(root)
# >>> frame.pack()
# >>> frame.config(height = 100, width = 200)
# >>> frame.config(relief = RIDGE)
# >>> ttk.Button(frame, text = 'Click Me').grid()
# >>> frame.config(padding = (30, 15))
# >>> ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()
# >>> 

# New constructor methods:
# .Frame(), LabelFrame(), new property padding, use of grid() instead of pack(). 

##
## Creating additional top-level windows
##

# We can add additional windows with top level window widgit
# each is its on Tk widgit object which can be the parent and geometry manager for other widgite
# These are not part of the themed Tk widgit set, thus no import ttk

# window.geometry('WIDTHxHEIGHT+X+Y')
# The geometry method takes one parameter which is a string containing the
# new width and height in pixels as well as the new x and y location of the windows
# top left corner, relative to the top left corner of the string.
# Format: Width in pixels, x, Height in pixels, +, x position, +, y position

# >>> from tkinter import *
# >>> root = Tk()
# >>> window = Toplevel(root)
# >>> window.title('New Window')
# ''
# >>> window.lower()
# >>> window.lift(root)
# >>> window.state('zoomed')
# ''
# >>> window.state('withdrawn')
# ''
# >>> window.state('iconic')
# ''
# >>> window.state('normal')
# ''
# >>> window.state
# <bound method Wm.wm_state of <tkinter.Toplevel object .51587664>>
# >>> window.state('normal')
# ''
# >>> window.iconify()
# ''
# >>> window.deiconify()
# ''
# >>> window.geometry('640x480+50+100')
# ''
# >>> window.resizable(False, False)
# ''
# >>> window.maxsize(640, 480)
# >>> window.minsize(200, 200)
# >>> window.resizable(True, True)
# ''
# >>> root.destroy()
# >>> 

# New constructor methods and parameters:
# Toplevel(), title(), lower(), lift(), 'zoomed', 'withdrawn', 'iconic',
# 'normal', iconify(), deiconify(), geometry('WIDTHxHEIGHT+X+Y'),
# resizable(True/False, True/False), maxsize(), minsize()

##
## Separating widgets within paned windows 
##

# The paned window is a geometry management widgit which can hold other widgits
# by stacking them vertically or horizontally
# It displays a divider between each widgit which the user can click and drag
# to adjust the relative size of the widgit within the window.

# adding the weight property allows the two windows to scale relative to one another


# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
# >>> panedwindow.pack(fill = BOTH, expand = True)
# >>> frame1 =ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
# >>> frame2 =ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
# >>> panedwindow.add(frame1, weight = 1)
# >>> panedwindow.add(frame2, weight = 4)
# >>> frame3 =ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
# >>> panedwindow.insert(1, frame3)
# >>> panedwindow.forget(1) 

# New constructor methods and parameters:
# Pandedwindow(root, orient = horizontal/vertical), parameters for pack(fill, expand = true/false)
# .Frame(parent, width, height, relief), add(frame, weight), insert(index, frame), forget()

##
## Grouping widgeting within a tabbed notebook 
##

# Making tabs like a browser using the notebook widgit.

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> notebook = ttk.Notebook(root)
# >>> notebook.pack()
# >>> frame1 = ttk.Frame(notebook)
# >>> frame2 = ttk.Frame(notebook)
# >>> notebook.add(frame1, text = 'One')
# >>> notebook.add(frame2, text = 'Two')
# >>> ttk.Button(frame1, text = 'Click Me').pack()
# >>> frame3 = ttk.Frame(notebook)
# >>> notebook.insert(1, frame3, text = 'Three')
# >>> notebook.forget(1)
# >>> notebook.add(frame3, text = 'Three')
# >>> notebook.select()
# '.51124944.53631120'
# >>> notebook.index(notebook.select())
# 1
# >>> notebook.select(2)
# ''
# >>> notebook.tab(1, state = 'disabled')
# {}
# >>> notebook.tab(1, state = 'hidden')
# {}
# >>> notebook.tab(1, state = 'normal')
# {}
# >>> notebook.tab(1, 'text')
# 'Two'
# >>> notebook.tab(1)
# {'compound': 'none', 'sticky': 'nsew', 'padding': [0], 'underline': -1, 'text': 'Two', 'image': '', 'state': 'normal'}
 
# New constructor methods and parameters:
# Notebook(), .index(what you're looking for the index of), .tab(), punching
# the index into notebook.tab(1) to reveal its properties.

##
## 5. Advanced Widgits
##

##
## Entering and displaying multiple lines with the Text widget 
##

# Similar to the entry widgit, it creates multi line area for text entry
# useful for things like surveys and comment boxes or login windows.
# powerful and complex, used for simple login into interactive code editor
# like IDLE.

# >>> from tkinter import *
# >>> root = Tk()
# >>> text = Text(root, width = 40, height = 10)
# >>> text.pack()
# >>> text.config(wrap = 'word')
# >>> text.get('1.0', 'end')
# 'This is a long message in the text box which is more than 40 characters.\n\n\n\n\n\n\n\nIf the message hits the bottom of the text box it will run off the screen.\n'
# >>> text.get('1.0', '1.end')
# 'This is a long message in the text box which is more than 40 characters.'
# >>> text.insert('1.0 + 2 lines', 'inserted message')
# >>> text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore...')
# >>> text.delete('1.0')
# >>> text.delete('1.0', '1.0 lineend')
# >>> text.delete('1.0', '3.0 lineend + 1 chars')
# >>> text.replace('1.0', '1.0 lineend', 'This is the first line.')
# >>> text.config(state = 'disables')
# >>> text.config(state = 'disabled')
# >>> text.delete('1.0', 'end')
# >>> text.config(state = 'normal')
# >>> 

##### Rewatch this video 
































