# import all the library used
import re, urllib, os, sys

# determine python version
version = sys.version_info[0]

# set user_input and import modules for correct version of python
if version == 2:  # python 2.x
    user_input = raw_input
    import urllib2

    urlopen = urllib2.urlopen  # open a url
    encode = urllib.urlencode  # encode a search line
    retrieve = urllib.urlretrieve  # retrieve url info
    cleanup = urllib.urlcleanup()  # cleanup url cache

else:  # python 3.x
    user_input = input
    import urllib.request
    import urllib.parse

    urlopen = urllib.request.urlopen
    encode = urllib.parse.urlencode
    retrieve = urllib.request.urlretrieve
    cleanup = urllib.request.urlcleanup()

# function to retrieve video title from provided link
def video_title(url):
    try:
        webpage = urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'

    return title

# download directly with a song name or link
def single_download(n,song=None):
    if not (song):
        song = sys.argv[1]

    if "youtube.com/" not in song:
        # try to get the search result and exit upon error
        try:
            query_string = encode({"search_query": song})
            html_content = urlopen("http://www.youtube.com/results?" + query_string)

            if version == 3:  # if using python 3.x
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            else:  # if using python 2.x
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read())
        except:
            print('Network Error')
            return None

        # make command that will be later executed

        formatType = '\"' + str(n) + "down.mp3\""
        command = 'youtube-dl.exe --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o '+formatType+" "+ \
                  search_results[0]
        print (command)
        #command = 'youtube-dl.exe --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 --auto-number' + search_results[0]

    try:  # Try downloading song
        print('Downloading %s' % song)
        os.system(command)
        # print(">> moving song to DownAudio")
        # os.system('move *down.mp3 DownAudio\\')
        print(">> moving song to SplitFiles")
        os.system('move ' + str(n) + 'down.mp3 SplitFiles\\')
    except:
        print('Error downloading %s' % song)
        return None

def downloadYouTubeAudio(n,searchQuery):
    single_download(n,searchQuery)
    #sys.exit(0)

#downloadYouTubeAudio(1,'When The Sun Goes Down Arctic Monkeys')