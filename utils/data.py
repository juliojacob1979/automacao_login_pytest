from faker import Faker

fake = Faker()

def get_valid_user():
    return {"username": "usuario_teste", "password": "senha123"}

def get_invalid_user():
    return {"username": fake.user_name(), "password": fake.password()}
