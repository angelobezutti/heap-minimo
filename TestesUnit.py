import unittest
from Heap_Pronto_Socorro import Paciente, adicionar_paciente, atender_proximo_paciente, listar_ultimos_pacientes_chamados


class TestesUnit(unittest.TestCase):
    def test_adicionar_paciente(self):
        paciente = Paciente("Jose", 30, 2)
        adicionar_paciente(paciente)
        self.assertEqual(len(fila_de_prioridades), 1)

    def test_atender_proximo_paciente(self):
        paciente1 = Paciente("Jose", 30, 2)
        paciente2 = Paciente("Maria", 40, 1)
        adicionar_paciente(paciente1)
        adicionar_paciente(paciente2)

        paciente_atendido = atender_proximo_paciente()
        self.assertEqual(paciente_atendido, paciente2)
        self.assertEqual(len(fila_de_prioridades), 1)

    def test_listar_ultimos_pacientes_chamados(self):
        paciente1 = Paciente("Jose", 30, 2)
        paciente2 = Paciente("Maria", 40, 1)
        historico_pacientes_chamados.append(paciente1)
        historico_pacientes_chamados.append(paciente2)

        # Chamada da função que lista os últimos pacientes chamados
        lista_pacientes = listar_ultimos_pacientes_chamados()

        # Verica se a lista contém o nome de um dos pacientes chamados
        self.assertIn("Nome: Paciente1, Idade: 30, Prioridade: 2", lista_pacientes)

if __name__ == '__main__':
    unittest.main()