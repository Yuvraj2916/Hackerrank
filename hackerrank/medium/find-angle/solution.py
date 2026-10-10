# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB=int(input())
BC=int(input())
AC=math.hypot(AB,BC)
angle=math.degrees(math.atan2(AB,BC))
degree_symbol = chr(176)
print(str(round(angle)) + degree_symbol)
