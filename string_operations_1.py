text =  "Python is a programming language. Current version is 3. I am learning it."

sentences = 0 
words = 0

for i in range ( len ( text ) ) :
    if text[i] == "." :
        sentences += 1
    if text[i] == " " :
        words += 1

    # print ( text[i] )
print ( "Found sentences : " , sentences )  
print ( "Found words : " , words ) 