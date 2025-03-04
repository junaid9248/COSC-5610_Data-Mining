class patientDB:
	def __init__(self):
		self.records = {}
	def add_patient_record(self, patient_data):
            pid= patient_data['Patient_ID']
            if not pid in self.records:
                self.records[pid]={
                    'Gender': patient_data['Gender'],
                    'Race': patient_data['Race'],
                    'Age': patient_data['Age'],
                    'Ethnicity': patient_data['Ethnicity'],
                    'Zip_code': patient_data['Zip_code'],
                    'Visits':[{ 'Visit ID': patient_data['Visit_ID'],
                               'Department':patient_data['Visit_department']}]
                }
            else:
                self.records[patient_data]['Visits'] = self.records[patient_data]['Visits'].append({ 'Visit ID': patient_data['Visit_ID'],
                               'Department':patient_data['Visit_department']})
                
        def display_all_records(self):
            """
            Displays all patient records.
            """
            if self.records:
                for pid, record in self.records.items():
                    print(f"Patient ID: {pid}")
                    print(f"Name: Not Available (Add name feature in future updates)")
                    print(f"Gender: {record['Gender']}")
                    print(f"Race: {record['Race']}")
                    print(f"Age: {record['Age']}")
                    print(f"Ethnicity: {record['Ethnicity']}")
                    print(f"Zip Code: {record['Zip_code']}")
                    print("Visits:")
                    for visit in record['visits']:
                        print(f"  - Visit ID: {visit.get('Visit_ID')}")
                        print(f"    Visit Department: {visit.get('Visit_department')}")
                        print(f"    Insurance: {visit.get('Insurance')}")
                    print("\n")
            else:
                print("No records available.")
        
def main():
        
    patient_data1 = {
        'Patient_ID': 'P001',
        'Visit_department': 'Cardiology',
        'Visit_ID': '',
        'Gender': 'Male',
        'Race': 'White',
        'Age': 30,
        'Ethnicity': 'Non-Hispanic',
        'Zip_code': '12345'
    }
    
    patientDB.add_patient_record(patient_data1)
    
    patientDB.display_all_records()