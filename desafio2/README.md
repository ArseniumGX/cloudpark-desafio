# API Rest Desafio CloudPark

API responsável por fazer os cadastros e
operação com veículos de um estacionamento.

## Pré requisitos

- Python 3
- PIP
- Django 4
- Django Rest Framework
- SQLite

## Preparando ambiente

Este passo leva em conta que você tem o ambiente de desenvolvimento Django com Rest Framework instalado globalmente. Caso nçao tenha verifique as respectivas documentações sobre como instalar o ambiente ou siga as instrução do subitem abaixa e volte aqui novamente no próximo paragrafo.

Estando no diretório root do projeto, abra o terminal no mesmo diretorio e execute o comandos abaixo:

```bash
python manage.py makemigrations
python manage.py migrate
```

O primeiro comando vair criar as migrations do projeto baseado nos models do projeto. Caso seja bem sucedido um arquino `.py` será criado no diretorio `cloudpark > migrations` com o conteúdo de criação das tabelas no banco de dados. O comando seguinte cria efetivamento todos as tabelas no banco de dados SQLite.

Passado esse primeiro passo, você pode configurar o Site Admin do django para testar as operações diretamente na interface. Este passo é opcional, mas caso queira seguir execute o comando abaixo e siga as instruções:

```bash
python manage.py createsuperuser
```

Após isso a aplicação está pronta para execução. Execute o comando abaixo:

```bash
python manage.py runserver
```

A aplicação será iniciada em localhost na porta 8000. Para acessar o Site Admin do djando acesse `http://localhost:8000/admin` e entre com o usuário e senha configurados anteriormente caso tenha optado em seguir os passos mensionados.

Com isso o ambiente está pronto para testes.

### VENV

Caso use ou prefira utilizar o ambiente virtual do python (venv) execute o comando no terminal para criar o ambiente:

```bash
python -m venv venv

```

Feito isso utilize o comando de ativação. No Windows use:

```bash
.\venv\Scripts\activate

```

Caso utilize Linux/macOS execute:

```bash
source venv/bin/activate

```

Com o ambiente ativo, utilize o comando para a instalar as dependências do projeto:

```
pip install django djangorestframework
```

Após isso, execute os passos do item acima.

## Testando a API

Com a aplicação rodando, os recursos da api estã acesse o endereço `http://localhost:8000/api/v1`. A partir deste endereço é possível acessar os recurso `/customer`, `/vehicle`, `/plan`, `/customerplan`, `/contract`, `/contractrule` e `/parkmoviment`. Por padrão, e por uma questão de testes internos, optei manter a requisição GET do root desses recursos.

O projeto possui um [arquivo](./insomnia_cloudparkapi_test.yaml) com os testes já pronto para execução na aplicação Insomnia para caso deseje utilizar.

### Customer

url: `http://localhost:8000/api/v1/customer`
methods: GET, POST, PUT
body:

```json
{
	"name": "John Doe",
	"card_id": "ASF126S1SA"
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/customer/:id`

### Customer

url: `http://localhost:8000/api/v1/vehicle`
methods: GET, POST, PUT
body:

```json
{
	"plate": "ASD12C1231",
	"model": "Ford Focus Fastback",
	"description": "Cor preto ano 2021",
	"customer_id": null
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/vehicle/:id`

### Plan

url: `http://localhost:8000/api/v1/plan`
methods: GET, POST, PUT
body:

```json
{
	"description": "Executivo",
	"value": 219.89
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/plan/:id`

### CustomerPlan

url: `http://localhost:8000/api/v1/customerplan`
methods: GET, POST, PUT
body:

```json
{
	"due_date": null,
	"customer_id": 1,
	"plan_id": 1
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/customerplan/:id`

### Contract

url: `http://localhost:8000/api/v1/contract`
methods: GET, POST, PUT
body:

```json
{
	"description": "Rotativo",
	"max_value": 89.9
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/contract/:id`

### ContractRule

url: `http://localhost:8000/api/v1/contractrule`
methods: GET, POST, PUT
body:

```json
{
	"until": 3,
	"value": 30.5,
	"contract_id": 1
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/contractrule/:id`

### ParkMoviment

url: `http://localhost:8000/api/v1/parkmoviment`
methods: GET, POST, PUT
body:

```json
{
	"entry_date": "2023-11-22T00:00:00Z",
	"exit_date": null,
	"value": null,
	"vehicle_id": 1
}
```

Para GET E PUT:
url: `http://localhost:8000/api/v1/parkmoviment/:id`

## Autor

Criado por José `ArseniumGX` Macedo.

## Licença

Este projeto está licenciado sob a [Licença MIT](../LICENSE).
