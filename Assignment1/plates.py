# Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    if not numbers_at_end(s):
        return False

    return True


def numbers_at_end(s):

    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i == len(s) - len(s[i:]):  # first number cannot be '0'
                return False
            if not s[i:].isdigit():
                return False
            break
    return True


if __name__ == "__main__":
    main()
