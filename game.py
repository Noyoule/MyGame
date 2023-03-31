import json
from tkinter import *
from interface import Interface
class Game:

   def __init__(self):
      self.interface = Interface(len(self.word()))
      self.word = self.generate_word()
      self.interface.buttun["command"]=self.test
      self.interface.buttun.pack(pady=5)
      self.cpt = 0
      self.cpt2 =0
      self.level = 2
      self.chance = 10
      self.reste_score_chance()
   def word(self):
      with open('mots.json') as file:
          mots = json.load(file)
      with open('info.json') as file:
         info = json.load(file)
      indice = info["niveau"]
      mot = mots[indice]
      return mot
     
   def choice_word(self):
      with open('mots.json') as file:
          mots = json.load(file)
      with open('info.json') as file:
         info = json.load(file)
      indice = info["niveau"]
      mot_choisi = mots[indice]
      return mot_choisi
   
  
   def generate_word(self):
      mot = self.choice_word()
      return mot
   
   def reste_score_chance(self):
      with open('info.json') as file:
               mots = json.load(file)
      self.interface.score["text"] = "Chance: " + str(self.chance)+ "   Score: " + str(mots["score"])

   def play(self,event):
      if self.chance >0:
         mot = self.choice_word()
         mot_choisi = mot
         letter = event.char
         position = []
         self.put_score()
         for i in range(len(mot_choisi)):
            if letter.lower() == mot_choisi[i]:
               position.append(i)
         if len(position)==0:
            self.decrement_chane(); 
         if self.finish()==1:
            self.reset_color2()
         else:
            self.interface.changer_donner(position,letter)
      else:
         if self.cpt2==0:
             self.interface.buttun["text"]= "Recommencer"
             with open('info.json') as file:
               mots = json.load(file)
               if mots["score"] >3:
                  mots["score"] -= 3
                  with open('info.json', 'w+') as file:
                     json.dump(mots, file)
                  self.interface.score["text"] = "Chance: " + str(self.chance)+ "   Score: " + str(mots["score"])
             self.put_score()
             self.cpt2= 1   

   def reset_color(self,event):
      if self.finish() ==0:
         for i in range(len(self.interface.frame2.children)):
                if i==0:
                    self.interface.frame2.children["!label"]["bg"]="white"
                else:
                    self.interface.frame2.children["!label"+str(i+1)]["bg"]="white"

   def reset_color2(self):
      for i in range(len(self.interface.frame2.children)):
                if i==0:
                    self.interface.frame2.children["!label"]["bg"]="green"
                else:
                    self.interface.frame2.children["!label"+str(i+1)]["bg"]="green"

   def load(self):
      self.interface.set_game(self)
      self.interface.placer_composant()

   def finish(self):
      verif = 1
      for i in range(len(self.interface.frame2.children)):
                if i==0:
                  if self.interface.frame2.children["!label"]["text"]==" ":verif = 0
                else:
                  if self.interface.frame2.children["!label"+str(i+1)]["text"]==" ":verif = 0
      return verif
   
   def put_score(self):
      if self.cpt ==0 or self.chance==0:
         if self.finish() == 1:
            with open('info.json') as file:
               mots = json.load(file)
            mots["score"]+=5
            mots["niveau"]+=1
            with open('info.json', 'w+') as file:
               json.dump(mots, file)
            with open('info.json') as file:
               info = json.load(file)
            score = info["score"]
            self.interface.score["text"] = "Chance: " + str(self.chance)+ "   Score: " + str(score)
            self.cpt=1 
      
   def decrement_chane(self):
      if self.finish()==0:
         self.chance-=1
         with open('info.json') as file:
            info = json.load(file)
            score = info["score"]
            self.interface.score["text"] = "Chance: " + str(self.chance)+ "   Score: " + str(score)


   def test(self):
      if self.finish()==1 or self.chance == 0:
         self.interface.buttun["text"]= "Suivant"
         self.word = self.generate_word()
         self.interface.window.children["!frame"].children["!frame"+str(self.level)].destroy()
         frame2 =Frame(self.interface.frameMain, bg='#104043')
         self.interface.frame2 = frame2
         self.interface.cadre = self.interface.creer_cadre(len(self.word))
         self.interface.frame2.grid(row=3, column=1, sticky=W, padx=2)
         self.cpt =0
         self.cpt2 =0
         self.chance = 10
         self.reste_score_chance()
         self.level+=1
         

   def new_game(self):
      self.load()
