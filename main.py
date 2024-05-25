import statistics as stats

def media(dados):
        return stats.mean(dados);


def proporcao(val, total):
        return round(val / total, 2)


def porcentagem(val, total):
        return round((val / total), 2) * 100


def desvio_padrao(dados):
        return stats.stdev(dados);


def mediana(dados):
        return stats.median(dados);


def espec(v_neg, f_pos):
        return (v_neg / (v_neg + f_pos)) * 100


def sensi(v_pos, f_neg):
        return (v_pos / (v_pos + f_neg)) * 100


def acuracia(acertos, total):
        return (acertos / total) * 100


def margem_erro(val_calc, val_correto):
        return ((val_calc - val_correto) / val_correto) * 100


def ex1():
        # a lista abaixo diz se uma certa pessoa estava doente ou não
        # qual a porcentagem de doentes?

        doentes = [True, False, False, False, True, True, False, True]
        num_doentes = 0

        for valor in doentes:
                if (valor == True):
                        num_doentes += 1

        print(f'Porcentagem de doentes: {porcentagem(num_doentes, len(doentes))}%')


def ex2():
        # abaixo estão duas listas
        # doente diz se a pessoa estava doente ou não
        # exame diz o que o resultado do exame disse sobre a pessoa
        # qual a acurácia desse teste?

        doentes = [True, False, False, False, True, True, False, True]
        exame = [True, True, False, False, False, True, False, True]
        num_acertos = 0

        for i in range(len(doentes)):
                if (doentes[i] == exame[i]):
                        num_acertos += 1

        print(f'Acurácia: {acuracia(num_acertos, len(doentes))}%')


def ex3():
        # uma empresa decidiu fechar todas as lojas que tiveram
        # lucro abaixo da média
        # quantas lojas serão fechadas?

        lojas = [55, 10, 3, 50, 5, 30, 39, 1, 9]
        media_lojas = media(lojas)
        lojas_fechadas = 0

        for loja in lojas:
                if (loja < media_lojas):
                        lojas_fechadas += 1

        print(f'Lojas a serem fechadas: {lojas_fechadas}')


def ex4():
        # o batimento cardíaco ideal em descanso é 70
        # mas se tiver uma margem de erro de até 25% ainda é aceitável
        # quantas pessoas estão com batimento dentro do aceitável?

        batimentos = [70, 90, 77, 81, 50, 60, 73]
        batimento_ideal = 70
        num_ideal = 0

        for batimento in batimentos:
                if ((margem_erro(batimento, batimento_ideal) < 25.0) and (margem_erro(batimento, batimento_ideal) > -25.0)):
                        num_ideal += 1
                
        print(f'Batimentos ideais: {num_ideal}')


def main():
        ex1()
        ex2()
        ex3()
        ex4()


main() # Chamando a função principal