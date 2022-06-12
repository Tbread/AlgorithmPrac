def solution(periods, payments, estimates):
    vip_inmonth = 0
    vip_nextmonth = 0
    vip_outmonth = 0
    for i in range(len(periods)):
        flag = 0
        receipt = sum(payments[i])
        if 5 > (periods[i] // 12) >= 2 and receipt >= 900000:
            vip_inmonth += 1
            flag = 1
        elif (periods[i] // 12) >= 5 and receipt >= 600000:
            vip_inmonth += 1
            flag = 1

            # 이번달 집계 완

        next_receipt = receipt + estimates[i] - payments[i][0]

        if flag == 0:
            if 5 > ((periods[i] + 1) // 12) >= 2 and next_receipt >= 900000:
                vip_nextmonth += 1
            elif ((periods[i] + 1) // 12) >= 5 and next_receipt >= 600000:
                vip_nextmonth += 1
        elif flag == 1:
            if 5 > ((periods[i] + 1) // 12) >= 2 and next_receipt < 900000:
                vip_outmonth += 1
            elif ((periods[i] + 1) // 12) >= 5 and next_receipt < 600000:
                vip_outmonth += 1
    return [vip_nextmonth, vip_outmonth]


solution([20, 23, 24],
         [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
          [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000],
          [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
         [100000, 100000, 100000])
