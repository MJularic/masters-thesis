import sys


filename = sys.argv[1]

my_meter = open("Ashley-Madison.txt.my_meter")
pars_meter = open(filename)

all_lines_meter = my_meter.readlines()
all_lines_pars = pars_meter.readlines()

length = len(all_lines_meter)

mismatches = []

for i in range(length):
    if all_lines_meter[i].split()[1] != all_lines_pars[i].split()[1]:
        mismatches.append({"my_meter": all_lines_meter[i].split()[1], "pars_meter": all_lines_pars[i].split()[1], "password": all_lines_meter[i].split()[0]})

count_my_strong = 0
count_my_medium = 0
count_pars_strong = 0
count_pars_medium = 0

for i in range(len(mismatches)):

    if mismatches[i]["my_meter"] == "Strong" and mismatches[i]["pars_meter"] != "Strong":        
        count_my_strong += 1
        #print(mismatches[i])

    if mismatches[i]["my_meter"] == "Medium" and mismatches[i]["pars_meter"] == "Weak":
        count_my_medium += 1
        #print(mismatches[i])

    if mismatches[i]["pars_meter"] == "Strong" and mismatches[i]["my_meter"] != "Strong":        
        count_pars_strong += 1
        #print(mismatches[i])

    if mismatches[i]["pars_meter"] == "Medium" and mismatches[i]["my_meter"] == "Weak":
        count_pars_medium += 1
        #print(mismatches[i])


print("Analysis done for " + filename + " !")
print("Password number: " + str(length))
print("Matches: " + str(length - len(mismatches)))
print("Mismatches: " + str(len(mismatches)))
print("My meter has declared a password Strong for " + str(count_my_strong) + " when PARS did not!")
print("My meter has declared a password Medium for " + str(count_my_medium) + " when PARS did not!")
print("PARS has declared a password Medium for " + str(count_pars_medium) + " when my meter did not!")
print("PARS has declared a password Strong for " + str(count_pars_strong) + " when my meter did not!")
