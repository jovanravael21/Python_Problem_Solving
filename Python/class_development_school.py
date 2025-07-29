class School():
    def __init__(self,name,level,number_of_students, number_of_teachers):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students
        self.number_of_teachers = number_of_teachers

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.number_of_students

    def get_number_of_teachers(self):
        return self.number_of_teachers

    def set_number_of_students(self,new_number_of_students):
        self.number_of_students = new_number_of_students

    def set_number_of_teachers(self,new_number_of_teachers):
        self.number_of_teachers = new_number_of_teachers

    def quick_facts(self):
        print(f'''
            School Name         : {self.get_name()}
            Level               : {self.get_level()} School
            Number of Students  : {self.get_number_of_students()}
            Number of Teachers  : {self.get_number_of_teachers()}
''')

class PrimarySchool(School):
    def __init__(self,name, level, number_of_students, number_of_teachers, pickup_policy=[]):
        super().__init__(name,level,number_of_students,number_of_teachers)
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy
    
    def set_pickup_policy(self,new_policy):
        self.pickup_policy.append(new_policy)

class MiddleSchool (School):
    def __init__(self,name, level, number_of_students, number_of_teachers):
        super().__init__(name,level,number_of_students,number_of_teachers)

class HighSchool (School):
    def __init__(self,name, level, number_of_students, number_of_teachers, sports_teams=[]):
        super().__init__(name,level,number_of_students,number_of_teachers)
        self.sports_teams = sports_teams

    def get_sport_teams(self):
        return self.sports_teams

    def set_sport_teams(self,new_sports_teams):
        self.sports_teams.append(new_sports_teams)
    

primary_school = PrimarySchool("SDH Bangka","Primary",100,10,["No Fighting","No Bullying"])
middle_school = MiddleSchool("SMP Dian Harapan", "Middle", 300,15)
high_school = HighSchool("UPH College","High",500,25,["Basketball","Football","Badminton"])

primary_school.quick_facts();
middle_school.quick_facts();
high_school.quick_facts();

primary_school.set_pickup_policy("No Disrespect")
high_school.set_sport_teams("Volleyball")

print(f'''
    School Name         : {primary_school.get_name()}
    Level               : {primary_school.get_level()} School
    Number of Students  : {primary_school.get_number_of_students()}
    Number of Teachers  : {primary_school.get_number_of_teachers()}
    Policy              : {primary_school.get_pickup_policy()}
''')

print(f'''
    School Name         : {middle_school.get_name()}
    Level               : {middle_school.get_level()} School
    Number of Students  : {middle_school.get_number_of_students()}
    Number of Teachers  : {middle_school.get_number_of_teachers()}
''')

print(f'''
    School Name         : {high_school.get_name()}
    Level               : {high_school.get_level()} School
    Number of Students  : {high_school.get_number_of_students()}
    Number of Teachers  : {high_school.get_number_of_teachers()}
    Sport Teams         : {high_school.get_sport_teams()}
''')