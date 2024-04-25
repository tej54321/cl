import sys

def mapper():
    for line in sys.stdin:
        name_scores = line.strip().split(", ")  # Split the line using comma as the delimiter
        name = name_scores[0]
        scores = list(map(int, name_scores[1].split()))  # Split scores using spaces as the delimiter
        average_score = sum(scores) / len(scores)
        grade = assign_grade(average_score)
        print(f"{name}\t{grade}")

def assign_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    mapper()

