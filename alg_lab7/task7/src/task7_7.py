from utils import read_data_from_file, write_data_to_file

def is_match(pattern, string):
    m, n = len(pattern), len(string)
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

if __name__ == '__main__':
    data = read_data_from_file('alg_lab7/task7/textf/input.txt')
    pattern = data[0].strip()  
    string = data[1].strip()   
    
    if is_match(pattern, string):
        write_data_to_file('alg_lab7/task7/textf/output.txt', ['YES'])
    else:
        write_data_to_file('alg_lab7/task7/textf/output.txt', ['NO'])
