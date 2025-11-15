scores = list(map(int, input("Enter scores separated by space: ").split()))

total = sum(scores)
avg = total / len(scores)

print("Sum =", total)
print("Average =", avg)
