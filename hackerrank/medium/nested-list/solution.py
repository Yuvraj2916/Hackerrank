if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest = sorted(set(score for _, score in records))[1]
    for name in sorted(name for name, score in records if score == second_lowest):
        print(name)
