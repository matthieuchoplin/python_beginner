from fractions import Fraction

f = Fraction(16, -10)

print(type(f))
print(dir(f))
for a in dir(f):
    if not a.startswith('_'):
        print(a)
        attr_ = getattr(f, a)
        if hasattr(attr_, '__call__'):
            print(attr_())
        else:
            print(attr_)
