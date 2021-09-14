# Check if two given sets have no elements in common

a = {1,2,3,4,5,6}
b = {4,5,6,7,9}
c = {8,0}

print('set a and b have common item : ', a.isdisjoint(b))
print('set b and c have common item : ', b.isdisjoint(c))
