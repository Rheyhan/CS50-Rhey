from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity==12
    jar = Jar(11)
    assert jar.capacity==11

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size==11


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(10)
    assert jar.size==1
