import json
from bs4 import BeautifulSoup

with open("tempest") as fp:
    soup = BeautifulSoup(fp, "html.parser")
pass_test_cases = soup.find_all('tr', class_ = "passClass")
fail_test_cases = soup.find_all('tr', class_ = "failClass")
Pass_test_cases_names = []
Fail_test_cases_names = []
Fail = []
Pass =[]

def get_test_name():
    print("pass_test_cases")
    
    for i in pass_test_cases:
        td_pass_test_name = i.find_all('td', class_ = "testname")
        for k in td_pass_test_name:
            Pass_test_cases_names.append(k.text)
        x = json.dumps(Pass_test_cases_names)
    print(x)
    print("\nfail_test_cases\n")
    
    for j in fail_test_cases:
        td_fail_test_name = j.find_all('td', class_ = "testname")
        for k in td_fail_test_name:
            Fail_test_cases_names.append(k.text)
        y = json.dumps(Fail_test_cases_names)
    print(y)

def get_status_fail():
    for j in fail_test_cases:
        Fail.append("Fail")
    z = json.dumps(Fail)
    print(z)

def get_status_pass():
    for i in pass_test_cases:
        Pass.append("Pass")
    result = json.dumps(Pass)
    print(result)

get_test_name()
get_status_fail()
get_status_pass()
 #   k = 0
  #  while k < len(report): 
   #     Count.append(report[k].text)
    #    print(Count)
     #   k+=1
    
#print("Fail test cases")
#for j in fail_class:
 #   td_fail_test_name = j.find_all('td', class_ = "testname")
  #  for k in td_fail_test_name:
   #     print(k.text)

