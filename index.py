import os
import requests

os.system("title Dowload Files")

def save_from_www(link, path):
    try:
        file_name = link.split('/')[-1]; r = requests.get(link, allow_redirects=True); open(f"{path}/{file_name}", 'wb').write(r.content)
        print(f"Dowload {file_name} | ok")
    except:
        print(f"Dowload {file_name} | crash")


path = input("Путь к учтановки: ")
link = input("Сылка на файл: ")
end = input("Окончание: ")
end2 = input("Что будет вместо окончание: ")

path1 = path.replace('\\','/')
save_from_www(link, path1)


for i in os.listdir(path):
    base = os.path.splitext(i)[0]
    if i.endswith(end):
        os.rename(f"{path1}/{i}", f"{path1}/{base + end2}")

        print(f"{path1}/{i}", f"{path1}/{base + end2}") 
