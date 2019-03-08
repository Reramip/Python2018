import fraction

def main():
    numerator1 = int(input("Enter numerator of first fraction: "))
    denominator1 = int(input("Enter denominator of first fraction: "))
    numerator2 = int(input("Enter numerator of second fraction: "))
    denominator2 = int(input("Enter denominator of second fraction: "))

    numerator = numerator1 * denominator2 + denominator1 * numerator2
    denominator = denominator1 * denominator2

    ans = fraction.Fraction(numerator, denominator)
    print("Sum:", ans.reduction())

main()