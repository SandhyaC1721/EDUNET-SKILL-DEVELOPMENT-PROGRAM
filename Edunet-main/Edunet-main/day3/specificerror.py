a="welcome"
print(a[5])
try:
    print(b[10])
except IndexError:
    print("handle index error")
else:
    print("given proper index")
finally:
    print("successfulycompleted")
print(a[-1])