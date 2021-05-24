import requests
import json

course=[]
id_list=[]
slug_list=[]

def api_first():
    x = requests.get('http://saral.navgurukul.org/api/courses')
    y=(x.text)
    # print(x.text)
    with open("courses.json","w") as f:
        fi=json.loads(y)
        json.dump(fi,f,indent=2)
    list1=(fi["availableCourses"])
    index=0
    while index<len(list1):
        course_available=list1[index]["name"]
        course.append(course_available)
        id_avaible=list1[index]["id"]
        id_list.append(id_avaible)
        print(index,course_available,id_avaible)
        index+=1
    # global user
    user=int(input("Enter id:- "))
    global w
    t=list1[user]
    w=t["id"]
    print("****","Cource Name : ",t["name"],"****")
    print()
api_first()

def api_second():
    s="http://saral.navgurukul.org/api/courses/74/exercises"
    s=s.replace("74",w)
    a=requests.get(s)
    # print(a)
    b=(a.text)

    with open("data2.json","w") as file1:
        file2=json.loads(b)
        json.dump(file2,file1,indent=4)
    value_dataa=file2["data"]
    sub_count=0
    for u in value_dataa:
        sub_count+=1
        sub=0
        print("**",sub_count,":",u["name"],"**")
        slug_data=u["slug"]
        slug_list.append(slug_data)
        if len(u["childExercises"])==0:
            print("       ",u["childExercises"],"       ")
        else:
            # print("childExercise")
            child_dict=u["childExercises"]
            ind=0
            while ind<len(child_dict):
                # print(type(child_dict[ind]))
                for  kill in child_dict[ind]:
                    if kill=="name":
                        sub+=1
                        print("       " ,child_dict[ind][kill],"       ")
                ind+=1
    print(len(slug_list))
    file1.close()
api_second()

def slug_fun():
    user_up_slug=input("enter weather you want to do up or slug: ")
    if user_up_slug=="up":
        api_first()
        api_second()
        slug_fun()
    elif user_up_slug=="slug":
        user_slug=int(input("enter your slug index: "))
        url='http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json'
        url=url.replace('requests__using-json',slug_list[user_slug])
    
        slug_url= requests.get(url)
        print(slug_url.text)
        next_previous=input("enter weather you want 1. up 2. Next 3. Previous 4. exit ")
        leng=len(slug_list)
        # print(slug_url)
        # print(slug_list[user_slug+1])
        if next_previous=="up":
            api_first()
            api_second()
            slug_fun()
        elif next_previous=="next":
            if user_slug==leng-1:
                print("no next slug exists")
            else:
                ind2=slug_list[user_slug+1]
                url=url.replace(slug_list[user_slug],slug_list[user_slug+1])
                slug_url1= requests.get(url)
                print(slug_url1.text)
        elif next_previous=="previous":
            if user_slug==0:
                print("no previous slug exists")
            else:
                ind3=slug_list[user_slug-1]
                url=url.replace(slug_list[user_slug],slug_list[user_slug-1])
                slug_url2= requests.get(url)
                print(slug_url2.text)
        elif next_previous=="exit":
            print("**EXIT**")
slug_fun()

