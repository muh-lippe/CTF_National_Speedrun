from sage.all import *
from Crypto.Util.number import *
import math

p = 7037189411095542101399661424968911136437683054370112146901929082044304815215238796508102607958937035244503421417531047089666788407261476886725999478615369796974319267082484766905663941137412874529930570384268875736600035220058436950599
n = 604928293513902242826844750697813298360296230589836965922445559460770464956330777297142978077171840381753362060166386141235478274641925844364093404007990669627544017237453555801510985434587758800309838580559380159655556994727763038972054055961008662617337727536706503888869143695786180320034250060574310562724453935738593360568145859518768293114591386063589064790586134071761566436891719201883451461515918132731425247986025975621160089191434740558642720428732247
u = 5124723399254519753965477778230820568274115995685406516489241951155141314318734047216941440562188021764716378577484405859111903738778224477333381592781148017098501746074849095701188434802818975767617255329420255949711066054049468803167
c = 310726350254360429088437156358460499035514323853708047519461603243147056286835156382941402126480154049593081421486020848538125531694986550091393457797356759194461290700917931171783019243503258123031885882322680819211732369309867241718158275015823673865567467449769107044499434442065689546731485951217928413599058868533165049407254866892923296832227322368063278457236148956502303822423581282369672779866499411399621396228547010983256343571496394052584949921815385
e = 65537

Fp = GF(p)
eb = Fp(e)

P.<x> = PolynomialRing(Fp)
R.<y> = PolynomialRing(Zmod(n))

f = (x^3 + x + 1) * x^(-2) - u

polynom_factor = factor(f)
print(polynom_factor)
for i, j in polynom_factor:
    es = Fp(-i.coefficients()[0])
    Spos = discrete_log(es, eb)
    g = y * (2^512) + Spos
    sols = g.monic().small_roots(X=2^512, beta=0.6)
    if sols:
        qr = sols[0] * 2^512 + Spos
        if n % qr == 0:
            print("Dapet")
            break


p_fac = int(n // int(qr))
d = inverse(e, p_fac - 1)
m = pow(c, d, p_fac)
flag = long_to_bytes(int(m))
print(flag)