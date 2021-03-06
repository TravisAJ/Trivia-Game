#!/usr/bin/python3
# Taffea Avenevoli and Daisy Arnold
# 03/09/20

#------------------ IMPORTS ------------------
import pickle as pk
import tkinter as tk
import random as rd
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
        Screen.category = "History"
    
        if Screen.option == "play":
            self.screen_play()
            
        elif Screen.option == "score":
            self.screen_score()

        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_geography(self):
        Screen.category = "Geography"
        
        if Screen.option == "play":
            self.screen_play()
            
        elif Screen.option == "score":
            self.screen_score()
            
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_music(self):
        Screen.category = "Music"
          
        if Screen.option == "play":
            self.screen_play()
            
        elif Screen.option == "score":
            self.screen_score()
            
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_gaming(self):
        Screen.category = "Gaming"
        
        if Screen.option == "play":
            self.screen_play()
            
        elif Screen.option == "score":
            self.screen_score()
            
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_random(self):
        Screen.category = ""
        
        if Screen.option == "play":
            self.screen_play()
        
        elif Screen.option == "score":
            self.screen_score()
                
        else:
            messagebox.showerror("ERROR", "Something went wrong")
    
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def screen_score(self):
        if len(scores[Screen.category]) != 0:
            screens[2].scr_scores.delete('0.0', 'end')
            for i in range(len(scores[Screen.category])):
                msg = str(i+1) + '. ' + scores[Screen.category][i][0] + ': ' + scores[Screen.category][i][1]  + '\n'
                screens[2].scr_scores.insert('insert', msg)
        Screen.current = 2
        Screen.switch_frame()   
        
    def screen_play(self):
        popup = tk.Tk()
        popup.title("Question 1")
        frm_question = QuestionMenu(popup, Screen.category)
        frm_question.grid(row = 0, column = 0)
        
#----- NAME ENTRY CLASS -----
class NameEntry(tk.Frame):
    def __init__(self, parent, category, score):
        
        self.score = score
        self.parent = parent
        self.category = category
        tk.Frame.__init__(self, master = parent)
        
        msg = "Your Score Is: " + str(score) + ". What is your name?" 
        self.lbl_score = tk.Label(self, text = msg, font = TITLE_FONT)
        self.lbl_score.grid(row = 0, column = 0)
        
        self.ent_name = tk.Entry(self, font = CHOICE_FONT)
        self.ent_name.grid(row = 1, column = 0)
        
        self.btn_submit = tk.Button(self, text = "Submit", font = BUTTON_FONT, command = self.submit_score)
        self.btn_submit.grid(row = 2, column = 0)
        
    def submit_score(self):
        name = self.ent_name.get()
        scores[self.category].append([name, str(self.score)])
        datafile = open("trivia_scores.pickle", "wb")
        pk.dump(scores, datafile)
        datafile.close()        
        messagebox.showinfo("Success", "Score submitted!")
        self.parent.destroy()
        
#----- QUESTION MENU CLASS -----
class QuestionMenu(tk.Frame):
    def __init__(self, parent, category):
        tk.Frame.__init__(self, master = parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)        
        
        self.question = []
        for cpyquestion in questions[category]:
            self.question.append(cpyquestion)

        self.selected_question = self.question.pop(rd.randint(0, len(self.question)-1))
        self.score = 0
        self.question_number = 1
        
        self.parent = parent
        self.category = category

        self.choice_var = tk.IntVar(self)
        self.choice_var.set(0)        
        
        self.lbl_question = tk.Label(self, bg = HEADER_BG, fg = HEADER_FG , text = self.selected_question[0] , font = TITLE_FONT)
        self.lbl_question.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.rad_choice1 = tk.Radiobutton(self, fg = "#9FA09C", text = self.selected_question[1], font = CHOICE_FONT, variable = self.choice_var, value = 1)
        self.rad_choice1.grid(row = 1, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice2 = tk.Radiobutton(self, fg = "#9FA09C", text = self.selected_question[2], font = CHOICE_FONT, variable = self.choice_var, value = 2)
        self.rad_choice2.grid(row = 2, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice3 = tk.Radiobutton(self, fg = "#9FA09C", text = self.selected_question[3], font = CHOICE_FONT, variable = self.choice_var, value = 3)
        self.rad_choice3.grid(row = 3, column = 0, columnspan = 3, sticky = "W")
        
        self.rad_choice4 = tk.Radiobutton(self, fg = "#9FA09C", text = self.selected_question[4], font = CHOICE_FONT, variable = self.choice_var, value = 4)
        self.rad_choice4.grid(row = 4, column = 0, columnspan = 3, sticky = "W")
        
        self.btn_quit = tk.Button(self, bg = "red", text = "QUIT", font = BUTTON_FONT, command = self.quit)
        self.btn_quit.grid(row = 5, column = 0, sticky = "news")
        
        self.btn_submit = tk.Button(self, bg = "green", text = "SUBMIT", font = BUTTON_FONT, command = self.submit)
        self.btn_submit.grid(row = 5, column = 2, sticky = "news")
        
    def quit(self):
        self.parent.destroy()
    
    def submit(self):
        if self.choice_var.get() == self.selected_question[5]:
            self.score += 1
            if not len(self.question) == 0:
                self.selected_question = self.question.pop(rd.randint(0, len(self.question)-1))
                self.update()
            else:
                popup = tk.Tk()
                popup.title("NEW HIGH SCORE")
                frm_highscore = NameEntry(popup, self.category, self.score)
                frm_highscore.grid(row = 0, column = 0)                
                self.parent.destroy()
            messagebox.showinfo(message = "Correct, Current Score: " + str(self.score))
        elif self.choice_var.get() == 0:
            messagebox.showerror(message = "ERROR: Please select an answer")
        else:  
            if not len(self.question) == 0:
                self.selected_question = self.question.pop(rd.randint(0, len(self.question)-1))
                self.update()
            else:
                popup = tk.Tk()
                popup.title("NEW HIGH SCORE")
                frm_highscore = NameEntry(popup, self.category, self.score)
                frm_highscore.grid(row = 0, column = 0)                     
                self.parent.destroy()
            messagebox.showinfo(message = "Incorrect, Current Score: " + str(self.score))
            
    def update(self):
        self.lbl_question.configure(text = self.selected_question[0])
        self.rad_choice1.configure(text = self.selected_question[1])
        self.rad_choice2.configure(text = self.selected_question[2])
        self.rad_choice3.configure(text = self.selected_question[3])
        self.rad_choice4.configure(text = self.selected_question[4])
        
        self.question_number += 1
        msg = "Question " + str(self.question_number)
        self.parent.title(msg)
        self.choice_var.set(0)        

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
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", bg = "orange", font = BUTTON_FONT, command = self.clear)
        self.btn_clear.grid(row = 2, column = 2, sticky = "news")
        
    def back(self):
        self.scr_scores.delete('0.0', "end")
        Screen.current = 1
        Screen.switch_frame()
        
    def clear(self):
        confirm = messagebox.askyesno("Clear", "Are you sure you want to clear?")
        if confirm:
            scores[Screen.category] = []
            self.scr_scores.delete('0.0', "end")
            datafile = open("trivia_scores.pickle", "wb")
            pk.dump(scores, datafile)
            datafile.close()             
            messagebox.showinfo("Success", "Scores Cleared!")
        
#---------- MAIN ----------
if __name__ == "__main__":
    questions = {}
    datafile = open("trivia_questions.pickle", "rb")
    questions = pk.load(datafile)
    datafile.close()
    
    scores = {}
    datafile = open("trivia_scores.pickle", "rb")
    scores = pk.load(datafile)
    datafile.close()
    
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