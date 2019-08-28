#change csv values
import sys, getopt

def changeValues(csv_path):
    text = open(csv_path, "r")
    text = ''.join([i for i in text]) \
        .replace("5more", "5") \
        .replace("more", "5")
    x = open(csv_path,"w")
    x.writelines(text)
    x.close()

if __name__ == '__main__':
    
    input_file = None
    args, _ = getopt.getopt(sys.argv[1:], "i:o:")

    for o, a in args:
        if o == '-i' and a:
            input_file = a

    if not input_file:
        print("Usage: %s -i \"input_file.csv\"" % sys.argv[0])
        exit(0)

    changeValues(input_file)