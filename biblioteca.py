import threading
import random
import time
from usuario import usuario

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

# Lock para acesso seguro aos dados
lock = threading.Lock()


# Criar e iniciar threads
threads = []
for i in range(10):
    t = threading.Thread(target=usuario, args=(i+1, livros, semaforos,
                                               leituras_por_livro,tempos_de_leitura
                                               , lock))
    threads.append(t)
    t.start()

# Esperar todas as threads finalizarem
for t in threads:
    t.join()

# Exibir estatísticas
print("\n=== Estatísticas ===")
for livro, total in leituras_por_livro.items():
    print(f"{livro}: {total} leitura(s)")

media_tempo = sum(tempos_de_leitura) / len(tempos_de_leitura) if tempos_de_leitura else 0
print(f"Tempo médio de leitura: {media_tempo:.2f} segundos")