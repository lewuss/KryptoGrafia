import time
import hashlib
from random import choice
from string import ascii_letters, digits


def hash_input(input_str, algorithm):
    hasher = hashlib.new(algorithm)
    hasher.update(input_str.encode("utf-8"))
    return hasher.hexdigest()


if __name__ == "__main__":
    # input_str = ''.join(choice(ascii_letters + digits) for _ in range(500))
    # input_str2 = ''.join(choice(ascii_letters + digits) for _ in range(500))
    input_str = 'teststring'
    input_str2 = 'ueststring'
    ##input_str = "wdbp"
    algorithms = [
        # "md5",
        # "sha1",
        # "sha256",
        "sha3_512",
    ]

    for algorithm in algorithms:
        start_time = time.time()
        hash_value = hash_input(input_str, algorithm)
        time_passed = time.time() - start_time
        print(f"{algorithm.upper()}: {hash_value}. Done in {time_passed}")
        int_value = int(hash_value, 16)
        binary = bin(int_value)[2:]

        start_time = time.time()
        hash_value2 = hash_input(input_str2, algorithm)
        time_passed = time.time() - start_time
        print(f"{algorithm.upper()}: {hash_value2}. Done in {time_passed}")
        int_value2 = int(hash_value2, 16)
        binary2 = bin(int_value2)[2:]

        print(binary)
        print(binary2)

        colision_number = 0
        for i in range(12):
            if binary[i] == binary2[i]:
                colision_number += 1
        print(f"Number of colisons: {colision_number}")
        number_of_changes = 0
        for i in range(len(binary)):
            if binary[i] != binary2[i]:
                number_of_changes += 1

        print("% bitów które się zmieniły przy zamianie t na u - ", number_of_changes*100 / len(binary))
