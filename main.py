from function import *

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
Question = "Quelle est l'importance de la democratie ?"
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
