from time import time_ns
from string import ascii_lowercase

#this function is used to compare two strings
def compare(string_1,string_2):
    if len(string_1)!=len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i]!=string_2[i]:
            return False
    return True

#this function takes password entered by user and compare it with the actual password
def login(user_password):
    password='abcdef'
    if compare(password,user_password):
        return "User access"
    return "User has not access"

# alphaNumeric=list(ascii_lowercase)
# {alphaNumeric.append(i) for i in range(10)}

#In this function we take each letter fromm a-z form a string and compare it with the actual pasword and record time taken by string from by using that charcater  
def cracked_letter(cracked,padding):
    '''
     time_result is a dictionary which stores time taken by each character
     key -> character
     value -> time taken in nano seconds
    '''
    time_result = {i:0 for i in ascii_lowercase}
    # This loop runs 10000 time so that we can get that time difference 
    for _ in range(10000):
        for letter in ascii_lowercase:
            '''
                forming a string(input_string) that needs to be compared with the actual password 
                input_string is formed by concatining the character with the string that we have cracked till now
            '''
            input_string=cracked+"-" * padding
            start=time_ns()
            login(input_string)
            end=time_ns()
            time_result[letter]+=(end-start)
    return sorted(time_result,key=time_result.get,reverse=True)[0]

#padding_length is the length of the password
#for now I am taking only passwords formed using the characters (a-z)
padding_length=6
cracked_letters=''

for _ in range(padding_length):
    next_letter=cracked_letter(cracked_letters,padding_length)
    cracked_letters+=next_letter
    padding_length-=1
    print(cracked_letters)
