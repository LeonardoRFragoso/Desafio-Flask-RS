# 🥗 **Diário de Refeições**

Um simples e eficiente sistema para registrar, gerenciar e monitorar suas refeições diárias, garantindo que você mantenha sua dieta sob controle. Desenvolvido com Flask e SQLAlchemy, este projeto oferece uma interface intuitiva para adicionar, editar, visualizar e deletar refeições.

## 🚀 **Funcionalidades**

- **Registrar Refeições:** Adicione uma nova refeição com nome, descrição, data e hora, e se está dentro da dieta ou não.
- **Editar Refeições:** Modifique qualquer detalhe de uma refeição existente, ajustando informações como nome, descrição, e status da dieta.
- **Excluir Refeições:** Remova refeições que não são mais relevantes ou foram registradas erroneamente.
- **Listar Refeições:** Visualize todas as suas refeições registradas em uma única lista.
- **Visualizar Detalhes:** Acesse informações detalhadas de uma refeição específica.

## 🛠️ **Tecnologias Utilizadas**

- **Python** - Linguagem principal para o desenvolvimento.
- **Flask** - Framework leve e poderoso para criar aplicações web.
- **SQLAlchemy** - ORM para manipulação de banco de dados.
- **Flask-Migrate** - Gerencia migrações do banco de dados.

## 🔧 **Como Começar**

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/diario-refeicoes.git
   cd diario-refeicoes
Crie e Ative um Ambiente Virtual:

python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

Instale as Dependências:

pip install -r requirements.txt

Configure o Banco de Dados:

flask db init
flask db migrate -m "Create tables"
flask db upgrade

Inicie a Aplicação:

python run.py

Acesse a Aplicação:

Abra o navegador e vá para http://127.0.0.1:5000

## 📄 **Endpoints**

POST /refeicoes - Cria uma nova refeição.
GET /refeicoes - Lista todas as refeições.
GET /refeicoes/<id> - Visualiza uma refeição específica.
PUT /refeicoes/<id> - Edita uma refeição existente.
DELETE /refeicoes/<id> - Deleta uma refeição.

## 📚 **Contribuição**


Sinta-se à vontade para contribuir com melhorias, correções e novas funcionalidades! Para colaborar, faça um fork do repositório e envie um pull request.

## 🧩 **License**

Este projeto está licenciado sob a MIT License.


Você pode copiar e colar esse conteúdo diretamente no seu arquivo README.md. Se precisar de mais alguma coisa, é só avisar!


