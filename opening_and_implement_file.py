# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import array

__author__ = "mia"
__date__ = "$Jan 25, 2019 12:53:39 AM$"

#table 7

#file variable reads testfile
file = open("testfile","r")

#num_lines variable holds num of lines from testfile
content = file.readlines()

for x in range(len(content)):
    print content[x],

#closes file
file.close()
