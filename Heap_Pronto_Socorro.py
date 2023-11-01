import heapq #Importando a lib heapq @Questão (1)
import random #Lib para gerar pacientes aleatórios @Questão (7)

# Classe para representar pacientes @Questão (2)
class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
    
    def __lt__(self, other):
        return self.prioridade < other.prioridade

# Fila de prioridades usando um heap mínimo @Questão (3)
fila_de_prioridades = []

# Função para adicionar pacientes à fila de prioridades @Questão (3)
def adicionar_paciente(paciente):
    heapq.heappush(fila_de_prioridades, (paciente.prioridade, paciente))

# Exemplo de atender o próximo paciente e adicionar ao histórico de pacientes chamados
def atender_proximo_paciente():
    if not fila_de_prioridades:
        print("Não há pacientes na fila.")
        return None

    paciente = heapq.heappop(fila_de_prioridades)  # A fila contém objetos Paciente
    historico_pacientes_chamados.append(paciente)

    # Acessando os atributos do objeto Paciente
    print(f"Atendendo paciente: {paciente[1].nome}, Idade: {paciente[1].idade}, Prioridade: {paciente[1].prioridade}")

    return paciente[1]

# Função para visualizar a fila de pacientes @Questão (4) e @Questão (5)
def visualizar_fila():
    if not fila_de_prioridades:
        print("Não há pacientes na fila.")
    else:
        print("Fila de Pacientes:")
        for _, paciente in fila_de_prioridades:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Prioridade: {paciente.prioridade}")

# Lista para acompanhar os últimos pacientes chamados @Questão (6)
historico_pacientes_chamados = []


# Função para listar os 5 últimos pacientes chamados @Questão (6)
def listar_ultimos_pacientes_chamados():
    if not historico_pacientes_chamados:
        print("Nenhum paciente chamado recentemente.")
    else:
        print("Últimos 5 pacientes chamados:")
        for paciente in historico_pacientes_chamados[-5:]:
            print(f"Nome: {paciente[1].nome}, Idade: {paciente[1].idade}, Prioridade: {paciente[1].prioridade}")

# Função para gerar pacientes aleatórios @Questão (7)
def gerar_pacientes_aleatorios(quantidade):
    nomes = ["Jose", "Maria", "Pedro", "Laura", "Gabriel"]
    pacientes_gerados = []

    for _ in range(quantidade):
        nome = random.choice(nomes)
        idade = random.randint(1, 99)
        prioridade = random.randint(1, 10)
        paciente = Paciente(nome, idade, prioridade)
        pacientes_gerados.append(paciente)

    return pacientes_gerados

# Loop do jogo @Questão (7)
while True:
    print("\nOpções:")
    print("1. Adicionar paciente")
    print("2. Atender próximo paciente")
    print("3. Visualizar fila de pacientes")
    print("4. Listar últimos pacientes chamados")
    print("5. Gerar pacientes aleatórios")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do paciente: ")
        idade = int(input("Idade do paciente: "))
        prioridade = int(input("Prioridade do paciente: "))
        paciente = Paciente(nome, idade, prioridade)
        adicionar_paciente(paciente)
    elif opcao == '2':
        atender_proximo_paciente()
    elif opcao == '3':
        visualizar_fila()
    elif opcao == '4':
        listar_ultimos_pacientes_chamados()
    elif opcao == '5':
        quantidade = int(input("Quantos pacientes aleatórios deseja gerar? "))
        pacientes_gerados = gerar_pacientes_aleatorios(quantidade)
        for paciente in pacientes_gerados:
            adicionar_paciente(paciente)
        print(f"{quantidade} pacientes gerados aleatoriamente e adicionados à fila.")
    elif opcao == '6':
        print("Encerrando o jogo.")
        break
    else:
        print("Opção inválida. Tente novamente.")
