## Introdução

Essa parte da aplicação é para testar as requisições a partir de um cliente, passando para um controle e finalmente um server.

## Rodando a aplicação

Inicie o backend da aplicação na outra pasta
```
docker-compose build
docker-compose run web python manage.py migrate
docker-compose up
```

Execute o arquivo criar_banco.py para criar um simples banco sqlite.

```
python3 criar_banco.py
```

Finalmente pode executar o cliente

```
python3 cliente.py
```