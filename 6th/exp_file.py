import os

file_path = 'sample.txt'
file_stat = os.stat(file_path)
print(oct(file_stat.st_mode & 0o777))  # use & to get last 3 digit, each digit is 3bit of 'rwx'
