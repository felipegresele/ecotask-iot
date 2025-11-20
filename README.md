# 🌱 EcoTask – IA Generativa + IoT + Web + Mobile  
**Projeto Integrado – Disruptive Architectures: IoT, IOB & Generative IA**

Este repositório contém a **API de Inteligência Artificial (Python)** utilizada no projeto EcoTask.  
A IA é responsável por gerar **planos sustentáveis**, oferecendo dicas personalizadas conforme o contexto do usuário.

Toda a demonstração detalhada das funcionalidades da aplicação está disponível **no vídeo de apresentação oficial**.

---

# 🚀 1. Tecnologias Utilizadas
- **Python + Google Gemini 2.5 Flash**
- **Render – Deploy da API**
- **PostgreSQL em deploy** (compartilhado com o projeto)
- **Integração com o Mobile** (React Native)
- **Integração com o Back-end Java (IoT)**

---

# 🤖 2. Endpoint Principal da IA (Python) – *Deploy ativo*

### **Link Deploy:**
```
https://ecotask-iot.onrender.com
```

### **URL:**
```
https://ecotask-iot.onrender.com/api/generate-plan
```

### Como testar:
Basta acessar o endpoint acima via Postman, Insomnia ou front-end.

### **Exemplo de JSON para enviar:**
```json
{
  "userContext": "sou um estudante que mora sozinho",
  "sustainabilityGoal": "quero começar a reciclar plástico e reduzir lixo"
}
```

### 📌 Regra importante da IA
A IA está **treinada e limitada ao tema sustentabilidade**.

Se o usuário enviar algo **fora do tema**, a resposta será:

```
"Desculpe — só posso responder perguntas sobre tarefas e atitudes que ajudam a natureza."
```

---

# 🗄️ 3. Banco de Dados (Python)
A API em Python utiliza um **banco PostgreSQL hospedado em deploy**, garantindo persistência e integração com o sistema.

Dados do banco

Hostname: dpg-d4dl5rq4d50c73drekvg-a
Port: 5432
Database: ecotask_api
Username: admin
Password: 6VPli4erVIm2qLc7OxHwTKFOqKnrQBgl
Internal Database URL: postgresql://admin:6VPli4erVIm2qLc7OxHwTKFOqKnrQBgl@dpg-d4dl5rq4d50c73drekvg-a/ecotask_api

---

# 📱 4. Integração com o Mobile
O aplicativo Mobile possui a aba **EcoTask IA**, que consome diretamente o endpoint:

```
https://ecotask-iot.onrender.com/api/generate-plan
```

Ou seja, o mobile está **totalmente conectado à IA do Python**.

---

# 🔧 5. Integração com Java (IoT)

Embora a IA principal seja a do Python, o projeto também possui integração com **back-end Java (IoT)** opcional, para demonstrar interoperabilidade entre disciplinas.

---

## ✔️ 5.1 Criar Conta no Java

### **Link Deploy:**
```
https://ecotask-java.onrender.com
```

### Endpoint:
```
POST https://ecotask-java.onrender.com/auth/register
```

### JSON obrigatório:
```json
{
  "username": "admin",
  "email": "felipe6@example.com",
  "password": "admin123",
  "role": "ADMIN"
}
```

⚠️ **Importante:**  
A role **DEVE ser sempre ADMIN** para ter autorização aos endpoints protegidos.

---

## ✔️ 5.2 Fazer Login para obter o Token

### Endpoint:
```
POST https://ecotask-java.onrender.com/auth/login
```

### JSON:
```json
{
  "email": "felipe6@example.com",
  "password": "admin123"
}
```

A resposta trará um **JWT Token**.  
Você deve colocá-lo como **Bearer Token** nas próximas requisições.

---

## ✔️ 5.3 Testar a IA integrada no Java (IoT)

### Endpoint:
```
GET https://ecotask-java.onrender.com/api/v1/plano-missao/gerar?context=moro sozinho em apartamento&goal=como economizar energia e agua
```

### Como usar:
- O token JWT deve estar no **Authorization → Bearer Token**
- Os valores de `context` e `goal` são enviados como **query params**

Exemplo:
```
context=moro sozinho em apartamento
goal=como economizar energia e agua
```

---

# 🎥 6. Vídeo de Apresentação
O vídeo contém **todas as funcionalidades completas do projeto**, incluindo:

- Demonstração da IA Python  
- Integração com o Mobile  
- Integração com o Java  
- Fluxo completo de testes  
- Arquitetura geral  

📌 **Link do vídeo:**  

https://youtu.be/A_wrS8L39-g

---

# 👥 7. Integrantes
- **Felipe Horta Gresele – RM556955**  
- **Arthur Cardoso Carinhanha – RM550615**  
- **João Henrique Dias – RM556221**

---

# ✔️ 8. Conclusão
Este projeto atende todos os requisitos da disciplina:

- IA Generativa (Gemini 2.5)  
- Integração com Web, Mobile e IoT  
- REST API funcional e documentada  
- Deploy de todos os serviços  
- Demonstração completa em vídeo  

