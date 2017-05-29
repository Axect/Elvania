# coding: utf-8
from sympy import *
init_printing()
from sympy.physics.quantum import *
from sympy.physics.quantum.boson import *
from sympy.physics.quantum.fermion import *
from sympy.physics.quantum.operatorordering import *
a=BosonOp('a')
b=BosonOp('b')
Commutator(a,Dagger(a))
Commutator(a,Dagger(a)).doit()
Commutator(a,b).doit(independent=True)
c=FermionOp('c')
d=FermionOp('d')
Commutator(c,Dagger(c))
Commutator(c,Dagger(c)).doit()
AntiCommutator(c,Dagger(c))
AntiCommutator(c,Dagger(c)).doit()
Commutator(a,c)
Commutator(a,c).doit()
normal_ordered_form(Dagger(a)*a)
normal_ordered_form(a*Dagger(a))
normal_ordered_form(a*Dagger(a)*a)
normal_ordered_form(a*Dagger(b))
normal_ordered_form(a*Dagger(b)).doit(independent=True)
normal_ordered_form(c*Dagger(d))
normal_ordered_form(c*Dagger(d)).doit(independent=True)
normal_ordered_form(c*Dagger(d),independent=True)
ket=BosonFockKet(2)
ket
bra=BosonFockBra(2)
bra*ket
bra*ket.doit()
(bra*ket).doit()
(bra*Dagger(a)*Dagger(a)*a*a*ket).doit()
qapply(bra*Dagger(a)*Dagger(a)*a*a*ket).doit()
get_ipython().magic(u'save bosonfermion 1-4 10-34')
