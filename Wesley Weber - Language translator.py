# This is my attempt at creating a language translator - Wesley Weber

# This is based of the following article:
# https://techvidvan.com/tutorials/python-language-translator/

#### - Using my understanding of the packages and code, i am trying to create my own spin of this translator - ####

# first i have to import "tkinter" and "translate".

# tkinter is used to create GUI(Graphical User interface) for you code.
# Importing all the packages from "tkinter"
from tkinter import *
from tkinter import font
from tkinter.ttk import Label

# translate is a package used to translate major langueages
from translate import Translator

# Creating the interface window for the user to select options (language to translate to and from)
Screen = Tk()
# Set window size
Screen.geometry("700x150")
# Set window color
Screen.configure(bg='blue')
# Window title
Screen.title("WEZ TRANSLATOR!")

# This will store the language of the text that is being translated.
InputLanguageChoice = StringVar()

# This will store the language in which the text is to be translated.
TranslateLanguageChoice = StringVar()

# List of language choices that can be selected to translate
LanguageChoices = {'Hindi','English','French','German','Spanish','Afrikaans'}

# Both these defaults can be changed to either of the languages in the list above.
# This is the default language where text will be imputed to be tranlated
InputLanguageChoice.set('English')
# This is the default language where the input will be translated to
TranslateLanguageChoice.set('Hindi')

#Define all the functions:
# The following function will translate text:
def Translate():
    # Getting the "InputLanguageChoice" data and the "TranslateLanguageChoice" so it can be translated 
    # from_lang : It is the language of the text that is being translated.
    # to_lang: It is the language of the text in which the text is to be translated.
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    # TextVar is a variable that contains the text that is to be translated.
    Translation = translator.translate(TextVar.get())
    # Stores the translated text
    OutputVar.set(Translation)


# This will be the internal text for my GUI 
# This will allow users to select things

# choice for input language
# This is for the dropdown list of languages to choose from in the GUI
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)

# Label(): This widget helps to implement display boxes where the text can be placed.
# grid(): Widgets are arranged on the screen with the help of grid.
Label(Screen,text="Choose a Language",font="bold",foreground="red").grid(row=0,column=1)
# pad x or y allows me to put spaces between labels or buttons
InputLanguageChoiceMenu.grid(row=1,column=1,padx=10, pady=10)
 
# choice in which the language is to be translated
# This is for the dropdown list of languages to choose from in the GUI
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)

# Label(): This widget helps to implement display boxes where the text can be placed.
# grid(): Widgets are arranged on the screen with the help of grid.
Label(Screen,text="Translated Language",font="bold",foreground="red").grid(row=0,column=5)
# pad x or y allows me to put spaces between labels or buttons
NewLanguageChoiceMenu.grid(row=1,column=5,padx=10, pady=10)

# The following will be for the input and output text:
# This will allow users to enter things

# Entry(): This widget helps to enter or display a single line text on the screen.
#### font = : this allows me to edit the font of the labels ####
Label(Screen,text="Enter Text",font="bold",).grid(row=2,column =0)
TextVar = StringVar()
#### width = : allows me to set how long the text box is
TextBox = Entry(Screen,textvariable=TextVar,width="30").grid(row=2,column = 1)
 
#### font = : this allows me to edit the font of the labels ####
Label(Screen,text="Output Text",font="bold").grid(row=2,column =5)
OutputVar = StringVar()
#### width = : allows me to set how long the text box is
TextBox = Entry(Screen,textvariable=OutputVar,width= "30").grid(row=2,column = 6)
 
# Button for calling function
# Button(): This widget creates a button.
# relief: It helps to provide 3-D effects around the outside of the widget.
#### font = : this allows me to edit the font of the labels ####
B = Button(Screen,text="Translate!",font="bold",foreground="green",command=Translate, relief = GROOVE).grid(row=5,column=2,columnspan =2,padx = 10,pady = 10)


# mainloop(): It helps to run the tkinter event loop.
Screen.mainloop()










