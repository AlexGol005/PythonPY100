A = 522
B = 100
C = 15
cond_1 = A > 45
cond_2 = B > 45
cond_3 = C > 45
print((cond_2 and cond_1 and not cond_3) or (cond_2 and cond_3 and not cond_1) or (cond_1 and cond_3 and not cond_2))
