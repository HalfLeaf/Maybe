# -*-coding:utf-8-*-

from maybe.instance.float_instance import FloatData

f = FloatData(inter_bits=3, decimal_bits=5)
f.parser()
for i in range(0, 20):
    print(f.get())
