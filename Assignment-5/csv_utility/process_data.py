def calculate_total(data):
    for row in data:
        marks = [int(row.get(subject, 0)) for subject in row if subject.lower() not in ("name", "rollno")]
        row["Total"] = sum(marks)
    return data
