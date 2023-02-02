def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1): #n + 1
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]: #m
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin

   print("Número de moedas para troco de cada valor até o valor do troco \n", minCoins, "\n")
   return minCoins[change]

def printCoins(coinsUsed,change):
   coinsFinally = []
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      coinsFinally.append(thisCoin)
      coin = coin - thisCoin
   print("Moedas utilizadas para o troco: ", coinsFinally, '\n')
   print("Maior moeda utilizada nos testes para cada valor \n", coinsUsed, '\n')

def main():

   change = 30
   coinsList = [100,50,25,10,1]
   coinsUsed = [0]*(change+1)
   coinCount = [0]*(change+1)

   print("Fazendo troco para",change,"requer", dpMakeChange(coinsList,change,coinCount,coinsUsed),"moedas")
   printCoins(coinsUsed, change)

main()