from function import *

#Function to create the directory cleaned
cleanFiles("./Speeches")

#Function to format the doc in the cleaned directory
ClearFiles(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')

#line to test the TF function in a specific texte
#with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned\Nomination_Giscard dEstaing.txt', "r") as file:
#    text = file.read()
#print((TF(text)))


#line to print the IDF function in the directory
#print(IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'))

#Do the TF IDF of all the word in the corpus
#print(TF_IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'))

#Function telling the list of all the word the given president say the most in his speech (say more than 15 time)
#print(Rep_words("Chirac"))

#Function telling if a word was say by a president and who say it the most
#Speak_word("Nation")