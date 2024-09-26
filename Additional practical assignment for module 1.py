grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_k = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
students_k.sort()
all_students = {students_k[0] : float(sum(grades[0]) / len(grades[0])), students_k[1] : float(sum(grades[1]) / len(grades[1])), students_k[2] : float(sum(grades[2]) / len(grades[2])), students_k[3] : float(sum(grades[3]) / len(grades[3])), students_k[4] : float(sum(grades[4]) / len(grades[4]))}
print(all_students)