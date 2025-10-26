def LIS_len(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1s

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:  # Check if we can extend the subsequence
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The length of the longest increasing subsequence

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of the longest increasing subsequence is:", LIS_len(nums))
    
    
#Running time:
# The time complexity of this algorithm is O(n^2) 
# because we have two nested loops. 
# The outer loop runs n times and the inner loop also 
# runs up to n times in the worst case, leading to n * n = n^2 operations.