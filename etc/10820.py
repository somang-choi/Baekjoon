import sys, string

def analyze(words):
    result = [0] * 4
    for w in words:
        code = ord(w)
        if code >= 97 and code <= 122:
            result[0] += 1
        elif code >= 65 and code <= 90:
            result[1] += 1
        elif code >= 48 and code <= 57:
            result[2] += 1
        elif code == 32:
            result[3] += 1
    return list(map(str, result))


while True:
    try:
        line = sys.stdin.readline()
    except:
        break

    if len(line) == 0:
        break
    else:
        result = analyze(list(line))
        sys.stdout.write('%s\n' % ' '.join(result))
