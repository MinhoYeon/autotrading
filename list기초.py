# 리스트에서 타입별로 분류하기
from _collections import defaultdict
my_list = [ 0, "a", "b", "c", 12, 24]
data = defaultdict(list)
for x in my_list:
    data[type(x)].append(x)
print(data[str])
print(data[int])

print([x for x in my_list if isinstance(x, int)])