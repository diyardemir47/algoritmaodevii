def roman_to_int(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    try:
        arabic_integer = roman_numerals[roman.upper()]
        return arabic_integer
    except KeyError:
        return None

def main():
    roman_numeral = input("Tek haneli Roma rakamını girin (I, V, X, L, C, D, M): ")

    arabic_integer = roman_to_int(roman_numeral)

    if arabic_integer is not None:
        print(f"{roman_numeral} Roma rakamı, Arabic integer olarak {arabic_integer} değerine eşittir.")
    else:
        print("Geçersiz Roma rakamı girişi.")

if __name__ == "__main__":
    main()
