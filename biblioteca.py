import threading
import random
import time

# Lista de livros disponíveis
livros = ['Livro A', 'Livro B', 'Livro C', 'Livro D', 'Livro E']

# Dicionário com semáforos por livro (2 acessos simultâneos permitidos)
semaforos = {livro: threading.Semaphore(2) for livro in livros}

# Estatísticas
leituras_por_livro = {livro: 0 for livro in livros}
tempos_de_leitura = []

# Lock para atualizar estatísticas com segurança
lock = threading.Lock()

def usuario(id_usuario):
    livro_escolhido = random.choice(livros)
    print(f"Usuário {id_usuario} tentando acessar '{livro_escolhido}'")

    sem = semaforos[livro_escolhido]
    
    with sem:
        print(f"Usuário {id_usuario} acessando '{livro_escolhido}'")
        inicio = time.time()
        tempo_leitura = random.uniform(1, 3)  # Simula entre 1 e 3 segundos de leitura
        time.sleep(tempo_leitura)
        fim = time.time()
        print(f"Usuário {id_usuario} finalizou leitura de '{livro_escolhido}'")

        with lock:
            leituras_por_livro[livro_escolhido] += 1
            tempos_de_leitura.append(fim - inicio)

# Criar e iniciar threads
threads = []
for i in range(10):
    t = threading.Thread(target=usuario, args=(i+1,))
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
