# prerequisite先决条件:

python3

sys

getopt



## help帮助:

**upup** can read the file line by line and 'capitalise the first letter of each line and lowercase others'. upup supports text formats such as .txt .md etc.

**upup** 能够逐行读取文件，并“大写每一行的首字母,让其余字母小写”。upup支持的文本格式有.txt .md等等<br><br>

how to use使用方法:

`python3 upup.py -h`

`python3 upup.py -i <inputfile> -o <outputfile>`

`python3 upup.py -m <inputfile1> <inputfile2> <outputfile1> `<br><br>


for example举例:

you can use `python3 upup.py -i ./dictionary.txt -o /new.txt` to capitalise the first letter of each line in your dictionary.txt and lowercase others and then output as new.txt.

你可以使用 `python3 upup.py -i ./dictionary.txt -o /new.txt` 来大写你dictionary.txt文件的每一行首字母，并让其余字母小写，并将文件输出为new.txt<br><br>

`-m` means merge. You can use this command to merge two files and delete the same lines to output a new file.

`-m` 指合并。你可以使用这条命令来让两个文件合并，并删除相同的行，生成一个新文件。

