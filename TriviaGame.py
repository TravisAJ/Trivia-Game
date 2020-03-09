#!/usr/bin/python3
# Taffea Avenevoli and Daisy Arnold
# 03/09/20

#------------------ IMPORTS ------------------
import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

'''Trivia Game Program'''

#------------- CONSTANTS -------------
TITLE_FONT = ("Times New Roman", 24)
LABEL_FONT = ("Times New Roman", 18)
BUTTON_FONT = ("Arial", 18)
CHOICE_FONT = ("Arial", 16)

#----- SCREEN CLASS -----
class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)
    def switch_frame():
        screens[Screen.current].tkraise()
        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.lbl_welcome = tk.Label(self, text = "Welcome to Trivia Game!", font = TITLE_FONT)
        self.lbl_welcome.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_play = tk.Button(self, text = "PLAY", font = BUTTON_FONT, command = self.go_play)
        self.btn_play.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_scores = tk.Button(self, text = "SCORES", font = BUTTON_FONT, command = self.go_score)
        self.btn_scores.grid(row = 1, column = 1, sticky = "news")
    
    def go_play(self):
        pass
    
    def go_score(self):
        pass

class SelectMenu(Screen):
    pass

class QuestionMenu(Screen):
    pass

class ScoreMenu(Screen):
    pass
        

#---------- MAIN ----------
if __name__ == "__main__":
    games = {}
    root = tk.Tk()
    root.title("Trivia Game")
    
    screens = [MainMenu(), SelectMenu(), QuestionMenu(), ScoreMenu()]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")
    #screens[1].grid(row = 0, column = 0, sticky = "news")
    #screens[2].grid(row = 0, column = 0, sticky = "news")
    #screens[3].grid(row = 0, column = 0, sticky = "news")

    root.grid_columnconfigure(1, weight = 1)
    root.grid_rowconfigure(1, weight = 1)

main = screens[0]
main.tkraise()

root.mainloop()