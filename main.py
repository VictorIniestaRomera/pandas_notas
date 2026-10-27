import pandas as pd;

STUDENTS_FILE = "./input/students.csv";
GRADES_FILE = "./input/grades.csv";

USERS_FILE = "./output/users.json";
AVERAGE_IMG = "./output/average.png";

def printJSON(json: pd) -> None:
    pd.set_option("display.max_columns", None);
    pd.set_option("display.max_rows", None);
    pd.set_option("display.width", 1000);
    
    print(json);

def genAverage(json: pd) -> None:
    gradeColumns = ["grade1", "grade2", "grade3"];

    json[gradeColumns] = json[gradeColumns].apply(pd.to_numeric, errors = "coerce");

    validGrades = json[json[gradeColumns].notna().all(axis=1)];

    average = validGrades[gradeColumns].mean();

    ax = average.plot.bar(
        title = "3 Notas medias",
        ylim = (0, 10),
        rot = 0,
        ylabel = "Nota Media",
        xlabel = "Actividades",
        grid=True
    );

    ax.get_figure().savefig(AVERAGE_IMG, bbox_inches = "tight", dpi = 300);

def main():
    try:
        students = pd.read_csv(STUDENTS_FILE, dtype={"id_student": "string"}, skipinitialspace=True,);
        grades = pd.read_csv(GRADES_FILE, dtype={"id_student": "string"}, skipinitialspace=True,);

        for s in students["id_student"].duplicated():
            if s is True:
                raise Exception("Duplicated id in Nº", s.__index__());
    
        for nd in students["name_student"].duplicated():
            for sd in students["surname_student"].duplicated():
                if nd is True and sd is True:
                    raise Exception("Duplicated full name in Nº", nd.__index__());

        for g in grades["id_student"].duplicated():
            if g is True:
                raise Exception("Duplicated id in Nº", g.__index__());

        usersFile = pd.merge(students, grades, on="id_student", how="left", );
        lusersFile = usersFile.fillna('N/D');
        lusersFile.to_json(USERS_FILE, orient="records", indent=4);

        printJSON(lusersFile);
        genAverage(lusersFile);
    except Exception as e:
        print("Exception caught: ", e);

if __name__ == "__main__":
    main();