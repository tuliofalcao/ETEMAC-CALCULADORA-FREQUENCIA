import mes

def f():
    print("")
    o.setFaltas(int(input("faltas de fevereiro: ")))
    n.setFaltas(int(input("faltas de março: ")))
    print("")
    print("======================")
    print(f"Outubro: {o.porcentagem()} %")
    print(f"Novembro: {n.porcentagem()} %")
    print("======================")
    print("")


o = mes.Mes("fevereiro", 16)
n = mes.Mes("março", 21)

f()
