import csv

file = open("CSV_dataset_exploration/Popular_Baby_Names.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()
m_names = 0
f_names = 0

for name in data:
    if (name[1] == "MALE"):
        m_names += int(name[4])
    elif(name[1]== "FEMALE"):
        f_names += int(name[4])

print("Females with popular names: " + str(f_names))
print("Males with popular names: " + str(m_names))
