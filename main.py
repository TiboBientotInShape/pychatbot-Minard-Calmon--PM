from function import *
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

