x = sorted([int(i) for i in input("Enter All Bid : ").split()])

if len(x) < 2:
    print("not enough bidder")
else:
    if x.count(max(x)) > 1:
        print("error : have more than one highest bid")
    else :
        print(f"winner bid is {x[-1]} need to pay {x[-2]}")