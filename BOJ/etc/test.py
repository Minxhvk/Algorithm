class DefaultDict(dict):
      def __missing__(self, key):
            return []

d = DefaultDict()
d['florp'] = 127

d = DefaultDict()
print(f"d 1: {d}")
print(f"d 2: {d['foo']}")

normal = dict()
normal['florp2'] = 127
print(f"normal 1 : {normal}")
print(f"normal 2 :  {normal['foo']}")