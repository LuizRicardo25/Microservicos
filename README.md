
# Introdução aos Microserviços

## O que são Microserviços?

Microserviços são um estilo arquitetônico de desenvolvimento de software que estrutura aplicações como uma coleção de serviços pequenos, independentes e modulares. Cada serviço executa um processo de negócio específico, funciona de maneira autônoma, e se comunica com outros serviços através de interfaces bem definidas, normalmente APIs.

### Características Principais

- **Independência**: Serviços podem ser desenvolvidos, implantados, e escalados independentemente.
- **Especialização**: Cada serviço é especializado em uma função ou recurso específico.
- **Descentralização**: Gestão descentralizada de dados e processos.
- **Flexibilidade Tecnológica**: Possibilidade de usar diferentes tecnologias e linguagens em serviços distintos.

## Diferença entre Microserviços e APIs Comuns

Enquanto microserviços e APIs são frequentemente discutidos juntos, eles representam conceitos distintos:

- **Microserviços**: Referem-se a uma abordagem arquitetônica para construir uma aplicação como um conjunto de serviços menores e independentes. Cada microserviço é focado em realizar uma função específica e se comunica com outros serviços.

- **APIs (Interface de Programação de Aplicações)**: São interfaces que permitem a comunicação entre diferentes peças de software. Em uma arquitetura de microserviços, os serviços frequentemente se comunicam entre si através de APIs, mas as APIs podem existir em muitos outros contextos e arquiteturas de software.

Em suma, microserviços utilizam APIs para interagir, mas a ideia de API é muito mais ampla e não se limita à arquitetura de microserviços.

## Como Iniciar com Microserviços

### Passo 1: Compreensão dos Fundamentos

Antes de mergulhar na criação de microserviços, é crucial entender os princípios fundamentais e as motivações por trás dessa abordagem arquitetônica. Livros como "Building Microservices" de Sam Newman podem ser uma excelente introdução.

### Passo 2: Definição do Domínio e Design

- Identifique os limites de domínio da sua aplicação. Isso ajudará a definir os serviços.
- Projete cada microserviço para ser autônomo e responsável por uma parte específica da funcionalidade de negócios.

### Passo 3: Escolha das Tecnologias

Decida as tecnologias e linguagens de programação adequadas para cada serviço. Microserviços oferecem a flexibilidade de combinar várias tecnologias em uma única aplicação.

### Passo 4: Desenvolvimento e Teste

Comece desenvolvendo serviços individualmente. Adote práticas de desenvolvimento que facilitam a independência e a escalabilidade, como containers. Não se esqueça da importância dos testes automatizados.

### Passo 5: Implementação de Comunicação entre Serviços

Defina como os serviços se comunicarão (REST, gRPC, mensageria etc.). Implemente APIs claras e bem documentadas para facilitar essa comunicação.

### Passo 6: Implantação e Monitoramento

Utilize ferramentas de CI/CD para automatizar a implantação dos serviços. Implemente monitoramento e logging para garantir a visibilidade e a saúde da aplicação.



# Microserviços A e B com Flask e Requests

Este guia demonstra a criação e interação entre dois microserviços simples usando Python. O `Serviço A` atua como um consumidor que pode solicitar uma mensagem do `Serviço B`, que atua como um fornecedor dessa mensagem.

## Requisitos

- Python
- Flask: Um microframework para aplicações web em Python.
- Requests: Uma biblioteca para fazer solicitações HTTP em Python.

Use o seguinte comando para instalar Flask e Requests, se ainda não estiverem instalados:

```bash
pip install flask requests
```

## Serviço B: Fornecedor de Mensagem

O `Serviço B` é um servidor web simples que retorna uma mensagem quando sua única rota é acessada.

### Criando o Serviço B

Crie um arquivo chamado `service_b.py` e adicione o seguinte código:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/get-message')
def get_message():
    return 'Mensagem do Serviço B'

if __name__ == '__main__':
    app.run(port=5001)
```

Este código configura o `Serviço B` para ouvir na porta 5001 e retornar "Mensagem do Serviço B" quando a rota `/get-message` é acessada.

### Executando o Serviço B

Para iniciar o serviço, abra um terminal, navegue até o diretório do arquivo `service_b.py` e execute:

```bash
python service_b.py
```

## Serviço A: Consumidor e Solicitador

O `Serviço A` tem duas rotas: uma retorna uma mensagem direta e outra faz uma solicitação ao `Serviço B` para obter uma mensagem.

### Criando o Serviço A

Crie um arquivo chamado `service_a.py`. Antes de começar, certifique-se de que a biblioteca `requests` está instalada para permitir chamadas HTTP entre os serviços.

Adicione o seguinte código ao arquivo `service_a.py`:

```python
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá do Serviço A'

@app.route('/call-service-b')
def call_service_b():
    response = requests.get('http://localhost:5001/get-message')
    return 'Serviço A chamando Serviço B: ' + response.text

if __name__ == '__main__':
    app.run(port=5000)
```

Este código inicia o `Serviço A` na porta 5000, oferecendo duas rotas: `/` retorna uma saudação do `Serviço A`, e `/call-service-b` faz uma chamada ao `Serviço B` e retorna a resposta.

### Executando o Serviço A

Abra um novo terminal, navegue até o diretório do arquivo `service_a.py` e execute:

```bash
python service_a.py
```

## Testando a Interação entre os Serviços

- Acesse `http://localhost:5000/` no navegador para ver a mensagem do `Serviço A`.
- Acesse `http://localhost:5000/call-service-b` para ver a mensagem do `Serviço A`, incluindo a mensagem obtida do `Serviço B`.

## Conclusão

Este guia demonstrou a criação e interação entre dois microserviços simples, ilustrando conceitos como comunicação HTTP, independência de serviços e simplicidade de implementação. Em aplicações reais, considerações adicionais como tratamento de erros e autenticação podem ser necessárias.