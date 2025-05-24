"""
There are two friends, John and Smith, and the parameters jerry and sunny to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.
"""


def angry(jerry, sunny):
    res = jerry == sunny
    print(res)


angry(True, True)
angry(False, True)
