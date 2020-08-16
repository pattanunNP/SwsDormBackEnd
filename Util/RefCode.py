import random 
import string

class refCode:

    @staticmethod
    def gennerate_refcode(roomcode,roomnumber,studentid):
        refCode = f"{roomcode}{roomnumber}{studentid}"
        return refCode

    
    @staticmethod
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        print("Random alphanumeric String is:", result_str)
        return result_str
