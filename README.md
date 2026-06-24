<div align="center">

# WhatsApp-Bulk-Sender

</div>

## (English 🇺🇸) About

Python-based automation system for sending WhatsApp messages through Evolution API, supporting multiple instances and JSON-driven message flows. 

Primarily, this script is designed to simulate conversations between instances created in the Evolution API.

## Prerequisites

Before running this project, you must already have a running [Evolution API](https://docs.evolutionfoundation.com.br/evolution-api/installation) instance.
The system depends on it for sending messages via WhatsApp.

This project is designed specifically to work with **Evolution API running in a Docker environment**, it is not guaranteed to work with standalone installations or other deployment methods.

Make sure you have:

- A working Evolution API server;
- At least one connected WhatsApp instance;
- Redis enabled and running (required by Evolution API).

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/GabHrq/WhatsApp-Bulk-Sender/
cd whatsapp-bulk-sender
```

### 2. Create virtual environment
```bash
python3 -m venv venv
```

### 3. Activate environment

> Linux / Mac OS
```bash
source venv/bin/activate
```

> Windows
```bash
venv\Scripts\activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configuration
Create a .json file (default name example: data.json) with the following structure:
```bash
{
  "instances": [
    {
      "name": "(...)",
      "phone": [
        "55(...)"
      ]
    }
  ],
  "texts": [
    "(...)"
  ]
}
```
An example is already provided inside this repository, so you can use it as a basis. A phone number string **must** start with "55".

### 6. Usage
Run the script:
```bash
python script.py
```

## To-do

- [x] Automated message sending via Evolution API
- [ ] Scheduled message delivery (APScheduler)
- [ ] Automatic instance rotation


## (Português 🇧🇷) Sobre
Sistema de automação em Python para envio de mensagens via WhatsApp utilizando Evolution API, com suporte a múltiplas instâncias e fluxos de mensagens baseados em JSON.

Principalmente, este script deve simular conversas entre instâncias criadas no Evolution API.

## Pré-requisitos

Antes de executar este projeto, é necessário que já tenha uma instância do [Evolution API](https://docs.evolutionfoundation.com.br/evolution-api/installation) em execução.
É necessário para que seja possível enviar mensagens pelo WhatsApp.

O projeto foi desenvolvido especificamente para funcionar com **Evolution API executando em contêiner Docker**, portanto não é garantido que funcione com outros tipos de instalação desta API.

Certifique-se de possuir:

- Um servidor com Evolution API operando corretamente;
- Pelo menos uma instância do WhatsApp conectada;
- Redis ativado e em execução (exigido pelo Evolution API).

## Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/GabHrq/WhatsApp-Bulk-Sender/
cd whatsapp-bulk-sender
```

### 2. Criar ambiente virtual
```bash
python3 -m venv venv
```

### 3. Ativar ambiente

> Linux / Mac OS
```bash
source venv/bin/activate
```

> Windows
```bash
venv\Scripts\activate
```
### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Configuração
Crie um arquivo .json (exemplo de nome padrão: "data.json") com a seguinte estrutura:
```bash
{
  "instances": [
    {
      "name": "(...)",
      "phone": [
        "55(...)"
      ]
    }
  ],
  "texts": [
    "(...)"
  ]
}
```
Um exemplo de arquivo foi providenciado neste repositório, portanto é possível usar como base. A string contendo um número de telefone **deve** começar com "55".

### 6. Usage
Execute o script:
```bash
python script.py
```

## A fazer

- [x] Envio de mensagens automatizado via Evolution API
- [ ] Agendamento de envio de mensagens (APScheduler)
- [ ] Revezamento automático de instâncias
