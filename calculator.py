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


answerVariableGlobal = ""
answerLabelForSquareRoot = ""

def changeAnswerEntryLabel(entry):
    global answerVariableGlobal
    global answerLabelForSquareRoot
    
    answerVariableGlobal = answerVariableGlobal + str(entry)
    answerLabelForSquareRoot = answerVariableGlobal
    answerEntryLabel.set(answerVariableGlobal)
    
def allClear():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerVariableGlobal = ""
    answerLabelForSquareRoot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")
    
def clearAnswerEntryLabel():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerLabelForSquareRoot = answerVariableGlobal
    answerVariableGlobal = ""
    answerEntryLabel.set(answerVariableGlobal)
    
def evaluateAnswer():
    global answerVariableGlobal
    try:
       eval(answerVariableGlobal)
       evaluatedValueAnswerLabelGlobal= str(eval(answerVariableGlobal) )   # This line should be alligned                 properly without any indentation error
       clearAnswerEntryLabel()
       answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)
#Here we are handling the error when the expression has some SyntaxError or for that matter any Error.
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")
        
        
def evaluateSquareRoot():
    global answerVariableGlobal
    global answerLabelForSquareRoot
    try:
        sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answerVariableGlobal)))
            clearAnswerEntryLabel()
            answerFinalLabel.set(sqrtAnswer)
#Error Handling  
        except(ValueError,SyntaxError,
               TypeError,ZeroDivisionError):
            clearAnswerEntryLabel()
            answerFinalLabel.set("Error!")                
        

root.mainloop()
