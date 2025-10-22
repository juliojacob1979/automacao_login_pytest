def login_api(username, password):
    # Simulação de endpoint de login (mock local)
    if username == "usuario_teste" and password == "senha123":
        return {"status": 200, "message": "Login realizado com sucesso"}
    elif not username or not password:
        return {"status": 400, "message": "Campos obrigatórios não preenchidos"}
    else:
        return {"status": 401, "message": "Credenciais inválidas"}
