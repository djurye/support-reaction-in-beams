# Documentação da Classe `ForcePy`

A classe `ForcePy` é utilizada para representar e calcular propriedades de uma força em um plano bidimensional. Ela permite o cálculo de componentes da força (Fx e Fy), módulo, ângulo e vetor unitário a partir de diferentes combinações de parâmetros fornecidos durante sua inicialização.

---

## **Inicialização**

```python
ForcePy(distance, param_given: pg = None, param1_value = None, param2_value = None)
```

### **Parâmetros**
- **`distance`** (`float`): A distância relativa à origem ou a um ponto de referência.
- **`param_given`** (`pg`, opcional): Indica qual combinação de parâmetros foi fornecida. Pode ser:
  - `pg.DECOMPOSED_FORCES` (Fx e Fy fornecidos),
  - `pg.MODULE_TETA` (módulo e ângulo fornecidos),
  - `pg.MODULE_NVECTOR` (módulo e vetor unitário fornecidos).
- **`param1_value`** (opcional): Valor do primeiro parâmetro conforme `param_given`.
- **`param2_value`** (opcional): Valor do segundo parâmetro conforme `param_given`.

### **Atributos Iniciais**
- **`distance`** (`float`): Distância fornecida.
- **`relative_distance`** (`float`): Calculada ou fornecida separadamente.
- **`module`** (`float`): Módulo da força.
- **`forcex`** (`float`): Componente horizontal da força.
- **`forcey`** (`float`): Componente vertical da força.
- **`nvector`** (`str`): Vetor unitário associado à direção da força.
- **`teta`** (`float | str`): Ângulo da força em radianos ou graus.
- **`tetadegree`** (`float`): Ângulo da força em graus.

---

## **Métodos**

### **`get_full_force()`**
Calcula todas as propriedades da força (módulo, direção e componentes) com base nos parâmetros fornecidos.

- **Funcionamento:**
  - Para `pg.DECOMPOSED_FORCES`: Usa os componentes Fx e Fy.
  - Para `pg.MODULE_TETA`: Usa módulo e ângulo (graus ou radianos).
  - Para `pg.MODULE_NVECTOR`: Usa módulo e vetor unitário.

---

### **Cálculos Baseados em Diferentes Combinações de Parâmetros**

#### **`get_full_force_by_fxfy()`**
Calcula o módulo, vetor unitário e ângulo da força a partir de Fx e Fy.

#### **`get_full_force_by_nvector_module()`**
Calcula Fx e Fy a partir do módulo e vetor unitário.

#### **`get_full_force_by_teta_module()`**
Calcula Fx e Fy a partir do módulo e ângulo.

---

### **Transformação de Ângulo**
#### **`transform_teta_in_rad()`**
Converte o ângulo fornecido em graus para radianos, se necessário.

---

### **Cálculos Auxiliares**
#### **`find_module_by_fxfy()`**
Calcula o módulo da força:
\[ \text{module} = \sqrt{Fx^2 + Fy^2} \]

#### **`find_nvector_by_fxfy()`**
Calcula o vetor unitário a partir de Fx e Fy:
\[ \mathbf{n} = \frac{1}{\text{module}} (Fx \mathbf{i} + Fy \mathbf{j}) \]

#### **`find_teta_by_fxfy()`**
Calcula o ângulo da força com base em Fx e Fy considerando o quadrante correto.

#### **`find_fxfy_by_nvector()`**
Calcula os componentes Fx e Fy usando o módulo e vetor unitário:
\[ Fx = \text{module} \cdot nx \]
\[ Fy = \text{module} \cdot ny \]

#### **`find_fxfy_by_teta()`**
Calcula os componentes Fx e Fy usando o módulo e ângulo:
\[ Fx = \text{module} \cdot \cos(\theta) \]
\[ Fy = \text{module} \cdot \sin(\theta) \]

---

## **Exemplo de Uso**

### **Exemplo 1: Criando uma força a partir de componentes**
```python
force = ForcePy(distance=10, param_given=pg.DECOMPOSED_FORCES, param1_value=3, param2_value=4)
print(force.module)  # Output: 5.0
print(force.nvector)  # Output: "0.6i 0.8j"
print(force.teta)  # Output: 0.9273 (em radianos)
```

### **Exemplo 2: Criando uma força a partir do módulo e ângulo**
```python
force = ForcePy(distance=5, param_given=pg.MODULE_TETA, param1_value=10, param2_value="30°")
print(force.forcex)  # Output: 8.66
print(force.forcey)  # Output: 5.0
```

---

## **Notas**
1. A classe presume que os ângulos podem ser fornecidos em graus (com o símbolo `"°"`) ou radianos.
2. O uso de `pg` deve ser devidamente configurado como um enum ou classe contendo as constantes mencionadas (`DECOMPOSED_FORCES`, etc.).

--- 

Essa documentação serve como guia para implementar, entender e testar a classe `ForcePy`.