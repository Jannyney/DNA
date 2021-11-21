import csv
from sys import argv

x = ""


def get_max(stri, gene):  # To get the max number of repetition
    ans = [0] * len(stri)
    for i in range(len(stri)-len(gene)):  # minus len(gene) to prevent repeating outside the len(stri) in the next step
        if stri[i: i + len(gene)] == gene:
            if stri[i - len(gene): i] != gene:  # if before i has an exist gene or not, if no
                ans[i] = 1
            else:
                ans[i] = ans[i-len(gene)] + 1
    return(max(ans))


if len(argv) == 3:
    with open(argv[1], "r") as file:
        reader = csv.reader(file)
        first = next(reader)[1:]

        with open(argv[2], "r") as text:
            s = text.read()
            lis = [get_max(s, DNA) for DNA in first]  # Make a list of the max of each gene

        for row in reader:
            person = row[0]
            Num_DNA = row[1:]  # Make a list of each row
            Num_DNA = list(map(int, Num_DNA))  # Change string to integer
            if Num_DNA == lis:
                x = person
                print(x)

    if x == "":
        print("No match")

else:
    print("Usage: python dna.py data.csv sequence.txt")