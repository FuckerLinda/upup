import sys
import getopt


#
# upup
#
def gbk(infile, outfile):
    file = open(infile, "r", encoding="gbk")
    file2 = open(outfile, "w")
    lines = file.readline();
    while lines:
        line = lines.replace("\n", "")
        # upcase the first letter
        new_line = line.capitalize();
        file2.write(new_line + "\n")
        # print to inspect
        # print(line)
        # print(type(line))
        lines = file.readline()
    file.close()


def utf_8(infile, outfile):
    file = open(infile, "r", encoding="utf-8")
    file2 = open(outfile, "w")
    lines = file.readline();
    while lines:
        line = lines.replace("\n", "")
        # upcase the first letter
        new_line = line.capitalize();
        file2.write(new_line + "\n")
        # print to inspect
        # print(line)
        # print(type(line))
        lines = file.readline()
    file.close()


#
# upup
#



#
# merge
#

def merge(f1, f2, f3):
    file1=f1
    file2=f2
    try:
        f1 = open(file1, "r")
        line1 = f1.readlines()
    except:
        f1.close()
        f1 = open(file1, "r",encoding="gbk")
        line1 = f1.readlines()
    try:
        f2 = open(file2, "r")
        line2 = f2.readlines()
    except:
        f2.close()
        f2 = open(file2, "r",encoding="gbk")
        line2 = f2.readlines()
    line3 = []

    for i in line1:
        if i not in line3:
            line3.append(i)
    for i in line2:
        if line3.count(i) == 0:
            line3.append(i)
    f3 = open(f3, "w")

    for i in line3:
        if "\n" not in i:
            continue
        i=str(i).replace("\n","\r\n")
        f3.write(i)




    """
    for i in line1:
        if i not in (line2 or line3):
            line3.append(i)
    f3=open(f3,"w")
    for i in line3:
        f3.write(i)
    """
    f1.close()
    f2.close()
    f3.close()


#
# merge
#






def main(argv):
    if len(sys.argv) > 1:
        inputfile = "";
        outputfile = "";
        mod = 0
        print("")
        # 参数输入
        try:
            opts, args = getopt.getopt(argv, "hi:o:m")
        # 无参时
        except getopt.GetoptError:
            print('if you need help, try to input "python3 test.py -h"')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('python3 test.py -h'
                      '\n'
                      '(help)'
                      '\n'
                      '\n'
                      'python3 test.py -i <inputfile> -o <outputfile>'
                      '\n'
                      '(capitalise your inputfile and then output)'
                      '\n'
                      '\n'
                      'python3 upup.py -m <inputfile1> <inputfile2> <outputfile1>\n'
                      '(merge inputfile1 and inputfile2,and delete the same lines to output a new file.)')
                sys.exit()
            elif opt in ("-i"):
                inputfile = arg
                mod = 1
            elif opt in ("-o"):
                outputfile = arg
            elif opt in ("-m"):
                mod = 2

        if mod == 1:
            print('input：', inputfile)
            print('output：', outputfile)
        elif mod == 2:
            print('input：', args[0], args[1])
            print('output：', args[2])

        ##upup
        if mod == 1:
            try:
                utf_8(inputfile, outputfile)
            except:
                try:
                    gbk(inputfile, outputfile)
                except Exception as e:
                    print("it seems that the encoding is nether utf-8 nor gbk")
                    print("e:",e)
                    print("e.with_traceback:",e.with_traceback())
                    exit(1)
        ##upup

        ##merge
        if mod == 2:
            f1 = args[0]
            f2 = args[1]
            f3 = args[2]
            try:
                merge(f1, f2, f3)
            except Exception as e:
                print("error!! WTF!? ")
                print("e:", e)
                print("e.with_traceback:", e.with_traceback())
                exit(1)
                ##merge

    else:
        print('if you need help, try to input "python3 test.py -h"')
        sys.exit(2)

    print("")


if __name__ == '__main__':
    main(sys.argv[1:])
