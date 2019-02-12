# count_change
Counts how many different ways we can make change for an ammount of money.

        count_change(money,coins)
where money is an int and coins an array of int. Examples:

        count_change(4, [1,2]) # =>  3
        count_change(15,[1]) # => 1
        count_change(11, [5,7]) # => 0
        count_change(10, [2,5,3,6]) # => 5
        count_change(199,[3,5,9,15]) # => 760
        


This is how it works. The actual index will be equal to the sum with value at [index-coin], e.g.

        coin 4, index 5 => 5-4=[1] => index[5] += index[1]
        
        coin 4, index 6 => 6-4=[2] => index[6] += index[2]
        
        coin 4, index 7 => 7-4=[3] => index[6] += index[3]
