from calculate_probability import CalculateProbability


cp = CalculateProbability("/home/mj/diplomski-rad/database/n-gram.db")

dump_file = open("/home/mj/diplomski-rad/data/Ashley-Madison.txt.my_meter", "w")

with open("/home/mj/diplomski-rad/data/password_files/Ashley-Madison.txt") as f:
    line = f.readline()
    while line:
        score = cp.calculate_probability(line.strip())
        if score < 60:
            dump_file.write(line.strip() + "\t" + "Weak\n")
        if 60 < score < 80:
            dump_file.write(line.strip() + "\t" + "Medium\n")
        if score > 80:
            dump_file.write(line.strip() + "\t" + "Strong\n")
        line = f.readline()

dump_file.close()