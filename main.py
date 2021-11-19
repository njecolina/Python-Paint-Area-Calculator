import math

def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area / cover)
  print(f"\nYou'll need {num_of_cans} cans of paint. Thank you for using this program!")

print('''
██████╗  █████╗ ██╗███╗   ██╗████████╗     █████╗ ██████╗ ███████╗ █████╗          
██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██╔══██╗         
██████╔╝███████║██║██╔██╗ ██║   ██║       ███████║██████╔╝█████╗  ███████║         
██╔═══╝ ██╔══██║██║██║╚██╗██║   ██║       ██╔══██║██╔══██╗██╔══╝  ██╔══██║         
██║     ██║  ██║██║██║ ╚████║   ██║       ██║  ██║██║  ██║███████╗██║  ██║         
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         
                                                                                   
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                   ''')
print("* Calculate the amount of paint buckets needed to paint specific area *\nVersion 0.0.1. - by Sonja Hranjec 2021.\n")

test_h = float(input("Height of wall (in meters): "))
test_w = float(input("Width of wall (in meters): "))
coverage = int(input("How many square meters can one can of paint cover? "))
paint_calc(height=test_h, width=test_w, cover=coverage)
