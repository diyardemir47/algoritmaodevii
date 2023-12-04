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

    total = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


def main():
    roman_numeral = input("Roma rakamını girin (örneğin, III): ").upper()

    try:
        arabic_integer = roman_to_int(roman_numeral)
        print(f"{roman_numeral} Roma rakamı, Arabic integer olarak {arabic_integer} değerine eşittir.")
    except KeyError:
        print("Geçersiz Roma rakamı girişi.")

if __name__ == "__main__":
    main()
