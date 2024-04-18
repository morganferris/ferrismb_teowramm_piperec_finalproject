import json
from cryptography.fernet import Fernet
from PIL import Image
import os,sys
from io import BytesIO



def decrypt_location(encrypted_data, english_file):
    with open(english_file, 'r', encoding='utf-8') as file:
        english_words = file.readlines()
    
    decrypted_location = ""
    for index in encrypted_data:
        try:
            line_number = int(index) # Adjusting to 0-based indexing
            decrypted_location += english_words[line_number].strip() + " "
        except IndexError:
            print(f"Index {index} is out of range.")
    
    return decrypted_location.strip()

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

def load_image(filename):
    '''
    load an image file from the disk
    @param: the file name, the file to load
    @return: the image object
    '''
    
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        
        return None
    return myimage
    


if __name__ == "__main__":


    encrypted_data = [

        "7480",

        "28894",

        "8018",

        "42049",

        "46049",

        "7487",

        "18797",

        "28898",

        "10953",

        "31563",

        "28799",

        "10355",

        "2756",

        "23887",

        "30997",

        "42547",

        "5209",

        "42686",

        "14761",

        "38919"

        ]
    english_file = "C:/Users/teowramm/git/ferrismb_teowramm_piperec_finalproject/ferrismb_teowramm_piperec_finalproject/UCEnglish.txt"
    decrypted_location = decrypt_location(encrypted_data, english_file)
    print("Decrypted location:", decrypted_location)
    
    # Decrypting the movie name
    key = b'bTkQSmlNDEfiNJCuSuyUq0PPtiH-DDUwiGLCjlVw6uY='
    encrypted_movie_name = b'gAAAAABlTNM6kuAuHJGUgPDEJcJX-feG_KgWzOGnZVsWMDDKGXjvuo7WgC8aAXO1oCJS7ItK-C6zHejJBJDLQ1OBbxZEoO-t5g=='
    decrypted_movie_name = decrypt_message(encrypted_movie_name, key)
    print("Decrypted Movie Name:", decrypted_movie_name)
    
    my_image = load_image("C:/Users/teowramm/git/ferrismb_teowramm_piperec_finalproject/ferrismb_teowramm_piperec_finalproject/FinalProject.jpeg")
    if my_image:
        my_image.show()
    else:
        print("Error: Failed to load the image.")

    
    
    

    


