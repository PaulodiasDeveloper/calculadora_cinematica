def ms_para_kmh(velocidade_ms):
    """
    Converte velocidade de m/s para km/h
    
    Fórmula: km/h = m/s × 3.6
    
    Parâmetros:
        velocidade_ms (float): Velocidade em m/s
    
    Retorna:
        float: Velocidade em km/h
    """
    return velocidade_ms * 3.6


def kmh_para_ms(velocidade_kmh):
    """
    Converte velocidade de km/h para m/s
    
    Fórmula: m/s = km/h ÷ 3.6
    
    Parâmetros:
        velocidade_kmh (float): Velocidade em km/h
    
    Retorna:
        float: Velocidade em m/s
    """
    return velocidade_kmh / 3.6


def perguntar_conversao(velocidade_ms, nome_velocidade="velocidade"):
    """
    Pergunta se o usuário quer converter a velocidade para km/h
    
    Parâmetros:
        velocidade_ms (float): Velocidade em m/s
        nome_velocidade (str): Nome da velocidade (ex: "velocidade final")
    
    Retorna:
        None: Apenas exibe o resultado
    """
    try:
        resposta = input(f"\n🔄 Deseja converter a {nome_velocidade} para km/h? (s/n): ").strip().lower()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            velocidade_kmh = ms_para_kmh(velocidade_ms)
            print(f"   📏 Conversão: {velocidade_ms} m/s = {velocidade_kmh:.2f} km/h")
            print(f"   📊 Cálculo: {velocidade_ms} × 3.6 = {velocidade_kmh:.2f} km/h")
        
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada")


def calcular_velocidade_final(velocidade_inicial, aceleracao, tempo):
    """
    Calcula a velocidade final usando: vF = vi + a×Δt
    
    Derivada de: a = (vF - vi)/Δt
    Rearranjando: vF = vi + a×Δt
    
    Parâmetros:
        velocidade_inicial (float): Velocidade inicial (vi) em m/s
        aceleracao (float): Aceleração (a) em m/s²
        tempo (float): Intervalo de tempo (Δt) em segundos
    
    Retorna:
        float: Velocidade final (vF) em m/s
    """
    if tempo < 0:
        raise ValueError("O tempo deve ser positivo ou zero")
    
    velocidade_final = velocidade_inicial + (aceleracao * tempo)
    return velocidade_final


def calcular_velocidade_inicial(velocidade_final, aceleracao, tempo):
    """
    Calcula a velocidade inicial usando: vi = vF - a×Δt
    
    Derivada de: a = (vF - vi)/Δt
    Rearranjando: vi = vF - a×Δt
    
    Parâmetros:
        velocidade_final (float): Velocidade final (vF) em m/s
        aceleracao (float): Aceleração (a) em m/s²
        tempo (float): Intervalo de tempo (Δt) em segundos
    
    Retorna:
        float: Velocidade inicial (vi) em m/s
    """
    if tempo <= 0:
        raise ValueError("O tempo deve ser positivo e maior que zero")
    
    velocidade_inicial = velocidade_final - (aceleracao * tempo)
    return velocidade_inicial


def calcular_tempo(velocidade_inicial, velocidade_final, aceleracao):
    """
    Calcula o tempo usando: Δt = (vF - vi)/a
    
    Fórmula original: a = (vF - vi)/Δt
    Rearranjando: Δt = (vF - vi)/a
    
    Parâmetros:
        velocidade_inicial (float): Velocidade inicial (vi) em m/s
        velocidade_final (float): Velocidade final (vF) em m/s
        aceleracao (float): Aceleração (a) em m/s²
    
    Retorna:
        float: Tempo (Δt) em segundos
    """
    if aceleracao == 0:
        raise ValueError("A aceleração não pode ser zero para calcular o tempo")
    
    tempo = (velocidade_final - velocidade_inicial) / aceleracao
    return tempo


def calcular_aceleracao(velocidade_inicial, velocidade_final, tempo):
    """
    Calcula a aceleração usando: a = (vF - vi)/Δt
    
    Fórmula original da cinemática
    
    Parâmetros:
        velocidade_inicial (float): Velocidade inicial (vi) em m/s
        velocidade_final (float): Velocidade final (vF) em m/s
        tempo (float): Intervalo de tempo (Δt) em segundos
    
    Retorna:
        float: Aceleração (a) em m/s²
    """
    if tempo <= 0:
        raise ValueError("O tempo deve ser positivo e maior que zero")
    
    aceleracao = (velocidade_final - velocidade_inicial) / tempo
    return aceleracao


def calcular_espaco_percorrido(velocidade_inicial, aceleracao, tempo):
    """
    Calcula o espaço percorrido usando a equação de Torricelli: 
    s = vi * t + (1/2) * a * t²
    
    Parâmetros:
        velocidade_inicial (float): Velocidade inicial (vi) em m/s
        aceleracao (float): Aceleração (a) em m/s²
        tempo (float): Tempo (t) em segundos
    
    Retorna:
        float: Espaço percorrido (s) em metros
    """
    espaco = (velocidade_inicial * tempo) + (0.5 * aceleracao * (tempo ** 2))
    return espaco


class CalculadoraCinematica:
    """
    Classe para cálculos de cinemática linear
    Baseada na equação: a = (vF - vi)/Δt
    """
    
    def __init__(self):
        self.historico = []
    
    def calcular_vf(self, vi, a, t, salvar=True):
        """Calcula velocidade final: vF = vi + a×Δt"""
        resultado = calcular_velocidade_final(vi, a, t)
        
        if salvar:
            self._salvar_calculo('Velocidade Final', {
                'vi': vi, 'a': a, 't': t, 'vf': resultado,
                'formula': f'vF = {vi} + ({a})×{t} = {resultado:.2f} m/s'
            })
        
        return resultado
    
    def calcular_vi(self, vf, a, t, salvar=True):
        """Calcula velocidade inicial: vi = vF - a×Δt"""
        resultado = calcular_velocidade_inicial(vf, a, t)
        
        if salvar:
            self._salvar_calculo('Velocidade Inicial', {
                'vf': vf, 'a': a, 't': t, 'vi': resultado,
                'formula': f'vi = {vf} - ({a})×{t} = {resultado:.2f} m/s'
            })
        
        return resultado
    
    def calcular_tempo(self, vi, vf, a, salvar=True):
        """Calcula tempo: Δt = (vF - vi)/a"""
        resultado = calcular_tempo(vi, vf, a)
        
        if salvar:
            self._salvar_calculo('Tempo', {
                'vi': vi, 'vf': vf, 'a': a, 't': resultado,
                'formula': f'Δt = ({vf} - {vi})/{a} = {resultado:.2f} s'
            })
        
        return resultado
    
    def calcular_aceleracao(self, vi, vf, t, salvar=True):
        """Calcula aceleração: a = (vF - vi)/Δt"""
        resultado = calcular_aceleracao(vi, vf, t)
        
        if salvar:
            self._salvar_calculo('Aceleração', {
                'vi': vi, 'vf': vf, 't': t, 'a': resultado,
                'formula': f'a = ({vf} - {vi})/{t} = {resultado:.2f} m/s²'
            })
        
        return resultado
    
    def _salvar_calculo(self, tipo, dados):
        """Salva cálculo no histórico"""
        self.historico.append({
            'tipo': tipo,
            'dados': dados
        })
    
    def mostrar_historico(self):
        """Exibe histórico de cálculos"""
        if not self.historico:
            print("Nenhum cálculo realizado ainda")
            return
        
        print("=== HISTÓRICO DE CÁLCULOS ===")
        for i, calc in enumerate(self.historico, 1):
            print(f"\n{i}. {calc['tipo']}:")
            print(f"   {calc['dados']['formula']}")
    
    def limpar_historico(self):
        """Limpa o histórico"""
        self.historico.clear()
        print("Histórico limpo!")


def menu_principal():
    """Menu interativo principal"""
    calc = CalculadoraCinematica()
    
    print("=== CALCULADORA DE CINEMÁTICA ===")
    print("Baseada na equação: a = (vF - vi)/Δt")
    print("Derivações:")
    print("• vF = vi + a×Δt")
    print("• vi = vF - a×Δt") 
    print("• Δt = (vF - vi)/a")
    print("• a = (vF - vi)/Δt")
    print("• s = vi * t + (1/2) * a * t²")
    print()
    
    while True:
        print("\n" + "="*50)
        print("Escolha o que deseja calcular:")
        print("1 - Velocidade Final (vF)")
        print("2 - Velocidade Inicial (vi)")
        print("3 - Tempo (Δt)")
        print("4 - Aceleração (a)")
        print("5 - Espaço Percorrido (s)")
        print("6 - Ver histórico")
        print("7 - Exemplos práticos")
        print("8 - Conversor m/s ↔ km/h")
        print("9 - Limpar histórico")
        print("0 - Sair")
        
        try:
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "0":
                print("Programa encerrado!")
                break
            
            elif opcao == "1":
                print("\n--- CALCULAR VELOCIDADE FINAL ---")
                print("Fórmula: vF = vi + a×Δt")
                vi = float(input("Velocidade inicial (m/s): "))
                a = float(input("Aceleração (m/s²): "))
                t = float(input("Tempo (s): "))
                
                vf = calc.calcular_vf(vi, a, t)
                print(f"\n✅ Resultado: vF = {vi} + ({a})×{t} = {vf:.2f} m/s")
                perguntar_conversao(vf, "velocidade final")
            
            elif opcao == "2":
                print("\n--- CALCULAR VELOCIDADE INICIAL ---")
                print("Fórmula: vi = vF - a×Δt")
                vf = float(input("Velocidade final (m/s): "))
                a = float(input("Aceleração (m/s²): "))
                t = float(input("Tempo (s): "))
                
                vi = calc.calcular_vi(vf, a, t)
                print(f"\n✅ Resultado: vi = {vf} - ({a})×{t} = {vi:.2f} m/s")
                perguntar_conversao(vi, "velocidade inicial")
            
            elif opcao == "3":
                print("\n--- CALCULAR TEMPO ---")
                print("Fórmula: Δt = (vF - vi)/a")
                vi = float(input("Velocidade inicial (m/s): "))
                vf = float(input("Velocidade final (m/s): "))
                a = float(input("Aceleração (m/s²): "))
                
                t = calc.calcular_tempo(vi, vf, a)
                print(f"\n✅ Resultado: Δt = ({vf} - {vi})/{a} = {t:.2f} s")
            
            elif opcao == "4":
                print("\n--- CALCULAR ACELERAÇÃO ---")
                print("Fórmula: a = (vF - vi)/Δt")
                vi = float(input("Velocidade inicial (m/s): "))
                vf = float(input("Velocidade final (m/s): "))
                t = float(input("Tempo (s): "))
                
                a = calc.calcular_aceleracao(vi, vf, t)
                print(f"\n✅ Resultado: a = ({vf} - {vi})/{t} = {a:.2f} m/s²")
            
            elif opcao == "5":
                print("\n--- CALCULAR ESPAÇO PERCORRIDO ---")
                print("Fórmula: s = vi * t + (1/2) * a * t²")
                vi = float(input("Velocidade inicial (m/s): "))
                a = float(input("Aceleração (m/s²): "))
                t = float(input("Tempo (s): "))
                
                s = calcular_espaco_percorrido(vi, a, t)
                print(f"\n✅ Resultado: s = {vi} * {t} + (1/2) * {a} * {t}² = {s:.2f} m")

            elif opcao == "6":
                calc.mostrar_historico()
            
            elif opcao == "7":
                exemplos_praticos()
            
            elif opcao == "8":
                menu_conversor()
            
            elif opcao == "9":
                calc.limpar_historico()
            
            else:
                print("❌ Opção inválida!")
        
        except ValueError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")


def menu_conversor():
    """Menu dedicado para conversões de velocidade"""
    print("\n" + "="*50)
    print("🔄 CONVERSOR DE VELOCIDADE")
    print("="*50)
    print("1 - m/s → km/h")
    print("2 - km/h → m/s")
    print("3 - Tabela de conversões comuns")
    print("0 - Voltar ao menu principal")
    
    try:
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- m/s → km/h ---")
            velocidade_ms = float(input("Digite a velocidade em m/s: "))
            velocidade_kmh = ms_para_kmh(velocidade_ms)
            print(f"📊 {velocidade_ms} m/s = {velocidade_kmh:.2f} km/h")
            print(f"🧮 Cálculo: {velocidade_ms} × 3.6 = {velocidade_kmh:.2f}")
        
        elif opcao == "2":
            print("\n--- km/h → m/s ---")
            velocidade_kmh = float(input("Digite a velocidade em km/h: "))
            velocidade_ms = kmh_para_ms(velocidade_kmh)
            print(f"📊 {velocidade_kmh} km/h = {velocidade_ms:.2f} m/s")
            print(f"🧮 Cálculo: {velocidade_kmh} ÷ 3.6 = {velocidade_ms:.2f}")
        
        elif opcao == "3":
            mostrar_tabela_conversoes()
        
        elif opcao == "0":
            return
        
        else:
            print("❌ Opção inválida!")
    
    except ValueError:
        print("❌ Por favor, digite um número válido!")
    except Exception as e:
        print(f"❌ Erro: {e}")


def mostrar_tabela_conversoes():
    """Mostra uma tabela com conversões comuns"""
    print("\n📋 TABELA DE CONVERSÕES COMUNS")
    print("-" * 40)
    print("   m/s   |   km/h   |   Situação")
    print("-" * 40)
    
    conversoes = [
        (1, "Caminhada lenta"),
        (5, "Corrida"),
        (10, "Ciclista rápido"),
        (15, "Carro na cidade"),
        (25, "Carro na estrada"),
        (30, "Limite urbano (108 km/h)"),
        (40, "Limite rodoviário"),
        (50, "Trem rápido"),
        (100, "Carro de corrida"),
        (200, "Trem-bala")
    ]
    
    for ms, situacao in conversoes:
        kmh = ms_para_kmh(ms)
        print(f"  {ms:4.0f}   |  {kmh:6.1f}  | {situacao}")
    
    print("-" * 40)


def exemplos_praticos():
    """Exemplos práticos com situações reais"""
    print("\n" + "="*50)
    print("🚗 EXEMPLOS PRÁTICOS")
    print("="*50)
    
    # Exemplo 1: Carro acelerando
    print("\n1️⃣ CARRO ACELERANDO:")
    print("   Um carro parte do repouso e acelera a 3 m/s² por 8 segundos.")
    print("   Qual a velocidade final?")
    
    vi1, a1, t1 = 0, 3, 8
    vf1 = calcular_velocidade_final(vi1, a1, t1)
    vf1_kmh = ms_para_kmh(vf1)
    
    print(f"   📊 Dados: vi = {vi1} m/s, a = {a1} m/s², t = {t1} s")
    print(f"   🧮 Cálculo: vF = {vi1} + {a1}×{t1} = {vf1} m/s")
    print(f"   ✅ Resposta: O carro alcançará {vf1} m/s ({vf1_kmh:.1f} km/h)")
    
    # Exemplo 2: Freagem
    print("\n2️⃣ CARRO FREANDO:")
    print("   Um carro a 25 m/s freia com desaceleração de 5 m/s².")
    print("   Quanto tempo leva para parar?")
    
    vi2, vf2, a2 = 25, 0, -5
    vi2_kmh = ms_para_kmh(vi2)
    t2 = calcular_tempo(vi2, vf2, a2)
    
    print(f"   📊 Dados: vi = {vi2} m/s ({vi2_kmh:.1f} km/h), vf = {vf2} m/s, a = {a2} m/s²")
    print(f"   🧮 Cálculo: Δt = ({vf2} - {vi2})/{a2} = {t2} s")
    print(f"   ✅ Resposta: O carro para em {t2} segundos")
    
    # Exemplo 3: Objeto em queda
    print("\n3️⃣ OBJETO EM QUEDA LIVRE:")
    print("   Uma bola é solta e cai por 3 segundos (g = 9.8 m/s²).")
    print("   Qual a velocidade final?")
    
    vi3, a3, t3 = 0, 9.8, 3
    vf3 = calcular_velocidade_final(vi3, a3, t3)
    vf3_kmh = ms_para_kmh(vf3)
    
    print(f"   📊 Dados: vi = {vi3} m/s, a = {a3} m/s², t = {t3} s")
    print(f"   🧮 Cálculo: vF = {vi3} + {a3}×{t3} = {vf3} m/s")
    print(f"   ✅ Resposta: A bola atinge {vf3} m/s ({vf3_kmh:.1f} km/h)")
    
    # Exemplo 4: Avião decolando
    print("\n4️⃣ AVIÃO DECOLANDO:")
    print("   Um avião acelera de 0 a 80 m/s em 20 segundos.")
    print("   Qual a aceleração?")
    
    vi4, vf4, t4 = 0, 80, 20
    vf4_kmh = ms_para_kmh(vf4)
    a4 = calcular_aceleracao(vi4, vf4, t4)
    
    print(f"   📊 Dados: vi = {vi4} m/s, vf = {vf4} m/s ({vf4_kmh:.1f} km/h), t = {t4} s")
    print(f"   🧮 Cálculo: a = ({vf4} - {vi4})/{t4} = {a4} m/s²")
    print(f"   ✅ Resposta: A aceleração é {a4} m/s²")


def teste_rapido():
    """Função para testes rápidos"""
    print("🧪 EXECUTANDO TESTES...")
    
    # Teste 1: Velocidade final
    vf = calcular_velocidade_final(10, 2, 5)  # vi=10, a=2, t=5
    assert vf == 20, f"Esperado 20, obtido {vf}"
    
    # Teste 2: Velocidade inicial  
    vi = calcular_velocidade_inicial(30, 5, 4)  # vf=30, a=5, t=4
    assert vi == 10, f"Esperado 10, obtido {vi}"
    
    # Teste 3: Tempo
    t = calcular_tempo(0, 15, 3)  # vi=0, vf=15, a=3
    assert t == 5, f"Esperado 5, obtido {t}"
    
    # Teste 4: Aceleração
    a = calcular_aceleracao(5, 25, 4)  # vi=5, vf=25, t=4
    assert a == 5, f"Esperado 5, obtido {a}"
    
    print("✅ Todos os testes passaram!")


if __name__ == "__main__":
    # Executa teste rápido primeiro
    teste_rapido()
    print()
    
    # Inicia o menu principal
    menu_principal()