x = 5400

start = 0
end = 500
while end < x:
    print(start,end)
    start = end
    end += 500
start = end - 500
end = x
print(start,end)