from fractions import Fraction

def doSomething(numerator, denominator):
    result = []
    while numerator != 0:
        unit_fraction = -(-denominator // numerator)  # Ceil division
        result.append(unit_fraction)
        numerator = numerator * unit_fraction - denominator
        denominator = denominator * unit_fraction
    return result

# Take input from the user
numerator = int(input())
denominator = int(input())

# Calculate Egyptian fraction representation
fraction_representation = doSomething(numerator, denominator)

# Display the output
for unit_fraction in fraction_representation:
    print(unit_fraction)
