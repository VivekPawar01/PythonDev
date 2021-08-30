class Student:
    def __init__(self,name,age,id,marks):
        self.name=name
        self.age=age
        self.id=id
        self.marks=marks
    def show(self):
        print(f'Name={(self.name)}',end=' & ')
        print(f'Age={(self.age)}',end=' & ')
        print(f'ID={(self.id)}',end=' & ')
        print(f'Marks={(self.marks)}')


s1=Student('vivek',29,101,79)
s1.show()
s2=Student('Ashish',29,102,89)
s2.show()
s3=Student('Rahul',26,103,73)
s3.show()



