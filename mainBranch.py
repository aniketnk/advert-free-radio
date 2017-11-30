import os
import editMp3 as edit
import ACRCloudCaller as acr
import delSF
import pygn
import getmp3

#for pygy
clientID = '1625994239-37C1C781B14052037E2D62A8A208CEDE'
userID = '48231282036076642-593EA2BA7F2F5069143C6E8EB0BA4374'

def getForPygy(artistToGenerate):
    #print(trackToGenerate)
    #global listOfSongs=[]
    playlist = pygn.createRadio(clientID=clientID, userID=userID, artist=artistToGenerate, track='', mood='', era='', genre='', popularity ='', similarity = '', count=noOfDownloads)
    #pl = playlist.copy()
    print(type(playlist))
    for song in playlist:
        songDict = dict(song)
        returnYouTubeSearch = songDict['track_title']+' '+songDict['album_artist_name']
        getmp3.downloadYouTubeAudio(playlist.index(song)+1,returnYouTubeSearch)


mainMp3 = 'tuneIn_samplecut.mp3' #sys.argv[1]

delSF.deleteFilesFrom(directory='SplitFiles')
delSF.deleteFilesFrom(directory='DownAudio')

f = open('AdOrNot.txt', 'w')
fjoin = open('joinlogs.txt','w')


noOfFiles = edit.splitMp3(mainMp3,0.5)
generatePlaylistFlag = 0
countIndexForDown = 1
noOfDownloads = '4'

#os.system('copy silence.mp3 SplitFiles\\out.mp3')
os.chdir('SplitFiles')
open('out.mp3','w')
os.chdir('..')

flagIsAdv = 0

for i in range(1,noOfFiles):
    fileNameString = "SplitFiles\\"
    fileNameString += "0" if i<10 else ""
    fileNameString += str(i) + "split.mp3"

    meta = acr.getMeta(fileNameString)
    # print(meta.startswith("{\"status\":{\"msg\":\"Success\""))
    #print(fileNameString, meta)
    if meta.startswith("{\"status\":{\"msg\":\"Success\""):#if it's a song
        flagIsAdv = 0
        f.write("<SONG>\n")
        edit.joinMp3("out.mp3",fileNameString[11:],"out.mp3", directory='SplitFiles')
        fjoin.write("out.mp3 + " + fileNameString[11:] + '\n')
        if generatePlaylistFlag == 0:
            artist = meta[meta.index("artists"):]
            artist = artist[artist.index(":\"") + 2:]
            artist = artist[:artist.index("\"")]
            getForPygy(artist)
            generatePlaylistFlag +=1
    else:
        f.write("<AD>\n")
        if generatePlaylistFlag == 0:
            continue
        elif flagIsAdv==0:
            f.write("<<Add Downloaded Song>>\n")
            #append song from playlist
            DtrackName = str(countIndexForDown) + "down.mp3"
            edit.joinMp3("out.mp3",DtrackName,"out.mp3", directory='SplitFiles')
            fjoin.write("out.mp3 + " + DtrackName + '\n')
            # os.system('move SplitFiles\\out.mp3 DownAudio\\')
            # edit.joinMp3("out.mp3", DtrackName, "out.mp3", directory="DownAudio")
            # os.system('move DownAudio\\out.mp3 SplitFiles\\')
            countIndexForDown += 1
            flagIsAdv += 1
        else:
            f.write("<<Do nothing>>\n")
            pass

os.system('cd')
os.system(r'copy /y SplitFiles\out.mp3 outputAudio.mp3')
try:
    os.system('start outputAudio.mp3')
except:
    pass





