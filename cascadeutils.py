import os

def genereate_negative_description_file():
    with open('neg.txt','w') as f:
        for filename in os.listdir('C:/Users/KUBAC/OneDrive/Pulpit/projekty/Garry-sMod-AI-zerobotnet/negatywne'):
            f.write('negatywne/'+ filename + '\n')

genereate_negative_description_file()


