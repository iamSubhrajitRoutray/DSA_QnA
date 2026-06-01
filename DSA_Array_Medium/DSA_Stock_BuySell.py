'''STOCK BUY SELL
Q)
You are given an array of prices where prices[i] is the price of a given stock on an ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.'''



''' DIRECT APPROACH '''

def stock(price):
    
    buy = min(price)
    
    sell = max(price)
    
    profit = sell - buy

    print(f'The profit for today is : {profit}')


prices = [2, 1, 5, 3, 9,4]

stock(prices)



''' BRUTE FORCE - 1 '''

def buy(arr):
    
    l = len(arr)
    
    buy = l
    
    for i in range(0, l):
        
        if arr[i] < buy:
            buy = arr[i]
    
    return buy


def sell(arr):
   
    l = len(arr)
    
    sell = 0
    
    for i in range(0, l):
       
        if arr[i] > sell:
            sell = arr[i]
    
    return sell


def profit(arr):
  
    profit = sell(arr) - buy(arr)
  
    print(f'The profit for today is {profit}.')



prices = [2, 4, 6, 3, 8, 1, 10, 5, 7, 9]

profit(prices)




''' OPTIMAL APPROACH - 1 '''

def stock(prices):
    
    sell = 0
    
    buy = float('inf')
    
    
    for price in prices:
        
        if price < buy:
            
            buy = price
        
        sell = max(sell, price - buy)
    
    print(sell)
    

prices = [2, 4, 6, 3, 8, 1, 10, 5, 7, 9]

stock(prices)


''' BRUTE FORCE - 2 '''

def stock(price):
    
    l = len(price)
    
    max_profit = 0
    
    for i in range(0, l):
        
        for j in range(i + 1, l):
            
            if price[j] > price[i]:
                
                p = price[j] - price[i]
                
                max_profit = max(max_profit, p)
    
    print(f'Profit : {max_profit}')



prices = [1,2,3,4,5]

stock(prices)



''' OPTIMAL - 2 '''

def stock(price):
    
    sell = 0
    
    buy = float('inf')
    
    l = len(price)
    
    for i in range(0, l):
        
        buy = min(buy, price[i])
        
        sell = max(sell, price[i] - buy)
    
    print(f'Profit : {sell}')
    

prices = [1,2,3,4,5]

stock(prices)