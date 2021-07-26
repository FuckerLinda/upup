import sys
import getopt


def gbk(infile,outfile):
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

def utf_8(infile,outfile):
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

def main(argv):
    if len(sys.argv) > 1:
        inputfile="";
        outputfile="";
        #参数输入
        try:
            opts, args = getopt.getopt(argv, "hi:o:")
        #无参时
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
                  '\n')
                sys.exit()
            elif opt in ("-i"):
                inputfile = arg
            elif opt in ("-o"):
                outputfile = arg
        print('input：', inputfile)
        print('output：', outputfile)
    else:
        print('if you need help, try to input "python3 test.py -h"')
        sys.exit(2)
    try:
        utf_8(inputfile,outputfile)
    except:
        try:
            gbk(inputfile,outputfile)
        except:
            print("error:the encoding is nether utf-8 nor gbk")
    print("finish.")

if __name__=='__main__':
    main(sys.argv[1:])
