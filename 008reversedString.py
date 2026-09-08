# [::-1] - [começo:fim:passo] = começo → vazio → começa do padrão / fim → vazio → vai até o final / passo → -1 → anda de trás para frente

def solution(string):
    return string[::-1]

print(solution('world'))# 'dlrow'
print(solution('hello'))# 'olleh'
print(solution(''))# ''
print(solution('h'))# 'h'