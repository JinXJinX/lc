def test(words, k):
    s = set()
    for i in range(len(words)-k+1):
        s.add(words[i:i+k])
    return sorted(list(s))

if __name__ == '__main__':
    t1s = 'acccab'
    t1k = 2
    print(test(t1s, t1k))
