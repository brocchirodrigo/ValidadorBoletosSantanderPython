def verifyTicketCode(ticket):
    ticket = ticket[::-1]
    t01 = int(ticket[0]) * 2
    t02 = int(ticket[1]) * 3
    t03 = int(ticket[2]) * 4
    t04 = int(ticket[3]) * 5
    t05 = int(ticket[4]) * 6
    t06 = int(ticket[5]) * 7
    t07 = int(ticket[6]) * 8
    t08 = int(ticket[7]) * 9
    t09 = int(ticket[8]) * 2
    t10 = int(ticket[9]) * 3
    t11 = int(ticket[10]) * 4
    t12 = int(ticket[11]) * 5
    t13 = int(ticket[12]) * 6
    t14 = int(ticket[13]) * 7
    t15 = int(ticket[14]) * 8
    t16 = int(ticket[15]) * 9
    t17 = int(ticket[16]) * 2
    t18 = int(ticket[17]) * 3
    t19 = int(ticket[18]) * 4
    t20 = int(ticket[19]) * 5
    t21 = int(ticket[20]) * 6
    t22 = int(ticket[21]) * 7
    t23 = int(ticket[22]) * 8
    t24 = int(ticket[23]) * 9
    t25 = int(ticket[24]) * 2
    t26 = int(ticket[25]) * 3
    t27 = int(ticket[26]) * 4
    t28 = int(ticket[27]) * 5
    t29 = int(ticket[28]) * 6
    t30 = int(ticket[29]) * 7
    t31 = int(ticket[30]) * 8
    t32 = int(ticket[31]) * 9
    t33 = int(ticket[32]) * 2
    t34 = int(ticket[33]) * 3
    t35 = int(ticket[34]) * 4
    t36 = int(ticket[35]) * 5
    t37 = int(ticket[36]) * 6
    t38 = int(ticket[37]) * 7
    t39 = int(ticket[38]) * 8
    t40 = int(ticket[39]) * 9
    t41 = int(ticket[40]) * 2
    t42 = int(ticket[41]) * 3
    t43 = int(ticket[42]) * 4

    sumTicket = (t01 + t02 + t03 + t04 + t05 + t06 + t07 + t08 + t09 + t10 + t11 + t12 + t13 + t14 + t15 + t16 + t17 + t18 + t19 + t20 + t21 + t22 + t23 + t24 + t25 + t26 + t27 + t28 + t29 + t30 + t31 + t32 + t33 + t34 + t35 + t36 + t37 + t38 + t39 + t40 + t41 + t42 + t43)

    mulTicket = sumTicket * 10
    resTicket = mulTicket % 11

    verifyDig = 0

    if resTicket == 10:
        verifyDig = 1
    elif resTicket == 1:
        verifyDig = 1
    elif resTicket == 0:
        verifyDig = 1
    else:
        verifyDig = resTicket

    return verifyDig
