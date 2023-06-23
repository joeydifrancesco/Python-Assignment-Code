import sys                   #importin sys module for command line arguments

class Grades():               #Class named Grades()
   
   def __init__(self):           
       self.grades = []
   
   def read_grades(self,file_name):       
       temp_grades = []                   #initializing two temparary lists
       temp_credits = []
       file1 = open(file_name,"r")
       
       while file1:                      
           line = (file1.readline()).split()       #reading line by line until the file is empty
           
           if(len(line)!=0):                       #If line is not empty spliting the list and saving values
               temp_grades.append(line[0])
               temp_credits.append(float(line[1]))       #converting into float
           else:
               break;                               #breaking the loop if line is empty that is end of the file
       grade = tuple(temp_grades)
       credits = tuple(temp_credits)           #creating grade and credits tuples from tempary lists
       self.grades.append(grade)                   #appending grade and credits to grades list
       self.grades.append(credits)
   
   def calculate_gpa(self):                   
       totalNumberOfCredits = 4.0 + 3.0 + 2.0 + 1.0 + 0.0       #total number of credits
       totalValue = 0
       
       for (grade,credits) in zip(self.grades[0],self.grades[1]):   #used to itearte over two items once
           if(grade == 'A'):
               totalValue += (credits*4.0)                   #Calculating totalValue according to the file values
           elif(grade == 'B'):
               totalValue += (credits*3.0)
           elif(grade == 'C'):
               totalValue += (credits*2.0)
           elif(grade == 'D'):
               totalValue += (credits*1.0)
           elif(grade == 'F'):
               totalValue += (credits*0.0)
       total_gpa = (totalValue / totalNumberOfCredits) #calculating the total gpa
       
       return total_gpa       #returning total gpa

def main(file_name):           #main function with file_name as parameter
   
   obj = Grades()               #Creating an object instance of class Grades
   obj.read_grades(file_name)       #calling read_grades function
   result = obj.calculate_gpa()   #calling calculate_gpa function
   print(f"\nThe GPA is {result}.\n");       #printing the result using f-string

if __name__ == "__main__":         
  
   if len(sys.argv) != 2:           #printing message if file name is not pass
       print("\nEnter Valid Number of Command Line Arguments\n")
   else:                  
       file_name = sys.argv[1]
       main(file_name)       #calling main() function with file_name as parameter