cifre = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
parovi = {'V':'I', 'X':'I', 'L':'X', 'C':'X', 'D':'C', 'M':'C'}

# -------------------------------------------------------------------------
# rim - funkcija koja pretvara rimske brojeve u arapske
# -------------------------------------------------------------------------
def rim(r):
    prev_el = r[0]
    res = cifre[prev_el]
    prev_el_c = 0
    for el in r[1:]:
        if el == prev_el:
            prev_el_c += 1
            if prev_el_c > 2:
                return -1
            else:
                res += cifre[el]
        else:
            if el != 'I' and parovi[el] == prev_el:
                res = res - cifre[prev_el] + (cifre[el] - cifre[prev_el])
            else:
                if cifre[el] > cifre[prev_el]:
                    return -1

                prev_el_c = 0
                res += cifre[el]
        
        prev_el = el

    return res
    
# -------------------------------------------------------------------------
