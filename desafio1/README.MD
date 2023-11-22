# Desafio 1

Este desafio consiste em um criação de um programa capaz de ler e escrever informações em um arquivo `config.json`.

## Requerimento

- Python 3

## Executando o projeto

Para incializar o projeto, abra o prompt de comando e execute o comando:

```bash
python3 app.py
```

### Informações para testes

O programa foi escrito em Python puro e possui uma interface no prompt de comando. Há duas opções possivels: 1. Ler configurações e 2. Escrever configurações.

A opção 1, faz a leitura do arquivo `config.json` e exibe as informações na tela. Caso o arquivo não exista, o mesmo é criado no diretório raiz do projeto com conteúdo vazio. Caso o arquivo exista e esteja vazio, o programa exibe uma mensagem informa que a ausência de informações.

Já a opção 2, o programa vai exigir entrada de 3 informações seguindo a ordem: nome do servidor, endereço ip do servidor e senha do servidor. Uma atenção ao endereço do servidor pois o sistema está verificando se está sendo passado no formato IPv4, e enquanto essa condição não for satisfeita o programa continuará pendindo para informar o endereço de ip.

No meu principal, para sair da aplicação use a opção 0 ou tecle `Ctrl+C`. Caso qualquer outra entrada diferente de 1, 2 ou 3 seja digitado, é exibido uma mensagem de opção inválida.

## Autor

Criado por José `ArseniumGX` Macedo

## Licença

Este projeto está licenciado sob a [Licença MIT](../LICENSE).
