a="welcome"
print(a[5])
try:
    print(a[10])
except:
    print("give proper index")
else:
    print("given proper index")
finally:
    print("successfulycompleted")
print(a[-1])