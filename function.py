import os
import math

chemin = (r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')

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

#Fonction pour mettre tout le fichier en minuscule
def cleanFiles(directory):
    if not os.path.exists("./cleaned"):#Verifier si le fichier cleaned n'est pas déja crée
        Cleaned = "./cleaned"#Associe un chemin
        os.mkdir(Cleaned)#Crée le répertoire
        for files in os.listdir(directory):#Fait le tour de fichier dans le repertoir directory
            os.chdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\Speeches')
            noms = files
            os.chdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned')
            open(noms, "w")
            os.chdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM')

        for files in os.listdir(directory):
            with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\Speeches/{file}'.format(file=files),"r") as Copy:
                with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"w") as Paste:
                    for ligne in Copy:
                        Paste.write(ligne.lower())

def ClearFiles(directory):
    os.chdir(directory)
    for files in os.listdir(directory):
        f = open("Ntext.txt", "w")
        with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
            text = file.read()
            text = text.replace(",","").replace("-","").replace(".","").replace("!","").replace("?","").replace("'"," ").replace("ã©","e").replace("ã¹","u").replace("ã¨","e").replace("ã§","c").replace("ã ","a").replace("ãª","e")
            f.write(text)
        f.close()
        os.remove(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files))
        os.rename("Ntext.txt",files)


def TF(text):
    DicTF={}
    for word in text.split():
       if word not in DicTF:
           DicTF.update({word:1})
       else:
           DicTF.update({word:DicTF[word]+1})
    return(DicTF)


def IDF(directory):
    os.chdir(directory)
    nb_files = 0
    text=""
    nb_word = 0
    IDF_word = 0
    for files in os.listdir(directory):
        nb_files += 1
        DicIDF = {}
        with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
            text += file.read()
            file.close()

    for word in text.split():
        if word not in DicIDF:
            for files in os.listdir(directory):
                with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
                    if word in file.read():
                        nb_word+=1

            IDF_word = math.log((nb_files/nb_word)+1)
            nb_word=0
            DicIDF.update({word:IDF_word})

    return(DicIDF)

def TF_IDF(directory):
    L2D_TF_IDF = []
    L_TF_IDF = []
    DicIDF = (IDF(directory))
    text=""
    for files in os.listdir(directory):
        with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
            text += file.read()
            file.close()

    for word in text.split():
        if not any(word in list for list in L2D_TF_IDF):
            L_TF_IDF.append(word)
            for texte in os.listdir(directory):
                with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{texte}'.format(texte=texte),"r") as txt:
                    DicTF = TF(txt.read())
                    if ((DicTF).get(word)) != None:
                        tf = ((DicTF).get(word))
                    else:
                        tf = 0
                    L_TF_IDF.append(round((DicIDF.get(word))*tf,2))
                txt.close()
            L2D_TF_IDF.append(L_TF_IDF)
            L_TF_IDF = []
    return(L2D_TF_IDF)


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
    for filename in os.listdir(chemin):
        if nom in filename.lower():
            with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=filename),"r") as file:
                text+=file.read()

    text_TF = TF(text)

    for word in text_TF:
        if text_TF[word]>15:
            list_word.append(word)
    return(list_word)

def Speak_word(word):
    text = ""
    word = word.lower()
    count = 0
    list_pres = []
    max_name = ""
    verif_max=0
    for files in os.listdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned'):
        with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
            text += file.read()
        for mot in text.split():
            if mot == word:
                count+=1
        if count>0 and files.replace("Nomination_","").replace(".txt","").replace("1","").replace("2","") not in list_pres:
            list_pres.append(files.replace("Nomination_","").replace(".txt","").replace("1","").replace("2",""))
            if verif_max<count:
                verif_max = count
                max_name = files.replace("Nomination_","").replace(".txt","").replace("1","").replace("2","")
        text = ""
        count=0
    print(list_pres)
    print(max_name)

def import_word():
    all_text = ""
    text = ""
    DicIDF = IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')
    verif_word = []
    check_all_text = 0
    nbText = 0
    import_mot = []
    for files in os.listdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned'):
        nbText+=1
        with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
            all_text += file.read()
            file.close()

    for word in all_text.split():
        if word not in verif_word:
            for files in os.listdir(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned'):
                with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned/{file}'.format(file=files),"r") as file:
                    text += file.read()
                    DicTF = TF(text)
                if word in text:
                    check_all_text+=1
                if (DicTF.get(word))==None or (DicTF.get(word)) > 5:
                    check_all_text = 0
                text =""
            if check_all_text==nbText:
                if DicIDF.get(word)<1:
                    import_mot.append(word)
            verif_word.append(word)
        check_all_text=0

    return(import_mot)

def TokenQ(Question):
    Q = Question.lower()
    list = []
    for i in Q:
        if ord(i) < 97 or ord(i)>122:
            Q = Q.replace(i," ")
    for i in Q.split():
        list.append(i)
    return(list)

def FindCorpus(list,DicCorpus):
    Newlist = []
    for i in list:
        if i in DicCorpus:
            Newlist.append(i)
    return(Newlist)
def formatMatrice_TF_IDF(Dic):
    Matrice_TF_IDF = []
    list_word = []
    for i in range (1,len(Dic[0])):
        for j in range (0,len(Dic)):
            list_word.append(Dic[j][i])
        Matrice_TF_IDF.append(list_word)
        list_word = []
    return(Matrice_TF_IDF)

def TF_Question(Question):
    Dic= {}
    for i in Question:
        if i not in Dic:
             Dic[i]=1
        else:
            Dic.update({i:Dic[i]+1})
    return(Dic)

def TF_IDF_Question(DicTF,IDF):
    Dic_TF_IDF_Question = {}
    for i in DicTF:
        Dic_TF_IDF_Question.update({i: round(DicTF[i] * IDF[i],2)})
    return Dic_TF_IDF_Question

def produit_scalaire(A,B,list):
    M = (len(list[0]))-1
    res = 0
    for i in range(M):
        res+=float(A[i])*float(B[i])
    return res

def normeV(A):
    res = 0
    M = len(A)
    for i in range(M):
        res+= ((float(A[i]))**2)
    return math.sqrt(res)

def similarity(A,B,list):
    res=0
    res=(produit_scalaire(A,B,list))/((normeV(A))*normeV(B))
    return res

