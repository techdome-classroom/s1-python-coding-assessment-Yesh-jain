def decode_message(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Empty pattern matches empty message

    # Handle the '*' at the start of the pattern
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]

# Test cases
# print(decode_message("aa", "a"))    # Output: False
# print(decode_message("aa", "*"))    # Output: True
# print(decode_message("cb", "?a"))   # Output: False
# print(decode_message("abc", "a*c")) # Output: True
