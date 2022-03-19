import math
score = float(input())
score2 = 10*math.sqrt(score)
print('Original:', '%.2f' % (score))
print('Adjusted: ', '%.2f' % (score2), '(+', round(score2-score), ')', sep='')
