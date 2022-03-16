def solution(money, costs):
    answer = 0
    for i in range (1,6):
        if i % 2 == 1:
            if costs[i-1] * 5 < costs[i]:
                costs[i] = costs[i-1] * 5
        if i % 2 == 0:
            if costs[i-1] * 2 < costs[i]:
                costs[i] = costs[i-1] * 2
    costs.reverse()
    coins = [500,100,50,10,5,1]
    for i in range(0,6):
        if money >= coins[i]:
            coin_ea = int(money/coins[i])
            money -= coin_ea * coins[i]
            sum = coin_ea * costs[i]
            answer += sum
            print(coin_ea,money,sum,answer)

    return answer


print(solution(4578,[1, 4, 99, 35, 50, 1000]))