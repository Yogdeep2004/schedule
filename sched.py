file=open("daily.txt",'a')
date=input("Enter the date : ")
file.write(f"Date : {date}\n")
sub=["TOC","CAO","web_pro","web_pro_lab","daa","daa_lab","mpmc","mpmc_lab","prob","prob_lab","german"]

n=11
for i in range(n):
    mes = input(f"Enter for sub{i} : ")
    file.write(f"{sub[i]} : {mes}\n")
file.write("\n")