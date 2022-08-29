import math

def solution(n):
    sqrt = int(math.sqrt(n))
    dns = []
    answer = []
    for i in range(1,sqrt+1):
        if n % i == 0:
            dns.append(i)
    for dn in dns:
        answer.append(dn)
        answer.append(n // dn)
    return sum(list(set(answer)))

solution(12)