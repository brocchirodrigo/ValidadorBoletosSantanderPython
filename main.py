import datetime
import ValidateGroup
import ticketNumber
import ValidateDigitCode

vencimento = str(input('Insira o vencimento [yyyy-MM-dd]: '))
valor = str(input('Insira o valor [0.00]: '))
cedente = str(input('Insira o cedente [6 últimos dígitos do convênio]: '))
nossoNumero = str(input('Insira o nosso número: '))

paramDueDate = '1997-10-07'
dueDate = vencimento

formatateDueDay = datetime.datetime.strptime(dueDate, '%Y-%m-%d')
formatedParamDueDate = datetime.datetime.strptime(paramDueDate, '%Y-%m-%d')

quantityOfDays = abs((formatateDueDay - formatedParamDueDate).days)
bank = '033'.zfill(3)
moneyCode = '9'.zfill(1)
assignor = cedente.zfill(7)
nn = nossoNumero.zfill(12)
typeCart = '101'.zfill(3)
ticketValue = valor

digitoNN = ticketNumber.verifyTicket(nn)

groupOne = ValidateGroup.ValidateGroup(str(bank + moneyCode + '9' + assignor[0:4]))
groupTwo = ValidateGroup.ValidateGroup(str(assignor)[4:8] + nn[0:7])
groupThree = ValidateGroup.ValidateGroup(str(nn[7:12] + str(digitoNN) + '0' + typeCart))

preCode = str(bank + moneyCode + str(quantityOfDays) + str(ticketValue).replace('.', '').zfill(10) \
              + '9' + assignor + nn + str(digitoNN) + '0' + typeCart)

digCode = ValidateDigitCode.verifyTicketCode(preCode)

line = bank + moneyCode + '9.' + assignor[0:4] + str(groupOne) +\
        ' ' + str(assignor)[4:8] + nn[0:2] + '.' + nn[2:7] + str(groupTwo) \
        + ' ' + nn[7:12] + '.' + str(digitoNN) + '0' + typeCart + str(groupThree) \
        + ' ' + str(digCode) + ' ' + str(quantityOfDays).zfill(4) + str(ticketValue).replace('.', '').zfill(10)

code = str(bank + moneyCode + str(digCode) + str(quantityOfDays) + str(ticketValue).replace('.', '').zfill(10) \
              + '9' + assignor + nn + str(digitoNN) + '0' + typeCart)

print('\nLinha digitavel: {}'.format(line))
print('Código de barras: {}'.format(code))