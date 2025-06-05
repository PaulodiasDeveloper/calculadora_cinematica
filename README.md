## 🚀 Calculadora de Cinemática Linear
Uma calculadora Python completa para resolver problemas de cinemática linear com interface interativa, histórico e exemplos práticos.

## 📋 Sobre o Projeto
Este projeto implementa as principais equações da cinemática linear em Python, permitindo calcular:

```
Velocidade Final (vF): vF=vi+a×Δt

Velocidade Inicial (vi): vi=vF−a×Δt

Tempo (Δt): Δt=(vF−vi)/a

Aceleração (a): a=(vF−vi)/Δt

Espaço Percorrido (s): s=vi×t+(1/2)×a×t 2
```
 

Além disso, a ferramenta oferece um conversor de unidades de velocidade e exemplos práticos para facilitar a compreensão dos conceitos.

Características

✅ Interface interativa com menu de opções

✅ Validação de dados e tratamento de erros

✅ Histórico de cálculos para acompanhar resultados

✅ Exemplos práticos automatizados  

✅ Conversor de unidades de velocidade (m/s ↔ km/h) 

✅ Documentação completa com docstrings  

✅ Código limpo seguindo boas práticas Python  


## 🔧 Instalação
Clone o repositório:

```
git clone https://github.com/seu-usuario/calculadora-cinematica.git
cd calculadora-cinematica
```

Execute o programa:
```
python seu_arquivo_principal.py
```

Requisitos: Python 3.6 ou superior (sem dependências externas)

## 🎯 Como Usar
Execução Simples

```
from seu_arquivo_principal import calcular_velocidade_final

# Calcular velocidade final: vi = 10m/s, a = 2m/s², t = 5s
velocidade_final = calcular_velocidade_final(10, 2, 5)
print(f"Velocidade Final: {velocidade_final} m/s") # Resultado: 20.0 m/s
```

Interface Interativa
Execute o programa e escolha uma das opções:

```
=== CALCULADORA DE CINEMÁTICA ===
Baseada na equação: a = (vF - vi)/Δt
Derivações:
• vF = vi + a×Δt
• vi = vF - a×Δt
• Δt = (vF - vi)/a
• a = (vF - vi)/Δt
• s = vi * t + (1/2) * a * t²

==================================================
Escolha o que deseja calcular:
1 - Velocidade Final (vF)
2 - Velocidade Inicial (vi)
3 - Tempo (Δt)
4 - Aceleração (a)
5 - Espaço Percorrido (s)
6 - Ver histórico
7 - Exemplos práticos
8 - Conversor m/s ↔ km/h
9 - Limpar histórico
0 - Sair
```

Usando a Classe

```
from seu_arquivo_principal import CalculadoraCinematica

calc = CalculadoraCinematica()

# Calcular velocidade final
vf = calc.calcular_vf(vi=0, a=3, t=8)
print(f"Velocidade Final: {vf} m/s")

# Calcular tempo
t = calc.calcular_tempo(vi=25, vf=0, a=-5)
print(f"Tempo: {t} s")

# Ver histórico
calc.mostrar_historico()
```

## 📊 Exemplos Práticos
O programa inclui exemplos automáticos com situações reais:

1️⃣ Carro Acelerando
Velocidade Inicial: 0 m/s

Aceleração: 3 m/s²

Tempo: 8 s

Resultado: O carro alcançará 24.0 m/s (86.4 km/h).

2️⃣ Carro Freando
Velocidade Inicial: 25 m/s

Velocidade Final: 0 m/s

Aceleração: -5 m/s² (desaceleração)

Resultado: O carro para em 5.0 segundos.

3️⃣ Objeto em Queda Livre
Velocidade Inicial: 0 m/s

Aceleração: 9.8 m/s² (gravidade)

Tempo: 3 s

Resultado: A bola atinge 29.4 m/s (105.8 km/h).

4️⃣ Avião Decolando
Velocidade Inicial: 0 m/s

Velocidade Final: 80 m/s

Tempo: 20 s

Resultado: A aceleração é 4.0 m/s².

## 🔬 Conceitos Físicos
Cinemática Linear
"O estudo do movimento de objetos sem considerar as forças que causam esse movimento, focando na posição, velocidade e aceleração em uma trajetória reta."

Fórmulas Principais:

```
## Fórmulas de Cinemática

| Para calcular       | Fórmula                                         | Função                         |
|---------------------|--------------------------------------------------|--------------------------------|
| Velocidade Final    | \( v_F = v_i + a \times \Delta t \)             | `calcular_velocidade_final()` |
| Velocidade Inicial  | \( v_i = v_F - a \times \Delta t \)             | `calcular_velocidade_inicial()` |
| Tempo               | \( \Delta t = \frac{v_F - v_i}{a} \)            | `calcular_tempo()`            |
| Aceleração          | \( a = \frac{v_F - v_i}{\Delta t} \)            | `calcular_aceleracao()`       |
| Espaço Percorrido   | \( s = v_i \times t + \frac{1}{2} \times a \times t^2 \) | `calcular_espaco_percorrido()` |

```

### Unidades de Medida (Sistema Internacional - SI)

- Velocidade (vi, vF): metros por segundo (m/s)

- Aceleração (a): metros por segundo ao quadrado (m/s²)

- Tempo (Δt, t): segundos (s)

- Espaço Percorrido (s): metros (m)

## 🛠️ Estrutura do Código

seu_arquivo_principal.py
├── ms_para_kmh()            # Converte m/s para km/h
├── kmh_para_ms()            # Converte km/h para m/s
├── perguntar_conversao()    # Pergunta sobre conversão de velocidade
├── calcular_velocidade_final()
├── calcular_velocidade_inicial()
├── calcular_tempo()
├── calcular_aceleracao()
├── calcular_espaco_percorrido()
├── class CalculadoraCinematica:
│   ├── __init__()
│   ├── calcular_vf()
│   ├── calcular_vi()
│   ├── calcular_tempo()
│   ├── calcular_aceleracao()
│   ├── _salvar_calculo()
│   ├── mostrar_historico()
│   └── limpar_historico()
├── menu_principal()         # Interface do usuário principal
├── menu_conversor()         # Menu para conversão de velocidade
├── mostrar_tabela_conversoes() # Tabela de conversões comuns
├── exemplos_praticos()      # Exibe exemplos práticos
└── teste_rapido()           # Testes de unidade básicos

## 🧪 Testes
Execute alguns testes rápidos para verificar as funções principais:

```
from seu_arquivo_principal import (
    calcular_velocidade_final,
    calcular_velocidade_inicial,
    calcular_tempo,
    calcular_aceleracao
)

# Teste 1: Velocidade final
assert calcular_velocidade_final(10, 2, 5) == 20, f"Esperado 20, obtido {calcular_velocidade_final(10, 2, 5)}"

# Teste 2: Velocidade inicial
assert calcular_velocidade_inicial(30, 5, 4) == 10, f"Esperado 10, obtido {calcular_velocidade_inicial(30, 5, 4)}"

# Teste 3: Tempo
assert calcular_tempo(0, 15, 3) == 5, f"Esperado 5, obtido {calcular_tempo(0, 15, 3)}"

# Teste 4: Aceleração
assert calcular_aceleracao(5, 25, 4) == 5, f"Esperado 5, obtido {calcular_aceleracao(5, 25, 4)}"

print("Todos os testes passaram! ✅")
```

## 🚨 Tratamento de Erros
O programa inclui validação robusta de entrada e tratamento de exceções:

❌ Tempo negativo: "O tempo deve ser positivo ou zero"

❌ Tempo zero: "O tempo deve ser positivo e maior que zero" (para cálculos que exigem tempo > 0)

❌ Aceleração zero: "A aceleração não pode ser zero para calcular o tempo"

❌ Entrada inválida: "Por favor, digite um número válido!"

❌ Opção inválida: "Opção inválida!"

## 🎓 Casos de Uso

Este programa é uma ferramenta valiosa para:

- Estudantes de Física - para resolver problemas de cinemática linear e entender os conceitos.

- Professores - como um recurso interativo para demonstrar as leis do movimento.

- Engenheiros e Técnicos - para cálculos rápidos e precisos em aplicações de movimento.

- Qualquer pessoa interessada em explorar os fundamentos da mecânica.

## 🤝 Contribuindo
Contribuições são muito bem-vindas! Se você tiver ideias para melhorias, encontrar bugs ou quiser adicionar novas funcionalidades, siga os passos abaixo:

1. Faça um fork do projeto.

2. Crie uma branch para sua funcionalidade (git checkout -b feature/minha-nova-feature).

3. Faça commit das suas mudanças (git commit -m 'Adiciona uma nova funcionalidade').

4. Faça push para a branch (git push origin feature/minha-nova-feature).

5. Abra um Pull Request.

## Ideias para melhorias:

• [ ] Adicionar cálculos para Movimento Circular Uniforme (MCU) ou Movimento Oblíquo.

• [ ] Desenvolver uma interface gráfica (GUI) usando bibliotecas como Tkinter ou PyQt.

• [ ] Incluir a opção de exportar o histórico de cálculos para arquivos como CSV ou PDF.

• [ ] Integrar funcionalidades de visualização, como gráficos de movimento (posição vs. tempo, velocidade vs. tempo) usando Matplotlib.

• [ ] Expandir a seção de exemplos práticos com mais cenários de aplicação.

• [ ] Aumentar a cobertura de testes unitários com uma estrutura como pytest.

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ por Paulo Roberto

## 📚 Referências

Bacharelado IBMR - Análise de Fenômenos Físicos da Natureza

Brasil Escola - Cinemática

Khan Academy - Cinemática

The Physics Classroom - Kinematic Equations

Documentação Oficial do Python

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!