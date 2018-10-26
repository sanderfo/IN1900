from math import exp, sin

class F:
    def __init__(self, a,w):
        self.a = a
        self.w = w

    def value(self, x):
        val = exp(-self.a * x)*sin(self.w*x)
        return val

    def __call__(self, x):
        val = exp(-self.a*x)*sin(self.w*x)
        return val

f = F(a=1, w=2)
print(f.value(10)) # Calculate f(x) in
print(f(10))
