'''
901. Online Stock Span
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 

Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 

Constraints:

1 <= price <= 105
At most 104 calls will be made to next.''
'''
class StockSpanner:

    def __init__(self):
        self.history = []  # Stores stock prices by day
        self.stk = []      # Monotonic decreasing stack of indices (prices)

    def next(self, price: int) -> int:
        # Add today's price to history
        self.history.append(price)
        n = len(self.history)
        
        # Pop from stack while top's price is less than or equal to current
        while self.stk and price >= self.history[self.stk[-1]]:
            self.stk.pop()
        
        # If stack is empty, all previous prices were <= current → span = n
        # Otherwise, span is the distance to the last higher price
        ans = n if not self.stk else n - 1 - self.stk[-1]
        
        # Push current index onto the stack
        self.stk.append(n - 1)
        
        return ans

class StockSpanner2:

    def __init__(self):
        self.stk = []  # stack of (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0] <= price:
            span += self.stk.pop()[1]
        self.stk.append((price, span))
        return span

# Example usage:
if __name__ == "__main__":
    sol = StockSpanner()
    print(sol.next(100))  # Output: 1
    print(sol.next(80))   # Output: 1
    print(sol.next(60))   # Output: 1
    print(sol.next(70))   # Output: 2
    print(sol.next(60))   # Output: 1
    print(sol.next(75))   # Output: 4
    print(sol.next(85))   # Output: 6