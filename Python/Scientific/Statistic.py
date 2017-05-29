# -*- coding: utf-8 -*-
import random
import math
class AxectList(object): # Y = a*X + b 를 구현하기 위한 클래스.
    def __init__(self, X):
        self.X = X
    def __len__(self):
        return len(self.X)
    def __add__(self, other): # T = X + b
        T = []
        for x in self.X:
            T.append(x + other)
        return AxectList(T)
    def __mul__(self, other): # T = X * a
        T = []
        for x in self.X:
            T.append(x*other)
        return AxectList(T)
    def __rmul__(self, other): # T = a * X
        T = []
        for x in self.X:
            T.append(x*other)
        return AxectList(T)
    def __setitem__(self, key, value):
        self.X[key] = value
    def __getitem__(self, key):
        return self.X[key]
#-----------------------------------------------------------------------------------------------
class NotEqualLenError(Exception): # Make Error
    pass
class UnNormalizeError(Exception):
    pass
class ScaleError(Exception):
    pass
def Putlist(x,p):
    if len(x) == len(p):
        return x, p
    else:
        raise NotEqualLenError()
def PutProb(p):
    if p <= 1:
        return p
    else:
        raise UnNormalizeError()
def Interval(a, n):
    if len(a) == n:
        return a
    else:
        raise ScaleError()
#-----------------------------------------------------------------------------------------------
class Statistic(object):
    def __init__(self, X, P):
        try:
            # Normalize Probability First
            q = 0
            T = []
            for p in P:
                q += p
            for i in range(0,len(P)):
                T.append(P[i]/q)
            # Take variable & probability by putlist because of error
            self.X, self.P = Putlist(X, T)
            self.N = len(self.X)
        except NotEqualLenError:
            print "Fit lengths of X and P"
    def mean(self):
        s = 0
        for i in range(0,self.N):
            s += self.X[i] * self.P[i]
        return s
    def deviation(self):
        T_x = []
        for x in self.X:
            T_x.append((x - self.mean()) ** 2)
        t = Statistic(T_x, self.P)
        return t.mean()
    def std(self):
        q = self.deviation()
        return (q) ** 0.5
#-----------------------------------------------------------------------------------------------
def Permutation(n,r):
    n_f = 1
    nr_f = 1
    for i in range(1,n+1):
        n_f *= i
    for j in range(1,n-r+1):
        nr_f *= j
    return n_f / nr_f
def Combination(n,r):
    r_f = 1
    for i in range(1,r+1):
        r_f *= i
    return Permutation(n,r) / r_f
#-----------------------------------------------------------------------------------------------
class BinaryDist(Statistic): # 이항분포
    def __init__(self, n, p):
        try:
            self.n = n
            self.p = PutProb(p) # Normalize p
            self.q = 1 - self.p
            self.X = []
            self.P = []
            for r in range(0,self.n + 1):
                self.X.append(r)
                self.P.append(Combination(self.n, r) * self.p ** r * self.q ** (n-r))
            self.N = len(self.X)
        except UnNormalizeError:
            print "Input proper probability"
    def __str__(self):
        return "B(%d, %.2f)" % (self.n, self.p)
#------------------------------------------------------------------------------------------------
def MC_int(f, a, N=1000000):
    try:
        a = Interval(a, 2)
        x_min = a[0]
        x_max = a[1]
        y_min = f(x_min)
        y_max = f(x_max)
        for i in range(N):
            x = x_min + (x_max - x_min) * float(i) / N
            y = f(x)
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = y
        Area = (x_max - x_min) * (y_max - y_min)
        count = 0
        for j in range(N):
            x = x_min + (x_max - x_min) * random.uniform(0,1)
            y = y_min + (y_max - y_min) * random.uniform(0,1)
            if math.fabs(y) <= math.fabs(f(x)):
                if f(x) > 0 and y > 0 and y <= f(x): # Over x-axis
                    count += 1
                if f(x) < 0 and y < 0 and y >= f(x): # Under x-axis
                    count -= 1
        return Area * float(count) / N
    except ScaleError:
        print "Impatible Length of Interval"
def Nintegration(f, x): # Apply Simpson's Rule
    try:
        x = Interval(x, 2)
        a = float(x[0])
        b = float(x[1])
        N = 100000
        h = (b - a) / N
        s = f(a) + f(b)
        for i in range(1, N, 2):
            s += 4 * f(a + i * h)
        for i in range(2, N-1, 2):
            s += 2 * f(a + i * h)
        return s * h / 3
    except ScaleError:
        print "Input proper interval"
#-----------------------------------------------------------------------------------------------
class NormalStatic(object): # 연속확률변수
    def __init__(self, f, x):
        try:
            x = Interval(x, 2) # dim 2 vector is only allowed
            self.x = x
            self.a = self.x[0]
            self.b = self.x[1]
            N = MC_int(f, self.x)
            def h(x):
                return float(f(x) / N)
            self.f = h
        except ScaleError:
            print "Input proper interval"
    def mean(self):
        def g(x):
            return self.f(x) * x
        return MC_int(g, self.x)
    def deviation(self):
        m = self.mean()
        def g(x):
            return self.f(x) * x ** 2
        return abs(MC_int(g, self.x) - m ** 2) # More simple method
    def std(self):
        return (self.deviation()) ** 0.5
    def __str__(self):
        return "N(%.2f, %.2f^2)" % (self.mean(), self.std())
