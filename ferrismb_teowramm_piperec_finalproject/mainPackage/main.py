
from decryptionPackage.decryption import *

if __name__ == "__main__":


    encrypted_data = ["20842", "46853"]
    english_file = "UCEnglish.txt"
    decrypted_location = decrypt_location(encrypted_data, english_file)
    print("Decrypted location:", decrypted_location)
