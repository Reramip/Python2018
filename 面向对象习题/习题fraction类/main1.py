import fraction

def main():
    numerator = int(input("Enter numerator of fraction: "))
    denominator = int(input("Enter denominator of fraction: "))
    ans = fraction.Fraction(numerator, denominator)
    print("Reduction to lowest terms:", ans.reduction())

main()