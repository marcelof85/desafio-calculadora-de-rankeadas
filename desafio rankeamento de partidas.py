## Objetivo:

##Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
##depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"



vitorias = int(input("Digite a quantidade de vitórias: ").strip())

derrotas = int(input("Digite a quantidade de derrotas: ").strip())

def saldo_vitorias(vitorias, derrotas):
    return vitorias - derrotas

def classificação_heroi():
    if saldo_vitorias(vitorias, derrotas) <= 10:
        return "Ferro"
    elif 10 < saldo_vitorias(vitorias, derrotas) <= 20:
        return "Bronze"
    elif 20 < saldo_vitorias(vitorias, derrotas) <= 50:
        return "Prata"
    elif 50 < saldo_vitorias(vitorias, derrotas) <= 80:
        return "Ouro"
    elif 80 < saldo_vitorias(vitorias, derrotas) <= 90:
        return "Diamante"
    elif 90 < saldo_vitorias(vitorias, derrotas) <= 100:
        return "Lendário"
    elif saldo_vitorias(vitorias, derrotas) > 100:
        return "Imortal"
    else:
        print("meu amigo, digita número nessas vitórias e derrotas, senão não vai....")

print(f"O herói de {saldo_vitorias(vitorias, derrotas)} Vitórias está no nível de {classificação_heroi()}")
    