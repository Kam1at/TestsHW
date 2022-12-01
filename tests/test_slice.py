from homeworktests.slice import my_slice


def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    assert my_slice([2, 4, 5, 7, 8]) == [2, 4, 5, 7, 8]
    assert my_slice([1, 2, 3, 4, 5], -4, -2) == [2, 3]
    assert my_slice([1, 3, 4, 7, 8], 10) == []
