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

# def __init__(self, master):  # All of the Tk widgit objects for the gui are created in the init constructor method, the init method takes the master parameter  
                                 # All handler methods are self contained within the class 
# self.label = ttk.Label(master, text = "Hello, Tkinter!")  #First widgit we create is a label, child of master, stored in a class variable so it can be accessed later so that we can change its text   
# self.label.grid(row = 0, column = 0, columnspan = 2)      #put into place using the grid command, puttin it where it belongs in the window
        
# ttk.Button(master, text = "Texas",
# command = self.texas_hello).grid(row = 1, column = 0) # Makes the Texas button and puts it in its proper place with the grid manager

# ttk.Button(master, text = "Hawaii",
# command = self.hawaii_hello).grid(row = 1, column = 1) # Makes the Hawaii button and puts it in its proper place with the grid manager
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

##
## Entering and displaying multiple lines with the text widget 
##

# Text widgit is similar to entry widgit
# Creates multi line area for text entry
# Good for free form text entry, like login or survey
# Wrap means how does the text get wrapped within the window, 'word' means it
# wraps after and before words where there are spaces.

# >>> from tkinter import *
# >>> root = Tk()
# >>> text = Text(root, width = 40, height = 10)
# >>> text.pack()
# >>> text.config(wrap = 'word')
# >>> text.get('1.0', 'end')
# 'This is a long message in the text box which is more than 40 characters. \n\n\n\n\n\n\n\nIf the message hits the bottom of the text box it will run off the screen. \n'
# >>> text.get('1.0', '1.end')
# 'This is a long message in the text box which is more than 40 characters. '
# >>> text.insert('1.0 + 2 lines', 'Inserted message')
# >>> text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore...')
# >>> text.delete('1.0')
# >>> text.delete('1.0', '1.0 lineend')
# >>> text.delete('1.0', '3.0 lineend + 1 chars')
# >>> text.replace('1.0', '1.0 lineend', 'This is the first line.')
# >>> text.config(state = 'disabled')
# >>> text.delete('1.0', 'end')
# >>> text.config(state = 'normal')

##
## Building a hierarchical treeview
##

# Can add buttons and images using this method

# >>> from tkinter import *
# >>> root = Tk()
# >>> text = Text(root, width = 40, height = 10)
# >>> text.pack()
# >>> text.config(wrap = 'word')
# >>> text.get('1.0', 'end')
# 'This is a long message in the text box which is more than 40 characters. \n\n\n\n\n\n\n\nIf the message hits the bottom of the text box it will run off the screen. \n'
# >>> text.get('1.0', '1.end')
# 'This is a long message in the text box which is more than 40 characters. '
# >>> text.insert('1.0 + 2 lines', 'Inserted message')
# >>> text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore...')
# >>> text.delete('1.0')
# >>> text.delete('1.0', '1.0 lineend')
# >>> text.delete('1.0', '3.0 lineend + 1 chars')
# >>> text.replace('1.0', '1.0 lineend', 'This is the first line.')
# >>> text.config(state = 'disabled')
# >>> text.delete('1.0', 'end')
# >>> text.config(state = 'normal')
# >>> text.tag_add('my_tag', '1.0', '1.0 wordend')
# >>> text.tag_configure('my_tag', background = 'yellow')
# >>> text.tag_remove('my_tag', '1.1', '1.3')
# >>> text.tag_ranges('my_tag')
# (<textindex object: '1.0'>, <textindex object: '1.1'>, <textindex object: '1.3'>, <textindex object: '1.4'>)
# >>> text.tag_names()
# ('sel', 'my_tag')
# >>> text.tag_names('1.0')
# ('my_tag',)
# >>> text.replace('my_tag.first', 'my_tag.last', 'That')
# >>> text.tag_delete('my_tag')
# >>> text.mark_names()
# ('insert', 'current', 'tk::anchor1')
# >>> text.insert('insert', '_')
# >>> text.mark_set('my_mark', 'end')
# >>> text.mark_gravity('my_mark', 'right')
# ''
# >>> text.mark_unset('my_mark')
 
##
## Adding columns and selecting items in the treeview
##

# Add additional columns to the treeview. Use bind method to capture specific event. 

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> treeview = ttk.Treeview(root)
# >>> treeview.pack()
# >>> treeview.insert('', '0', 'item1', text = 'First Item')
# 'item1'
# >>> treeview.insert('', '1', 'item2', text = 'Second Item')
# 'item2'
# >>> treeview.insert('', '2', 'item3', text = 'Third Item')
# 'item3'
# >>> logo = PhotoImage(file = 'C:\\Users\\James Clavelli\\Desktop\\Ex_Files_Python_Tkinter\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch05\\python_logo.gif').subsample(10,10)
# >>> treeview.insert('item2', 'end', 'python', text = 'Python', image = logo)
# 'python'
# >>> treeview.config(height = 5)
# >>> treeview.move('item2', 'item1', 'end')
# >>> treeview.item('item1', open = True)
# {}
# >>> treeview.item('item1', 'open')
# 1
# >>> treeview.detach('item3')
# >>> treeview.move('item3', 'item2', '0')
# >>> treeview.config(columns = ('version'))
# {}
# >>> treeview.column('#0', width = 150)
# {}
# >>> treeview.heading('version', text = 'Version')
# {}
# >>> treeview.set('python', 'version', '3.4.1')
# ''
# >>> treeview.item('python', tags = ('software'))
# ''
# >>> treeview.tag_configure('software', background = 'yellow')
# {}
# >>> def callback(event):
# 	print(treeview.selection())

	
# >>> treeview.bind('<<TreeviewSelect>>', callback)
# '48199000callback'
# >>> ('item2',)
# ('item3',)
# ('python',)
# ('item3',)
# ('python',)
# ('item3',)
# ('python',)
# ('item3',)
# ('python',)
# ('item3',)
# ('python',)
# ('item3', 'python')
# ('item3',)
# ('item3', 'python')
# ('item3',)
# ('item2',)
# ('item3',)
# ('python',)
# ('item3',)
# ('item3',)
# ('item3',)
# >>> treeview.config(selectmode = 'browse')
# >>> treeview.config(selectmode = 'none')
# >>> treeview.selection_add('python')
# >>> ('item3', 'python')
# ('item3', 'python')
# ('item3', 'python')
# >>> treeview.selection_toggle('python')
# >>> ('item3',)

##
## Building cascading menus 
##

# Dropdown menus are universally seen in programs with gui's
# Organizing and presenting actions to the user
# Don't let menus grow too long or become too deeply nested
# Always test drive guis 

# >>> from tkinter import *
# >>> root = Tk()
# >>> root.option_add('*tearOff', False)
# >>> menubar = Menu(root)
# >>> root.config(menu = menubar)
# >>> file = Menu(menubar)
# >>> edit = Menu(menubar)
# >>> help_ = Menu(menubar)
# >>> menubar.add_cascade(menu = file, label = 'File')
# >>> menubar.add_cascade(menu = edit, label = 'Edit')
# >>> menubar.add_cascade(menu = help_, label = 'Help')
# >>> file.add_command(label = 'New', command = lambda: print('New File'))
# >>> New File
# New File
# >>> file.add_separator()
# >>> file.add_command(label = 'Open...', command = lambda: print('Opening File...'))
# >>> file.add_command(label = 'Save', command = lambda: print('Save File'))
# >>> file.entryconfig('New', accelerator = 'Ctrl + N')
# >>> logo = PhotoImage(file = 'C:\\Users\\James Clavelli\\Desktop\\Ex_Files_Python_Tkinter\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch05\\python_logo.gif').subsample(10, 10)
# >>> file.entryconfig('Open...', image = logo, compound = 'left')
# >>> Opening File...

# >>> file.entryconfig('Open...', state = 'disabled')
# >>> file.delete('Save')
# >>> save = Menu(file)
# >>> file.add_cascade(menu = save, label = 'Save')
# >>> save.add_command(label = 'Save As', command = lambda: print('Saving As...'))
# >>> save.add_command(label = 'Save All', command = lambda: print('Saving All...'))
# >>> Saving As...

# >>> choice = IntVar()
# >>> edit.add_radiobutton(label = 'One', variable = choice, value = 1)
# >>> edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
# >>> edit.add_radiobutton(label = 'Three', variable = choice, value = 3)
# >>> file.post(400, 300)

##
## Drawing a basic line on the Canvas
##

# Space on which to draw shapes, images and other widgits
# Basic drawing space/diagram, to building custom widgit with look and feel

# >>> from tkinter import *
# >>> root = Tk()
# >>> canvas = Canvas(root)
# >>> canvas.pack()
# >>> canvas.config(width = 640, height = 480)
# >>> line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
# >>> canvas.itemconfigure(line, fill = 'green')
# >>> canvas.coords(line)
# [160.0, 360.0, 480.0, 120.0]
# >>> canvas.coords(line, 0, 0, 320,  240, 640, 0)
# []
# >>> canvas.itemconfigure(line, smooth = True)
# >>> canvas.itemconfigure(line, splinesteps = 5)
# >>> canvas.itemconfigure(line, splinesteps = 100)
# >>> canvas.itemconfigure(line, splinesteps = 1000)
# >>> canvas.itemconfigure(line, splinesteps = 10000)

##
## Drawing complex shapes on the Canvas
##

# Draw different shapes to the canvas, more complex then justl ines. 
# Canvas acts as geometry manager

# rect = canvas.create_rectangle(160, 120, 480, 360)
# canvas.itemconfigure(rect, fill = 'yellow')
# oval = canvas.create_oval(160, 120, 480, 360)
# arc = canvas.create_arc(160, 1, 480, 240)
# canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
# poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
# text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

# logo = PhotoImage(file = 'python_logo.gif') # Change path as needed
# image = canvas.create_image(320, 240, image = logo)

# canvas.lift(text)
# canvas.lower(image)
# canvas.lower(image, text)

# button = Button(canvas, text = 'Click Me')
# canvas.create_window(320, 60, window = button)

# canvas.itemconfigure(rect, tags = ('shape'))
# canvas.itemconfigure(oval, tags = ('shape', 'round'))
# canvas.itemconfigure('shape', fill = 'grey')
# print(canvas.gettags(oval))

# root.mainloop()

##
## Attaching scroll bars to widgets 
##

# Scroll-Enabled Widgits:
# X-Scroll text, canvas, treeview, entry (x only), spinbox(x only), combobox(x only)
# y-Scroll text, canvas, treeview 

# From the course

# >>> from tkinter import *
# >>> from tkinter import ttk
# >>> root = Tk()
# >>> text = Text(root, width = 40, height = 10, wrap = 'word')
# >>> text.grid(row = 0, column = 0)
# >>> scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
# >>> scrollbar.grid(row = 0, column = 1, sticky = 'ns')
# >>> text.config(yscrollcommand = scrollbar.set)

# Pre loaded from file

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
# xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
# yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
# canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

# canvas.grid(row = 1, column = 0)
# xscroll.grid(row = 2, column = 0, sticky = 'ew')
# yscroll.grid(row = 1, column = 1, sticky = 'ns')

# def canvas_click(event):
#     x = canvas.canvasx(event.x)
#     y = canvas.canvasy(event.y)
#     canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

# canvas.bind('<1>', canvas_click)

# root.mainloop()

##
## Configuring Widgit Styles  
##


# 10 Widgit states:
# active, disables, focus, pressed, selected, background, readonly, alternate
# invalid, hover. more info at: www.tkdocs.com/widgets/index.html

# When selecting themes:
# T + widget name, i.e., TButton, TFrame, etc.

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# button1 = ttk.Button(root, text = 'Button 1')
# button2 = ttk.Button(root, text = 'Button 2')      
# button1.pack()
# button2.pack()

# style = ttk.Style()

# print(style.theme_names())
# print(style.theme_use())
# style.theme_use('classic')
# style.theme_use('vista')

# print(button1.winfo_class())
# style.configure('TButton', foreground = 'blue')
# style.configure('Alarm.TButton', foreground = 'orange',
               #  font = ('Arial', 24, 'bold'))
# button2.configure(style = 'Alarm.TButton')
# style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                      #   ('disabled', 'grey')])
# button2.state(['disabled'])

# print(style.layout('TButton'))
# print(style.element_options('Button.label'))
# print(style.lookup('TButton', 'foreground'))

##
## Prompting users with the Messagebox and dialogs 
##

# Pop up message for problems
# Message box methods

# Three variations of the message box:
# showinfo()
# showwarning()
# showerror()
# askyesno()
# askokcancel()
# askretrycancel()
# askyesnocancel()
# askquestion()

# Filedialog Types

# askopenfile(mode)
# askopenfiles(mode)
# askopenfilename()
# askopenfilenames()

# >>> from tkinter import messagebox
# >>> messagebox.showinfo(title = 'A Friendly Message', message = 'Hello, Tkinter!')
# 'ok'
# >>> messagebox.askyesno(title = "Hungry?", message = "Do you want SPAM?")
# True
# >>> from tkinter import filedialog
# >>> filedialog.askopenfile()
# >>> filename = filedialog.askopenfile()
# >>> filename
# <_io.TextIOWrapper name='C:/Users/James Clavelli/Documents/GitHub/The-Tech-Academy-Course-Work/Python/python_databases_5.py' mode='r' encoding='cp1252'>
# >>> from tkinter import colorchooser
# >>> colorchooser.askcolor(initialcolor = '#FFFFFF')
# ((0.0, 128.5, 255.99609375), '#0080ff')

##
## 6. Geometry Management 
##

##
## Using the pack gemetry manager
##

# Pros
# pack() is the simplest to use
# Simplest to use, use when a widget is expanded to fill its entire parent
# Use to stack multiple widgits vertically or horizontally

# Cons
# Limited capability for complex layouts

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# label = ttk.Label(root, text = "Hello, Tkinter!",
#           background = 'yellow')
# label.pack(side = LEFT, anchor = 'nw')
# print(label)

# ttk.Label(root, text = "Hello, Tkinter!",
#           background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
# ttk.Label(root, text = "Hello, Tkinter!",
#           background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10) 


# for widget in root.pack_slaves():
#     widget.pack_configure(fill = BOTH, expand = True)
#     print(widget.pack_info()) # prints dictionaries with values related to packmanager

# label.pack_forget()
    
# root.mainloop()

##
## Using the grid geometry manager 
##

# For organizing widgits in 2 dimensions, the Grid Geometry Manager is a better choice

# Pros
# Easy to organize widgets in two dimensions
# Grid organizational style typical in modern GUI layouts

# Cons
# Slightly more involved than pack Geometry Manager 

# Planning your GUI:
# Plan how you'll lay them out ahead of time, like wire framing a web site

# grid_slaves(), grid_configure(), grid_info(), grid_forget()

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# root.rowconfigure(0, weight = 1)
# root.rowconfigure(1, weight = 3)

# root.columnconfigure(2, weight = 1)

# ttk.Label(root, text = "Yellow",
#           background = "yellow").grid(row = 0, column = 2, rowspan = 2, stick = 'nsew')
# ttk.Label(root, text = "Blue",
#           background = "blue").grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')
# ttk.Label(root, text = "Green",
#           background = "green").grid(row = 0, column = 0, stick = 'nsew', padx = 10, pady = 10)
# ttk.Label(root, text = "Orange",
#           background = "orange").grid(row = 0, column = 1, stick = 'nsew', ipadx = 25, ipady = 25)

# root.mainloop()

##
## Using the Grid Geometry Manager 
##

# When app requires exact control of placement, use place manager
# Specify location and size of widgit in absolute and relative terms

# Pros
# Provides exact control of widget location and size
# Describe location in absolute and/or relative terms
# Provides exact control

# Cons
# Difficult to manage a large number of widgets
# **Use place manager for specialized pieces of GUI's which is placed inside of a frame

# Other Grid Methods:
# place_slaves(), place_configure(), place_info(), place_forget()

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# root.geometry('640x480+200+200')

# ttk.Label(root, text = "Yellow", background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
# ttk.Label(root, text = "Blue",
#           background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
# ttk.Label(root, text = "Green",
#           background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
# ttk.Label(root, text = "Orange",
#           background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

# root.mainloop()

##
## 7. Event Handling
##

##
## Configuring command callbacks 
##

# Events need to do things. Don't make useless buttons!

# Lambda: creates an anonymous function creating the callback function ... huh?

# Button
# Checkbutton
# Radiobutton
# Spinbox
# Scale
# Scrollbar

##
## Binding to Keyboard Events 
##

# Trigger events based on events from the mouse or keyboard.
# ButtonPress, Button

# from tkinter import *
# from tkinter import ttk        


# root = Tk()

# def callback(number):
#     print(number)

# ttk.Button(root, text = "Click Me 1", command = lambda: callback(1)).pack()  
# ttk.Button(root, text = "Click Me 2", command = lambda: callback(2)).pack()
# ttk.Button(root, text = "Click Me 3", command = lambda: callback(3)).pack()

# root.mainloop()

##
## Binding to keyboard events 
##

# Callbacks only available for specific actions
# Tkinter can bind to events with specific handlers
# There's a wide variety of event types
# Addt'l events: ButtonPress, ButtonRelease, Enter, Leave, Motion, KeyPress
# KeyRelease, FocusIn, FocusOut

# Event Format          |        Event Description
# <Key>, <KeyPress>              User pressed any key
# <KeyPress-Delete>              User pressed Delete key
# <KeyRelease-Right>             User released Right Arrow key

# Keyboard Events
# Event Format                 |                   Event Description
# a,b,c,1,2,3,etc.... and               User Pressed a "printable" key
# <space>, <less>
# <Shift_L>, <Control_R>, <F5>,         User pressed a "special" key
# <Up>
# <Return>                              User pressed the Enter key
# <Control-Alt-Next>                    User pressed Ctrl+Alt+Page down keys

# add argument to Lambda function     'lambda e:' the e is an argument 

# The exercise in this section is really interesting, as each key press
# reveals information about the key in the IDLE gui

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# def key_press(event):
#     print('type: {}'.format(event.type))
#     print('widget: {}'.format(event.widget))
#     print('char: {}'.format(event.char))
#     print('keysym: {}'.format(event.keysym))
#     print('keycode: {}'.format(event.keycode))

# def shortcut(action):
#     print(action)


# root.bind('<Control-c>', lambda e: shortcut('Copy'))
# root.bind('<Control-v>', lambda e: shortcut('Paste'))

# root.mainloop()

##
## Binding to Mouse Events 
##

# Mouse buttons are 1, 2, 3 1 is left click, 2 is scroll, 3 is right click

# Made a drawing application:

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# def mouse_press(event):
#     global prev
#     prev = event
#     print('type: {}'.format(event.type))
#     print('widget: {}'.format(event.widget))
#     print('num: {}'.format(event.num))
#     print('x: {}'.format(event.x))
#     print('y: {}'.format(event.y))
#     print('x_root: {}'.format(event.x_root))
#     print('y_root: {}'.format(event.y_root))


# canvas = Canvas(root, width = 640, height = 480, background = 'white')
# canvas.pack()

# def draw(event):
#     global prev
#     canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
#     prev = event

# canvas.bind('<ButtonPress>', mouse_press)
# canvas.bind('<B1-Motion>', draw)

# root.mainloop()

##
## Binding to Virtual Events
##

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# entry = ttk.Entry(root)
# entry.pack()

# entry.bind('<<Copy>>', lambda e: print('Copy'))
# entry.bind('<<Paste>>', lambda e: print('Paste'))

# entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
# entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

# print(entry.event_info('<<OddNumber>>'))

# entry.event_generate('<<OddNumber>>')
# entry.event_generate('<<Paste>>')

# entry.event_delete('<<OddNumber>>')

# root.mainloop()

##
## Binding to multiple events
##

# from tkinter import *
# from tkinter import ttk        
    
# root = Tk()

# label1 = ttk.Label(root, text = 'Label 1')
# label2 = ttk.Label(root, text = 'Label 2')
# label1.pack()
# label2.pack()

# label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label1'))
# label1.bind('<1>', lambda e: print('<1> Label'))

# root.bind('<1>', lambda e: print('<1> Root'))

# label1.unbind('<1>')
# label1.unbind('<ButtonPress>')

# root.bind_all('<Escape>', lambda e: print("Escape!"))

# root.mainloop()

##
## 8. Building an Application 
##

##
## Defining project requirements
##

##
## Planning the Design
##

##
## Creating the widgets
##

# from tkinter import *
# from tkinter import ttk

# class Feedback:

#     def __init__(self, master):    

#         self.frame_header = ttk.Frame(master)

#         self.logo = PhotoImage(file = 'tour_logo.gif')
#         ttk.Label(self.frame_header, image = self.logo)
#         ttk.Label(self.frame_header, text = "Thanks for Exploring!")
#         ttk.Label(self.frame_header, text = ("We're glad you chose Explore California for your recent adventure. "
                                             "Please tell us what yo uthought about the 'Desert to Sea' tour."))
        

#         self.frame_content = ttk.Frame(master)

#         ttk.Label(self.frame_content, text = 'Name:')
#         ttk.Label(self.frame_content, text = 'Email:')
#         ttk.Label(self.frame_content, text = 'Comments:')

#         self.entry_name = ttk.Entry(self.frame_content, width = 24)
#         self.entry_email = ttk.Entry(self.frame_content, width = 24)

#         self.text_comments = Text(self.frame_content, width = 50, height = 10)

#         ttk.Button(self.frame_content, text = 'Submit')
#         ttk.Button(self.frame_content, text = 'Clear')
        
        
            
# def main():            
    
#     root = Tk()
#     feedback = Feedback(root)
#     root.mainloop()
    
# if __name__ == "__main__": main()


##
## Laying out of the widgets 
##

# from tkinter import *
# from tkinter import ttk

# class Feedback:

#     def __init__(self, master):    

#         self.frame_header = ttk.Frame(master)
#         self.frame_header.pack()
        
#         self.logo = PhotoImage(file = 'tour_logo.gif')
#         ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
#         ttk.Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
#         ttk.Label(self.frame_header, wraplength = 300,
#                   text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

#         self.frame_content = ttk.Frame(master)
#         self.frame_content.pack()
        
#         ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

#         self.entry_name = ttk.Entry(self.frame_content, width = 24)
#         self.entry_email = ttk.Entry(self.frame_content, width = 24)
#         self.text_comments = Text(self.frame_content, width = 50, height = 10)

#         self.entry_name.grid(row = 1, column = 0, padx = 5)
#         self.entry_email.grid(row = 1, column = 1, padx = 5)
#         self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

#         ttk.Button(self.frame_content, text = 'Submit').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
#         ttk.Button(self.frame_content, text = 'Clear').grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

# def main():            
    
#     root = Tk()
#     feedback = Feedback(root)
#     root.mainloop()
    
# if __name__ == "__main__": main()

##
## Binding to events
##

# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

# class Feedback:

#     def __init__(self, master):    

#         self.frame_header = ttk.Frame(master)
#         self.frame_header.pack()
        
#         self.logo = PhotoImage(file = 'tour_logo.gif')
#         ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
#         ttk.Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
#         ttk.Label(self.frame_header, wraplength = 300,
#                   text = ("We're glad you chose Explore California for your recent adventure.  "
#                           "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

#         self.frame_content = ttk.Frame(master)
#         self.frame_content.pack()
        
#         ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

#         self.entry_name = ttk.Entry(self.frame_content, width = 24)
#         self.entry_email = ttk.Entry(self.frame_content, width = 24)
#         self.text_comments = Text(self.frame_content, width = 50, height = 10)

#         self.entry_name.grid(row = 1, column = 0, padx = 5)
#         self.entry_email.grid(row = 1, column = 1, padx = 5)
#         self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

#         ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
#         ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

#     def submit(self):
#         print('Name: {}'.format(self.entry_name.get()))
#         print('Email: {}'.format(self.entry_email.get()))
#         print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
#         self.clear()
#         messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
                            
#     def clear(self):
#         self.entry_name.delete(0, 'end')
#         self.entry_email.delete(0, 'end')
#         self.text_comments.delete(1.0, 'end')

# def main():            
    
#     root = Tk()
#     feedback = Feedback(root)
#     root.mainloop()
    
# if __name__ == "__main__": main()

##
## Finishing the GUI with style
##

# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

# class Feedback:

#     def __init__(self, master):    

#         self.frame_header = ttk.Frame(master)
#         self.frame_header.pack()
        
#         self.logo = PhotoImage(file = 'tour_logo.gif')
#         ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
#         ttk.Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
#         ttk.Label(self.frame_header, wraplength = 300,
#                   text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

#         self.frame_content = ttk.Frame(master)
#         self.frame_content.pack()
        
#         ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
#         ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

#         self.entry_name = ttk.Entry(self.frame_content, width = 24)
#         self.entry_email = ttk.Entry(self.frame_content, width = 24)
#         self.text_comments = Text(self.frame_content, width = 50, height = 10)

#         self.entry_name.grid(row = 1, column = 0, padx = 5)
#         self.entry_email.grid(row = 1, column = 1, padx = 5)
#         self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

#         ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
#         ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

#     def submit(self):
#         print('Name: {}'.format(self.entry_name.get()))
#         print('Email: {}'.format(self.entry_email.get()))
#         print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
#         self.clear()
#         messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
                            
#     def clear(self):
#         self.entry_name.delete(0, 'end')
#         self.entry_email.delete(0, 'end')
#         self.text_comments.delete(1.0, 'end')

# def main():            
    
#     root = Tk()
#     feedback = Feedback(root)
#     root.mainloop()
    
# if __name__ == "__main__": main()







