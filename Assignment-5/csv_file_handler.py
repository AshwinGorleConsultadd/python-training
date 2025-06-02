from csv_utility.fetch_data import read_csv
from csv_utility.process_data import calculate_total
from csv_utility.report_data import save_to_csv

data = read_csv("./csv_utility/student_scores.csv")
processed_data = calculate_total(data)
save_to_csv(processed_data, "./csv_utility/student_score_with_total.csv")
