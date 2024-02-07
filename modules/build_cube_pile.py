def find_number(number: int) -> int:
    if number == 1:
        return 1
    if number == 9:
        return 2
    raise ValueError("❗️ Input should be a number")
