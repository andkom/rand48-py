from rand48 import Rand48

rng = Rand48(1538857073237)
assert rng.random() == 0.6400923397828205
assert rng.random() == 0.20170841895667824
assert rng.random() == 0.19708366795806354
assert rng.random() == 0.7711449869389728
assert rng.random() == 0.7308651738682106