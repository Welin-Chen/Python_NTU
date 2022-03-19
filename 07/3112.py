s1 = input()
s2 = input()
pos = s1.find(s2)

while(pos != -1):
    print(pos, "\t", s1[pos-2:pos], "+", s1[pos:(pos+len(s2))],
          "+", s1[pos+len(s2):pos+len(s2)+2], sep='')

    pos = s1.find(s2, pos+1)
