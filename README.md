# Automação de Cadastro de Base de Dados com Python

## Descrição do Projeto
Este script em Python utiliza bibliotecas como `pyautogui` e `pandas` para realizar a automação de cadastro de uma base de dados de produtos em um sistema web. Ele automatiza tarefas repetitivas, como preenchimento de formulários, utilizando técnicas de manipulação do teclado, mouse e leitura de dados de uma planilha. 

Esse tipo de automação é particularmente útil para empresas que precisam cadastrar grandes quantidades de produtos, economizando tempo e minimizando erros humanos.

---

## Dependências

Antes de executar o script, instale as bibliotecas necessárias:
```bash
pip install pyautogui pandas openpyxl
```

---

## Funcionalidades Principais

1. **Abertura de Navegador e Acesso ao Sistema**:
   - O script abre o Google Chrome e acessa automaticamente o sistema da empresa através de um link predefinido.

2. **Login Automático**:
   - Faz login no sistema preenchendo automaticamente os campos de e-mail e senha.

3. **Importação de Dados**:
   - Lê os dados de uma planilha `.csv` contendo informações sobre os produtos a serem cadastrados.

4. **Cadastro Automatizado**:
   - Preenche os formulários no sistema web com os dados de cada produto, incluindo informações como:
     - Código do produto
     - Marca
     - Tipo
     - Categoria
     - Preço unitário
     - Custo
     - Observações (se houver)

---

## Como Utilizar

1. **Preparar a Planilha de Produtos**:
   - Certifique-se de ter uma planilha chamada `produtos.csv` no mesmo diretório do script. 
   - O arquivo deve conter as seguintes colunas:
     - `codigo`
     - `marca`
     - `tipo`
     - `categoria`
     - `preco_unitario`
     - `custo`
     - `obs`

2. **Configurar Coordenadas de Clique**:
   - As coordenadas de clique (`x` e `y`) usadas para navegar no sistema podem variar de acordo com a resolução e o layout da tela. Use o seguinte comando no Python para identificar as coordenadas corretas:
     ```python
     import pyautogui
     print(pyautogui.position())
     ```

3. **Executar o Script**:
   - Execute o script com:
     ```bash
     python nome_do_arquivo.py
     ```

4. **Monitorar a Execução**:
   - O script utilizará um delay (`pyautogui.PAUSE = 1.5`) para garantir que as ações sejam realizadas no tempo correto.
   - Certifique-se de que nenhuma interação manual interrompa o processo.

---

## Organização do Código

- **Passo 1: Abrir o Sistema**:
  - O navegador Google Chrome é iniciado e o link do sistema é acessado automaticamente.
  
- **Passo 2: Fazer Login**:
  - Preenche e submete o formulário de login utilizando dados predefinidos.

- **Passo 3: Importar Base de Dados**:
  - A planilha `produtos.csv` é lida utilizando a biblioteca `pandas`, e os dados são armazenados em uma tabela para uso subsequente.

- **Passo 4: Cadastro Automático**:
  - Itera sobre cada linha da tabela e preenche os campos do formulário com os dados correspondentes.

---

## Pontos de Atenção

1. **Segurança**:
   - O script contém dados sensíveis, como e-mail e senha. Evite compartilhar ou armazenar o script em locais públicos sem criptografia ou proteção. Use variáveis de ambiente.

2. **Compatibilidade com Resolução de Tela**:
   - As coordenadas usadas para os cliques podem variar. Caso o layout ou a resolução da tela mude, será necessário ajustar os valores de `x` e `y`.

3. **Erros no Sistema Web**:
   - Certifique-se de que o sistema web esteja funcional e não haja alterações na interface que possam quebrar o fluxo da automação.

---

## Exemplo de Planilha de Produtos (`produtos.csv`)

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
101,MarcaA,Eletrônico,Hardware,250.00,200.00,Produto importado
102,MarcaB,Alimento,Laticínios,5.50,3.00,Sem glúten
103,MarcaC,Bebida,Refrigerante,3.00,2.50,Nan
```

---

## Requisitos do Ambiente

- Sistema Operacional Utilizado: Ubuntu
- Resolução de Tela: Ajuste as coordenadas de acordo com o seu monitor
- Versão do Python Utilizada: Python 3.7.17

---

## Observações Finais

Revise o código e os dados antes de rodá-lo em um ambiente real para evitar erros ou impactos inesperados.
