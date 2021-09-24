def findall(x):
  allthings = []
  while x>0:
    fx = 5+2*(x-1)
    print(fx)
    x = x-1
    allthings.append(str(fx))
  addallthings = '+'.join(allthings)
  print(str(eval(addallthings))+' total chairs in all the rows.')

findall(int(input("How many rows of chairs? ")))

#a simple explicit rule solver. It gets all the chairs in x rows, then adds them all. for math class.
