import utils

def longest_common_subsequence(a, b):
    n = len(a)
    m = len(b)
    
    dp = [[0] * (m + 1) for x in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

if __name__ == "__main__":
  data = utils.read_data_from_file('alg_lab7/task4/textf/input.txt')
  res = longest_common_subsequence(data[1], data[3])
  utils.write_data_to_file("alg_lab7/task4/textf/output.txt", str(res))