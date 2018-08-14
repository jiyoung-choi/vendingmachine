# 여기서 왜 cmd를 쓰나?
change = 0
# class를 쓰면 global을 안써도 됩니다. ㅎㅎ 나중에 배울거에욧


def init():
    global change
    change = 0

def run(raw):
    global change

    tokens = raw.split(" ")
    cmd, params = tokens[0], tokens[1:]

    if cmd == "잔액":
        return "잔액은 " + str(change) + "원입니다."
    elif cmd == "동전":
        coin = params[0]
        change += int(coin)
        # change = change + int(coin)과 같은 말.
        return coin + "원을 넣었습니다."
    else:
        return "알 수 없는 명령어입니다."
