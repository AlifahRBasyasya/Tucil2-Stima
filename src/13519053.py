# Nama      : Alifah Rahmatika Basyasya
# NIM       : 13519053
# Tanggal   : 27 Februari 2021
# Deskripsi : Topological Sorting Pengambilan Mata Kuliah - Decrease and Conquer (Tucil2 Stima)

#FUNGSI DAN PROSEDUR
def AppName():
    print("                                     _  .-')    .-')      ('-.           _ (`-.              ('-.         .-') _      .-') _   ('-.  _  .-')   ")
    print("                                    ( \( -O )  ( OO ).  _(  OO)         ( (OO  )            ( OO ).-.    ( OO ) )    ( OO ) )_(  OO)( \( -O )  ")
    print("   .-----.  .-'),-----.  ,--. ,--.   ,------. (_)---\_)(,------.       _.`     \ ,--.       / . --. /,--./ ,--,' ,--./ ,--,'(,------.,------.  ")
    print("  '  .--./ ( OO'  .-.  ' |  | |  |   |   /`. '/    _ |  |  .---'      (__...--'' |  |.-')   | \-.  \ |   \ |  |\ |   \ |  |\ |  .---'|   /`. ' ")
    print("  |  |('-. /   |  | |  | |  | | .-') |  /  | |\  :` `.  |  |           |  /  | | |  | OO ).-'-'  |  ||    \|  | )|    \|  | )|  |    |  /  | | ")
    print(" /_) |OO  )\_) |  |\|  | |  |_|( OO )|  |_.' | '..`''.)(|  '--.        |  |_.' | |  |`-' | \| |_.'  ||  .     |/ |  .     |/(|  '--. |  |_.' | ")
    print(" ||  |`-'|   \ |  | |  | |  | | `-' /|  .  '.'.-._)   \ |  .--'        |  .___.'(|  '---.'  |  .-.  ||  |\    |  |  |\    |  |  .--' |  .  '.' ")
    print("(_'  '--'\    `'  '-'  '('  '-'(_.-' |  |\  \ \       / |  `---.       |  |      |      |   |  | |  ||  | \   |  |  | \   |  |  `---.|  |\  \  ")
    print("   `-----'      `-----'   `-----'    `--' '--' `-----'  `------'       `--'      `------'   `--' `--'`--'  `--'  `--'  `--'  `------'`--' '--' ")

def ReadFile(namafile):
    #Membaca file dan menyimpannya dalam matriks yang merepresentasikan graf prereq.
    #Kolom pertama matriks merupakan representasi sebuah simpul.
    #Kolom berikutnya pada baris yang sama, merupakan simpul yang memiliki
    #busur masuk ke kolom 1
    #KAMUS LOKAL
    global Matriks
    #ALGORITMA
    file = open("../test/" + namafile, "r")
    prereq = file.readline().strip(" \n.")
    while (prereq != ""):
        kode = prereq.replace(" ", "").split(",")
        Matriks.append(kode)
        prereq = file.readline().strip(" \n.")

def RemoveEdge(Matriks, Semester):
    #Menghapus mata kuliah yang sudah dapat diambil di semester ini
    #Menghapus busur-busur masuk terkait mata kuliah yang bersangkutan
    #KAMUS LOKAL
    #i : integer
    #ALGORITMA
    for i in range(len(Matriks)):
        for mk in Semester:
            if (mk in Matriks[i]):
                Matriks[i].remove(mk)

def AssignSemester():
    #Menempatkan mata kuliah yang tidak memiliki prerequisite pada semester saat ini
    #KAMUS LOKAL
    #i : integer
    #Semester : array of string
    Semester = []
    global Matriks
    global Assigned
    global CountSem
    #ALGORITMA
    for i in range(len(Matriks)):
        #Semua prerequisite sudah diambil atau tidak memiliki prerequisite
        if (len(Matriks[i]) == 1):
            Semester.append(Matriks[i][0])
    Assigned.append(Semester)
    CountSem += 1
    RemoveEdge(Matriks,Semester)

def AssignForAll(Done):
    #Menempatkan semua mata kuliah pada semester yang sesuai berdasarkan prerequisite
    #KAMUS LOKAL
    #i : integer
    #ALGORITMA
    while (not Done):
        Done = True
        #Memproses secara rekursif
        AssignSemester()
        for i in range(len(Matriks)):
            if (len(Matriks[i]) != 0):
                Done = False

def OutputSemester(Assigned):
    #KAMUS LOKAL
    #i,j : integer
    #ALGORITMA
    for i in range(CountSem):
        if (len(Assigned[i]) != 0):
            print("Semester", (i+1), ":")
            for j in range(len(Assigned[i])):
                print(Assigned[i][j])

#PROGRAM UTAMA COURSE PLANNER
#Course Planner menerima masukan sebuah namafile (dalam .txt) yang berisi daftar mata kuliah beserta prerequisitenya
#Course Planner kemudian mengolah daftar tersebut dan menampilkan daftar pengambilan mata kuliah tiap semester
#KAMUS
#Matriks, Assigned : array of array of string
#CountSem : integer
#Done : boolean
Matriks = []
Assigned = []
CountSem = 0
Done = False
#ALGORITMA
AppName()
namafile = input("Masukkan nama file beserta .txt: ")
ReadFile(namafile)
AssignForAll(Done)
print("Pengambilan yang diperbolehkan untuk tiap semester adalah sebagai berikut.")
OutputSemester(Assigned)
