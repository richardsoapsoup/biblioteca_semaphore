import threading
from usuario import usuario  # importa a função do outro arquivo

# Lista de livros
livros = ['Livro A', 'Livro B', 'Livro C', 'Livro D', 'Livro E']

# Semáforos para controle de acesso
semaforos = {livro: threading.Semaphore(2) for livro in livros}

# Estatísticas
leituras_por_livro = {livro: 0 for livro in livros}
tempos_de_leitura = []

# Lock para acesso seguro aos dados
lock = threading.Lock()

# Criar e iniciar threads
threads = []
for i in range(10):
    t = threading.Thread(target=usuario, args=(i+1, livros, semaforos, leituras_por_livro, tempos_de_leitura, lock))
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
