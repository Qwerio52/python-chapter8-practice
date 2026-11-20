
下面是全部7份py文件，挨个复制保存：

### 8.1_table_tennis.py
```python
# 8.1 乒乓竞技分析
import random

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                scoreA += 1
        # 每2分换发球
        if (scoreA + scoreB) % 2 == 0:
            serving = "B" if serving == "A" else "A"
    return scoreA, scoreB

def gameOver(a,b):
    return (a >=11 or b >=11) and abs(a-b) >=2

def simNGame(probA, probB, n):
    winA, winB = 0, 0
    for _ in range(n):
        sa, sb = simOneGame(probA, probB)
        if sa > sb:
            winA +=1
        else:
            winB +=1
    return winA, winB

def main():
    probA = float(input("选手A得分概率："))
    probB = float(input("选手B得分概率："))
    n = int(input("模拟场次："))
    wa, wb = simNGame(probA, probB, n)
    print(f"A获胜 {wa} 场，胜率 {wa/n:.2%}")
    print(f"B获胜 {wb} 场，胜率 {wb/n:.2%}")

if __name__ == "__main__":
    main()