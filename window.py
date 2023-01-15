from tkinter import *

class window:
    def __init__(self,capture) -> None:
        self.root = Tk()
        self.root.title('Simple Calculator')
        self.displayLabel = Entry(self.root, borderwidth = 5, width = 25)
        self.displayLabel.grid(row = 0,column = 0, columnspan=3, padx = 10, pady = 10)
        self.buttons = {}
        self.___initButtons__(capture)
        self.root.resizable(0,0)
        return
    

    def ___initButtons__(self, operations):
        # Tuple shows (value, row, column, padx, pady, rowspan,columnspan, command)
        btnValues = [('0',4,1,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'0')), 
                     ('1',3,0,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'1')), 
                     ('2',3,1,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'2')), 
                     ('3',3,2,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'3')), 
                     ('4',2,0,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'4')), 
                     ('5',2,1,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'5')), 
                     ('6',2,2,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'6')), 
                     ('7',1,0,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'7')), 
                     ('8',1,1,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'8')), 
                     ('9',1,2,45,20,1,1,lambda: operations.UpdateDisplayLabel(self.displayLabel,'9')), 
                     ('C',4,2,45,20,1,1,lambda:operations.ClearDisplayLabel(self.displayLabel)), 
                     ('=',5,1,95,20,1,2,lambda:operations.GetOutput(self.displayLabel)), 
                     ('+',4,0,45,50,2,1,lambda:operations.Addition(self.displayLabel))]
        
        for (val,rowNum,colNum,padX,padY,rowSpan,columnSpan,opr) in btnValues:
            self.buttons[val] = Button(self.root, text = val,padx = padX,pady = padY, command = opr)
            self.buttons[val].grid(row = rowNum, column=colNum, rowspan = rowSpan, columnspan=columnSpan)
        return 