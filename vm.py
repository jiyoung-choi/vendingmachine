# 여기서 왜 cmd를 쓰나?
# class를 쓰면 global을 안써도 됩니다. ㅎㅎ 나중에 배울거에욧
# class에 def 함수를 쓰면 메서드가 됩니다.
# 메서드는 self 인자(receiver, 여기서는 test_vm.py의 m)를 항상 받아야합니다.

class VendingMachine:
    def __init__(self):
        self._change = 0

#

    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다."
        elif cmd == "동전":
            coin = params[0]
            self._change += int(coin)
            # change = change + int(coin)과 같은 말.
            return coin + "원을 넣었습니다."
        else:
            return "알 수 없는 명령어입니다."
