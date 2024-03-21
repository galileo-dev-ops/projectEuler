sumNum = 0
start = 1
end = 2
while end <= 4000000:
    if end % 2 == 0:
        sumNum += end
    start, end = end, start + end
print(sumNum)
