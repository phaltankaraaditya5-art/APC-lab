class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, disease):
        super().__init__(name)
        self.disease = disease


class Surgeon(Doctor):
    def __init__(self, name, specialization, surgeries_done):
        super().__init__(name, specialization)
        self.surgeries_done = surgeries_done

    def display(self):
        print("Surgeon:", self.name, "Specialization:", self.specialization, "Surgeries:", self.surgeries_done)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, specialization, disease, research_area):
        Doctor.__init__(self, name, specialization)
        Patient.__init__(self, name, disease)
        self.research_area = research_area

    def display(self):
        print("Researcher:", self.name, "Area:", self.research_area)


s = Surgeon("Dr. Sharma", "Cardiology", 500)
mr = MedicalResearcher("Dr. Rehan", "Neurology", "Migraine", "Brain Studies")

s.display()
mr.display()