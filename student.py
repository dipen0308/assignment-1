import csv
from datetime import datetime

ATTENDANCE_FILE = 'attendance.csv'
STUDENT_LIST_FILE = 'students.csv'

def load_students():
    """Loads student names from a CSV file."""
    students = []
    try:
        with open(STUDENT_LIST_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ensure the row is not empty
                    students.append(row[0])
    except FileNotFoundError:
        print(f"'{STUDENT_LIST_FILE}' not found. Please create it with student names.")
    return students

def mark_attendance(students):
    """Marks attendance for today's date."""
    today = datetime.now().strftime('%Y-%m-%d')
    attendance_records = []

    # Load existing attendance for today if available
    try:
        with open(ATTENDANCE_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header
            if header[0] == 'Date' and today in header: # Check if today's date column exists
                for row in reader:
                    if row:
                        attendance_records.append(row)
            else: # If header doesn't match or today's date column is missing, create new records
                attendance_records = [[student, 'A'] for student in students] # Initialize all as Absent
    except FileNotFoundError:
        attendance_records = [[student, 'A'] for student in students] # Initialize all as Absent

    print(f"\nMarking attendance for {today}:")
    for i, student in enumerate(students):
        status = input(f"Is {student} Present (P) or Absent (A)? ").upper()
        if status not in ['P', 'A']:
            status = 'A' # Default to Absent if invalid input
        
        # Update or add attendance record
        found = False
        for record in attendance_records:
            if record[0] == student:
                record[1] = status
                found = True
                break
        if not found:
            attendance_records.append([student, status])

    # Save updated attendance
    with open(ATTENDANCE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student Name', today]) # Header for the attendance file
        for record in attendance_records:
            writer.writerow(record)
    print("Attendance marked and saved successfully.")

def view_attendance():
    """Displays attendance records."""
    try:
        with open(ATTENDANCE_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(','.join(row))
    except FileNotFoundError:
        print("No attendance records found.")

def main():
    students = load_students()
    if not students:
        print("Please add student names to 'students.csv' before proceeding.")
        return

    while True:
        print("\nStudent Attendance Management System")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            mark_attendance(students)
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()