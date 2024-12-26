import secrets


def generate_code():
    numbers = '1234567'

    return ''.join(secrets.choice(numbers) for i in range(6))