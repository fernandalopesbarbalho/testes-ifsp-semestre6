import unittest
from aluno import AlunoClass 
from turma import TurmaClass
from conexao import ConexaoClass
import mongomock #Projeto: https://github.com/mongomock/mongomock


class alunoTest(unittest.TestCase):
  @mongomock.patch(servers=(('localhost.com', 27017),))
  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...')
    self.aluno = AlunoClass('Fabio', 'Teixeira', 10)
    self.turma = TurmaClass()
    self.turma.cadastrarAlunos([self.aluno])
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')

  def test_salvarAluno(self):   
    colecao_nome = 'alunos'
    resposta = self.aluno.salvar(conexao = self.conexao, colecao = colecao_nome)
    self.assertEqual(True, resposta, 'Aluno cadastrado incorretamente!')
    aluno_salvo = self.conexao[colecao_nome].find_one({'nome': self.aluno.nome})
    self.assertIsNotNone(aluno_salvo, 'Aluno não foi encontrado no banco de dados mock!')
    self.assertEqual(self.aluno.sobrenome, aluno_salvo['sobrenome'])
    self.assertEqual(self.aluno.nota, aluno_salvo['nota'])

  def test_salvarTurma(self):   
    resposta = self.turma.salvar(conexao = self.conexao, colecao = 'turma')  
    self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!')

if __name__ == "__main__":
  unittest.main()