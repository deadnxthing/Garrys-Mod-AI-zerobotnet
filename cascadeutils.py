import os

def genereate_negative_description_file():
    with open('neg.txt','w') as f:
        for filename in os.listdir('negatywne2'):
            f.write('negatywne2/'+ filename + '\n')

genereate_negative_description_file()



#C:\Users\KUBAC\Downloads\opencv\build\x64\vc15\bin
