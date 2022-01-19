lista = ['Parte 1', 'Parte 2', 'Parte 3']


def escrita_arquivo(texto):
    diretorio = 'C:/Users/RRodr/Documents/GitHub/meusProjetos/Digital Innovation One/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrita_arquivo('Banco de Notas.\n')
    aluno = '\nRafael:\n 8,\n 6,\n 8,\n 7'
    atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')

