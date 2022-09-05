from countryinfo import CountryInfo
count = input("Enter your country : ")
country =  CountryInfo(count)
print("Capital : ",country.capital())
print("Currencies : ",country.currencies())
print("Language : ",country.languages())
print("Borders : ",country.borders())
print("Others names : ",country.alt_spellings())