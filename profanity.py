import urllib.request

def read_file():
    name = input ("Guess file name :")
    file = open(r"D:\Udacity\movie_quotes.txt")
    contents_of_file = file.read()
    print (contents_of_file)
    file.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_read):
       encoded_text = urllib.parse.quote (text_to_read, 'utf-8')
       connection = urllib.request.urlopen ("http://www.wdylike.appspot.com/?q="+encoded_text)
       output = connection.read()
       print (output)
       if b'true' in output:
           print ("Profanity Alert")
       elif b'false' in output:
           print ("The document has no curse words")
       else:
           print ("Couln't scan the document properly")
       connection.close()

read_file()
    
