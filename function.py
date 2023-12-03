import os
import math
#Fonction pour mettre tout le fichier en minuscule
def cleanFiles(directory):
    if not os.path.exists("./cleaned"):
        Cleaned = "./cleaned"
        os.mkdir(Cleaned)
        for files in os.listdir(directory):
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
            text = text.replace(",","").replace("-","").replace(".","").replace("!","").replace("?","").replace("'"," ")    #.replace("ã©","e").replace("ã¹","u").replace("ã¨","e").replace("ã§","c").replace("ã ","a").replace("ãª","e")
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
                    L_TF_IDF.append((DicIDF.get(word))*tf)
                txt.close()
            L2D_TF_IDF.append(L_TF_IDF)
            L_TF_IDF = []
    return(L2D_TF_IDF)


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







