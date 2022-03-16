# ddd-giuliano# ddd-karen-arcoverde
DDD - Backend - Giuliano Bontempo Domiciano

Link: https://ddd-silvermotors.herokuapp.com
***
## Índice

- [Atributos do cliente](#Cliente)
- [Rotas do Cliente](#Rotas)
- [Exemplos](#exemplos)

***

### Cliente
|Campo|Tipo|Argumentos|Descrição|
|-----|-----|-----|-----|
|email|string(70)|nullable(False), unique(True)|Email do usuário|
|senha_hash|string()|nullable(False)|Senha hashed do usuário|
|nome|string(150)|unique(True)|Nome do usuário|
|cpf|string(15)|nullable(False), unique(true|CPF do usuário|
|celular|string(20)|nullable(False), unique(True)|Celular do usuário|
|cep|string(20)|nullable(False)|CEP do usuário|
|endereço|string(150)||Endereço do usuário|
|complemento|string(30)||Complemento do endereço do usuário|
|data_de_nascimento|string(30)||data de nascimento do usuário|
|avatar|string(64)|unique(True)|Foto de identificação do usuário relacionada ao digital ocean|



***
## Rotas
|Endpoint|Método|Descrição|
|-----|-----|-----|
|/cliente/post|POST|Cadastra um novo cliente|
|/clienteget|GET|Mostra todos os clientes|
|/cliente/<int:id>|GET|Mostra um cliente específico (Requer o token daquele cliente)|
|/cliente/<int:id>|PATCH|Altera as informaçoes de um cliente específico (Requer o token daquele cliente)|
|/cliente/<int:id>|DELETE|Deleta um cliente específico (Requer o token daquele cliente)|
|/cliente/login|POST|Faz o login de cliente, recebendo um token de autenticação|

***
## Exemplos

### POST /login
```
{
    "email": "giuliano.domiciano@gmail.com",
    "senha": "123456789"
}
```
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNzY3Mzk0MiwianRpIjoiYzczYjY0MzEtMjk4Ni00YTUxLWJhNDEtOGIwZjQwY2IxMGFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjI3NjczOTQyLCJleHAiOjE2Mjc2NzQ4NDJ9.GS16yvd8gkkWjdhV09DDMtz9Qedd0rcQwJmjC1yNLq4"
}
