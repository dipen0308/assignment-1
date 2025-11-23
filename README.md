#  Student Attendance Management System

This is a simple, command-line **Student Attendance Management System** built with **Python 3**. It uses standard Python modules (`csv` and `datetime`) to load a list of students from one CSV file and record daily attendance into another CSV file.

---

###  Features

* **Load Student List:** Reads student names from a file named `students.csv`.
* **Mark Daily Attendance:** Allows the user to mark each student as **Present (P)** or **Absent (A)** for the current date.
* **Persistent Storage:** Saves all attendance records to a file named `attendance.csv`.
* **View Records:** Displays the contents of the `attendance.csv` file directly to the console.

---

###  Getting Started

#### Prerequisites

* **Python 3.x** installed on your system.

#### Installation

1.  **Save the code:** Save the provided Python code into a file named `attendance_system.py`.
2.  **Create Student List:** In the same directory, create a file named **`students.csv`**. This file should contain one student name per line.

    **Example `students.csv` content:**
    ```csv
    Alice Johnson
    Bob Smith
    Charlie Brown
    ```
3.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the files, and run the main script.

    ```bash
    python attendance_system.py
    ```

---

###  Usage

When you run the script, a main menu will appear, prompting you to choose an action.

#### 1. Mark Attendance

Selecting option **1** will start the attendance process for the current date.

* The system will iterate through every student in `students.csv`.
* You will be prompted to enter **P** (Present) or **A** (Absent) for each student.
* The system defaults to **A** if any other input is given.
* Once finished, the data will be saved to **`attendance.csv`**.

#### 2. View Attendance

Selecting option **2** will read and display the current contents of the **`attendance.csv`** file in the console.

**Example `attendance.csv` output after marking attendance:**

| Student Name | 2025-11-23 |
| :--- | :--- |
| Alice Johnson | P |
| Bob Smith | A |
| Charlie Brown | P |

---

###  Code Structure

The system is organized into four main functions:

| Function | Purpose |
| :--- | :--- |
| `load_students()` | Reads names from `students.csv`. |
| `mark_attendance(students)` | Handles user input to mark attendance and saves to `attendance.csv`. |
| `view_attendance()` | Reads and prints the entire `attendance.csv` file. |
| `main()` | Sets up the main loop and menu for user interaction. |

---

###  Contributing

Contributions are welcome! If you have suggestions for improvement, such as adding features like calculating attendance percentages or exporting reports, please fork the repository and submit a pull request.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

###  License

Distributed under the MIT License. See `LICENSE` for more information.
