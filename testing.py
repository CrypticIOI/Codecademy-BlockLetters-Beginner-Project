# CrypticIOI
# signed CrypticIOI on github
# Heavly Addicted to Monster Hunter World
# Big BIG Hype for Monster Hunter Wilds

Letter_C1 = " CCC "
Letter_C2 = "C   C"
Letter_C3 = "C    "
Letter_C4 = "C    "
Letter_C5 = "C    "
Letter_C6 = "C   C"
Letter_C7 = " CCC "

Letter_R1 = "RRRR "
Letter_R2 = "R   R"
Letter_R3 = "R   R"
Letter_R4 = "RRRR "
Letter_R5 = "R R  "
Letter_R6 = "R  R "
Letter_R7 = "R   R"

Letter_Y1 = "Y   Y"
Letter_Y2 = " Y Y "
Letter_Y3 = "  y  "
Letter_Y4 = "  Y  "
Letter_Y5 = "  Y  "
Letter_Y6 = "  Y  "
Letter_Y7 = "  Y  "

Letter_P1 = "PPPP "
Letter_P2 = "P   P"
Letter_P3 = "P   P"
Letter_P4 = "PPPP "
Letter_P5 = "P    "
Letter_P6 = "P    "
Letter_P7 = "P    "

Letter_T1 = "TTTTT"
Letter_T2 = "  T  "
Letter_T3 = "  T  "
Letter_T4 = "  T  "
Letter_T5 = "  T  "
Letter_T6 = "  T  "
Letter_T7 = "  T  "

Letter_I1 = "IIIII"
Letter_I2 = "  I  "
Letter_I3 = "  I  "
Letter_I4 = "  I  "
Letter_I5 = "  I  "
Letter_I6 = "  I  "
Letter_I7 = "IIIII"

Letters_C = [Letter_C1, Letter_C2, Letter_C3, Letter_C4, Letter_C5, Letter_C6, Letter_C7]
Letters_R = [Letter_R1, Letter_R2, Letter_R3, Letter_R4, Letter_R5, Letter_R6, Letter_R7]
Letters_Y = [Letter_Y1, Letter_Y2, Letter_Y3, Letter_Y4, Letter_Y5, Letter_Y6, Letter_Y7]
Letters_P = [Letter_P1, Letter_P2, Letter_P3, Letter_P4, Letter_P5, Letter_P6, Letter_P7]
Letters_T = [Letter_T1, Letter_T2, Letter_T3, Letter_T4, Letter_T5, Letter_T6, Letter_T7]
Letters_I = [Letter_I1, Letter_I2, Letter_I3, Letter_I4, Letter_I5, Letter_I6, Letter_I7]

for c, r, y, p, t, i, in zip(Letters_C, Letters_R, Letters_Y, Letters_P, Letters_T, Letters_I,):
    print(c + "  " + "  " + r + "  " + y + "  " + p + "  " + t + "  " + i + "  " + c)
