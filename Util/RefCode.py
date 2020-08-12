import random 


class refCode:

    @staticmethod
    def gennerate_refcode(roomcode,roomnumber,studentid):
        refCode = f"{roomcode}{roomnumber}{studentid}"
        return refCode