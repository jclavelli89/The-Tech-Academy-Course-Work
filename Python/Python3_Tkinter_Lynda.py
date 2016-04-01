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

 





















