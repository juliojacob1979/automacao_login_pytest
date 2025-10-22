Feature: Login do usuario

  Scenario: Login com sucesso
    Given que o usuario esta na pagina de login
    When ele informa usuario "student" e senha "Password123"
    Then ele deve ver a mensagem de sucesso "Logged In Successfully"

  Scenario: Login com usuario invalido
    Given que o usuario esta na pagina de login
    When ele informa usuario "invalid_user" e senha "Password123"
    Then ele deve ver a mensagem de erro "Your username is invalid!"

  Scenario: Login com senha invalida
    Given que o usuario esta na pagina de login
    When ele informa usuario "student" e senha "wrongpass"
    Then ele deve ver a mensagem de erro "Your password is invalid!"

  Scenario: Login com usuario vazio
    Given que o usuario esta na pagina de login
    When ele informa usuario "<vazio>" e senha "Password123"
    Then ele deve ver a mensagem de erro "Your username is invalid!"

  Scenario: Login com senha vazia
    Given que o usuario esta na pagina de login
    When ele informa usuario "student" e senha "<vazio>"
    Then ele deve ver a mensagem de erro "Your password is invalid!"
