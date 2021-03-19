def ValidateGroup(group):
    group = group[::-1]

    t01 = int(group[0]) * 2
    t01 = str(t01)
    if int(t01) > 9:
        t01 = int(t01[0]) + int(t01[1])
    else:
        t01 = int(t01)

    t02 = int(group[1]) * 1
    t02 = str(t02)
    if int(t02) > 9:
        t02 = int(t02[0]) + int(t02[1])
    else:
        t02 = int(t02)

    t03 = int(group[2]) * 2
    t03 = str(t03)
    if int(t03) > 9:
        t03 = int(t03[0]) + int(t03[1])
    else:
        t03 = int(t03)

    t04 = int(group[3]) * 1
    t04 = str(t04)
    if int(t04) > 9:
        t04 = int(t04[0]) + int(t04[1])
    else:
        t04 = int(t04)

    t05 = int(group[4]) * 2
    t05 = str(t05)
    if int(t05) > 9:
        t05 = int(t05[0]) + int(t05[1])
    else:
        t05 = int(t05)

    t06 = int(group[5]) * 1
    t06 = str(t06)
    if int(t06) > 9:
        t06 = int(t06[0]) + int(t06[1])
    else:
        t06 = int(t06)

    t07 = int(group[6]) * 2
    t07 = str(t07)
    if int(t07) > 9:
        t07 = int(t07[0]) + int(t07[1])
    else:
        t07 = int(t07)

    t08 = int(group[7]) * 1
    t08 = str(t08)
    if int(t08) > 9:
        t08 = int(t08[0]) + int(t08[1])
    else:
        t08 = int(t08)

    t09 = int(group[8]) * 2
    t09 = str(t09)
    if int(t09) > 9:
        t09 = int(t09[0]) + int(t09[1])
    else:
        t09 = int(t09)

    if len(group) == 10:
        t10 = int(group[9]) * 1
        t10 = str(t10)
        if int(t10) > 9:
            t10 = int(t10[0]) + int(t10[1])
        else:
            t10 = int(t10)
    else:
        t10 = 0

    sumGroup = int(t01 + t02 + t03 + t04 + t05 + t06 + t07 + t08 + t09 + t10)

    resGroup = sumGroup % 10

    verifyGroup = 0

    if resGroup == 0:
        verifyGroup = 0
    else:
        verifyGroup = (10 - resGroup)

    return verifyGroup
