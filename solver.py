import sys
import csv

def main(*args, **kwargs):
    po = set(("a", "e", "i", "o", "u", "y"))
    pi = set((",", ".", "-"))
    args = args[0]
    with open("words.txt", "r") as in_file:
        spamreader = csv.reader(in_file, delimiter=',', quotechar='|')
        for row in spamreader:
            if not set(row[0].lower()).intersection(po):
                continue

            if set(row[0].lower()).intersection(pi):
                continue

            d = {"XX": 0}
            for i in args:
                if i not in d:
                    d[i] = 0
                d[i] += 1
            good = True
            for ch in row[0].lower():
                if ch in d:
                    if d [ch] > 0:
                        d[ch] -= 1
                    else:
                        d["XX"] -= 1
                        if d["XX"] < 0:
                            good = False
                            break
                else:
                    d["XX"] -= 1
                    if d["XX"] < 0:
                        good = False
                        break
            if good:
                if (len(row[0])) <4:
                    continue
                print(row[0].lower())
    pass


if __name__ == "__main__":
    main(sys.argv[1:])
