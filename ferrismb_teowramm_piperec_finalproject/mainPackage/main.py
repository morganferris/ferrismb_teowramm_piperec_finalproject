
from decryptionPackage.decryption import *

if __name__ == "__main__":


    encrypted_data = ["20842", "46853"]
    english_file = "C:/Users/teowramm/git/ferrismb_teowramm_piperec_finalproject/ferrismb_teowramm_piperec_finalproject/UCEnglish.txt"
    decrypted_location = decrypt_location(encrypted_data, english_file)
    print("Decrypted location:", decrypted_location)
    

