from super_gcd.gcd import gcd


def test_gcd_of_3_and_6():
    result = gcd(3, 6)
    assert result == 3


def test_gcd_of_2_and_4():
    result = gcd(2, 4)
    assert result == 2


def test_gcd_of_1_and_5():
    result = gcd(1, 5)
    assert result == 1


def test_gcd_of_4_and_8():
    result = gcd(4, 8)
    assert result == 4


def test_gcd_of_505_and_32623():
    result = gcd(505, 32623)
    assert result == 101


def test_gcd_of_626629665_and_23830046682():
    result = gcd(626629665, 23830046682)
    assert result == 1509951
