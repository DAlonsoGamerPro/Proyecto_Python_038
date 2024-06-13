from tkinter import *
import requests
import json
root = Tk()
root.title("Noticias_BBC")
root.geometry("670x550")
root.config(bg="gray12")

newsupdate = Label(root,text="Actualización de las Noticias de B.B.C.", font=("Helvetica", 17, "bold"), background="gray12", fg="white")
newsupdate.place(relx=0.5,rely=0.1,anchor=CENTER)

news1 = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="red", wraplength=500,justify=LEFT)
news1.place(relx=0.2,rely=0.17,anchor=W)

news1_content = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="white", wraplength=500,justify=LEFT)
news1_content.place(relx=0.2,rely=0.24,anchor=W)

news2 = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="red", wraplength=500,justify=LEFT)
news2.place(relx=0.2,rely=0.32,anchor=W)

news2_content = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="white", wraplength=500,justify=LEFT)
news2_content.place(relx=0.2,rely=0.41,anchor=W)

news3 = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="red", wraplength=500,justify=LEFT)
news3.place(relx=0.2,rely=0.5,anchor=W)

news3_content = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="white", wraplength=500,justify=LEFT)
news3_content.place(relx=0.2,rely=0.59,anchor=W)

news4 = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="red", wraplength=500,justify=LEFT)
news4.place(relx=0.2,rely=0.68,anchor=W)

news4_content = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="white", wraplength=500,justify=LEFT)
news4_content.place(relx=0.2,rely=0.77,anchor=W)

news5 = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="red", wraplength=500,justify=LEFT)
news5.place(relx=0.2,rely=0.85,anchor=W)

news5_content = Label(root, font=("Helvetica", 12, "bold"), background="gray12", fg="white", wraplength=500,justify=LEFT)
news5_content.place(relx=0.2,rely=0.94,anchor=W)

api_requests = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d19e527b11df48c0bcc07c26dfe0a65e")
open_bbc_page = json.loads(api_requests.content)

title1 = open_bbc_page["articles"][0]["title"]
print(title1)

desc1 = open_bbc_page["articles"][0]["description"]
print(desc1)

title2 = open_bbc_page["articles"][1]["title"]
print(title2)

desc2 = open_bbc_page["articles"][1]["description"]
print(desc2)

title3 = open_bbc_page["articles"][2]["title"]
print(title3)

desc3 = open_bbc_page["articles"][2]["description"]
print(desc3)

title4 = open_bbc_page["articles"][3]["title"]
print(title4)

desc4 = open_bbc_page["articles"][3]["description"]
print(desc4)

title5 = open_bbc_page["articles"][4]["title"]
print(title5)

desc5 = open_bbc_page["articles"][4]["description"]
print(desc5)

news1["text"] = "Título 1: " + title1
news1_content["text"] = "Descripción: " + desc1

news2["text"] = "Título 2: " + title2
news2_content["text"] = "Descripción: " + desc2

news3["text"] = "Título 3: " + title3
news3_content["text"] = "Descripción: " + desc3

news4["text"] = "Título 4: " + title4
news4_content["text"] = "Descripción: " + desc4

news5["text"] = "Título 5: " + title5
news5_content["text"] = "Descripción: " + desc5



root.mainloop()