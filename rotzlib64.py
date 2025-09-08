import base64
import zlib
import binascii
import codecs

def text_to_decimal(text):
    """Convert each character in the text to its decimal ASCII representation."""
    try:
        return ' '.join(str(ord(char)) for char in text)
    except Exception as e:
        print(f"Error in text_to_decimal: {e}")
        return ""

def decimal_to_text(decimal_text):
    """Convert decimal ASCII values back to text with error handling."""
    try:
        return ''.join(chr(int(num)) for num in decimal_text.split() if num.isdigit())
    except ValueError as e:
        print(f"ValueError in decimal_to_text: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error in decimal_to_text: {e}")
        return ""

def decimal_to_rot13(decimal_text):
    """Apply ROT13 to the decimal ASCII text."""
    try:
        text = decimal_to_text(decimal_text)
        rot13_text = codecs.encode(text, 'rot_13')
        return ' '.join(str(ord(char)) for char in rot13_text)
    except Exception as e:
        print(f"Error in decimal_to_rot13: {e}")
        return ""

def rot13_to_decimal(rot13_text):
    """Reverse ROT13 transformation from decimal ASCII text back to original decimal text."""
    try:
        text = decimal_to_text(rot13_text)
        original_text = codecs.decode(text, 'rot_13')
        return ' '.join(str(ord(char)) for char in original_text)
    except Exception as e:
        print(f"Error in rot13_to_decimal: {e}")
        return ""

def rot13_to_base64(rot13_text):
    """Encode ROT13 text in base64."""
    try:
        byte_array = bytearray(int(num) for num in rot13_text.split() if num.isdigit())
        return base64.b64encode(byte_array).decode('utf-8')
    except ValueError as e:
        print(f"ValueError in rot13_to_base64: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error in rot13_to_base64: {e}")
        return ""

def base64_to_rot13(base64_text):
    """Decode base64 text back to ROT13 decimal ASCII."""
    try:
        byte_array = base64.b64decode(base64_text)
        return ' '.join(str(byte) for byte in byte_array)
    except binascii.Error as e:
        print(f"Base64 decoding error in base64_to_rot13: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error in base64_to_rot13: {e}")
        return ""

def base64_to_zlib(base64_text):
    """Compress base64 encoded text using zlib."""
    try:
        base64_bytes = base64_text.encode('utf-8')
        return zlib.compress(base64_bytes)
    except Exception as e:
        print(f"Error in base64_to_zlib: {e}")
        return b""

def zlib_to_base64(zlib_data):
    """Decompress zlib data back to base64 encoded text."""
    try:
        decompressed_data = zlib.decompress(zlib_data)
        return decompressed_data.decode('utf-8')
    except zlib.error as e:
        print(f"Zlib decompression error in zlib_to_base64: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error in zlib_to_base64: {e}")
        return ""

def zlib_to_inflate_hex_decimal(zlib_data):
    """Convert zlib-compressed data to inflated hex, then to decimal."""
    try:
        hex_data = binascii.hexlify(zlib_data).decode('utf-8')
        return ' '.join(str(int(hex_data[i:i+2], 16)) for i in range(0, len(hex_data), 2))
    except Exception as e:
        print(f"Error in zlib_to_inflate_hex_decimal: {e}")
        return ""

def inflate_hex_decimal_to_zlib(hex_decimal):
    """Convert inflated hex decimal back to zlib data."""
    try:
        hex_data = ''.join(f"{int(num):02x}" for num in hex_decimal.split() if num.isdigit())
        return binascii.unhexlify(hex_data)
    except ValueError as e:
        print(f"ValueError in inflate_hex_decimal_to_zlib: {e}")
        return b""
    except Exception as e:
        print(f"Unexpected error in inflate_hex_decimal_to_zlib: {e}")
        return b""

def encode_text(text):
    try:
        decimal_text = text_to_decimal(text)
        rot13_text = decimal_to_rot13(decimal_text)
        base64_encoded = rot13_to_base64(rot13_text)
        zlib_compressed = base64_to_zlib(base64_encoded)
        inflated_hex_decimal = zlib_to_inflate_hex_decimal(zlib_compressed)
        return inflated_hex_decimal
    except Exception as e:
        print(f"Error in encode_text: {e}")
        return ""

def decode_text(encoded_text):
    try:
        zlib_compressed = inflate_hex_decimal_to_zlib(encoded_text)
        base64_encoded = zlib_to_base64(zlib_compressed)
        rot13_text = base64_to_rot13(base64_encoded)
        decimal_text = rot13_to_decimal(rot13_text)
        return decimal_to_text(decimal_text)
    except Exception as e:
        print(f"Error in decode_text: {e}")
        return ""

input_text = input("Enter the text to encode and decode: ")
encoded_text = encode_text(input_text)
print(f"Encoded Text: {encoded_text}")
decoded_text = decode_text(encoded_text)
print(f"Decoded Text: {decoded_text}")

if decoded_text == input_text:
    print("Encoding and decoding successful!")
else:
    print("Decoding failed: Original and decoded texts do not match.")