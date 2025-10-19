class AlunoClass:
  def __init__(self, nome, sobrenome, nota):    
    self.nome = nome
    self.sobrenome = sobrenome
    self.nota = nota

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota)    

  def salvar(self, conexao, colecao):    
    aluno_dados = self.__dict__
    resultado = conexao[colecao].insert_one(aluno_dados)
    return resultado.acknowledged