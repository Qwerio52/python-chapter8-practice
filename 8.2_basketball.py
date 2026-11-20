# 8.2 篮球竞技分析
import random

def simOneGame(probA, probB, rounds=50):
    scoreA, scoreB = 0, 0
    for i in range(rounds):
        if i % 2 == 0:
            # A进攻
            if random.random() < probA:
                scoreA += 2
        else:
            # B进攻
            if random.random() < probB:
                scoreB += 2
    return scoreA, scoreB

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
    probA = float(input("A进攻得分概率："))
    probB = float(input("B进攻得分概率："))
    n = int(input("模拟场次："))
    wa, wb = simNGame(probA, probB, n)
    print(f"A获胜 {wa} 场，胜率 {wa/n:.2%}")
    print(f"B获胜 {wb} 场，胜率 {wb/n:.2%}")
    print("\n对比乒乓：乒乓球是快速单球、11分制+净胜2分；篮球是回合累计得分，没有局点规则，胜负波动特征不一样")

if __name__ == "__main__":
    main()