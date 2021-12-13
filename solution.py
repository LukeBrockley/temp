import sys

def secure(words, s):
    w = set([word.lower() for word in words])
    ret = s.split(' ')
    flag = False

    for i in range(len(ret)):
        phrase = ret[i]
        st, cur = [], ''

        for x, j in enumerate(phrase):
            if j.isalnum() or (j == "'" and cur and x != len(phrase) - 1 and phrase[x+1].isalnum()):
                cur += j
            else:
                if cur:
                    if cur.lower() in w:
                        flag = True
                        cur = '*' * len(cur)
                    st.append(cur)
                    cur = ''
                st.append(j)
        if cur and cur.lower() in w:
            flag = True
            st.append('*' * len(cur))
        else:
            st.append(cur)

        ret[i] = ''.join(st)

    return flag, ' '.join(ret)

def main(argv):
    if not len(argv):
        return -1
    str, words= argv[0], argv[1:]
    print(str, words)
    print(secure(words,str))

if __name__ == "__main__":
    main(sys.argv[1:])