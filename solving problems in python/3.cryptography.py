user_input = input("Enter e for encryption or Enter d for decrption: ")
user_text = input("Enter the string: ")

#function for encoding a string

def encode(user_text):
    if user_input == 'e':
        text = user_text.encode()
        print("The encoded text is:", text)


#function for decoding
def decode(user_text):
    if user_input == 'd':
    
#encoding string  
        str = user_text.encode() 
    
        print ("The encoded string format is : ",) 
        print (str)
    
#printing the decode string
        print ("The decoded string is : ",) 
        print (str.decode('utf8', 'strict'))

encode(user_text)
decode(user_text)
