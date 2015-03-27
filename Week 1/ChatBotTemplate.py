file = open("stop-words.txt")

#Read Text File
stopwords = file.readlines()

#Create Function to Remove Stop Words
def RemoveStopWords(message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " ", " ")
    return message

#Ask Question and Call Function After Input
while True:
    input = raw_input("What is your name? : ")
    input = " " + input + " "
    name = RemoveStopWords(input)
    print("Hello" + name)
    