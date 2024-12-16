import utils

def longest_common_subsequence(a, b, c):
    n, m, l = len(a), len(b), len(c)

    dp = [[[0] * (l + 1) for x in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]

if __name__ == "__main__":
  data = utils.read_data_from_file('alg_lab7/task5/textf/input.txt')
  res = longest_common_subsequence(data[1], data[3], data[5])
  utils.write_data_to_file("alg_lab7/task5/textf/output.txt", str(res))
  print('lab7/task5')
  print(res)