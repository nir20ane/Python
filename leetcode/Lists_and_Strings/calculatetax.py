def calculateTax(amount):
    tax = 0
    if amount < 20001:
        return 0
    elif amount >= 20001:

        amount1 = amount - 20000
        if amount != 0 or amount1 >= (43000 - 20001):
            tax += amount1 * 0.15
            amount2 = amount1 - (43000 - 20001)
            if amount2 != 0:
                tax += amount2 * 0.27
    return tax/59000*100

print(calculateTax(40002))
