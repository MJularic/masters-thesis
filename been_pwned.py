import requests
import hashlib


class BeenPwned:

    def __init__(self, password):
        self.password = password

    def is_pwned(self):
        sha1_password = hashlib.sha1(self.password.encode())
        hash = sha1_password.hexdigest()
        hash = hash.upper()
        hash_list = list(hash)

        first_5_chars = ""

        for i in range(5):
            first_5_chars = first_5_chars + hash_list[i]

        data = requests.get(url="https://api.pwnedpasswords.com/range/" + first_5_chars)

        lines = data.text.split("\n")

        for line in lines:
            h, num_of_occurence = line.split(":")
            if (first_5_chars + h) == hash:
                return num_of_occurence
        return 0
