import random

def create(fn, encoding="utf-8"):
    fp = open(fn, "r", encoding=encoding)
    lines = fp.readlines()
    probs = []
    curr = []
    for l in lines:
        s = l[0]
        if ord("0") <= ord(s) <= ord("9"):
            if curr:
                probs.append(curr)
            p = a = ""
            for c in l:
                if ord("A") <= ord(c) <= ord("E"):
                    a += c
                else:
                    p += c
            curr = [[p, a]]
        elif ord("A") <= ord(s) <= ord("E"):
            curr.append(l)
    return probs
    
def main():
    import sqlite3
    conn = sqlite3.connect('../Question_Bank.db')
    c = conn.cursor()

    probs = create("base.txt")
    random.shuffle(probs)
    for p in probs:
        a = p[0][1]
        Problem = p[0][0].replace('）','').replace(')','').replace('【','').replace('】','').replace('（','').replace('(','')
        Answer_str = ''
        Answer = []
        for n in p[1:]:
            Answer.append(n.replace('\n','')[2:])
        for i in a:
            Answer_str += Answer[ord(i)-65] + '&'
        SQL = "INSERT INTO Data VALUES (?,?)"
        c.execute(SQL, (Problem, Answer_str))
        conn.commit()
    conn.close()



        
if __name__ == "__main__":
    main()