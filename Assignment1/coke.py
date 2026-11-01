#Coke Machine

def main():
    price = 50
    # cost of one Coke
    amount_due = price

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # valid denominations only
        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            # invalid coins should be ignored
            continue

    # calculate change if there is overpay
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
