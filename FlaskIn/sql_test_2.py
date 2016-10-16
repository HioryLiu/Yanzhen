class Student:
    name = ''
    age = 0
     
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
 
def convert_to_dict(obj):

    dict = {}
    dict.update(obj.__dict__)
    return dict
       
         
def convert_to_dicts(objs):
    obj_arr = []
     
    for o in objs:
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
     
    return obj_arr
           
 
def class_to_dict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
     
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict
    
stu = Student('zhangsan', 20)
 
print '-----------'
print convert_to_dict(stu)
  
print '-----------'
print convert_to_dicts([stu, stu])
 
print '-----------'
print class_to_dict(stu)
 
print '-----------'
print class_to_dict([stu, stu])
 
stua = Student('zhangsan', 20)
stub = Student('lisi', 10)
 
stu_set = set()
stu_set.add(stua)
stu_set.add(stub)
print class_to_dict(stu_set)