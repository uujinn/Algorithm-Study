import math
import time

start = time.time() 

# 0.06310 - 0.07155 sec
# a = [0] * 999999
# for i in range(999999):
#     a[i] = 1

# 0.07400 - 0.08023 sec
a = []
for _ in range(999999):
    a.append(1)
end = time.time()

print(f"{end - start:.5f} sec")
