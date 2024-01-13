from function import *
import os
# -*- coding: utf-8 -*-

chemin = (r'C:\Users\trist\PycharmProjects/pychatbot-Minard-Calmon--PM/cleaned')

#Function to create the directory cleaned
cleanFiles("./Speeches")

#Function to format the doc in the cleaned directory
ClearFiles(chemin)

print(" PyChatBot\n\n", "Bienvenue sur PyChatBot, un ChatBot ayant comme base de données des discours présidentiels.\n")
print(" Sélectionnez une fonctionnalité en entrant le numéro de la fonction. \n")
print(" 1. Afficher la liste des présidents qui ont leur discours dans la base de données. \n",
      "2. Afficher la fréquence des termes (Term Frequency - TF) d'un des textes dans la base de données. \n",
      "3. Afficher l'IDF (Inverse Document Frequency) d'un mot dans la totalité des textes de la base de données. \n",
      "4. Afficher le TF-IDF d'un mot dans le corpus de documents. \n",
      "5. Afficher la liste des mots les moins importants dans le corpus de documents. \n",
      "6. Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé. \n",
      "7. Afficher la liste des mots les plus répétés par un président, hormis les mots dits non importants. \n",
      "8. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé d'un mot recherché et celui qui l’a répété le plus de fois. \n",
      "9. Hormis les mots dits « non importants », quels sont les mots que tous les présidents ont évoqués. \n \n"
      "10. Posez une question, vous verrez les étapes.\n\n")


rep = int(input("Quel fonction voulez vous utiliser : "))
while rep<1 or rep>10:
      rep= int(input("Valeur incorrect, refaire : "))


if rep ==1:
      print("Voici la liste des présidents ce trouvant dans notres base de donnée :")
      for i in (pren_pres(list_pres(chemin,"txt"))):
            print(i)

if rep==2:
      nb = 0
      list = []
      TF_txt = {}
      print("Sélectioner un text")
      for filename in os.listdir(chemin):
            nb+=1
            print(nb,".",(filename).replace("_"," ").replace(".txt",""))
            list.append(filename)
      print("\n Sélectionner un texte de 1 à",nb)
      selec = int(input())
      while selec<0 or selec>nb:
            selec = int(input("Saisir une nouvelles valeurs : "))
      txt = list[selec-1]
      print(txt,"\n")
      with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned\{name}'.format(name=txt), "r") as file:
            text = file.read()
      TF_txt=(TF(text))
      x = input("Voulez vous chercher un mot en particulier ? O/N \n")
      while x != "O" and x != "N" and x != "o" and x != "n":
            x = input("Veuillez ressaisir une nouvelle valeur correct. O/N \n")
      if x=="O" or x=="o":
            mot = input("Quel mot chercher vous ?\n")
            if mot.lower() in TF_txt:
                  print("Le TF du mot choisi dans le texte sélectionner est :",TF_txt[mot.lower()])
            else:
                  print("Le mot rechercher ne ce trouve pas dans le texte sélectionner")
      if x=="N" or x == "n":
            print(TF(text))
if rep==3:
      dic = IDF(chemin)
      reps = (input("Saisir quel mot rechercher : "))
      print(dic.get("{mot}".format(mot=reps)))

if rep==4:
      reps = (input("Saisir quel mot rechercher : "))
      list = TF_IDF(chemin)
      for i in list:
            if reps in i:
                  print(i)

if rep==5:
      print(mots_nimport(TF_IDF(chemin)))

if rep==6:
      print(mots_import(TF_IDF(chemin)))

if rep==7:
      print("Sélectionner un président parmis cette liste : ")
      nb = 0
      for i in (pren_pres(list_pres(chemin,"txt"))):
            nb+=1
            print(nb,"-",i)
      reps = int(input("\n Saisir un président (numéro) : "))
      if reps==1:
            print(Rep_words("Chirac"))
      if reps==2:
            print(Rep_words("Giscard dEstaing"))
      if reps==3:
            print(Rep_words("Hollande"))
      if reps==4:
            print(Rep_words("Macron"))
      if reps==5:
            print(Rep_words("Mitterrand"))
      if reps==6:
            print(Rep_words("Sarkozy"))

if rep==8:
      reps = (input("Saisir quel mot rechercher : "))
      Speak_word("{mot}".format(mot=reps))

if rep==9:
      print(import_word())

if rep==10:
      reps = input("Saisir une question : \n")
      print("Question traité par une Tokenisation \n", TokenQ(reps))
      print("Liste de mot qui figure dans la question et le corpus de documents \n",(FindCorpus(TokenQ(reps),IDF(chemin))))
      print("Formatage de notre TF_IDF du corpus de documents, passant donc de dictionnaire à matrice \n",(formatMatrice_TF_IDF(TF_IDF(chemin))))
      print("Donne le TF des mots dans la question \n",(TF_Question(TokenQ(reps))))
      TF_Q = TF_Question(FindCorpus(TokenQ(reps),IDF(chemin)))
      IDF_Q = (IDF(chemin))
      print("Donne le TF_IDF de la question \n",(TF_IDF_Question(TF_Q,IDF_Q)))
