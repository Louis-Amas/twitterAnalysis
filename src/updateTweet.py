from sys import argv
import time
from Updater import Updater



def saveFile(filename):
    with open(filename, 'a+') as fOut:
        for key in dic:
            line = str(key) + ';'
            for val in dic[key]:
                line += str(val) + ';'
            fOut.write(line[:-1] + '\n')



if __name__ == '__main__':

'''
     Prend des fichiers csv de 900 lignes maximum et récupère les informations sur les tweets corespondant
     format du csv 'id;followers_count;friends_count;favourites_count;statuses_count;lang;text'
     Ecrit dans un nouveau fichier csv le nombre de retweet
'''

    if len(argv) < 3:
        print(argv[0] + ' files.csv updatedCsv')
        exit(1)

    csv_files_in = argv[1:-1]
    csv_file_out = argv[len(argv) - 1]
    history = argv[len(argv) - 2]


    for i, csvFileIn in enumerate(csv_files_in):
        dic = dict()
        with open(csvFileIn, 'r') as fIn:
            fIn.readline()
            for line in fIn:
                tab = line[:-1].split(';')
                dic[tab[0]] = tab[1:]
        updater = Updater(dic)
        updater.find()
        for key in updater.dict_of_retweet:
            dic[key].append(updater.dict_of_retweet[key])
        print(i, ' / ', len(csv_files_in))
        saveFile(csv_file_out)
        print("Sleeping for 900 s last fic:" + csvFileIn + ' gathered ', 900 * i, ' / ', 900 * i / len(csv_files_in) * 900 * 100, '%')
        with open('history', 'a+') as h:
            h.write(csvFileIn + '\n')
        time.sleep(900)
