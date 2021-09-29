import base64
import re
import zlib
import configparser

##########################################
#                                        #
# SMART Card QR code decoder and encoder #
# Created: September 21st 2021           #
#                                        #
##########################################



def Base64UrltoNumeric(base64data):
    """ Takes a Base64Url encoded string and returns the SHC data that can be converted to QR"""

    result = 'shc:/'

    # Takes the Unicode representation of the char and appends it to 'result' string
    for x in base64data:
        result += str((ord(x)-45))

    return result

def NumericToBase64Url(qr_numeric_data):
    """Takes a comlete QR string and returns the Base64Url representation"""

    #Regex to start at the 5th element and make a list of groupings of two digits
    parts = re.findall('..', qr_numeric_data[5:])
    jws = ""

    # convert each double digit to Unicode representation
    for p in parts:
        jws += chr(int(p) + 45)

    return jws

def Base64UrlToJson(base64Url_data):
    """Takes the base64Url encoded string, decodes and decompresses data into plain readable JSON"""

    def decode(data):
        """Helper function to help decode the Base64URLtoJson (Not too sure whats going on here but it works)"""

        missing_padding = len(data) % 4
        if missing_padding:
            data += str(b'=') * (4 - missing_padding)
        return base64.urlsafe_b64decode(data)

    #Create a list with the 3 parts: Header, Payload, Signature
    jws_parts = list(map(decode, base64Url_data.split(".")))

    #Decompress the data (Not quite sure how to re-encode/reverse this)
    shc_data = zlib.decompress(jws_parts[1], wbits=-15)

    return shc_data


def main():

    #Decoding process: Numeric QR String -> Base64url -> RawDeflate -> Plain JSON data
    #Encoding Proccess: Plain JSON data -> RawInflate -> Base64Url -> Numeric QR string

    parser = configparser.ConfigParser()
    parser.read("config.txt")

    example_qr_data = parser.get("example_data", "qr_data")
    example_base64data = parser.get("example_data", "base_64_data")

    base64_data = NumericToBase64Url(example_qr_data)

    plain_JSON = ''
    plain_JSON = Base64UrlToJson(base64_data)

    new_qr_code = Base64UrltoNumeric(base64_data)

    print(plain_JSON)



if __name__ == "__main__":
    main()
