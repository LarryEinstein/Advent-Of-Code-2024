with open(r"python\day2\day2_example.txt", "rb") as file:
    data = file.read()

decoded_data = data.decode("utf-8")
rows = decoded_data.strip().split("\r\n")
data_as_rows = [list(map(int, row.split())) for row in rows]

report = data_as_rows[0]

print("original report = ", report)
# Try removing each level once and check if the resulting report is safe
for i in range(len(report)):
    modified_report =  report[:i] + report[i+1:]
    print(f"modified report {i} = ", modified_report)