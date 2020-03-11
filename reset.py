import pickle
import tkinter as tk
from tkinter import messagebox

questions = {"Gaming":[['Which year did Super Mario Bros release in North America?', '1990', '1985', '2000', '1969', 2], 
                  ['Minecraft was made by which company?', 'Mojang', 'Microsoft', 'Disney', 'Nintendo', 1],
                  ['What is the main character in Tomb Raider?', 'Chun-Li', 'Sonya Blade', 'Lara Croft', 'Samus Aran', 3],
                  ['How many chacters are there in Super Smash Bros Ult. (Excluding DLC)?', '69', '74', '26', '58', 2],
                  ['What is the "worst" Nintendo 64 game?', 'Superman 64', 'Super Mario 64', 'Donkey Kong 64', 'Doom 64', 1],
                  ['How many times has Kingdom Hearts 2 been re-release?', '2', '8', '1', '4', 4],
                  ['Who is the main artist in the Beat Saber OST?', 'Pegboard Nerds', 'Jaroslav Beck', 'Taylor Swift', 'Boom Kitty', 2],
                  ['What was the first LEGO Video Game?', 'Lego Island', 'Lego Star Wars', 'Lego Batman', 'Lego Indiana Jones', 1],
                  ['What was the first offical video game?', 'Donkey Kong', 'Pong', 'Pacman', 'Mario Bros', 2],
                  ['What color is Inky in Pacman?', 'Orange', 'Red', 'Blue', 'Pink', 3]],
             "History" :[['Question 1', 'a1', 'a2', 'a3', 'a4', 1], ['Question 2', 'a1', 'a2', 'a3', 'a4', 4]]
             }

scores = { "Gaming" : [['Christian', '9']],
           "History" : [['Name2', 'Score']],
           "Geography" : [['Name3', 'Score']],
           "Music" : [['Name4', 'Score']],
           "Random" : [['Name5', 'Score']]
           }

LABEL_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Times New Roman", 18)

class Reset_Frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
        self.lbl_reset = tk.Label(self, text = "CHOOSE DATA TO RESET", font = LABEL_FONT)
        self.lbl_reset.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
    
        self.btn_questions = tk.Button(self, text = "QUESTIONS", font = BUTTON_FONT, command = self.reset_questions)
        self.btn_questions.grid(row = 1, column = 0, sticky = "news")
        
        self.btn_questions = tk.Button(self, text = "SCORES", font = BUTTON_FONT, command = self.reset_scores)
        self.btn_questions.grid(row = 1, column = 1, sticky = "news")         

    def reset_questions(self):
        datafile = open("trivia_questions.pickle", "wb")
        pickle.dump(questions, datafile)
        datafile.close()
        messagebox.showinfo(message = "Questions Reset.")
        
    def reset_scores(self):
        datafile = open("trivia_scores.pickle", "wb")
        pickle.dump(scores, datafile)
        datafile.close()
        messagebox.showinfo(message = "Scores Reset.")    
    
root = tk.Tk()
root.title("Data Reset")
    
main = Reset_Frame()
main.grid(row = 0, column = 0, sticky = "news")
main.tkraise()
    
root.mainloop()