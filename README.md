# Get Jobs Linkedin

## Dependências do projeto
    • Selenium
    • Falsk
    • Openpyxl
    • Pandas
As dependências devem ser instaladas dentro da ``venv`` do projeto


## Ativando o ambiante virtual
No Windows:
```bash
    venv\scripts\activate
```

No IOS/Linux:
```bash
    venv/bin/activate
```

## Instalando dependências
As dependências devem ser instaladas utilizando um gerenciador de pacotes como o ``pip``

Selenium
```bash
    pip install selenium
```
Falsk
```bash
    pip install flask
```
Openpyxl
```bash
    pip install openpyxl
```
Pandas
```bash
    pip install pandas
```

## Iniciando o projeto

```bash
    py server.py
```

O servidor irá rodar localmente na porta ``8888``

### Endpoint

    /robo

No corpo da requisição, deve ter um objeto JSON com as seguntes informações:

```bash
    {
        "username": "seu_email_do_linkedin",
        "password": "sua_senha",
        "search": "palavras_da_busca",
        "phone": numero_pra_onde_será_mandado_as_vagas
    }
```

*O número deve respeitar a exigência de 13 digitos no seguinte formato: ``código do país + código de área + número contendo 9 dígitos``. EX.: ``5511123456789``.*

Caso seu linkedin não esteja altenticado no seu navegador, será preciso informar o código de validação, que é enviado para seu e-mail, junto ao corpo da requisição.

```bash
    {
        ...
        "validation": codigo_de_validação
    }
```