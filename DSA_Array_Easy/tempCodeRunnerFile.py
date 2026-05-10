prices = [2, 4, 6, 3, 8, 1, 10, 5, 7, 9]

# profit(prices)




# '''OPTIMAL APPROACH - 1'''

# def stock(prices):
    
#     sell = 0
    
#     buy = float('inf')
    
    
#     for price in prices:
        
#         if price < buy:
            
#             buy = price
        
#         sell = max(sell, price - buy)
    
#     print(sell)
    

# prices = [2, 4, 6, 3, 8, 1, 10, 5, 7, 9]

# stock(prices)


# '''BRUTE FORCE - 2'''

# def stock(price):
    
#     l = len(price)
    
#     max_profit = 0
    
#     for i in range(0, l):
#         for j in range(i + 1, l):
#             if price[j] > price[i]:
#                 p = price[j] - price[i]
#                 max_profit = max(max_profit, p)
#     print(f'Profit : {max_profit}')

# prices = [1,2,3,4,5]
# stock(prices)



# '''OPTIMAL - 2'''

# def stock(price):
    
#     sell = 0
    
#     buy = float('inf')
    
#     l = len(price)
    
#     for i in range(0, l):
        
#         buy = min(buy, price[i])
        
#         sell = max(sell, price[i] - buy)
    
#     print(f'Profit : {sell}')
    

# prices = [1,2,3,4,5]

# stock(prices)