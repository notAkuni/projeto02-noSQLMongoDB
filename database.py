from pymongo.mongo_client import MongoClient
from urllib.parse import quote_plus
from bson.objectid import ObjectId


username = quote_plus('gabrielschanz')
password = quote_plus('g14092000')

uri = "mongodb+srv://" + username + ":" + password + "@cluster0.dchip16.mongodb.net/?retryWrites=true&w=majority"

#CONEXÃO COM O BANCO DE DADOS
client = MongoClient(uri)
mydb = client["Projeto"]
colStudent = mydb["student"]
colInstructor = mydb["instructor"]
colSection = mydb["section"]
colTeaches = mydb["teaches"]
colDepartment = mydb["department"]


##PREPARAÇÃO DO BANCO DE DADOS
list_insert_student = [
    {'ID':'00128', 'name':'Zhang', 'dept_name':'Comp. Sci.', 'tot_cred':'102'},
    {'ID':'12345', 'name':'Shankar', 'dept_name':'Comp. Sci.', 'tot_cred':'32'},
    {'ID':'19991', 'name':'Brandt', 'dept_name':'History', 'tot_cred':'80'},
    {'ID':'23121', 'name':'Chavez', 'dept_name':'Finance', 'tot_cred':'110'},
    {'ID':'44553', 'name':'Peltier', 'dept_name':'Physics', 'tot_cred':'56'},
    {'ID':'45678', 'name':'Levy', 'dept_name':'Physics', 'tot_cred':'46'},
    {'ID':'54321', 'name':'Williams', 'dept_name':'Comp. Sci.', 'tot_cred':'54'},
    {'ID':'55739', 'name':'Sanchez', 'dept_name':'Music', 'tot_cred':'38'},
    {'ID':'70557', 'name':'Snow', 'dept_name':'Physics', 'tot_cred':'0'},
    {'ID':'76543', 'name':'Brown', 'dept_name':'Comp. Sci.', 'tot_cred':'58'},
    {'ID':'76653', 'name':'Aoi', 'dept_name':'Elec. Eng.', 'tot_cred':'60'},
    {'ID':'98765', 'name':'Bourikas', 'dept_name':'Elec. Eng.', 'tot_cred':'98'},
    {'ID':'98988', 'name':'Tanaka', 'dept_name':'Biology', 'tot_cred':'120'}
]

list_insert_instructor = [
    {'ID':'10101', 'name':'Srinivasan', 'dept_name':'Comp. Sci.', 'salary':'65000'},
    {'ID':'12121', 'name':'Wu', 'dept_name':'Finance', 'salary':'90000'},
    {'ID':'15151', 'name':'Mozart', 'dept_name':'Music', 'salary':'40000'},
    {'ID':'22222', 'name':'Einstein', 'dept_name':'Physics', 'salary':'95000'},
    {'ID':'32343', 'name':'El Said', 'dept_name':'History', 'salary':'60000'},
    {'ID':'33456', 'name':'Gold', 'dept_name':'Physics', 'salary':'87000'},
    {'ID':'45565', 'name':'Katz', 'dept_name':'Comp. Sci.', 'salary':'75000'},
    {'ID':'58583', 'name':'Califieri', 'dept_name':'History', 'salary':'62000'},
    {'ID':'76543', 'name':'Singh', 'dept_name':'Finance', 'salary':'80000'},
    {'ID':'76766', 'name':'Crick', 'dept_name':'Biology', 'salary':'72000'},
    {'ID':'83821', 'name':'Brandt', 'dept_name':'Comp. Sci.', 'salary':'92000'},
    {'ID':'98345', 'name':'Kim', 'dept_name':'Elec. Eng.', 'salary':'80000'}
]

list_insert_section = [
    {'course_id':'BIO-101', 'sec_id':'1', 'semester':'Summer', 'year':'2017', 'building':'Painter', 'room_number':'514', 'time_slot_id':'B'},
    {'course_id':'BIO-301', 'sec_id':'1', 'semester':'Summer', 'year':'2018', 'building':'Painter', 'room_number':'514', 'time_slot_id':'A'},
    {'course_id':'CS-101', 'sec_id':'1', 'semester':'Fall', 'year':'2017', 'building':'Packard', 'room_number':'101', 'time_slot_id':'H'},
    {'course_id':'CS-101', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Packard', 'room_number':'101', 'time_slot_id':'F'},
    {'course_id':'CS-190', 'sec_id':'1', 'semester':'Spring', 'year':'2017', 'building':'Taylor', 'room_number':'3128', 'time_slot_id':'E'},
    {'course_id':'CS-190', 'sec_id':'2', 'semester':'Spring', 'year':'2017', 'building':'Taylor', 'room_number':'3128', 'time_slot_id':'A'},
    {'course_id':'CS-315', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Watson', 'room_number':'120', 'time_slot_id':'D'},
    {'course_id':'CS-319', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Watson', 'room_number':'100', 'time_slot_id':'B'},
    {'course_id':'CS-319', 'sec_id':'2', 'semester':'Spring', 'year':'2018', 'building':'Taylor', 'room_number':'3128', 'time_slot_id':'C'},
    {'course_id':'CS-347', 'sec_id':'1', 'semester':'Fall', 'year':'2017', 'building':'Taylor', 'room_number':'3128', 'time_slot_id':'A'},
    {'course_id':'EE-181', 'sec_id':'1', 'semester':'Spring', 'year':'2017', 'building':'Taylor', 'room_number':'3128', 'time_slot_id':'C'},
    {'course_id':'FIN-201', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Packard', 'room_number':'101', 'time_slot_id':'B'},
    {'course_id':'HIS-351', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Painter', 'room_number':'514', 'time_slot_id':'C'},
    {'course_id':'MU-199', 'sec_id':'1', 'semester':'Spring', 'year':'2018', 'building':'Packard', 'room_number':'101', 'time_slot_id':'D'},
    {'course_id':'PHY-101', 'sec_id':'1', 'semester':'Fall', 'year':'2017', 'building':'Watson', 'room_number':'100', 'time_slot_id':'A'},
]

list_insert_teaches = [
    {'ID':'10101', 'course_id':'CS-101', 'sec_id':'1', 'semester':'Fall', 'year':'2017'},
    {'ID':'10101', 'course_id':'CS-315', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'10101', 'course_id':'CS-347', 'sec_id':'1', 'semester':'Fall', 'year':'2017'},
    {'ID':'12121', 'course_id':'FIN-201', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'15151', 'course_id':'MU-199', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'22222', 'course_id':'PHY-101', 'sec_id':'1', 'semester':'Fall', 'year':'2017'},
    {'ID':'32343', 'course_id':'HIS-351', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'45565', 'course_id':'CS-101', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'45565', 'course_id':'CS-319', 'sec_id':'1', 'semester':'Spring', 'year':'2018'},
    {'ID':'76766', 'course_id':'BIO-101', 'sec_id':'1', 'semester':'Summer', 'year':'2017'},
    {'ID':'76766', 'course_id':'BIO-301', 'sec_id':'1', 'semester':'Summer', 'year':'2018'},
    {'ID':'83821', 'course_id':'CS-190', 'sec_id':'1', 'semester':'Spring', 'year':'2017'},
    {'ID':'83821', 'course_id':'CS-190', 'sec_id':'2', 'semester':'Spring', 'year':'2017'},
    {'ID':'83821', 'course_id':'CS-319', 'sec_id':'2', 'semester':'Spring', 'year':'2018'},
    {'ID':'98345', 'course_id':'EE-181', 'sec_id':'1', 'semester':'Spring', 'year':'2017'}
]

list_insert_department = [
    {'dept_name':'Biology', 'building':'Watson', 'budget':'90000'},
    {'dept_name':'Comp. Sci.', 'building':'Taylor', 'budget':'100000'},
    {'dept_name':'Elec. Eng.', 'building':'Taylor', 'budget':'85000'},
    {'dept_name':'Finance', 'building':'Painter', 'budget':'120000'},
    {'dept_name':'History', 'building':'Painter', 'budget':'50000'},
    {'dept_name':'Music', 'building':'Packard', 'budget':'80000'},
    {'dept_name':'Physics', 'building':'Watson', 'budget':'70000'}
]

dict_advisor = {
    '00128': '45565',
    '12345': '10101',
    '23121': '76543',
    '44553': '22222',
    '45678': '22222',
    '76543': '45565',
    '76653': '98345',
    '98765': '98345',
    '98988': '76766'
}

##INSERÇÃO DOS DADOS
'''
insereStudent = colStudent.insert_many(list_insert_student)
insereInstructor = colInstructor.insert_many(list_insert_instructor)
insereSection = colSection.insert_many(list_insert_section)
insereTeaches = colTeaches.insert_many(list_insert_teaches)
insereDepartment = colDepartment.insert_many(list_insert_department)
'''

##PREENCHER O CAMPO ADVISOR DO ALUNO
for x in range(len(list(dict_advisor.keys()))):
    query_student = { "ID": { "$eq": list(dict_advisor.keys())[x] } }
    instructor = colInstructor.find_one({ "ID": list(dict_advisor.values())[x] })
    newvalues = { "$set": { "advisor": ObjectId(instructor.get('_id')) } }
    colStudent.update_one(query_student, newvalues)
    
##PREENCHER O CAMPO TEACHES DA SECTION
for teach in colTeaches.find():
    myquery_section = { "course_id": { "$eq": teach.get('course_id') }, "sec_id": teach.get('sec_id') }     
    instructor = colInstructor.find_one({ "ID": teach.get('ID') })
    if instructor:
        section = colSection.find_one(myquery_section)
        if section and 'instructor' not in section:
            newvalues = { "$set": { "instructor": ObjectId(instructor.get('_id')) } }    
            colSection.update_many(myquery_section, newvalues)

## CONSULTA 1
def consulta1():
    print("------------------ CONSULTA 1 ------------------")
    for x in colStudent.find():
        instructor = colInstructor.find({ "_id": x.get('advisor') })
        for person in instructor:
            print("Aluno:", x.get('name'), "| Departamento:", x.get('dept_name'), "| Professor:", person.get('name'))
    print("-----------------------------------------------")
  
## CONSULTA 2
def consulta2():
    print("------------------ CONSULTA 2 ------------------")
    seen = set()
    for section in colSection.find():
        instructor = colInstructor.find_one({ "_id": section.get('instructor') }) 
        if instructor:
            result = (instructor.get('name'), section.get('building'), section.get('room_number'))
            if result not in seen:
                print("Professor:", result[0], "| Predio:", result[1], "| Sala:", result[2])
                seen.add(result)
    print("-----------------------------------------------")

## CONSULTA 3
def consulta3():
    print("------------------ CONSULTA 3 ------------------")
    for department in colDepartment.find():
        dept_name = department.get("dept_name")
        budget = department.get("budget")
        student_count = colStudent.count_documents({"dept_name": dept_name})
        instructor_count = colInstructor.count_documents({"dept_name": dept_name})
        
        total_salary = 0        
        for instructor in colInstructor.find({"dept_name": dept_name}):
            total_salary += int(instructor.get("salary"))            
    
        avg_salary = total_salary / instructor_count
        
        print("Departamento:", dept_name, "| Orcamento: ", budget, "| Qtde Alunos:", student_count, "| Media Salario:", avg_salary)
    print("-----------------------------------------------")

consulta1()
consulta2()
consulta3()