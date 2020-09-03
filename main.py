# Author: John Scott jjs6893@psu.edu
# Collaborator: Jason Swope jbs6237@psu.edu
# Collaborator: Jacob Dally jed5801@psu.edu
# Collaborator: Chinmay Vibhute ckv55108@psu.edu
temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
if(unit == "F" or unit == "f"):
  print(f"{temp}° in Fahrenheit is equivalent to {(temp - 32) / 1.8}° Celsius.")
elif(unit == "C" or unit == "c"):
  print(f"{temp}° in Celsius is equivalent to {(temp * 1.8) + 32}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")