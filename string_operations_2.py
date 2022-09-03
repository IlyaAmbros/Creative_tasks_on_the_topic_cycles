message = "Hi, my phone number is 069123456!"
out = ""

for i in range ( len ( message ) ) :
    if message[i] in "1234567890" :
        out += "*"
    else :
        out += message[i]

print ( out )
