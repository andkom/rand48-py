import time


class Rand48:
    RNG_DSCALE = 1 << 53
    RNG_STATE_WIDTH = 48
    RNG_HIGH_BITS = 26
    RNG_LOW_BITS = 27
    RNG_MULTIPLIER = 0x5DEECE66D
    RNG_ADDEND = 0xB
    RNG_MASK = (1 << RNG_STATE_WIDTH) - 1

    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time())
        self.seed(seed)

    def __next(self, bits):
        nextstate = self.state * self.RNG_MULTIPLIER
        nextstate += self.RNG_ADDEND
        nextstate &= self.RNG_MASK
        self.state = nextstate
        return nextstate >> (self.RNG_STATE_WIDTH - bits)

    def seed(self, seed):
        self.state = (seed ^ self.RNG_MULTIPLIER) & self.RNG_MASK

    def random(self):
        high = self.__next(self.RNG_HIGH_BITS) << self.RNG_LOW_BITS
        low = self.__next(self.RNG_LOW_BITS)
        return (high + low) / self.RNG_DSCALE
