#157439114	
def encrypted_instructions(encoded: str) -> str:
    stack_number = []
    stack_string = []
    current_str = ""
    current_number = 0

    for symbol in encoded:
        if symbol.isdigit():
            current_number = current_number * 10 + int(symbol)

        elif symbol.isalpha():
            current_str += symbol
        elif symbol == '[':
            stack_number.append(current_number)
            stack_string.append(current_str)
            current_str = ""
            current_number = 0
        elif symbol == ']':
            prev_str = stack_string.pop()
            repeat_count = stack_number.pop()
            current_str = prev_str + current_str * repeat_count

    return current_str


if __name__ == "__main__":
    encoded = input()
    print(encrypted_instructions(encoded))