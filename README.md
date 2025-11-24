# 🚀 LAB-API-DevOps-Final 🛠️

## 🎓 Projeto Final de DevOps - IMPACTA

---

### Visão Geral

Este projeto consiste em uma **API RESTful** simples, desenvolvida em **Python** com o framework **Flask**, cujo foco principal é a demonstração prática e funcional de uma *pipeline* de **Integração Contínua (CI)** e **Entrega Contínua (CD)**.

O sistema garante que a aplicação só seja implantada no ambiente de produção após passar por testes automatizados bem-sucedidos.

---

### Status da Pipeline CI/CD

O status da sua pipeline no GitHub Actions é o reflexo mais importante deste projeto:

![GitHub Actions Workflow Status](https://github.com/rafaelferracinidev/LAB-API-DevOps-Final/actions/workflows/ci-cd.yml/badge.svg)

| Etapa | Ferramenta | Status de Conclusão |
| :--- | :--- | :--- |
| **Integração Contínua (CI)** | GitHub Actions / Pytest | ✅ Passando nos Testes |
| **Entrega Contínua (CD)** | GitHub Actions / Deploy Hook | ✅ Deploy Acionado |
| **Ambiente de Produção** | Render.com | ✅ Online |

---

### ⚙️ Tecnologias e Arquitetura

O projeto utiliza as seguintes ferramentas para compor a *pipeline* de DevOps:

* **Linguagem:** Python 3.x e Flask
* **Testes:** Pytest (Testes Unitários)
* **CI/CD (Workflow):** GitHub Actions
* **Hospedagem:** Render.com
* **Acionamento de Deploy:** **Deploy Hook** (URL Privada)

### 💡 Fluxo da Pipeline (`ci-cd.yml`)

1.  **Acionamento:** O *workflow* inicia automaticamente a cada novo `push` na branch `main`.
2.  **`build-and-test`:** Este *job* instala as dependências (incluindo a correção para o `werkzeug`), e executa todos os testes unitários com o Pytest.
3.  **`deploy`:** Só é executado se o `build-and-test` for bem-sucedido. Ele utiliza o comando `curl` com o **Secret** do Deploy Hook para notificar o Render e iniciar a implantação.

---

### 💻 Como Rodar Localmente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/rafaelferracinidev/LAB-API-DevOps-Final.git](https://github.com/rafaelferracinidev/LAB-API-DevOps-Final.git)
    cd LAB-API-DevOps-Final
    ```
2.  **Instale as Dependências (Python):**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute a Aplicação:**
    ```bash
    python app.py
    ```
    A API estará acessível em `http://127.0.0.1:5000/`.

---

### 🌐 Ambiente de Produção

A aplicação está disponível em:

* **URL:** `https://lab-api-devops-final.onrender.com`
* **Endpoint Raiz (Teste):**
    ```
    GET /
    Retorna: {"message": "API is running"} 
    ```
    (Acesso confirmado após o deploy)

---
### **Autor**
* **Rafael Ferracinidev**