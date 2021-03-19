def verifyTicket(ticket):
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

    sumTicket = (t01 + t02 + t03 + t04 + t05 + t06 + t07 + t08 + t09 + t10 + t11 + t12)

    resTicket = sumTicket % 11

    verifyDig = 0

    if resTicket == 10:
        verifyDig = 1
    elif resTicket == 1:
        verifyDig = 0
    elif resTicket == 0:
        verifyDig = 0
    else:
        verifyDig = (11 - resTicket)

    return verifyDig

