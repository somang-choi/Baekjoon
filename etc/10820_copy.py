import sys

def analyze(words):
    result = [0] * 4
    for w in words:
        if w.islower():
            result[0] += 1
        elif w.isupper():
            result[1] += 1
        elif w.isdigit():
            result[2] += 1
        elif w.isspace():
            result[3] += 1
    return list(map(str, result))


while True:
    try:
        line = sys.stdin.readline().rstrip('\n')
    except:
        break

    if len(line) == 0:
        break
    else:
        result = analyze(list(line))
        sys.stdout.write('%s\n' % ' '.join(result))
