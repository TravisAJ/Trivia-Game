#!/usr/bin/python3
# Taffea Avenevoli and Daisy Arnold
# 03/09/20

#------------------ IMPORTS ------------------
import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as Scr
from tkinter import messagebox

'''Trivia Game Program'''

#------------- CONSTANTS -------------
TITLE_FONT = ("Times New Roman", 24)
LABEL_FONT = ("Times New Roman", 18)
BUTTON_FONT = ("Arial", 18)
CHOICE_FONT = ("Arial", 16)
SCROLL_FONT = ("Times New Roman", 16)
HEADER_BG = "#76747A"
HEADER_FG = "#DEDAE6"


#----- SCREEN CLASS -----
class Screen(tk.Frame):
    current = 0
    option = ""
    category = ""
    def __init__(self):
        tk.Frame.__init__(self)
    def switch_frame():
        screens[Screen.current].tkraise()

#----- MAIN MENU CLASS -----        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.grid_rowconfigure(0, weight=20)
        self.grid_rowconfigure(1, weight=1)
        
        self.lbl_welcome = tk.Label(self, text = "Welcome to Trivia Game!", font = TITLE_FONT)
        self.lbl_welcome.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_play = tk.Button(self, text = "PLAY", font = BUTTON_FONT, command = self.go_play)
        self.btn_play.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_scores = tk.Button(self, text = "SCORES", font = BUTTON_FONT, command = self.go_score)
        self.btn_scores.grid(row = 1, column = 2, sticky = "news")
    
    def go_play(self):
        Screen.option = "play"
        Screen.current = 1
        Screen.switch_frame()
    
    def go_score(self):
        Screen.option = "score"
        Screen.current = 1
        Screen.switch_frame()

#----- SELECT MENU CLASS -----
class SelectMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_select = tk.Label(self, bg = HEADER_BG, fg = HEADER_FG, text = "Select a Category", font = TITLE_FONT)
        self.lbl_select.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_history = tk.Button(self, text = "HISTORY", font = BUTTON_FONT, command = self.go_history)
        self.btn_history.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_geography = tk.Button(self, text = "GEOGRAPHY", font = BUTTON_FONT, command = self.go_geography)
        self.btn_geography.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_music = tk.Button(self, text = "MUSIC", font = BUTTON_FONT, command = self.go_music)
        self.btn_music.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_gaming = tk.Button(self, text = "GAMING", font = BUTTON_FONT, command = self.go_gaming)
        self.btn_gaming.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_random = tk.Button(self, text = "RANDOM", font = BUTTON_FONT, command = self.go_random)
        self.btn_random.grid(row = 3, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_back = tk.Button(self, bg = "red", text = "BACK", font = BUTTON_FONT, command = self.go_back)
        self.btn_back.grid(row = 4, column = 0, columnspan = 2, sticky = "news")        
        
    def go_history(self):
        if Screen.option == "play":
            popup = tk.Tk()
            popup.title("Question 1")
            frm_question = QuestionMenu(popup, "history")
            frm_question.grid(row = 0, column = 0)
        elif Screen.option == "score":
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_geography(self):
        if Screen.option == "play":
            popup = tk.Tk()
            popup.title("Question 1")
            frm_question = QuestionMenu(popup, "geography")
            frm_question.grid(row = 0, column = 0)
        elif Screen.option == "score":
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_music(self):
        if Screen.option == "play":
            popup = tk.Tk()
            popup.title("Question 1")
            frm_question = QuestionMenu(popup, "music")
            frm_question.grid(row = 0, column = 0)
        elif Screen.option == "score":
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_gaming(self):
        if Screen.option == "play":
            popup = tk.Tk()
            popup.title("Question 1")
            frm_question = QuestionMenu(popup, "gaming")
            frm_question.grid(row = 0, column = 0)
        elif Screen.option == "score":
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_random(self):
        if Screen.option == "play":
            popup = tk.Tk()
            popup.title("Question 1")
            frm_question = QuestionMenu(popup, "random")
            frm_question.grid(row = 0, column = 0)
        elif Screen.option == "score":
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()

#----- QUESTION MENU CLASS -----
class QuestionMenu(tk.Frame):
    def __init__(self, parent, category):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.choice_var = tk.IntVar(self)
        self.choice_var.set(None)        
        
        self.lbl_question = tk.Label(self, bg = HEADER_BG, fg = HEADER_FG , text = "Sample Question", font = TITLE_FONT)
        self.lbl_question.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.rad_choice1 = tk.Radiobutton(self, fg = "#9FA09C", text = "Choice 1", font = CHOICE_FONT, variable = self.choice_var, value = 1)
        self.rad_choice1.grid(row = 1, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice2 = tk.Radiobutton(self, fg = "#9FA09C", text = "Choice 2", font = CHOICE_FONT, variable = self.choice_var, value = 2)
        self.rad_choice2.grid(row = 2, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice3 = tk.Radiobutton(self, fg = "#9FA09C", text = "Choice 3", font = CHOICE_FONT, variable = self.choice_var, value = 3)
        self.rad_choice3.grid(row = 3, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice4 = tk.Radiobutton(self, fg = "#9FA09C", text = "Choice 4", font = CHOICE_FONT, variable = self.choice_var, value = 4)
        self.rad_choice4.grid(row = 4, column = 0, columnspan = 3, sticky = "W")
        
        self.btn_quit = tk.Button(self, bg = "red", text = "QUIT", font = BUTTON_FONT, command = self.quit)
        self.btn_quit.grid(row = 5, column = 0, sticky = "news")
        
        self.btn_submit = tk.Button(self, bg = "green", text = "SUBMIT", font = BUTTON_FONT, command = self.submit)
        self.btn_submit.grid(row = 5, column = 2, sticky = "news")
        
    def quit(self):
        self.parent.destroy()
    
    def submit(self):
        messagebox.showwarning("WIP", "Submit WIP")

#----- SCORE MENU CLASS -----
class ScoreMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.lbl_scores = tk.Label(self, bg = HEADER_BG, fg = HEADER_FG, text = "Highscores", font = TITLE_FONT)
        self.lbl_scores.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.scr_scores = Scr(self, height = 5, width = 30, font = SCROLL_FONT)
        self.scr_scores.grid(row = 1, column = 0, columnspan = 3) 
        
        self.btn_back = tk.Button(self, text = "BACK", bg ="red", font = BUTTON_FONT, command = self.back)
        self.btn_back.grid(row = 2, column = 0, sticky="news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", bg = "orange", font = BUTTON_FONT, command = self.clear)
        self.btn_clear.grid(row = 2, column = 2, sticky="news")
        
    def back(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def clear(self):
        messagebox.showwarning("WIP", "Clear WIP")
        
#---------- MAIN ----------
if __name__ == "__main__":
    games = {}
    root = tk.Tk()
    root.title("Trivia Game")
    
    screens = [MainMenu(), SelectMenu(), ScoreMenu()]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")

    root.grid_columnconfigure(1, weight = 1)
    root.grid_rowconfigure(1, weight = 1)
    
main = screens[0]
main.tkraise()

root.mainloop()