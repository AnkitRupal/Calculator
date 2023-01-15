from tkinter import *

class capture:
    def __init__(self) -> None:
        self.nums = []
        return 


    def UpdateDisplayLabel(self,displayLabel,val) -> None:
        idx = displayLabel.index(INSERT)
        displayLabel.insert(index = idx, string = str(val))
        return 


    def ClearDisplayLabelText(self, displayLabel) -> None:
        displayLabel.delete(0, len(displayLabel.get()))
        return 


    def ClearDisplayLabel(self,displayLabel) -> None:
        self.ClearDisplayLabelText(displayLabel)
        self.resetNums()
        return 


    def resetNums(self) -> None:
        self.nums = []
        return


    def Addition(self,displayLabel) -> None:
        self.nums.append(int(displayLabel.get()))
        self.ClearDisplayLabelText(displayLabel)
        return 


    def GetOutput(self,displayLabel) -> None:
        self.nums.append(int(displayLabel.get()))
        self.ClearDisplayLabelText(displayLabel)
        self.UpdateDisplayLabel(displayLabel,str(sum(self.nums)))
        self.resetNums()
        return 