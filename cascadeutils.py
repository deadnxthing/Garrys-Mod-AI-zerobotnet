import os

def genereate_negative_description_file():
    with open('neg.txt','w') as f:
        for filename in os.listdir('negatywne2'):
            f.write('negatywne2/'+ filename + '\n')

genereate_negative_description_file()


# $ C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 1100 -numNeg 3300 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999
#-data sztuczna/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 1000 -numNeg 3000 -numStages 20 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999


#C:\Users\KUBAC\Downloads\opencv\build\x64\vc15\bin