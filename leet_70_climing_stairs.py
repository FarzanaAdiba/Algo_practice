#optimized approach using memoization - T(n) = O(n)
#creating memo dictionary
def stair_memo(n, memo={}):
    if memo is None:
        memo={}
    if n<0:
        return 0
    if n<=2:
        return n
    memo[n] = stair_memo(n-1, memo) + stair_memo(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    num = int(input("Enter the number of stairs: "))
    print(f"Stairs of {num} using memoization is {stair_memo(num)}")
    
