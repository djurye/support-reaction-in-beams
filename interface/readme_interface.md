### `README.md`

# InterfaceApp: Interface para Cálculo de Forças e Resultantes

Este projeto implementa uma interface gráfica em Python utilizando o módulo `tkinter` para calcular forças e resultantes aplicadas em um sistema de barras. A aplicação é dividida em diversos frames (`Frame_forces`, `Frame_illustrations` e `Frame_resultants`) que organizam visualmente os componentes e interações.

## Estrutura do Projeto

### Componentes Principais

1. **Frame_forces**  
   Responsável por gerenciar a entrada de dados das forças aplicadas. Os usuários podem adicionar, remover e visualizar forças diretamente neste frame.

2. **Frame_illustrations**  
   Exibe visualmente a barra com as forças aplicadas. Cada força é representada por vetores (setas) com base nos valores fornecidos.

3. **Frame_resultants**  
   Exibe as forças resultantes calculadas, permitindo uma visualização clara do equilíbrio ou desequilíbrio do sistema.

4. **Canvas para Botões**  
   Contém botões para interações como adicionar forças, apagar forças, calcular resultantes e redefinir a interface.

---

## Funcionalidades

### Botões
- **Adicionar força**: Permite inserir uma nova força no sistema.
- **Apagar força**: Remove uma força existente.
- **Calcular Resultante**: Realiza os cálculos necessários para determinar as forças resultantes no sistema.
- **Novo**: Reinicia a interface e limpa todas as entradas e resultados.

### Comportamento Dinâmico
- A interface ajusta dinamicamente o layout com o redimensionamento da janela.
- As forças e resultantes são organizadas e exibidas de forma clara em seus respectivos frames.

---

## Estrutura do Código

### Classe `InterfaceApp`
A classe principal da aplicação, derivada de `tk.Tk`. 

#### Construtor
Configura:
- **Título da Janela**: `"Interface com Frame Forces e Frame Illustration"`.
- **Tamanho Inicial**: `1000x600`.

#### Métodos
- `add_force`: Adiciona uma nova força ao sistema.
- `del_force`: Remove a força selecionada.
- `calculate`: Calcula as forças resultantes e atualiza os frames correspondentes.
- `reset`: Reinicia a interface e redefine todos os dados.
- `get_force_list`: Processa os dados de força para incluir distâncias, componentes, ângulos e parâmetros específicos.

### Configuração dos Frames
Os frames são organizados em uma grade, com pesos ajustados para garantir uma expansão uniforme.

---

## Dependências

Certifique-se de que as seguintes dependências estão instaladas:
- Python 3.7 ou superior.
- Módulo `tkinter` (incluso por padrão na maioria das distribuições do Python).

### Arquivos Importados
- `frame_forces.py`
- `frame_illustrations.py`
- `frame_resultants.py`
- `index.py`
- `models/forcePy.py`
- `enum/param_given.py`

---

## Como Executar

1. Certifique-se de que todos os arquivos necessários estão no mesmo diretório ou acessíveis no `PYTHONPATH`.
2. Execute o arquivo principal:
   ```bash
   python interface_app.py
   ```
3. A interface será aberta e estará pronta para uso.

---

## Layout da Interface

A interface é dividida em 4 seções principais:
- **Frame de Ilustrações (canto superior esquerdo)**: Mostra a barra e as forças aplicadas.
- **Frame de Forças (canto superior direito)**: Permite entrada e gerenciamento das forças.
- **Frame de Resultantes (parte inferior esquerda)**: Exibe as forças resultantes calculadas.
- **Canvas para Botões (parte inferior direita)**: Contém os botões para interação.

---

## Melhorias Futuras

- Adicionar validação de entradas para evitar erros ao inserir dados inconsistentes.
- Implementar a exportação de resultados em formato de arquivo (CSV ou JSON).
- Melhorar a visualização gráfica das forças no frame de ilustrações.

---

Desenvolvido com o objetivo de facilitar o cálculo e visualização de forças em sistemas estáticos. A aplicação é modular e extensível para futuros aprimoramentos.