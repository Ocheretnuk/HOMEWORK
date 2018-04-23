tarelki = int(input(''))
fari = int(input(''))
if (fari*2) < tarelki:
    g = tarelki % (fari * 2)
    print ("Моющее средство закончилось. Осталось", g, "тарелок")
if (fari*2) > tarelki:
    w = ((fari * 2) - tarelki ) / 2
    print ("Все тарелки вымыты. Осталось", w, "ед. моющего средства")
if tarelki == (fari*2):
    print ("Все тарелки вымыты, моющее средство закончилось")
