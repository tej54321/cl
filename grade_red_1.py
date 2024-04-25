import sys

def reducer():
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for line in sys.stdin:
        name, grade = line.strip().split("\t")
        grade_counts[grade] += 1

    for grade, count in grade_counts.items():
        print(f"Grade {grade}: {count} students")
        
if __name__ =="__main__":
	reducer()
