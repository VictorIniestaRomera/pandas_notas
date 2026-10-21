import pandas as pd;

STUDENTS_FILE = "./input/students.csv";
GRADES_FILE = "./input/grades.csv";

def main():
    try:
        students = pd.read_csv(STUDENTS_FILE, dtype={"id_student": "string"}, skipinitialspace=True,);
        grades = pd.read_csv(GRADES_FILE, dtype={"id_student": "string"}, skipinitialspace=True,);

        for d in students["id_student"].duplicated():
            if d is True:
                raise Exception("Duplicated id in Nº", d.__index__());

        for nd in students["name_student"].duplicated():
            for sd in students["surname_student"].duplicated():
                if nd is True and sd is True:
                    raise Exception("Duplicated full name in Nº", nd.__index__());
    
        students.info();
    except Exception as e:
        print("Exception caught: ", e);

if __name__ == "__main__":
    main();