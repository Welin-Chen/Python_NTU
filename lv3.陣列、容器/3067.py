itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}  # 這是第一個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}  # 這是第二個集合

A1 = input()
A2 = input()
B1 = input()
B2 = input()
itemsA.add(A1)
itemsA.add(A2)
itemsB.add(B1)
itemsB.add(B2)
itemsA.remove("蘋果")
itemsB.remove("蓮霧")
print("iA:", sorted(list(itemsA)))
print("iB:", sorted(list(itemsB)))
print("union:", sorted(list(itemsA | itemsB)))
print("intersection:", sorted(list(itemsA & itemsB)))
print("A diff B:", sorted(list(itemsA - itemsB)))
print("B diff A:", sorted(list(itemsB - itemsA)))
print("A xor B:", sorted(list(itemsB ^ itemsA)))

# iA: ['火龍果', '百香果', '芭樂', '香蕉', '鳳梨']
# iB: ['水梨', '百香果', '蘋果', '西瓜', '鳳梨']
# union: ['水梨', '火龍果', '百香果', '芭樂', '蘋果', '西瓜', '香蕉', '鳳梨']
# intersection: ['百香果', '鳳梨']
# A diff B: ['火龍果', '芭樂', '香蕉']
# B diff A: ['水梨', '蘋果', '西瓜']
# A xor B: ['水梨', '火龍果', '芭樂', '蘋果', '西瓜', '香蕉']
# 火龍果
# 百香果
# 百香果
# 西瓜
