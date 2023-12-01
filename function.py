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


