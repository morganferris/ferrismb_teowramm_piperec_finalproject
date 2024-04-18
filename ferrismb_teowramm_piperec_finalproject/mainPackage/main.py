# Name: Elizabeth Piper, Morgan Ferris, Mikaela Teowratanakul
# email: piperec@mail.uc.edu, ferrismb@mail.uc.edu, teowramm@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date: April 23rd, 2024
# Course/Section: IS 4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment where we have to decode to messages and upload an image based on that encryption
# Brief Description of what this module does: This module calls all of the functions 
# Citations:
# Anything else that's relevant:
from decryptionPackage.decryption import *

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
    english_file = "../UCEnglish.txt"
    decrypted_location = decrypt_location(encrypted_data, english_file)
    print("Decrypted location:", decrypted_location)
    
    # Decrypting the movie name
    key = b'bTkQSmlNDEfiNJCuSuyUq0PPtiH-DDUwiGLCjlVw6uY='
    encrypted_movie_name = b'gAAAAABlTNM6kuAuHJGUgPDEJcJX-feG_KgWzOGnZVsWMDDKGXjvuo7WgC8aAXO1oCJS7ItK-C6zHejJBJDLQ1OBbxZEoO-t5g=='
    decrypted_movie_name = decrypt_message(encrypted_movie_name, key)
    print("Decrypted Movie Name:", decrypted_movie_name)
    
    my_image = load_image("../FinalProject.jpeg")
    if my_image:
        my_image.show()
    else:
        print("Error: Failed to load the image.")
    

