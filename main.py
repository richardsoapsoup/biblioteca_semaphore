import threading
import random
import time

# Lista de livros disponíveis na biblioteca
livros = ["Livro A", "Livro B", "Livro C"]

# Semáforos para cada livro, permitindo até 2 acessos simultâneos
semaforos = {}
for livro in livros:
    semaforos[livro] = threading.Semaphore(2)

# Estatísticas
leituras_por_livro = {}
for livro in livros:
    leituras_por_livro[livro] = 0
tempos_de_leitura = []

# Lock para proteger as estatísticas
estatisticas_lock = threading.Lock()

def usuario_thread(usuario_id):
    livro_escolhido = random.choice(livros)
    print(f"Usuário {usuario_id} tentando acessar '{livro_escolhido}'")

    with semaforos[livro_escolhido]:
        print(f"Usuário {usuario_id} acessando '{livro_escolhido}'")
        tempo_leitura = random.uniform(1, 3)  # tempo de leitura entre 1 e 3 segundos
        inicio = time.time()
        time.sleep(tempo_leitura)
        fim = time.time()

        print(f"Usuário {usuario_id} finalizou leitura de '{livro_escolhido}'")

        with estatisticas_lock:
            leituras_por_livro[livro_escolhido] += 1
            tempos_de_leitura.append(fim - inicio)

# Criando e iniciando as threads
threads = []
for i in range(10):
    t = threading.Thread(target=usuario_thread, args=(i+1,))
    threads.append(t)
    t.start()

# Aguardando todas as threads terminarem
for t in threads:
    t.join()

# Exibindo estatísticas
print("\nEstatísticas:")
for livro, total in leituras_por_livro.items():
    print(f"Total de leituras de '{livro}': {total}")

tempo_medio = sum(tempos_de_leitura) / len(tempos_de_leitura)
print(f"Tempo médio de leitura: {tempo_medio:.2f} segundos")