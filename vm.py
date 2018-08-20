# 여기서 왜 cmd를 쓰나?
# class를 쓰면 global을 안써도 됩니다. ㅎㅎ 나중에 배울거에욧
# class에 def 함수를 쓰면 메서드가 됩니다.
# 메서드는 self 인자(receiver, 여기서는 test_vm.py의 m)를 항상 받아야합니다.


class VendingMachine:
    def __init__(self):
        self._change = 0

# def __init__이 "상태"를 의미함.
# 클래스에는 상태와 메서드를 정의한다. 인스턴스가 만들어지면 상태가 생기고,
# _를 넣는다는 건 건드리지말라는 의미.
# run은 메소드

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
        # elif cmd == "음료 커피":
        #     return "잔액이 부족합니다."
        elif cmd == "음료":
            price = 150
            unknown_beverage = params[0]
            if unknown_beverage != "커피":
                return "알 수 없는 음료입니다."
            if self._change < price:
                return "잔액이 부족합니다."
            self._change = self._change - price
            return unknown_beverage + "가 나왔습니다."
        else:
            return "알 수 없는 명령어입니다."
#
# v1 = VendingMachine()
# v2 = VendingMachine()
# v1.run("동전 100")

# v1.run("동전 100")을 실행하면 self에 vi이 담기고 raw에 "동전 100"이 담긴다.
