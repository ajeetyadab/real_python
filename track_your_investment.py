def invest(amount,rate,years):
    roi = amount
    for i in range(1,years+1):
        roi = roi + roi*rate
        print(f"return for year {i} is {roi:.2f}")

invest(100,.25,10)