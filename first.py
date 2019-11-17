def encode(string):
    l=len(string)
    encoded_string=[]
    for i in range(l):
        encoded_string.append(string[i])
        encoded_string.append('#')
    return(encoded_string)
def decode(string):
    l=len(string)
    decoded_string=[]
    for i in range(l):
        if i%2==0:
            decoded_string.append(string[i])
    return(decoded_string)
for i in range(10):
    print(i)
print(encode("chat"))
l=['a','b','g','#']
print(decode(encode("chat")))
str=''
k=encode("chat")
for i in range(len(k)):
    str=str+k[i]
print(str)
