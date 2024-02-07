def find_number(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("❗️ Input should be a number")
    index = 0
    while number > 0:
        index += 1
        number -= index**3
    return index if number == 0 else -1
