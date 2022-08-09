BRUTTO = float(input('Enter your brutto salary :'))  # Salary in BRUTTO
PERCENT_OF_TAX = float(input('Enter your percent of TAX :'))  # Use number of tax in %
ZUS = round(0.1371 * BRUTTO, 2)  # Pension contributions
ZDROWOTNE = round((BRUTTO - ZUS) * 0.09, 2)  # Healthcare
TAX = round((BRUTTO - ZUS - ZDROWOTNE - 250 - 425) * PERCENT_OF_TAX / 100, 2)  # Sum of your tax
Salary_netto = round(BRUTTO - ZUS - ZDROWOTNE - TAX, 2)
print(f' Your ZUS is {ZUS},\n Your zdrowotne is {ZDROWOTNE},\n sum of your tax {TAX},\n And your salary netto is {Salary_netto}')
