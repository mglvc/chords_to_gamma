C_and_Am = [["C", "F", "G", "Am", "Dm", "E"], ["Em", "A"]]
C_sharp_and_A_sharp_m = [["C#", "F#", "G#", "A#m", "D#m", "F"],[ "Fm", "A#"]]
D_and_Bm = [["D", "G", "A", "Bm", "Em", "F#"],[ "F#m", "B"]]
D_sharp_and_Cm = [["D#", "G#", "A#", "Cm", "Fm", "G"], ["Gm", "C"]]
E_and_C_sharp_m = [["E", "A", "B", "C#m", "F#m", "G#"], ["G#m", "C#"]]
F_and_Dm = [["F", "A#", "C", "Dm", "Gm", "A"], ["Am", "D"]]         
F_sharp_and_D_sharp_m = [["F#", "B", "C#", "D#m", "G#m", "A#"], ["A#m", "D#"]]
G_and_Em = [["G", "C", "D", "Em", "Am", "B"], ["Bm", "E"]]
G_sharp_and_Fm = [["G#", "C#", "D#", "Fm", "A#m", "C"], ["Cm", "F"]]
A_and_F_sharp_m = [["A", "D", "E", "F#m", "Bm", "C#"], ["C#m", "F#"]]
A_sharp_and_Gm = [["A#", "D#", "F", "Gm", "Cm", "D"], ["Dm", "G"]]
B_and_G_sharp_m = [["B", "E", "F#", "G#m", "C#m", "D#"], ["D#m", "G#"]]

a, b, c = map(str, input().split())

flag = 0
for element in C_and_Am[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1    
    if flag == 3:
        if a == C_and_Am[0][0]:
            print("C")
        else:
            print("Am")
        print(C_and_Am)
        exit()

flag = 0
for element in C_sharp_and_A_sharp_m[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1    
    if flag == 3:
        if a == C_sharp_and_A_sharp_m[0][0]:
            print("C#")
        else:
            print("A#m")
        print(C_sharp_and_A_sharp_m)
        exit()
    
flag = 0
for element in D_and_Bm[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1    
    if flag == 3:
        if a == D_and_Bm[0][0]:
            print("D")
        else:
            print("Bm")
        print(D_and_Bm)
        exit()
        
flag = 0
for element in D_sharp_and_Cm[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == D_sharp_and_Cm[0][0]:
            print("D#")
        else:
            print("Cm")
        print(D_sharp_and_Cm)
        exit() 
            
flag = 0
for element in E_and_C_sharp_m[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == E_and_C_sharp_m[0][0]:
            print("E")
        else:
            print("C#m")
        print(E_and_C_sharp_m)
        exit()
                
flag = 0
for element in F_and_Dm[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == F_and_Dm[0][0]:
            print("F")
        else:
            print("Dm")
        print(F_and_Dm)
        exit()                
    
flag = 0
for element in F_sharp_and_D_sharp_m[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == F_sharp_and_D_sharp_m[0][0]:
            print("F#")
        else:
            print("D#m")
        print(F_sharp_and_D_sharp_m)
        exit()

flag = 0
for element in G_and_Em[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == G_and_Em[0][0]:
            print ("G")
            print(G_and_Em)
        else:
            print("Em")
            print(G_and_Em)
        exit()
    
flag = 0
for element in G_sharp_and_Fm[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == G_sharp_and_Fm[0][0]:
            print("G#")
        else:
            print("Fm")
        print(G_sharp_and_Fm)
        exit()
        
flag = 0
for element in A_and_F_sharp_m[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == A_and_F_sharp_m[0][0]:
            print("A")
        else:
            print("F#m")
        print(A_and_F_sharp_m)
        exit() 
            
flag = 0
for element in A_sharp_and_Gm[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == A_Sharp_and_Gm[0][0] :
            print("A#")
        else:
            print("Gm")
        print(A_sharp_and_Gm)
        exit()
                
flag = 0
for element in B_and_G_sharp_m[0]:
    if element == a:
        flag += 1
    if element == b:
        flag += 1
    if element == c:
        flag += 1
    if flag == 3:
        if a == B_and_G_sharp_m[0][0]:
            print("B")
        else:
            print("G#m")
        print(B_and_G_sharp_m)
        exit()                    
