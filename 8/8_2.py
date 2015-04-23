
def find_fraction(summ):
    if summ < 2:
        return False
    piv = summ / 2
    if summ % 2 == 0:
        if piv % 2 == 0:
            return (piv - 1, piv + 1)
        else:
            return (piv - 2, piv + 2)
    else:
        return (piv, piv + 1)

print find_fraction()