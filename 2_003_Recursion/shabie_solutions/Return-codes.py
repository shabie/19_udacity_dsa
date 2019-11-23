from math import log10


def get_alphabet(digit):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(digit + 96)


def all_codes(number):

    # Step 0: if number is a single digit return its character
    if number == 0:
        return []
    elif number < 10:
        return [get_alphabet(number)]

    # Step 1: check count of single digits
    num_digits = int(log10(number) + 1)

    results = []

    # Step 2: isolate last digit and get its character. For example 3 in 123
    last_digit = number % 10
    last_digit_chr = get_alphabet(last_digit)

    # Step 3: Get the codes of remaining digits
    remain = number // 10
    remain_codes = all_codes(remain)

    # Step 4: Append the single char to the codes of remaining digits
    for code in remain_codes:
        results.append(code + last_digit_chr)

    # Step 5a: Check if this last single digit can be combined with the next one
    # to create alphabets. For example 23 in 123
    divisor = 10 ** max((num_digits - 1), 2)   # divisor can't be < than 100
    last_two_digits = number % divisor
    is_valid_alphabet_number = 0 < last_two_digits <= 26

    # Step 5b: if yes, generate other combinations with which it can be combined
    if is_valid_alphabet_number:
        remain = number // divisor
        remain_codes = all_codes(remain)

        last_two_digits_chr = get_alphabet(last_two_digits)

        if len(remain_codes) > 0:
            for code in remain_codes:
                results.append(code + last_two_digits_chr)
        else:
            # in a 2-digit only scenario remain_codes is empty and the alphabet
            # itself is to be appended
            results.append(last_two_digits_chr)

    return results

results = all_codes(123)
print(results)
