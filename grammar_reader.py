RULE = {}

def isTerminal(string):
    terminals = ["STRING","NUM","NEWLINE","KBKI","KBKA","KSKI",
                "KSKA","KKKI","KKKA","TITIKKOMA","TITIKDUA","POWAS",
                "POW","FLOORDIVAS","FLOORDIV","MULAS","DIVAS","ADDAS",
                "SUBAS","MODAS","ARROW","ADD","SUB","MUL","DIV","MOD",
                "LEQ","L","GEQ","G","NEQ","ISEQ","EQ","AND","OR","NOT",
                "IF","ELSE","ELSE IF","FOR","IN","OF","DO","WHILE","SWITCH",
                "CASE","DEFAULT","TRY","CATCH","FINALLY","THROW","DELETE","CONTINUE",
                "BREAK","FALSE","TRUE","CLASS","FUNCTION","RETURN","FROM","IMPORT","AS",
                "RAISE","WITH","NULL","TYPE","COMMA","KARTITIK","TITIK","IS","MULTILINE","ID","NEW",
                "BITORAS", "BITANDAS", "NULLISHAS", "NULLISH", "BITLEFT", "BITRIGHT", "BITOR",
                "BITAND", "BITNOT", "TERNARY", "STRICTEQ", "STRICTNEQ", "BITLEFTAS", "BITRIGHTAS"]
    return string in terminals

def read_grammar(nama_file):
    #Buka file yang berisi aturan - aturan grammar dalam bentuk A -> B 
    files = open(nama_file)
    cfg = []
    for file in files : 
        #Menghapus tanda panah
        file = file.replace('->',"")
        #Menggabungkan aturan ke dalam cfg, dalam bentuk array
        cfg.append(file.split())
    #Mengembalikan CFG dalam bentuk array
    return cfg

def add_new_rule(rule):
    # Menambah aturan ke kamus
    global RULE

    if rule[0] not in RULE:
        RULE[rule[0]] = []
    RULE[rule[0]].append(rule[1:])

def convert_grammar(grammar):
    # Meng-convert cfg menjadi cnf
    global RULE

    #Siapin array kosong untuk menampung unit productions dan result
    unit_productions, result = [], []
    idx = 0

    #Looping semua aturan dalam CFG
    for rule in grammar:
        new_rules = []
        #Jika jumlah aturan = 2 dan bukan terminal
        if (len(rule) == 2 and rule[1][0] != "'"):
            #Tambahkan aturan ke dalam unit_productions
            unit_productions.append(rule)
            add_new_rule(rule)
            continue
        #Jika jumlah aturan > 2 
        elif (len(rule) > 2):
            #Buat variabel baru yang namanya menggunakan metode enumerate
            items = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if (isTerminal(rule[0])):
                for item in items:
                    rule[item[1]] = f"{rule[0]}{str(idx)}"
                    new_rules += [f"{rule[0]}{str(idx)}", item[0]]
                idx += 1
            
            while (len(rule) > 3):
                new_rules.append([f"{rule[0]}{str(idx)}", rule[1], rule[2]])
                rule = [rule[0]] + [f"{rule[0]}{str(idx)}"] + rule[3:]
                idx += 1
        add_new_rule(rule)
        result.append(rule)
        if new_rules:
            result.extend(new_rules)

    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE:
            for item in RULE[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.insert(0,new_rule)
                else:
                    unit_productions.append(new_rule)
                add_new_rule(new_rule)
    return result

def write_cnf(fileCNF,fileName):
    # Menulis hasil convert ke dalam file txt
    file = open(fileName, 'w')
    for cnf in fileCNF:
        file.write(cnf[0])
        file.write(" -> ")
        for i in cnf[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

def read_cnf():
    files = open("grammar_reader.txt")
    cnf = []
    for file in files : 
        #Menghapus tanda panah
        file = file.replace('->',"")
        #Menggabungkan aturan ke dalam cnf, dalam bentuk array
        cnf.append(file.split())
    #Mengembalikan cnf dalam bentuk array
    return cnf

