#       __         .' '.
#     _/__)        .   .       .
#    (8|)_}}- .      .        .
#     `\__)    '. . ' ' .  . '
#                          -vietrux-


s = []  
c = []  
m = {}  

def ins():  
    while True:
        try:
            ns = int(input("Enter the number of students: "))
            if ns > 0:
                return ns
            else:
                print("The number of students must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def isi():  
    sid = input("Enter student ID: ")
    sn = input("Enter student name: ")
    sd = input("Enter student date of birth (DD/MM/YYYY): ")
    s.append((sid, sn, sd))
    print(f"Student {sn} added successfully.")

def inc():  
    while True:
        try:
            nc = int(input("Enter the number of courses: "))
            if nc > 0:
                return nc
            else:
                print("The number of courses must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ici():  
    cid = input("Enter course ID: ")
    cn = input("Enter course name: ")
    c.append((cid, cn))
    m[cid] = {}
    print(f"Course {cn} added successfully.")

def imc():  
    if not c:
        print("No courses available. Please add courses first.")
        return
    
    print("Available courses:")
    for cid, cn in c:
        print(f"{cid}: {cn}")
    
    sc = input("Enter the course ID to input marks: ")
    if sc not in m:
        print("Invalid course ID.")
        return
    
    if not s:
        print("No students available. Please add students first.")
        return
    
    print("Available students:")
    for sid, sn, _ in s:
        print(f"{sid}: {sn}")
        while True:
            try:
                mk = float(input(f"Enter mark for {sn}: "))
                if 0 <= mk <= 20:
                    m[sc][sid] = mk
                    break
                else:
                    print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    print("Marks added successfully.")


def lc():  
    if not c:
        print("No courses available.")
    else:
        print("List of courses:")
        for cid, cn in c:
            print(f"{cid}: {cn}")

def ls():  
    if not s:
        print("No students available.")
    else:
        print("List of students:")
        for sid, sn, sd in s:
            print(f"{sid}: {sn}, DoB: {sd}")

def smc():  
    if not c:
        print("No courses available. Please add courses first.")
        return
    
    print("Available courses:")
    for cid, cn in c:
        print(f"{cid}: {cn}")
    
    sc = input("Enter the course ID to show marks: ")
    if sc not in m:
        print("Invalid course ID.")
        return
    
    if not m[sc]:
        print("No marks available for this course.")
    else:
        print(f"Marks for {sc}:")
        for sid, mk in m[sc].items():
            sn = next(name for id, name, _ in s if id == sid)
            print(f"{sn} (ID: {sid}): {mk}")

def main():  
    help = "Student Mark Management System\n1. Input number of students\n2. Input student information\n3. Input number of courses\n4. Input course information\n5. Input marks for a course\n6. List courses\n7. List students\n8. Show student marks for a course\n9. Help\n10. Exit"
    print(help)
    while True:
        ch = input("Enter your choice: ")
        
        if ch == '1':
            ns = ins()
            for _ in range(ns):
                isi()
        elif ch == '2':
            isi()
        elif ch == '3':
            nc = inc()
            for _ in range(nc):
                ici()
        elif ch == '4':
            ici()
        elif ch == '5':
            imc()
        elif ch == '6':
            lc()
        elif ch == '7':
            ls()
        elif ch == '8':
            smc()
        elif ch == '9':
            print(help)
        elif ch == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()