class student:
    school_name = "ABCD Public School"

    @classmethod
    def mod_school_name(cls, name):
        cls.school_name = name
        # ? Notice the use of cls instance variable here instead of self. Since this is 'class method' and not instance method


print(student.school_name)

student.mod_school_name("XYZ Public School")

print(student.school_name)
