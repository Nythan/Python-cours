def est_inclus(motif:str,chaine:str) -> bool:
    v=""
    g = False
    for i in range(len(chaine)-len(motif)+1):
        for y in range(i, i + len(motif)):
            v = v+chaine[y]
        if v == motif:
            g= True

        else:
            v = ""
    return g

assert est_inclus("AATC", "GTACAAATCTTGCC") == True
assert est_inclus("AGTC", "GTACAAATCTTGCC") == False
assert est_inclus("AGTC", "GTACAAATCTTGCA") == False
assert est_inclus("AGTC", "GTACAAATCTAGTC") == True