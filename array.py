import sys

if len(sys.argv) == 4:
    english = int(sys.argv[1])
    maths = int(sys.argv[2])
    kannada = int(sys.argv[3])
else:
    english = 50
    maths = 75
    kannada = 100

scores = [english, maths, kannada]


score = sum(scores)
avg = score / 3
maximum = max(scores)
minimum = min(scores)


print("Total score:", score)
print("Average:", avg)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
