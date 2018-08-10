
# String -> String
# Encrypt the given string with the loaded cipher
char_lookup = {}


# File Name -> (None)
# Read the given file, load the char_lookup with the
# indicated key
def load_cipher(f_name):
    global char_lookup
    ff = open(f_name)
    lines = ff.readlines()
    for line in lines:
        char_lookup[line[2]] = line[0]
    ff.close()

def decrypt(string):
    cipher = ''
    for char in string:
        if ord(char) in range(ord('A'), ord('Z')+1) or\
           ord(char) in range(ord('a'), ord('z')+1):
            cipher += char_lookup[char]
        else:
            cipher += char

    return cipher

            
       
    


            
