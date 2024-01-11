from function import *
import os
# -*- coding: utf-8 -*-


chemin = (r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')

#Function to create the directory cleaned
cleanFiles("./Speeches")

#Function to format the doc in the cleaned directory
ClearFiles(chemin)

#line to test the TF function in a specific texte
#with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned\Nomination_Giscard dEstaing.txt', "r") as file:
#    text = file.read()
#print((TF(text)))


#line to print the IDF function in the directory
#print(IDF(chemin))

#Do the TF IDF of all the word in the corpus
#print(TF_IDF(chemin))

#Function telling if a word was say by a president and who say it the most
#Speak_word("Nation")

#Function important word that all the president said
#print(import_word())

#Function Tokenisiation of the question
#Question = "Quelle est l'importance de la democratie ?"
#print(TokenQ(Question))

#Function that find a correspondance between the question and the corpus
#print(FindCorpus(TokenQ(Question),IDF(chemin)))

#Function not obligatory in order to make the correct format (changing the dic of the TF-IDF into a matrice)
#print(formatMatrice_TF_IDF(TF_IDF(chemin)))

#Function to tell the TF of each word in the question
#print(TF_Question(TokenQ(Question)))

#Function to tell the TF-IDF of the question
#TF_Q = TF_Question(FindCorpus(TokenQ(Question),IDF(chemin)))
#IDF_Q = (IDF(chemin))
#print(TF_IDF_Question(TF_Q,IDF_Q))

#produit_scalaire(TF_IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'))

print(" PyChatBot\n\n","Bienvenue sur PyChatBot, un ChatBot avec un base de donnée sur des discours de presidents.\n")
print(" Selection une fonctionnalite en entrant le numero de la fonction. \n")
print(" 1. Afficher la liste de présidents qui on leur discours dans la base de donnee. \n",
      "2. Afficher le TF (Term Frequency) d'un des texte dans la base de donnee. \n",
      "3. Le IDF d'un mot dans la totalite des texts de la base de donnee. \n",
      "4. Affiche le TF_IDF d'un mot dans le corpus de documents. \n",
      "5. Affiche la liste des mots les moins importants dans le corpus de documents. \n",
      "6. Affiche le(s) mot(s) ayant le score TD-IDF le plus élevé \n",
      "7. Affiche la liste des mots les plus répéte par un présidet hormis les mots dits non importants \n",
      "8. Indique le(s) nom(s) du (des) president(s) qui a (ont) parlé de la d'un mot et celui qui l’a repete le plus de fois \n",
      "9. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les presidents ont evoques. \n \n"
      " 10. Dites une question, vous verrez les étapes\n\n")

rep = int(input("Quel fonction voulez vous utiliser : "))
while rep<1 or rep>10:
      rep= int(input("Valeur incorrect, refaire : "))

chemin = (r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')

if rep ==1:
      print("Voici la liste des présidents ce trouvant dans notres base de donnée :")
      for i in (pren_pres(list_pres(chemin,"txt"))):
            print(i)

if rep==2:
      nb = 0
      list = []
      print("Sélectioner une text")
      for filename in os.listdir(chemin):
            nb+=1
            print(nb,".",(filename).replace("_"," ").replace(".txt",""))
            list.append(filename)
      print("\n Sélectionner un texte de 1 à",nb)
      selec = int(input())
      while selec<0 or selec>nb:
            selec = int(input("Saisir une nouvelles valeurs : "))
      txt = list[selec-1]
      print(txt)
      with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned\{name}'.format(name=txt), "r") as file:
            text = file.read()
      print((TF(text)))

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
