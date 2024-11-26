# Documentação da Classe `Resultants`

A classe `Resultants` é utilizada para calcular as forças resultantes e momentos em um sistema com múltiplas forças aplicadas. Ela opera com objetos do tipo `ForcePy`, gerenciando listas de forças e suas respectivas resultantes.

---

## **Inicialização**

```python
Resultants(forces: list[fp] = None, resultants: list[fp] = None)
```

### **Parâmetros**
- **`forces`** (`list[fp]`, opcional): Lista de forças aplicadas ao sistema. Cada força deve ser um objeto da classe `ForcePy`.
- **`resultants`** (`list[fp]`, opcional): Lista de forças resultantes do sistema, geralmente com duas entradas. Caso não seja fornecida, inicializa como uma lista vazia.

### **Atributos Iniciais**
- **`sum_forcex`** (`float`): Soma das componentes horizontais de todas as forças aplicadas.
- **`sum_forcey`** (`float`): Soma das componentes verticais de todas as forças aplicadas.
- **`sum_moment`** (`float`): Soma dos momentos gerados por todas as forças aplicadas em relação a um ponto de referência.
- **`forces`** (`list[fp]`): Lista de forças fornecidas ou inicializada como vazia.
- **`resultants`** (`list[fp]`): Lista de forças resultantes fornecida ou inicializada como vazia.

---

## **Métodos**

### **`get_distance_from_pin()`**
Calcula a distância relativa de cada força e resultante em relação ao pino de apoio (ponto de referência).

- **Descrição:**
  - A distância do pino é baseada na posição da primeira força resultante (`resultants[0]`).
  - Atualiza o atributo `relative_distance` de cada força e resultante.

---

### **Cálculos de Somatório**

#### **`get_sum_forcex()`**
Calcula a soma das componentes horizontais das forças aplicadas.

- **Descrição:**
  - Para cada força na lista `forces`, adiciona `forcex` ao atributo `sum_forcex`.

#### **`get_sum_forcey()`**
Calcula a soma das componentes verticais das forças aplicadas.

- **Descrição:**
  - Para cada força na lista `forces`, adiciona `forcey` ao atributo `sum_forcey`.

#### **`get_sum_moment()`**
Calcula o momento total em relação ao pino.

- **Descrição:**
  - Para cada força na lista `forces`, calcula o momento como:
    \[ \text{momento} = force.forcey \times force.relative_distance \]
  - Soma os momentos ao atributo `sum_moment`.

---

### **Cálculos das Resultantes**

#### **`get_resultantx()`**
Calcula a componente horizontal das forças resultantes.

- **Descrição:**
  - Atribui à primeira resultante (`resultants[0]`) o valor negativo da soma das forças horizontais (`-sum_forcex`).
  - Define a componente horizontal da segunda resultante (`resultants[1]`) como `0`.

#### **`get_resultanty()`**
Calcula a componente vertical das forças resultantes.

- **Descrição:**
  - Calcula a força vertical da segunda resultante com base no momento total e na distância relativa:
    \[ \text{forcey (resultant 1)} = - \frac{\text{sum_moment}}{\text{relative_distance}} \]
  - Atualiza `sum_forcey` ao adicionar esta força.
  - Calcula a força vertical da primeira resultante como o valor negativo do somatório atualizado de forças verticais.

#### **`get_full_resultant()`**
Calcula todas as propriedades das forças resultantes (módulo, ângulo, etc.).

- **Descrição:**
  - Utiliza o método `get_full_force_by_fxfy()` da classe `ForcePy` para calcular as propriedades de ambas as resultantes.

---

## **Exemplo de Uso**

### **Exemplo 1: Sistema com duas forças**
```python
from models.forcePy import ForcePy

# Definindo forças aplicadas
force1 = ForcePy(distance=2, param_given=pg.DECOMPOSED_FORCES, param1_value=5, param2_value=3)
force2 = ForcePy(distance=4, param_given=pg.DECOMPOSED_FORCES, param1_value=-2, param2_value=7)

# Definindo forças resultantes
resultant1 = ForcePy(distance=0)
resultant2 = ForcePy(distance=6)

# Inicializando o sistema
resultants = Resultants(forces=[force1, force2], resultants=[resultant1, resultant2])

# Calculando propriedades
resultants.get_distance_from_pin()
resultants.get_sum_forcex()
resultants.get_sum_forcey()
resultants.get_sum_moment()
resultants.get_resultantx()
resultants.get_resultanty()
resultants.get_full_resultant()

# Exibindo resultados
print(f"Sum of Fx: {resultants.sum_forcex}")
print(f"Sum of Fy: {resultants.sum_forcey}")
print(f"Resultant Force 1: Fx = {resultants.resultants[0].forcex}, Fy = {resultants.resultants[0].forcey}")
print(f"Resultant Force 2: Fx = {resultants.resultants[1].forcex}, Fy = {resultants.resultants[1].forcey}")
```

---

## **Notas**
1. A classe é projetada para sistemas de duas resultantes. Para casos mais complexos, a lógica deverá ser adaptada.
2. A precisão dos cálculos depende dos valores fornecidos e do uso correto da classe `ForcePy` para representar forças individuais.