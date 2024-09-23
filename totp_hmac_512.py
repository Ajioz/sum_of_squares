import hmac
import hashlib
import time
import struct

def generate_totp(email, secret_suffix, time_step=30, digits=10, hash_algorithm=hashlib.sha512):
    # Combine email with secret suffix
    secret = f"{email}{secret_suffix}".encode()

    # Get the current time and divide by the time step
    current_time = int(time.time() / time_step)
    
    # Convert time into a byte array (8-byte integer)
    time_bytes = struct.pack(">Q", current_time)
    
    # Create HMAC-SHA-512 hash using the secret and time
    hmac_hash = hmac.new(secret, time_bytes, hash_algorithm).digest()

    # Dynamic truncation to get a 4-byte string (RFC6238)
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset + 4]

    # Convert truncated hash to an integer
    code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    
    # Reduce the code to the desired number of digits
    totp_password = code % (10 ** digits)
    
    # Zero-pad the result if necessary
    return f"{totp_password:0{digits}}"

# Usage
email = "sunny.ajiroghene@gmail.com"
secret_suffix = "HENNGECHALLENGE003"
totp_password = generate_totp(email, secret_suffix)
print(f"TOTP Password: {totp_password}")
