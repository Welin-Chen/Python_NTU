itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}  # 這是第一個集合
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}  # 這是第二個集合
symmetric_diff_AB = itemsA ^ itemsB
print(sorted(list(symmetric_diff_AB)))
