def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   print(coinsUsed)
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():

   change = 30
   coinsList = [100,50,25,10,1]
   coinsUsed = [0]*(change+1)
   coinCount = [0]*(change+1)

   print("Fazendo troco para",change,"requer")
   print(dpMakeChange(coinsList,change,coinCount,coinsUsed),"cédulas")
   print("Elas são:")
   printCoins(coinsUsed,change)

main()