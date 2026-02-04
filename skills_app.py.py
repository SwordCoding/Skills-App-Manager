import sqlite3

# Create Data bse and connection


Db = sqlite3.connect ("app.db")

# Settingup the cursor
cr = Db.cursor ()
cr.execute ("Create Table if not exists Skills (skill_name Text, progress Integer , User_Id Integer)" )


# Set user id for every user
Uid = input ("Please Enter Your User ID ")

def Add_Repeted_UserID () :
        cr.execute ( f"select * from Skills where User_Id = {Uid}")
        Result_Of_Add_Repeted_UserID = cr.fetchone () 

        if Result_Of_Add_Repeted_UserID == None :
                print ( f"Welcome New User {Uid} You can start adding skills. " )
                
        else :
                print ( f"Welcome Back User {Uid}. ")
                
Add_Repeted_UserID() # استدعيت الفانكشن اللي عملتها عشان تشتغل

# save every change you made by
#Db.commit ()

# close data base 
#Db.close ()

# commit and close method مع بعض بقى
# بدل ما اكتبهم كل شويه عملت فانكشن وحطيهم فيها 
# ومعاهم يدي رساله نجاح
# لكن خليك عارف المشكله هنا انه هيقفل البرنامح علطول بعد ما يخلص
def Commit_and_Close_Method () :
        Db.commit()
        Db.close ()
        # Connection of Commit And Close Has been Done 
        print ("Database is Closed ")

# فالو عايزين نكمل ونحفظ اللي 
# حصل بدون مانقفل البرنامج هنعمل
# ودا وظيفه الفانكشن دا commit () فقط 
def Only_Commit_Method () :
        Db.commit ()



Input_message = """
What Do You Want ?
"A" : Add A New Skills
"S" : Show All Of Your Skills
"U" : Update Your Skills 
"D" : Delete One Of Your Skills
"Q" : Quit The App
Choose an Option : 
"""

Command_List = ["A" , "S" , "U" , "D" , "Q"] # ليست يظهر فيها الاختيارات اللي قصاد المستخدم

def Add_A_New_Skills() :
        Skill_Name = input ("Enter Your New Skill Name ").strip().capitalize()
        cr.execute ( f"select skill_name from Skills where skill_name = '{Skill_Name}' and User_Id = {Uid} ")
        
        # متتكررش لنفس المستخدم Skill هبدا افلتر عشان الـ
        Result_Of_New_Skill_Name = cr.fetchone() # None انها هتديني القيه لو موجوده ولو لا تديك Fetchone() سبب استعمالي 
        
        if Result_Of_New_Skill_Name == None :
                print ( f"Skill {Skill_Name} Is Not Exist So You Can Add It. ")
        else :
                print ( f"Skill {Skill_Name} Is Already Exist So You Can't Add it. ")
                return
                """
                هنا if,else شرح اللي عملته 
                result كانه بيقول لو نتيجة البحث 
                يعني ملقيناش اللي بندور عليه  None طلعت فاضية 
                اطبع ان هو مش موجود 
                fetchone () والمستخدم يقدر يضيفه ودا سبب استعماله لـ
                عشان لما يكون فاضي ومفهوش اللي بيدور عليه بيدي 
                None
                fetchone () طب لو  لقينا والنتيجه بتاعة
                None مش 
                اطبع لا مش هتقدر تضيف حاجه
                """
        Skill_Progress = int( input ("Enter Your Skill Progress ") )
        
        cr.execute (
                f"Insert Into Skills (skill_name , progress , User_Id) Values ( '{Skill_Name}' , {Skill_Progress} , {Uid} ) ")
        print ( f"Your Skill {Skill_Name} Is Successfully Added")
        Only_Commit_Method ()
"""
عملت فانكشن لاضافه المهارات
للاسم و للكفاءه input فا جواها فيه كذا 
وبعدها النقطه اللي ربطت بين االـ 
database 
والكود بتاعي و الفانكشن دي بذات
Skills وبعدها عملت فحص للـ
عشان لو موجوده ميطبعهاش 


"""

def Show_All_Of_Your_Skills () :
        cr.execute (f"select * from Skills where User_Id = {Uid}")
        Result_Of_Selected_Data = cr.fetchall ()
        print ( f"You Have { len( Result_Of_Selected_Data ) } Skills. ")
        for Row in Result_Of_Selected_Data :
                print ( f"Progress is {Row [1] }% And Your Id Is {Row [2] } " )
        Only_Commit_Method ()

"""
databaseقولت لبايثون حدد ليا من الـ 
كل دا idالمهارات وخوصوصا اللي ليهم الـ 
المستخدم بيدخله idو الـ
فا المعم بعدها عملت متغير وقولت
لبايثون يجيب ليا كل اللي اتحدد 
fechall()  من الداتا بيز دا باستعمال 
و بعدها عملت لوب على المتغير اللي فيه كل اللي اتحدد دا
"""

def Update_Your_Skills () :
        Update_Your_Skill_Name_input = input ("Enter Your Skill Name ") .strip().capitalize()
        Uid_input_update = input ("To Make Sure You are Real User Plese Enter your ID ")
        if Uid_input_update != Uid :
                print ("You Write an Wrong User ID ")
                return
        Update_Your_Skills_Progress_input = int ( input ("Write Your Skill Progress ") )
        cr.execute ( f"update Skills set progress = {Update_Your_Skills_Progress_input} where Skill_name = '{Update_Your_Skill_Name_input}' and User_Id = {Uid_input_update}")
        print ("Your New Progress Is Successfully Updated")
        
        Only_Commit_Method ()

def Delete_One_Of_Your_Skills () :
        Delete_Skill = input ("Enter Skill Name You Want To Delete ")
        Uid_input = input ("To Make Sure You are Real User Plese Enter your ID ")
        cr.execute ( f"delete from Skills where skill_name = '{Delete_Skill}' and User_Id = {Uid_input}  ")
        print ( f"Your {Delete_Skill} Has Been Deleted")
        Only_Commit_Method ()

"""
input عملت فانكشن تمسح المهارات و حطيت فيها متغير بـ
id ومكان اليوزر يدخل فيه الـ
عشان اضمن ان دا المستخدم الحقيقي
databaseوبعدها ربط دا كله والفانكشن بـ
وطبعت رساله وبس
"""

def Quit_The_App () :
        if User_input == "Q" :
                print ("App Is Cloosed ... Goodbye ")
        Commit_and_Close_Method
        

# Check if Command is Exist or not
#if User_input in Command_List :
        #print (f"Commmand is Found in {User_input}")

        """
و  ب الـ فانكشن ( الميثود ) اللي عملتهم user input هنا بدات اربط بين الـ
elif صغيره ووجواها if الكبيره كام if وحطيت جوا الـ 

"""
#        if User_input == "A" :
#                Add_A_New_Skills ()
#        
#        elif User_input == "S" :
#                Show_All_Of_Your_Skills()
#        
#        elif User_input == "U" :
#                Update_Your_Skills ()
#        
#        elif User_input == "D" :
#                Delete_One_Of_Your_Skills ()
#        
#        else :
#                print ("App Is Closed. ")
#else:
#        raise KeyError (f"{User_input} Is Wrong, Please Choose From Option")

"""
loop  دي من غير if condition طب ما الـ
هتخلي الـبرنامج بعد كل عمليه يقفل ومش هيكمل
طب الحل ؟ 
While Loop 
if conditon وحط جواها الـ
وبس سهله
"""

while True:
        User_input = input(Input_message).strip().capitalize()

        if User_input in Command_List:
                if User_input == "A":
                        Add_A_New_Skills()
        
                elif User_input == "S":
                        Show_All_Of_Your_Skills()
        
                elif User_input == "U":
                        Update_Your_Skills()
        
                elif User_input == "D":
                        Delete_One_Of_Your_Skills()
        
                elif User_input == "Q":
                        print("App Is Closed.")
                        Commit_and_Close_Method() # هنا بنقفل الاتصال ونخرج
                        break

else:   
                raise KeyError (f"{User_input} Is Wrong, Please Choose From Option")