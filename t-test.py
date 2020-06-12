from os import listdir
from os.path import isfile, join
import numpy as np
from scipy import stats

AGR_FILE_TYPE = '.agr'
LOCAL_WORKING_DIRECTORY = '.'

def is_agr_file(file_name):
  return file_name.endswith(AGR_FILE_TYPE)

# Read files in current directory
all_agr_files = [f for f in listdir(LOCAL_WORKING_DIRECTORY) if is_agr_file(join(LOCAL_WORKING_DIRECTORY, f))]

sanitized_lines = []
split_string = ""
y_values = []
file_names = []
payload = {}

for file in all_agr_files:
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

t_test_result, p_value = stats.ttest_ind(np_prod_2,np_prod_20)
print("t test result = " + str(t_test_result))
print("p value result = " + str(2*p_value))
