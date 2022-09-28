# Hexagon's perimeter and area calculator with geometric identifier
s = float(input("To calculate Hexagon's perimeter and area enter line metric: "))
apothem = float(input("Enter apothem of hexagon: "))

if apothem == s:
    print("This is a straight hexagon")
elif apothem < s:
    print("Hexagon cannot be created.")
else:
    print("This ain't straight hexagon")
perimeter = (s * 6)
area = (1/2 * perimeter * apothem)
"""
asdsadas
"""
print("Area:", area ,"Perimeter:", perimeter)