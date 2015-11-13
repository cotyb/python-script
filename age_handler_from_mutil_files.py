#!/usr/bin/python
#coding:utf-8
'''
get the relationship between qqage and predicted qqage
input: multi files containing qq information
output: graphs, data detail and so on
in the graph, the color from 1 to 6 is
blue, green, black, red, cyan, yellow
'''
__author__ = 'cotyb'

import os
import matplotlib.pyplot as plt
from itertools import islice
import time

#cwd: current work directory
cwd = os.getcwd()
#data_dir:the location of the age data
data_dir = cwd + "\\age1\\"
#result_dir: store the final result.txt data and graphs
result_dir = cwd + "\\result\\"
#files:all qq data files to handle
#delta_cnt:{delta:number}
delta_cnt1 = {}
delta_cnt2 = {}
delta_cnt3 = {}
delta_cnt4 = {}
delta_cnt5 = {}
delta_cnt6 = {}
delta_cnt7 = {}
delta_cnt8 = {}
delta_cnt9 = {}
#period_cnt:{the delta < aget: count}
period_cnt1 = {}
period_cnt2 = {}
period_cnt3 = {}
period_cnt4 = {}
period_cnt5 = {}
period_cnt6 = {}
period_cnt7 = {}
period_cnt8 = {}
period_cnt9 = {}
#delta_age:{delta:qqage}
delta_age1 = {}
delta_age2 = {}
delta_age3 = {}
delta_age4 = {}
delta_age5 = {}
delta_age6 = {}
delta_age7 = {}
delta_age8 = {}
delta_age9 = {}
#count:the number of qq
count_all = 0
count_campus = 0
files = os.listdir("age1")
total_files = len(files)
#file_num: to detect the file are handling
file_num = 0
#result:it's a txt file to store the  result data
result = open(result_dir + "\\result.txt","w")
distribution = open(result_dir + "\\distribution.txt","w")
for file in files:
    file_num += 1
    print "you are running file %d at %s" %(file_num, time.ctime())
    #print "remaining file number is %d" %(total_files - file_num)
    fr = open(data_dir + file, "r+")
    all_lines = fr.readlines()
    for line in all_lines[1:]:
    #for line in islice(fr,1,None):
        count_all += 1
        if not line.__contains__("*"):
            count_campus += 1
        line = line.replace("*","-1")
        line = eval(line)
        qq_age = line[1]
        pre_age1 = line[2]
        pre_age2 = line[3]
        pre_age3 = line[4]
        pre_age4 = line[5]
        pre_age5 = line[6]
        pre_age6 = line[7]
        delta2 = pre_age2 - qq_age
        if abs(delta2) in delta_cnt2:
            delta_cnt2[abs(delta2)] += 1
        else:
            delta_cnt2.setdefault(abs(delta2),1)
        if abs(delta2) in delta_age2:
            if qq_age in delta_age2[abs(delta2)]:
                delta_age2[abs(delta2)][qq_age] += 1
            else:
                delta_age2[abs(delta2)][qq_age] = 1
        else:
            delta_age2[abs(delta2)] = {}
            delta_age2[abs(delta2)][qq_age] = 1
        delta4 = pre_age4 - qq_age
        if abs(delta4) in delta_cnt4:
            delta_cnt4[abs(delta4)] += 1
        else:
            delta_cnt4.setdefault(abs(delta4),1)
        if abs(delta4) in delta_age4:
            if qq_age in delta_age4[abs(delta4)]:
                delta_age4[abs(delta4)][qq_age] += 1
            else:
                delta_age4[abs(delta4)][qq_age] = 1
        else:
            delta_age4[abs(delta4)] = {}
            delta_age4[abs(delta4)][qq_age] = 1
        delta6 = pre_age6 - qq_age
        if abs(delta6) in delta_cnt6:
            delta_cnt6[abs(delta6)] += 1
        else:
            delta_cnt6.setdefault(abs(delta6),1)
        if abs(delta6) in delta_age6:
            if qq_age in delta_age6[abs(delta6)]:
                delta_age6[abs(delta6)][qq_age] += 1
            else:
                delta_age6[abs(delta6)][qq_age] = 1
        else:
            delta_age6[abs(delta6)] = {}
            delta_age6[abs(delta6)][qq_age] = 1
        if pre_age1 != -1:
            delta1 = pre_age1 - qq_age
            if abs(delta1) in delta_cnt1:
                delta_cnt1[abs(delta1)] += 1
            else:
                delta_cnt1.setdefault(abs(delta1),1)
            if abs(delta1) in delta_age1:
                if qq_age in delta_age1[abs(delta1)]:
                    delta_age1[abs(delta1)][qq_age] += 1
                else:
                    delta_age1[abs(delta1)][qq_age] = 1
            else:
                delta_age1[abs(delta1)] = {}
                delta_age1[abs(delta1)][qq_age] = 1
            delta3 = pre_age3 - qq_age
            if abs(delta3) in delta_cnt3:
                delta_cnt3[abs(delta3)] += 1
            else:
                delta_cnt3.setdefault(abs(delta3),1)
            if abs(delta3) in delta_age3:
                if qq_age in delta_age3[abs(delta3)]:
                    delta_age3[abs(delta3)][qq_age] += 1
                else:
                    delta_age3[abs(delta3)][qq_age] = 1
            else:
                delta_age3[abs(delta3)] = {}
                delta_age3[abs(delta3)][qq_age] = 1
            delta5 = pre_age5 - qq_age
            if abs(delta5) in delta_cnt5:
                delta_cnt5[abs(delta5)] += 1
            else:
                delta_cnt5.setdefault(abs(delta5),1)
            if abs(delta5) in delta_age5:
                if qq_age in delta_age5[abs(delta5)]:
                    delta_age5[abs(delta5)][qq_age] += 1
                else:
                    delta_age5[abs(delta5)][qq_age] = 1
            else:
                delta_age5[abs(delta5)] = {}
                delta_age5[abs(delta5)][qq_age] = 1
            delta2 = pre_age2 - qq_age
            if abs(delta2) in delta_cnt7:
                delta_cnt7[abs(delta2)] += 1
            else:
                delta_cnt7.setdefault(abs(delta2),1)
            if abs(delta2) in delta_age7:
                if qq_age in delta_age7[abs(delta2)]:
                    delta_age7[abs(delta2)][qq_age] += 1
                else:
                    delta_age7[abs(delta2)][qq_age] = 1
            else:
                delta_age7[abs(delta2)] = {}
                delta_age7[abs(delta2)][qq_age] = 1
            delta4 = pre_age4 - qq_age
            if abs(delta4) in delta_cnt8:
                delta_cnt8[abs(delta4)] += 1
            else:
                delta_cnt8.setdefault(abs(delta4),1)
            if abs(delta4) in delta_age8:
                if qq_age in delta_age8[abs(delta4)]:
                    delta_age8[abs(delta4)][qq_age] += 1
                else:
                    delta_age8[abs(delta4)][qq_age] = 1
            else:
                delta_age8[abs(delta4)] = {}
                delta_age8[abs(delta4)][qq_age] = 1
            delta6 = pre_age6 - qq_age
            if abs(delta6) in delta_cnt9:
                delta_cnt9[abs(delta6)] += 1
            else:
                delta_cnt9.setdefault(abs(delta6),1)
            if abs(delta6) in delta_age9:
                if qq_age in delta_age9[abs(delta6)]:
                    delta_age9[abs(delta6)][qq_age] += 1
                else:
                    delta_age9[abs(delta6)][qq_age] = 1
            else:
                delta_age9[abs(delta6)] = {}
                delta_age9[abs(delta6)][qq_age] = 1
    fr.close()
print >> result, "the number of qq is %d:" %count_all
print >> result, "the number of qq that have camput qq group is: %d" %count_campus
for i in xrange(1,101):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    for key in delta_cnt1:
        if key < i:
            count1 = count1 + delta_cnt1[key]
    period_cnt1[i] = 1.0 * count1/count_campus
    for key in delta_cnt2:
        if key < i:
            count2 = count2 + delta_cnt2[key]
    period_cnt2[i] = 1.0 * count2/count_all
    for key in delta_cnt3:
        if key < i:
            count3 = count3 + delta_cnt3[key]
    period_cnt3[i] = 1.0 * count3/count_campus
    for key in delta_cnt4:
        if key < i:
            count4 = count4 + delta_cnt4[key]
    period_cnt4[i] = 1.0 * count4/count_all
    for key in delta_cnt5:
        if key < i:
            count5 = count5 + delta_cnt5[key]
    period_cnt5[i] = 1.0 * count5/count_campus
    for key in delta_cnt6:
        if key < i:
            count6 = count6 + delta_cnt6[key]
    period_cnt6[i] = 1.0 * count6/count_all
    for key in delta_cnt7:
        if key < i:
            count7 = count7 + delta_cnt7[key]
    period_cnt7[i] = 1.0 * count7/count_campus
    for key in delta_cnt8:
        if key < i:
            count8 = count8 + delta_cnt8[key]
    period_cnt8[i] = 1.0 * count8/count_campus
    for key in delta_cnt9:
        if key < i:
            count9 = count9 + delta_cnt9[key]
    period_cnt9[i] = 1.0 * count9/count_campus
print >> result,"the first group data are blue, and it's result data are:"
print >> result,period_cnt1
print >> result,"the second group data are green, and it's result data are:"
print >> result,period_cnt2
print >> result,"the third group data are black, and it's result data are:"
print >> result,period_cnt3
print >> result,"the forth group data are red, and it's result data are:"
print >> result,period_cnt4
print >> result,"the fifth group data are cyan, and it's result data are:"
print >> result,period_cnt5
print >> result,"the sixth group data are yellow, and it's result data are:"
print >> result,period_cnt6
print >> result,"the seventh group data are yellow, and it's result data are:"
print >> result,period_cnt7
print >> result,"the eighth group data are yellow, and it's result data are:"
print >> result,period_cnt8
print >> result,"the ninth group data are yellow, and it's result data are:"
print >> result,period_cnt9
result.close()
dis_list = [delta_age1, delta_age2, delta_age3, delta_age4, delta_age5, delta_age6, delta_age7, delta_age8, delta_age9]
for i in range(0,9):
    for key in dis_list[i]:
        d = dis_list[i][key]
        dis_list[i][key] = sorted(d.items(), key=lambda d:d[1], reverse=True)

for i in range(1,10):
    print >> distribution, "the age distribution according to delta age of group %d is :" %i
    for key in dis_list[i-1]:
        print >> distribution, "key: %d, distribution: %s" %(key, dis_list[i-1][key])
# print >> distribution, "the age distribution according to delta age of group 1 is:"
# print >> distribution, delta_age1
# print >> distribution, "the age distribution according to delta age of group 2 is:"
# print >> distribution, delta_age2
# print >> distribution, "the age distribution according to delta age of group 3 is:"
# print >> distribution, delta_age3
# print >> distribution, "the age distribution according to delta age of group 4 is:"
# print >> distribution, delta_age4
# print >> distribution, "the age distribution according to delta age of group 5 is:"
# print >> distribution, delta_age5
# print >> distribution, "the age distribution according to delta age of group 6 is:"
# print >> distribution, delta_age6
# print >> distribution, "the age distribution according to delta age of group 7 is:"
# print >> distribution, delta_age7
# print >> distribution, "the age distribution according to delta age of group 8 is:"
# print >> distribution, delta_age8
# print >> distribution, "the age distribution according to delta age of group 9 is:"
# print >> distribution, delta_age9
distribution.close()
#in the graph, the color from 1 to 6 is
#blue, green, black, red, cyan, yellow
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt1.keys(),period_cnt1.values(),"b")
plt.savefig(result_dir + "all1.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt2.keys(),period_cnt2.values(),"g")
plt.savefig(result_dir + "all2.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt3.keys(),period_cnt3.values(),"k")
plt.savefig(result_dir + "all3.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt4.keys(),period_cnt4.values(),"r")
plt.savefig(result_dir + "campus_left1.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt5.keys(),period_cnt5.values(),"c")
plt.savefig(result_dir + "campus_left2.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt6.keys(),period_cnt6.values(),"y")
plt.savefig(result_dir + "campus_left3.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt7.keys(),period_cnt7.values(),"y")
plt.savefig(result_dir + "campus_right1.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt8.keys(),period_cnt8.values(),"y")
plt.savefig(result_dir + "campus_right2.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt9.keys(),period_cnt9.values(),"y")
plt.savefig(result_dir + "campus_right3.png")
plt.close()
# plt.title("the age error distribution")
# plt.xlabel("error level(Years)")
# plt.ylabel("Cumulative Score(CS)")
# plt.show()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt1.keys(),period_cnt1.values(),"b")
plt.plot(period_cnt2.keys(),period_cnt2.values(),"g")
plt.plot(period_cnt3.keys(),period_cnt3.values(),"k")
plt.savefig(result_dir + "all_all.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt4.keys(),period_cnt4.values(),"b")
plt.plot(period_cnt5.keys(),period_cnt5.values(),"g")
plt.plot(period_cnt6.keys(),period_cnt6.values(),"k")
plt.savefig(result_dir + "all_campus_left.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt4.keys(),period_cnt4.values(),"b")
plt.plot(period_cnt7.keys(),period_cnt7.values(),"g")
plt.savefig(result_dir + "all_campus_one.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt5.keys(),period_cnt5.values(),"b")
plt.plot(period_cnt8.keys(),period_cnt8.values(),"g")
plt.savefig(result_dir + "all_campus_two.png")
plt.close()
plt.figure(figsize=(15,7.5))
plt.plot(period_cnt6.keys(),period_cnt6.values(),"b")
plt.plot(period_cnt9.keys(),period_cnt9.values(),"g")
plt.savefig(result_dir + "all_campus_three.png")
plt.close()