import pygn
#Run only once
clientID = "1625994239-37C1C781B14052037E2D62A8A208CEDE"
#userID = pygn.register(clientID)
IDFile = open('userID','r')
userID = IDFile.readline()

# metadata = pygn.search(clientID=clientID, userID=userID, track='idfc')
# print(metadata)
#
# pl = pygn.createRadio(clientID=clientID, userID=userID, artist='Eagles', track='', mood='', era='', genre='', popularity ='', similarity = '', count='5')
# #pl = pygn.createRadio(clientID=clientID, userID=userID, artist='', track='Brianstorm', count='5')
# for i in pl:
#     print(i)