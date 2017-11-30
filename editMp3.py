import os
import glob
import shutil
import string
from pydub import AudioSegment

def splitMp3(toSplit,splitTime=0.5):
    os.system('mp3splt\mp3splt ' + toSplit + ' -g %[@N=0,@o] -o "@nsplit" -t ' + str(splitTime))
    os.system('move *split.mp3 SplitFiles\\')
    os.system('set count=0 & for %x in (*) do @(set /a count+=1 >nul)')
    length = len(glob.glob('SplitFiles\\*'))
    #os.system('cd')
    return length

# def joinMp3(*tracks):
#     megaString = ""
#     for i in tracks:
#         megaString+=i
#         megaString+='+'
#     megaString = megaString[0:-1]
#     os.system("copy /b "+megaString+" temp.mp3")
#     os.system("copy temp.mp3 out.mp3")
#     os.system("del temp.mp3")
#splitMp3('brianstorm.mp3',0.5)
#joinMp3('SplitFiles\\01split.mp3','SplitFiles\\13split.mp3','SplitFiles\\04split.mp3')
#
# def joinMp3(track1,track2,outputFile):
#     os.system('cd SplitFiles')
#     os.system('cd')
#     os.system('copy /b ' + track1 + '+' + track2 + ' ' + outputFile)
#     print('copy /b ' + track1 + '+' + track2 + ' ' + outputFile)
#     os.system('cd ..')

# #joinMp3('track1.mp3', 'track2.mp3', 'output.mp3')

#
# def joinMp3(track1,track2,outputFile):
#     #print('C:\\Users\\parth\\PycharmProjects\\HashCode17\\SplitFiles\\' + track1)
#     os.system('cd SplitFiles')
#     track1 = AudioSegment.from_mp3(track1)
#     track2 = AudioSegment.from_mp3(track2)
#     newOutputFile = track1 + track2
#     newOutputFile.export(outputFile,format='mp3')
#     os.system('cd ..')
#
# #joinMp3('track1.mp3', 'track2.mp3', 'output.mp3')
#
# def joinMp3(track1, track2, outputFile, directory = ''):
#         #os.system('cd SplitFiles\\')
#         os.chdir(directory)
#         os.system('cd')
#         os.system('copy /b ' + track1 + "+" + track2 + " temp.mp3")
#         os.system('copy /y temp.mp3 '+ outputFile)
#         os.system('del temp.mp3')
#         #os.system('cd ..')
#         os.chdir('..')
#         os.system('cd')
#         f = open('joinlogs.txt','a')
#         f.write(">>joined "+track2+'\n')
#         print(">>joined ", track2)

def joinMp3(track1, track2, outputFile,directory='.' ):
    os.chdir(directory)
    print(track1, '+', track2)
    try:
        os.remove('temp.mp3')
    except FileNotFoundError:
        pass
    finally:
        temp  =  open('temp.mp3','wb') #creates new temp file

    try:
        open(track1)
    except FileNotFoundError:
        open(track1,'wb')
    try:
        open(track2)
    except FileNotFoundError:
        open(track2,'wb')

    shutil.copyfileobj(open(track1,'rb'),temp)
    shutil.copyfileobj(open(track2, 'rb'), temp)
    temp.close()

    out  =  open(outputFile,'wb')
    shutil.copyfileobj(open('temp.mp3','rb'), out)
    out.close()
    os.remove('temp.mp3')
    os.chdir('..')