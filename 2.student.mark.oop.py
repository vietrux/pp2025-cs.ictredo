#       __         .' '.
#     _/__)        .   .       .
#    (8|)_}}- .      .        .
#     `\__)    '. . ' ' .  . '
#                          -vietrux-

class StudentMarkManagement:
    def __init__(self):
        self.s = []  # List of students (sid, sn, sd)
        self.c = []  # List of courses (cid, cn)
        self.m = {}  # Dictionary for marks {cid: {sid: mark}}

    def ins(self):  
        while True:
            try:
                ns = int(input("Enter the number of students: "))
                if ns > 0:
                    return ns
                else:
                    print("The number of students must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def isi(self):  
        sid = input("Enter student ID: ")
        sn = input("Enter student name: ")
        sd = input("Enter student date of birth (DD/MM/YYYY): ")
        self.s.append((sid, sn, sd))
        print(f"Student {sn} added successfully.")

    def inc(self):  
        while True:
            try:
                nc = int(input("Enter the number of courses: "))
                if nc > 0:
                    return nc
                else:
                    print("The number of courses must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ici(self):  
        cid = input("Enter course ID: ")
        cn = input("Enter course name: ")
        self.c.append((cid, cn))
        self.m[cid] = {}
        print(f"Course {cn} added successfully.")

    def imc(self):  
        if not self.c:
            print("No courses available. Please add courses first.")
            return
        
        print("Available courses:")
        for cid, cn in self.c:
            print(f"{cid}: {cn}")
        
        sc = input("Enter the course ID to input marks: ")
        if sc not in self.m:
            print("Invalid course ID.")
            return
        
        if not self.s:
            print("No students available. Please add students first.")
            return
        
        print("Available students:")
        for sid, sn, _ in self.s:
            print(f"{sid}: {sn}")
            while True:
                try:
                    mk = float(input(f"Enter mark for {sn}: "))
                    if 0 <= mk <= 20:
                        self.m[sc][sid] = mk
                        break
                    else:
                        print("Mark must be between 0 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        print("Marks added successfully.")

    def lc(self):  
        if not self.c:
            print("No courses available.")
        else:
            print("List of courses:")
            for cid, cn in self.c:
                print(f"{cid}: {cn}")

    def ls(self):  
        if not self.s:
            print("No students available.")
        else:
            print("List of students:")
            for sid, sn, sd in self.s:
                print(f"{sid}: {sn}, DoB: {sd}")

    def smc(self):  
        if not self.c:
            print("No courses available. Please add courses first.")
            return
        
        print("Available courses:")
        for cid, cn in self.c:
            print(f"{cid}: {cn}")
        
        sc = input("Enter the course ID to show marks: ")
        if sc not in self.m:
            print("Invalid course ID.")
            return
        
        if not self.m[sc]:
            print("No marks available for this course.")
        else:
            print(f"Marks for {sc}:")
            for sid, mk in self.m[sc].items():
                sn = next(name for id, name, _ in self.s if id == sid)
                print(f"{sn} (ID: {sid}): {mk}")

    def show_help(self):
        help_text = (
            "Student Mark Management System\n"
            "1. Input number of students\n"
            "2. Input student information\n"
            "3. Input number of courses\n"
            "4. Input course information\n"
            "5. Input marks for a course\n"
            "6. List courses\n"
            "7. List students\n"
            "8. Show student marks for a course\n"
            "9. Help\n"
            "10. Exit"
        )
        print(help_text)

    def main(self):
        self.show_help()
        while True:
            ch = input("Enter your choice: ")
            
            if ch == '1':
                ns = self.ins()
                for _ in range(ns):
                    self.isi()
            elif ch == '2':
                self.isi()
            elif ch == '3':
                nc = self.inc()
                for _ in range(nc):
                    self.ici()
            elif ch == '4':
                self.ici()
            elif ch == '5':
                self.imc()
            elif ch == '6':
                self.lc()
            elif ch == '7':
                self.ls()
            elif ch == '8':
                self.smc()
            elif ch == '9':
                self.show_help()
            elif ch == '10':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    smms = StudentMarkManagement()
    smms.main()
