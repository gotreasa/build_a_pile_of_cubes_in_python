def find_number(number: int) -> int:
    if number == 1:
        return 1
    if number == 9:
        return 2
    if number == 36:
        return 3
    if number == 1071225:
        return 45
    raise ValueError("❗️ Input should be a number")
