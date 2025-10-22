import time
def contagem_regressiva (n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
contagem_regressiva(5)