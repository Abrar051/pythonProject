with open('Example.txt','r') as readfile:
    with open('Example1.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
