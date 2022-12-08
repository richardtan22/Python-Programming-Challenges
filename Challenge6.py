"""
MaxProfit
Given a log of stock prices compute the maximum possible earning.

Consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because
A[2] - A[0] = 21123 - 23171 = -2048. If a share was bought on day 4 and sold on day 5,
a profit of 354 would occur because A[5] - A[4] = 21367 - 21013 = 354.
Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold
on day 5.

"""

def buy_and_sell(stock_price):
    max_profit_val, current_max_val = 0, 0 
    for price in reversed(stock_price):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val


A = [23171, 21011, 21123, 21366, 21013, 21367]
buy_and_sell(A)
