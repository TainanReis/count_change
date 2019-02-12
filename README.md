# count_change
Counts how many different ways we can make change for an ammount of money.

the actual index will be equal to the sum with value at [index-coin], e.g.
        coin 4, index 5 => 5-4=[1] => index[5] += index[1]
        coin 4, index 6 => 6-4=[2] => index[6] += index[2]
        coin 4, index 7 => 7-4=[3] => index[6] += index[3]
