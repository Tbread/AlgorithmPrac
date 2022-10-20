def solution(users, emoticons):
    answer = []
    minPrice = int(sum(emoticons) * 0.6)
    maxBuyer = 0
    for _ in users:
        if users[1] <= minPrice:
            maxBuyer += 1



solution([[40,10000],[25,10000]],[7000,9000])