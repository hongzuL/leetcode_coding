# 151. Reverse Words in a String

def p151(s):
    s_list = s.split(" ")
    out_s = ""
    for i in range(1,len(s_list)+1):
        s = s_list[-i]
        if s != "":
            if out_s != "":
                out_s += " "
            out_s += s

    return out_s

def main():
    s = "  hello  world  "
    out_s = p151(s)
    print(out_s)

main()