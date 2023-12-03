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

#Function telling if a word was say by a president and who say it the most
#Speak_word("Nation")

#Function that all the president say and are important
print(import_word())


if __name__ == '__main__':
    directory = "./Speeches"
    files_name = list_pres(directory, ".txt")
    print(files_name)
    files_surnames = pren_pres(files_name)
    print(files_surnames)


list=TF_IDF(r'C:\Users\minar\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')
print(mots_nimport(list))

list=TF_IDF(r'C:\Users\minar\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')
print(mots_import(list))

print(Rep_words("Chirac"))
