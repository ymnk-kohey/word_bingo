#Python3にて作成

s = int(input())                                                #標準入力（整数）
a = [list(map(str, input().split())) for i in range(s)]         #二重リスト（配列）に標準入力
d = [[0 for i in range(s)] for j in range(s)]                   #要素が全て０の（s x s）二重リスト（配列）
n = int(input())                                                #標準入力（整数）

for word in range(n):                    #n回繰り返す                               
    w = input()                          #標準入力（文字列）
    for i in range(s):
        for j in range(s):
            if a[i][j] == w:             #aにwと同じ数字があるかを確認
                d[i][j] = 1              #同じ数字があれば、対応するdに１を代入

ans = "no"          #最初は"no"と仮定
count = 0

#横でビンゴしているかを確認

for i in range(s):
    if ans == "yes":
        break
    count = 0
    for j in range(s):
        count += d[i][j]
        if count == s:
            ans = "yes"

#縦でビンゴしているかを確認

for i in range(s):
    if ans == "yes":
        break
    count = 0
    for j in range(s):
        count += d[j][i]
        if count == s:
            ans = "yes"

#左上から右下にかけて斜めにビンゴしているかを確認

count = 0
for i in range(s):
    if ans == "yes":
        break
    count += d[i][i]
    if count == s:
        ans = "yes"

#右上から左下にかけて斜めにビンゴしているかを確認

count = 0
for i in range(s):
    if ans == "yes":
        break
    count += d[i][(s - 1) - i]
    if count == s:
        ans = "yes"

print(ans)          #標準出力（"yes"か"no"）