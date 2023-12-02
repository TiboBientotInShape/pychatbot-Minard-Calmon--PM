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

cleanFiles("./Speeches")
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

ClearFiles(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned')


def TF(text):
    DicTF={}
    for word in text.split():
       if word not in DicTF:
           DicTF.update({word:1})
       else:
           DicTF.update({word:DicTF[word]+1})
    return(DicTF)

#with open(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM\cleaned\Nomination_Giscard dEstaing.txt', "r") as file:
#    text = file.read()
#print((TF(text)))

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

#print(IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'))


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
            print(word)
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



print(TF_IDF(r'C:\Users\trist\PycharmProjects\pychatbot-Minard-Calmon--PM/cleaned'))



