arr1 = input('l1:').split()
arr2 = input('l2:').split()

arr1.reverse()
l1 = ''.join(arr1)
l1 = l1.zfill(len(arr1))

arr2.reverse()
l2 = ''.join(arr2)
l2 = l2.zfill(len(arr2))

out = int(l1) + int(l2)
print(list(str(out)))



