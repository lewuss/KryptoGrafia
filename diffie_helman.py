import random
import sympy


def diffie_hellman_key_exchange():
    prime = 9929843971
    primitive_root = sympy.primitive_root(prime)

    alice_private_key = random.randint(2, prime - 1)
    bob_private_key = random.randint(2, prime - 1)

    alice_public_key = pow(primitive_root, alice_private_key, prime)
    bob_public_key = pow(primitive_root, bob_private_key, prime)

    alice_shared_secret = pow(bob_public_key, alice_private_key, prime)
    bob_shared_secret = pow(alice_public_key, bob_private_key, prime)

    if alice_shared_secret == bob_shared_secret:
        print('keys are equal')
        return alice_shared_secret
    else:
        print('keys are not equal')
        return 0


if __name__ == "__main__":
    shared_secret = diffie_hellman_key_exchange()
    print(f"Shared Keys {shared_secret}")
