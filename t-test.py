from os import listdir
from os.path import isfile, join
import io
import numpy as np
from scipy import stats

def is_agr_file(file_name):
  return file_name.endswith('.agr')

# Read files in current directory
my_path = "."
all_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
clean_files = [ f for f in all_files if is_agr_file(f) ]

sanitized_lines = []
split_string = ""
y_values = []
file_names = []
payload = {}

for file in clean_files:
  file = open(file)
  file_names += [file.name]
  lines = file.readlines()
  if file not in payload:
    y_values = []
  payload[file.name] = y_values
  for line in lines:
    if "@" not in line:
      split_string = line.split()
      sanitized_lines += [split_string]
      y_values += [float(split_string[1])]

prod_2_list = payload.get(file_names[0])
prod_20_list = payload.get(file_names[1])

#convert list to numpy array
np_prod_2 = np.array(prod_2_list)
np_prod_20 = np.array(prod_20_list)

# this actually works for t-test lol. Didnt need to do lines 45 through 54. Both values (t_stat  annd t2  are  same)
t2, p2 = stats.ttest_ind(np_prod_2,np_prod_20)
print("t = " + str(t2))
print("p = " + str(2*p2))


