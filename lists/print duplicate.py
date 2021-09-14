l1 = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80, 70]
_ = []
for i in l1:
    if l1.count(i) > 1:
        _.append(i)
        l1.remove(i)
print(_)
