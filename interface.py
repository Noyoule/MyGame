from tkinter import *
import json
from random import *


class Interface:
   
    def __init__(self,n):
        self.n = n
        self.window = self.creer_fenetre()
        self.frameMain = Frame(self.window, bg='#194043')
        self.frame = Frame(self.frameMain, bg='#194043')
        self.frame2 = Frame(self.frameMain, bg='#104043')
        self.label_title = Label(self.frame, text="Jeux de lettre", font=("JetBrains Mono", 25), bg="#194043", fg='white')
        self.cadre =self.creer_cadre(n)
        self.score = self.creer_composant2()
        self.buttun = self.creer_composant1()


    def action(self,event):
        self.label_title["text"] = event.char

    def creer_fenetre(self):
        window = Tk()
        window.title("Jeu de lettre")
        window.geometry("1024x720")
        window.minsize(600, 380)
        window.config(background='#194043')
        window.resizable(True,True)
        return window

    # with open('animaux.json') arepertoires file:
    #   mots = json.load(file)
    
    def creer_composant1(self):
        # button
        button = Button(self.frame, text="Suivant", font=("JetBrains Mono", 15), bg='#194043', fg='white',command="")
        button.pack(pady=5,fill=X)
        return button

    def creer_composant2(self):
        with open('info.json') as file:
            info = json.load(file)
        score = info["score"]
        score_texte = "Chance: " + str(10)+ "   Score: " + str(score)
        # button
        score = Label(self.window, text=score_texte, font=("JetBrains Mono", 15), bg='#194043', fg='white')
        score.pack(fill=BOTH)
        return score
    # second texte
    def creer_cadre(self,n):
        height = 2
        width = 3
        if n > 13:
            height = 1
            width = 2
        labels = []
        i = 0
        for i in range(0, n):
            label = Label(self.frame2, text=" ", height=height, width=width, font=("JetBrains Mono", 20), bg="white", fg='black')
            labels.append(label)
            #print(labels)
            label.grid(row=0, column=i, padx=5)
            i += 1
        #print(labels[5]["text"])
        #print(self.frame2.children)
        #print(self.frame2.children)
        return labels

    def placer_composant(self):
        self.label_title.pack()
        self.frame.grid(row=0, column=1)
        self.frame2.grid(row=3, column=1, sticky=W, padx=2)
        self.frameMain.pack(expand=YES)
        self.window.mainloop()
    
    def set_game(self, game):
            self.window.bind("<KeyPress>", game.play)
            self.window.bind("<KeyRelease>", game.reset_color)

    def changer_donner(self,position,c):
        if len(position) > 0 :
            for i in range(len(position)):
                indice =position[i] 
                if indice ==0:
                    self.frame2.children["!label"]["text"]= c.upper()
                else:
                    self.frame2.children["!label"+str(indice+1)]["text"]= c.upper()
        else:
            for i in range(len(self.frame2.children)):
                if i==0:
                    self.frame2.children["!label"]["bg"]="#fa8484"
                else:
                    self.frame2.children["!label"+str(i+1)]["bg"]="#fa8484"
    

    def change_game(self):
        game = print("birn")                
                    