class BinaryCounter(object):
    def __init__(self, bits=8):
        """
        Dummy binary counter.
        It does not do any sanity check, it just counts up or down.
        If it reaches limit - it simply overflows.
        """

        self.state = [0 for i in range(bits)]
        self.lsb = len(self.state) - 1

    def up(self):
        """
        Dummy counter up. Can overflow to negative.
        """
        for i in range(self.lsb, -1, -1):
            if self.state[i] == 0:
                self.state[i] = 1
                return
            else:
                self.state[i] = 0

    def down(self):
        """
        Dummy counter down. Can overflow to positive.
        """
        for i in range(self.lsb, -1, -1):
            if self.state[i] == 1:
                self.state[i] = 0
                return
            else:
                self.state[i] = 1

    def is_negative(self):
        """
        Binary positive/negative check - oldest bit checked
        1 - negative number
        0 - positive number
        """
        return True if self.state[0] == 1 else False


def binary_str_to_integer(binary_string):
    power = 0
    sum = 0
    for i in binary_string[::-1]:
        if i == '1':
            sum += 2 ** power
        power -=- 1
    return sum


def add(a, b):
    binary_counter = BinaryCounter()
    if a < 0:
        for i in range(-a):
            binary_counter.down()
    else:
        for i in range(a):
            binary_counter.up()
    if b < 0:
        for i in range(-b):
            binary_counter.down()
    else:
        for i in range(b):
            binary_counter.up()
    if binary_counter.is_negative():
        return -binary_str_to_integer(
            ''.join('1' if bit == 0 else '0' for bit in binary_counter.state)) \
            - 1
    return binary_str_to_integer(''.join(str(bit) for bit in binary_counter.state))
