import os

def list_pres(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            res = filename.replace("Nomination_", "").replace(".txt", "").replace("1", "").replace("2", "")
            if res not in files_names:
                files_names.append(res)
    return files_names

def pren_pres(list):
    files_surnames = []
    for i in list:
        if i == 'Chirac':
            files_surnames.append("Jack Chirac")

        if i == 'Giscard dEstaing':
            files_surnames.append("Valery Giscard dEstaing")

        if i == 'Hollande':
            files_surnames.append("François Hollande")

        if i == 'Macron':
            files_surnames.append("Emmanuel Macron")

        if i == 'Mitterrand':
            files_surnames.append("François Mitterrand")

        if i == 'Sarkozy':
            files_surnames.append("Nicolas Sarkozy")
    return files_surnames

def mots_nimport(L2D):
    list_mots = []
    verif = 0
    longeur_list = len(L2D)
    longueur_list_TF_IDF = len(L2D[0])
    for mots in range(0,longeur_list):
        for TF_IDF in range(1,longueur_list_TF_IDF):
            if L2D[mots][TF_IDF]==0.0:
                verif+=1
        if verif==7:
            list_mots.append(L2D[mots][0])
        verif = 0
    return(list_mots)

def mots_import(L2D):
    list_mots = []
    somme = 0
    longeur_list = len(L2D)
    longueur_list_TF_IDF = len(L2D[0])
    for mots in range(0,longeur_list):
        for TF_IDF in range(1,longueur_list_TF_IDF):
                somme+=L2D[mots][TF_IDF]
        if somme>=50:
            list_mots.append(L2D[mots][0])
        somme = 0
    return(list_mots)

def Rep_words(nom):
    text = ""
    nom = nom.lower()
    list_word = []
    for filename in os.listdir(r'C:\Users\minar\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'):
        if nom in filename.lower():
            with open(r'C:\Users\minar\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=filename),"r") as file:
                text+=file.read()

    text_TF = TF(text)

    for word in text_TF:
        if text_TF[word]>15:
            list_word.append(word)
    return(list_word)