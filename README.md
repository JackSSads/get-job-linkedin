# Get Jobs Linkedin

Este projeto utiliza Selenium para automatização, Flask para a criação de um servidor web, Openpyxl para manipulação de arquivos Excel, e Pandas para análise de dados. O objetivo é realizar scraping de vagas de emprego no LinkedIn e enviar as informações para um número de telefone via WhatsApp Web.

## Dependências do projeto
    • Selenium
    • Falsk
    • Openpyxl
    • Pandas
As dependências devem ser instaladas dentro do ambiente virtual (``venv``) do projeto.


## Ativando o ambiante virtual
No Windows:
```bash
    venv\scripts\activate
```

No macOS/Linux:
```bash
    source venv/bin/activate
```

## Instalando dependências
As dependências devem ser instaladas utilizando o gerenciador de pacotes ``pip``.
Instale as dependências executando o comando abaixo:

```bash
    pip install -r requirements.txt
```

## Iniciando o projeto

Para iniciar o servidor, execute o seguinte comando:

```bash
    py server.py
```

O servidor irá rodar localmente na porta ``8888``

### Endpoint

    ["POST"]/robo

No corpo da requisição, deve haver um objeto JSON com as seguintes informações:

```bash
    {
        "username": "seu_email_do_linkedin",
        "password": "sua_senha",
        "search": "palavras_da_busca",
        "phone": numero_pra_onde_será_mandado_as_vagas
    }
```

*O número deve respeitar a exigência de 13 dígitos no seguinte formato: ``código do país + código de área + número contendo 9 dígitos``. Ex.: ``5511123456789``.*

OBS.: Caso seu LinkedIn não esteja autenticado no seu navegador, será preciso informar o código de validação, que é enviado para seu e-mail. Isso fará com que o navegador seja adicionado à lista de dispositivos confiáveis do seu LinkedIn.

## Atenção
### *Fique atento, pois será necessário que você faça login no WhatsApp Web com seu dispositivo.*

## Saída
Ao executar todos os passos corretamente, iniciará o processo de scraping no site do LinkedIn e, logo em seguida, iniciará o envio das mensagens para o número especificado.