# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #topay word berekend met een user input als een getal
paid = int(float(input('Paid amount: ')) * 100) #paid word berekend met een user input als een getal
change = paid - toPay #simpele som die een som maakt met de opgegeven waardes.

if change > 0: #als uit de bovenstaande som 0 kwam word coinvalue 50
  coinValue = 50 #coinvalue word gezet
  
  while change > 0 and coinValue > 0: #als change en coinvalue 0 zijn word het volgende herhaald
    nrCoins = change // coinValue # nrcoins = change gedeelt door (en naar beneden afgerond) coinvalue

    if nrCoins > 0: #als nrcoins dankzij de bovenstaande som 0 is...
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #word return maximal (met het uitgerekende nrcoins) coins of (de eerder gezette coinvalue) cents! geprint.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # het vraagt voor hoeveel coins je hebt teruggegeven
      change -= nrCoinsReturned * coinValue #coinvalue keer nrcoinsreturned min change word change.

# comment on code below: het checked hoeveel van de verschillende coins je hebt teruggegeven. (samen met mijn really scuffed code)
    if coinValue == 500
      coinValue = 300
    elif coinValue == 300
      coinValue = 200
    elif coinValue == 200
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als change na dat alles nog steeds 0 is word er verteld hoeveel er moest worden betaald.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')