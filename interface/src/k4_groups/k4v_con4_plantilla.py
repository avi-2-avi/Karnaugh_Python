def k4v4(listing, label):
    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    #1	2	3	a	
    #4	<=	a	<=	16		

    if          line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #1	2	b	a	
    #4	<=	b	<=	15		
    #5	<=	a	<=	16		

    # b == 4

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #1	c	b	a	
    #2	<=	c	<=	14		
    #3	<=	b	<=	15		
    #4	<=	a	<=	16		

    ## c = 3

    # b == 4

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 4

    # b == 5

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #d	c	b	a	
    #2	<=	d	<=	13		
    #3	<=	c	<=	14		
    #4	<=	b	<=	15		
    #5	<=	a	<=	16		

    ### d = 2

    ## c = 3

    # b == 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 4

    # b == 5

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 3

    ## c = 4

    # b == 5

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 4

    ## c = 5

    # b == 6

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 5

    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 6

    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 7

    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 8

    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 9

    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 10

    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 11

    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 12

    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 13

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    return label
