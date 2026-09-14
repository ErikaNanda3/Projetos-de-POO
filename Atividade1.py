
##1. Duas classes, uma delas usando objetos da outra.
##2. Atributos fechados (private em Java, _ em Python), acessados por getters e
##setters ou properties.
##3. Construtor que exige os dados indispensáveis e reaproveita os setters para validar.
##4. Duas formas de criar o objeto: sobrecarga em Java ou parâmetros padrão em Python.
##5. Pelo menos duas regras de validação que recusem valores inválidos.
##6. A demonstração roda e mostra uma criação válida, uma recusa e as duas
##formas de criação.

#Comparador de melhor aluno


class Aluno:
        def__init__(self):
  
        self.nome = ""
        self.periodo = 1
        self.notaFinal = 0.0

#Tratamentos de erros
@property
def nome(self):
        return self._nome

@nome.setter
def nome(self, novoNome):
    if novoNome:
       self._nome = novoNome
    else:
        print("nome inválido")
@property
def periodo(self):
        return self._periodo

@periodo.setter
def periodo(self, periodo):
        if 1 <= periodo <= 10:
            self._periodo = periodo
        else:
            print("Período inválido:", periodo)
            
def notaFinal(self):
        return self._notaFinal

@periodo.setter
def notaFinal(self, notaFinal):
        if 0.00 <= notaFinal <= 10.0:
            self._notafinal = notaFinal
        else:
            print("Nota final inválido:", notaFinal)
            
def compara(self):
    if <= periodo <= 10:
        self._periodo = periodo
    else:
        print("Período inválido:", periodo)
                        
class ComparadorMelhorAluno:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def encontrar_melhor(self):
        if not self.alunos:
            return None
        
        # Encontra o aluno com a maior nota final
        melhor = self.alunos[0]
        for a in self.alunos:
            if a.notaFinal > melhor.notaFinal:
                melhor = a
        return melhor

if __name__ == "__main__":
    
    print("=== 1. Testando Recusa de Valores Inválidos ===")
    aluno_recusa = Aluno(nome="", periodo=15, notaFinal=12.0)
    
    print("\n=== 2. Criando Alunos ===")
    
    aluno1 = Aluno
    aluno1.nome = "Érika"            
    aluno1.periodo = 4 
    aluno1.notaFinal = 10.0
    
    aluno2 = Aluno
    aluno2.nome = "Nicolas"            
    aluno2.periodo = 9 
    aluno2.notaFinal = 10.0
    
    aluno3 = Aluno
    aluno3.nome = "Julieta"            
    aluno3.periodo = 3 
    aluno3.notaFinal = 6.0
            
    print("\n=== 3. Comparando e Exibindo o Melhor Aluno ===")
   
    comparador = ComparadorMelhorAluno()
    comparador.adicionar_aluno(aluno1)
    comparador.adicionar_aluno(aluno2)
    comparador.adicionar_aluno(aluno3)

    melhor = comparador.encontrar_melhor()
    if melhor:            
        print("O melhor aluno é", melhor.nome, "do" melhor.periodo "° período, com nota final " melhor.notaFinal ".\n")
        
## travei na parte de criar comparador e está com bastante erros de sintax        
            
                    
