'''
1)Create a Person class that serves as a base class for both doctors and patients. This class should contain:
*Name
*Age
*Gender
*A method to return formatted personal details.
2)Create a Patient class that inherits from Person and includes:
*Disease information
*A method to return full patient details.
3)Create a Doctor class that iherits from Person and includes:
*Specialization
*A private list to store assigned patients
*Methods to assign a patient, retrieve doctor details and list assigned patients.
4)Implement a "menu-driven interface" that allows the following actions:
1.Add a new doctor
2.Add a new patient
3.Assign a patient to a doctor
4.view all patients assigned to a particular doctor 
5.Search and view details of a specific patient
'''
class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender
        print("Super Class Constructor")
    def PersonDetails(self):
        print(f"Person's Name : {self.Name}")
        print(f"Person's Age : {self.Age}")
        print(f"Person's Gender : {self.Gender}")
class Patient(Person):
    def __init__(self, name, age, gender, disease):
        super().__init__(name, age, gender)
        self.Disease = disease
    def get_Details(self):
        print(f"Person's Name : {self.Name}")
        print(f"Person's Age : {self.Age}")
        print(f"Person's Gender : {self.Gender}")
        print(f"Disease Description : {self.Disease}")
class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.Specialization = specialization
        self.__Patients = []
    def assign_patients(self, patient):
        self.__Patients.append(patient)
    def get_doctor_details(self):
        self.PersonDetails()
        print(f"Specialization: {self.Specialization}")
    def get_assigned_patients(self):
        if not self.__Patients:
            return "No Patients Assigned."
        result = ""
        for p in self.__Patients:
            result += f"- {p.Name} ({p.Disease})\n"
        return result.strip()
doctors = []
patients = []
def find_doctor_by_name(name):
    for doc in doctors:
        if doc.Name.lower() == name.lower():
            return doc
    return None
def find_patient_by_name(name):
    for pat in patients:
        if pat.Name.lower() == name.lower():
            return pat
    return None
def main():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Register Doctor")
        print("2. Register Patient")
        print("3. Assign Patient to Doctor")
        print("4. View Doctor and Assigned Patients")
        print("5. View Patient Details")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            name = input("Doctor Name: ")
            age = int(input("Doctor Age: "))
            gender = input("Doctor Gender: ")
            specialization = input("Specialization: ")
            doc = Doctor(name, age, gender, specialization)
            doctors.append(doc)
            print("Doctor registered successfully.")
        elif choice == '2':
            name = input("Patient Name: ")
            age = int(input("Patient Age: "))
            gender = input("Patient Gender: ")
            disease = input("Disease: ")
            pat = Patient(name, age, gender, disease)
            patients.append(pat)
            print("Patient registered successfully.")
        elif choice == '3':
            patient_name = input("Enter Patient Name: ")
            doctor_name = input("Enter Doctor Name: ")
            pat = find_patient_by_name(patient_name)
            doc = find_doctor_by_name(doctor_name)
            if pat and doc:
                doc.assign_patients(pat)
                print("Patient assigned successfully.")
            else:
                print("Doctor or Patient not found.")
        elif choice == '4':
            doctor_name = input("Enter Doctor Name: ")
            doc = find_doctor_by_name(doctor_name)
            if doc:
                doc.get_doctor_details()
                print("Assigned Patients: ")
                print(doc.get_assigned_patients())
            else:
                print("Doctor not found.")
        elif choice == '5':
            patient_name = input("Enter Patient Name: ")
            pat = find_patient_by_name(patient_name)
            if pat:
                pat.get_Details()
            else:
                print("Patient not found.")
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()