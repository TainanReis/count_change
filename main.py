def count_change(money,coins):
  print(money, coins)
  # sort the array ascending
  coins.sort()
  # to store the combinations. Starts an array with a size that equals the money
  # each value starts with 0, so we can sum later on
  resultArray = [0]*(money+1)
  # there will never be a coin 0. That said, the first index is 1
  resultArray[0] = 1

  # this will run the code for each coin
  # all the indexes, except [0]=1, start with 0
  # I'll let the prints commented so you can see how this is working
  for coin in coins:
    index = 0
    #print("#Coin: ", coin)
    while ( (index <= money) ):
      if ( index >= coin ):
        temp = index-coin
        resultArray[index] += resultArray[temp]
        #print(resultArray)
      index += 1
      
  return resultArray[money]
