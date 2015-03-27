import twitter, datetime, urllib2

#Open Chrome History
currentSession = open("/Users/cchan/Library/Application Support/Google/Chrome/Default/Current Session")

#Read Last Session
lastSession = currentSession.read()

#My Twitter ID
user = 220193873

#Open Text File
file = open("TwitterCredentials.txt")

cred = file.readline().strip().split(",")

startIndex = lastSession.rfind("http")
endIndex = lastSession.find(chr(0), startIndex) 

#Get Page Address
url = lastSession[startIndex:endIndex]
print(url)

urlreceived = urllib2.urlopen(url) 
html = urlreceived.read()

#Get Content
beginTitle = html.find("<title>") + len("<title>")
finishTitle = html.find("</title>", beginTitle)
theTitle = html[beginTitle:finishTitle]

#Read Text File
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#Get Timestamp
timestamp = datetime.datetime.utcnow()

#Post Tweet
response = api.PostUpdate("My favourite Website is " + str(theTitle) + " at " + url + str(timestamp))

print("Status updated to: " + response.text) 

#Print the last Twitter Post
statuses = api.GetUserTimeline(user) 
print (statuses[0].text)