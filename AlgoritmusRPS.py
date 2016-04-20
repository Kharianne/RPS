#Computer           Player      Value1          Value2
#=====================================================
#Rock               Scissors    0               2
#Rock               Paper       0               1
#Paper              Scissors    1               2
#Paper              Rock        1               0
#Scissors           Paper       2               1
#Scissors           Rock        2               0


print ((0-2)%3, "win")
print ((0-1)%3, "lost")
print ((1-2)%3, "lost")
print ((1-0)%3, "win")
print ((2-1)%3, "win")
print ((2-0)%3, "lost")