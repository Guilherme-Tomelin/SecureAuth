# SecureAuth

## Propósito
O projeto SecureAuth foi desenvolvido com o propósito de servir como parte do meu portfólio. Consiste em um sistema de autenticação básico com páginas funcionais de login, cadastro, perfil de usuário e edição de perfil.

## Tecnologias Utilizadas
- Python
- Django
- HTML
- CSS

## Estrutura Básica do Projeto
O projeto utiliza views para realizar redirecionamentos e renderização de páginas, além de utilizar o banco de dados SQLite. As funcionalidades são divididas entre as aplicações "user_profile" e "users". Existem templates para as páginas: login, registro, perfil, edição de perfil e páginas de erro. Alguns templates herdam conteúdo de base.html.

## Instalação e Configuração
1. Clone o repositório para sua máquina.
2. Instale as dependências listadas no arquivo requirements.txt usando o comando `pip install -r requirements.txt`.
3. Certifique-se de definir a variável de ambiente `DJANGO_SECRET_KEY` em seu ambiente de execução.
4. Execute o servidor Django usando o comando `python manage.py runserver`.


## Recursos Principais
- Autenticação de Usuário (Login e Cadastro)
- Visualização e Edição de Perfil
- Validações de Formulário
