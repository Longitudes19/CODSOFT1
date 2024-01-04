# Password generator using python

import random
import string

password = ''
def generate_easy_password(length):
    global password
    characters = string.ascii_letters + string.digits
    for i in range(length):
        password = password + random.choice(characters)
    return password    

def generate_complex_password(length):
    global password
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        password = password + random.choice(characters)
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password greater than or equal to 5: "))
            if length < 5:
                raise ValueError("Length of the password should be greater than or equal to 5")
    
            complexity = input("Choose the complexity of the password as (easy/complex): ")
    
            if complexity not in ['easy','complex']:
                raise ValueError("Incorrect choice. The complexity of the password can either be easy/complex")
    
            if complexity == 'easy':
                password = generate_easy_password(length)
            elif complexity == 'complex':
                password = generate_complex_password(length)
            
            print('Generated Password: ', password)    
            break
        
        except ValueError as e:
            print(f'Error: {e}\n')
            continue
        
        
if __name__ == '__main__':
        main()    
            
        
            
        
        
        