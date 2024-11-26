# Interface com Forças e Resultantes

Este projeto é uma interface gráfica desenvolvida com **Tkinter** para calcular e ilustrar as forças e resultantes em um sistema de barras. O programa permite adicionar e remover forças, calcular as resultantes e visualizar os resultados graficamente.

## Funcionalidades

- **Adicionar Forças**: Permite adicionar forças ao sistema, com seus respectivos parâmetros (como distância, componentes de força, ângulo, etc.).
- **Apagar Forças**: Remove forças previamente adicionadas ao sistema.
- **Calcular Resultantes**: Calcula as resultantes das forças aplicadas, levando em consideração suas componentes e distâncias.
- **Visualização Gráfica**: Exibe as forças e resultantes em uma barra, mostrando as direções e magnitudes.

## Requisitos
Não é necessário nenhum requisito para executar o programa pelo executavel: "**Calcule Forças de Reação nos Apoios**".
Caso não deseje utilizar o executável, você deve ter o **Python** e as seguintes bibliotecas instaladas:

- **Tkinter**: Usada para criar a interface gráfica.


## Como Rodar o Projeto

### 1. Rodar como script Python

Para rodar o projeto diretamente, execute o seguinte comando:

```bash
python app.py
```
ou abra o executável : "**Calcule Forças de Reação nos Apoios**".

Isso abrirá a interface gráfica onde você poderá interagir com o sistema de forças.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

```
pasta-principal/
│
├── app.py                       # Arquivo principal que executa a aplicação
├── index.py                     # Script com a ordem de funções para determinar a força resultant 
nos apoios
├── Calcule Reação nos Apoios    # Executável
├── interface/                   # Pasta com arquivos relacionados à interface gráfica do programa
│   └── interface.py             # Frame principal do programa
│   └── frame_forces.py          # Frame que gerencia as forças
│   └── frame_illustrations.py   # Frame que gerencia a visualização das forças
│   └── frame_resultants.py      # Frame que gerencia as resultantes
├── models/                      # Contém os modelos de dados e cálculos
│   └── forcePy.py               # Modela uma força e realiza cálculos
│   └── resultants.py            # 
├── enums/                       # Contém enums para parâmetros específicos
│   └── param_given.py           # Define os tipos de parâmetros usados para descrever forças
├── test/                        # Contém arquivos de teste do programa
│   └── test_forcePy.py          # Testa a classe ForcePy

```

## Como Contribuir

Contribuições são bem-vindas! Para contribuir com o projeto:

1. Fork este repositório.
2. Crie uma nova branch (`git checkout -b feature/nome-da-feature`).
3. Faça as alterações e commit (`git commit -am 'Adicionando nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nome-da-feature`).
5. Abra um pull request.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se você tiver dúvidas ou precisar de mais informações, entre em contato!
```