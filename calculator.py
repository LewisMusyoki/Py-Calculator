from tkinter import *
import math

root = Tk() #Instantiate and assign to a var 'root'
root.title('Calculator App') #Set the title of application window

#answerEntryLabel
answerEntryLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerEntryLabel,
justify = LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
#answerFinalLabel
answerFinalLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerFinalLabel,
justify = LEFT, height=2, width=7).grid(columnspan = 4 , ipadx=120)

def createButton(txt,x,y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAnswerEntryLabel(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)
#buttons list stores the button values to be incoroporated in the calculator for first 4 rows
buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
#buttonsListTraversalCounter is used to traverse across the buttons list
buttonsListTraversalCounter = 0
#The for loop to create buttons for the application
for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1
        
        
#Button for SquareRoot
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "√",
       command = lambda:evaluateSquareRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)
#Button for AC button - clear the workspace
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)
#Button for value 0 - have 2 columnspace and different dimensions
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAnswerEntryLabel(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)
#Button for "=" - final calc button
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evaluateAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)




        

root.mainloop()
