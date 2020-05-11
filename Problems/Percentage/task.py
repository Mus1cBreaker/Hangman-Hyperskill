def get_percentage(number, round_digits=0):
    for x in range(0, 2):
        number *= 10
        x += 1
    number = round(number, round_digits)
    if len(str(number).split(".")) > 1 and round_digits > len(str(number).split(".")[1]):
        round_digits = len(str(number).split(".")[1])
    elif len(str(number).split(".")) < 2:
        round_digits = 0
    answer = f"%.{round_digits}f" % number
    answer += "%"
    return answer
