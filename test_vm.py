#pipenv가 설정되지 않는다면 그냥 pip install pytest > pytest로 테스트.

# def test_plus():
#     assert 3 == 1 + 2

# 관습적으로 앞에(3)이 내가 기대하는 값,
# 뒤에(1 + 2)가 실행하는값으로 씁니다.


from vm import *


def test_initial_change_should_be_zero():
    m = VendingMachine()

# VendingMachine 인스턴스가 생성

    assert "잔액은 0원입니다." == m.run("잔액")

def test_insert_coin_and_check():
    m = VendingMachine()
    assert "100원을 넣었습니다." == m.run("동전 100")
    assert "잔액은 100원입니다." == m.run("잔액")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다." == m.run("잔액")

def unknow_output():
    assert "알 수 없는 명령입니다." == m.run("웅앵")

# 각 테스트는 최소한 겹치지 않도록 만드는 게 가장 중요합니다.
# 테스트는 실행 순서와 결과와 상관 없이 테스트가 서로 간섭을 받지 않아야합니다. - init()

def test_short():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다." == m.run("음료 커피")

def test_enough():
    m = VendingMachine()
    m.run("동전 500")
    assert "커피가 나왔습니다." == m.run("음료 커피")
    assert "잔액은 350원입니다." == m.run("잔액")

def test_unknown_drink():
    m = VendingMachine()
    m.run("동전 500")
    assert "알 수 없는 음료입니다." == m.run("음료 맥주")
