n = int(input())

class_A = "A +" if n % 2 == 0 and n % 25 == 0 else "A -"
class_B = "B +" if n % 2 == 1 and n % 25 == 0 else "B -"  
class_C = "C +" if n % 8 == 0 else "C -"

print(class_A, class_B, class_C)