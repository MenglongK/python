import subprocess
subprocess.run("clear", shell=True)

raw_data = "sTUDENT | 2026 | sOk pANha | 007 | 19 | 3.75"

print("===========Student Report===========")
print("Student ID:", raw_data.split("|")[0].strip().capitalize()+"-"+raw_data.split("|")[1].strip())
print("Name:", raw_data.split("|")[2].strip().title())
print("Age:", raw_data.split("|")[4].strip())
print("GPA:", raw_data.split("|")[5].strip())
print("\n")
print("ID container 2026:", "2026" in raw_data)
print("Next your age:", int(raw_data.split("|")[4].strip())+1)
print("Double GPA:", float(raw_data.split("|")[5].strip())*2)