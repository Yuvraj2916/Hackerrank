if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))

        if command == "insert":
            arr.insert(args[0], args[1])
        elif command == "print":
            print(arr)
        elif command == "remove":
            arr.remove(args[0])
        elif command == "append":
            arr.append(args[0])
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()
