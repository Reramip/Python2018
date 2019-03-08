import fraction

def main():
    strNumerator = input("Enter a positice decimal number less than 1: ")
    length = len(strNumerator)
    strNumerator = strNumerator[1:]     #remove the dot
    strDenominator = '1'
    for i in range(length-1):
        strDenominator += '0'       #produce the denominator
    numerator = int(strNumerator)
    denominator = int(strDenominator)
    ans = fraction.Fraction(numerator, denominator)
    print("Converted to fraction:", ans.reduction())

main()