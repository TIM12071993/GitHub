import sys
import monkey
if __name__ == "__main__":
   print("Hello World")
   print("Starting to understand Git. This is already my second commit")
   print("Hello World again")
   print("I think I already understand the basic concept of add and commit. Really?")
   print("sup")
   monkey.print_monkeys([0,1,2,3,4,5])
   def print_palmtrees(num):
        for i in range(num):
            sys.stdout.write(' /|\\')
        sys.stdout.write('\n')
        for i in range(num):
            sys.stdout.write('  | ')
        sys.stdout.write('\n\n')
   print_palmtrees(7)
   print ("Hello Again")
   
   
   
