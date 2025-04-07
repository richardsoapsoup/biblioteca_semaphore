import random
import time
import threading

def usuario(id_usuario, livros, semaforos, leituras_por_livro, tempos_de_leitura, lock):
    livro_escolhido = random.choice(livros)
    print(f"Usuário {id_usuario} tentando acessar '{livro_escolhido}'")

    sem = semaforos[livro_escolhido]
    
    with sem:
        print(f"Usuário {id_usuario} acessando '{livro_escolhido}'")
        inicio = time.time()
        tempo_leitura = random.uniform(1, 3)
        time.sleep(tempo_leitura)
        fim = time.time()
        print(f"Usuário {id_usuario} finalizou leitura de '{livro_escolhido}'")

        with lock:
            leituras_por_livro[livro_escolhido] += 1
            tempos_de_leitura.append(fim - inicio)
