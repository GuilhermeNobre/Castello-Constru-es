from tkinter import *
from PIL import ImageTk, Image
from math import pow, pi

root = Tk()
root.title("Castello v1.0")
root.iconbitmap("C:/Users\Guilherme Nobre\PycharmProjects\castello\Images\castello.ico")

def p1():
    global my_image2
    top = Toplevel()
    top.title('1- Controle de consumo')
    top.iconbitmap("C:\Banco Dados/castello.ico")

    def bc1():
        e1.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=1, column=5, padx=10)

    def bc2():
        e2.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=2, column=5, padx=10)

    def bc3():
        e3.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=3, column=5, padx=10)

    def bc4():
        e4.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=4, column=5, padx=10)

    def bc5():
        e5.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=5, column=5, padx=10)

    def bc6():
        e6.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=6, column=5, padx=10)

    def bc7():
        e7.delete(0, END)
        andar_label = Label(top, text="")
        andar_label.grid(row=7, column=5, padx=10)

    # DEF

    def click8():
        n_andar: int = (e1.get())
        andar_g = n_andar
        n_apt: int = (e2.get())
        apt_g = n_apt
        n_socia: int = (e3.get())
        socia_g = n_socia
        n_servic: int = (e4.get())
        servic_g = n_servic
        n_zelador: int = (e5.get())
        zelador_g = n_zelador
        n_carros: int = (e6.get())
        carros_g = n_carros
        n_jardim: int = (e7.get())
        jardim_g = n_jardim
        consumo_diario: int = (e8.get())
        consumo_g = consumo_diario

        p1 = int(andar_g) * int(apt_g) * int(socia_g) * 2
        p2 = int(andar_g) * int(apt_g) * int(servic_g) * 1
        p3 = int(zelador_g)
        pt = str(p1 + p2 + p3)

        cd1 = int(pt) * int(consumo_g)
        cd2 = int(andar_g) * int(apt_g) * 50 * int(carros_g)
        cd3 = int(jardim_g) * 30
        cdt = cd1 + cd2 + cd3

        cap = 2 * int(cdt)

        rti = 0.2 * int(cap)

        ri = (2 / 3) * int(cap)

        rs = (1 / 3) * int(cap) + int(rti)

        andar_label = Label(top, text="População Total: " + pt)
        andar_label.grid(row=10, column=0, padx=10, sticky=W)

        consumo_diario_final = Label(top, text="Consumo diários " + str(cdt) + " litros/dia")
        consumo_diario_final.grid(row=11, column=0, padx=10, sticky=W)

        capacidade_reservatorio = Label(top, text="Capacidade do reservatório " + str(cap) + " litros")
        capacidade_reservatorio.grid(row=12, column=0, padx=10, sticky=W)

        reserva__tecnica_incendio = Label(top, text="Reserva Incendio {:.0f} litros".format(rti))
        reserva__tecnica_incendio.grid(row=13, column=0, padx=10, sticky=W)

        reserva_inferior = Label(top, text="Reserva Inferior {:.0f} litros".format(ri))
        reserva_inferior.grid(row=14, column=0, padx=10, sticky=W)

        reserva_superior = Label(top, text="Reserva Superior {:.0f} litros".format(rs))
        reserva_superior.grid(row=15, column=0, padx=10, sticky=W)

    # LABELs
    labTitle = Label(top, text="CONSUMO DIARIOS")
    lab_andar = Label(top, text="Número de Andar: ")
    lab_aps = Label(top, text="Número de apartamentos: ")
    lab_quarto_soci = Label(top, text="Número de quartos sociais: ")
    lab_quarto_serv = Label(top, text="Número de quartos serviços: ")
    lab_zelador = Label(top, text="Número de alojamento zelador:")
    lab_carro = Label(top, text="Número de carros por garagem:")
    lab_jardim = Label(top, text="Número de área de jardins: ")
    lab_consumo = Label(top, text='Consumo diário média 1 pessoa: ')
    soma_total = Label(top, text="CONFIRMAR VALORES: ")

    # LOCALIZAÇÃO_Labes
    labTitle.grid(row=0, column=0, columnspan=1)
    lab_andar.grid(row=1, sticky=W, padx=15)
    lab_aps.grid(row=2, sticky=W, padx=15)
    lab_quarto_soci.grid(row=3, sticky=W, padx=15)
    lab_quarto_serv.grid(row=4, sticky=W, padx=15)
    lab_zelador.grid(row=5, sticky=W, padx=15)
    lab_carro.grid(row=6, sticky=W, padx=15)
    lab_jardim.grid(row=7, sticky=W, padx=15)
    lab_consumo.grid(row=8, sticky=W, padx=15)
    soma_total.grid(row=9, sticky=W, padx=20)

    # Entrys

    e1 = Entry(top, width=10)
    e2 = Entry(top, width=10)
    e3 = Entry(top, width=10)
    e4 = Entry(top, width=10)
    e5 = Entry(top, width=10)
    e6 = Entry(top, width=10)
    e7 = Entry(top, width=10)
    e8 = Entry(top, width=10)

    # LOCALIZAÇÃO_entrys
    e1.grid(row=1, column=1, padx=15)
    e2.grid(row=2, column=1, padx=15)
    e3.grid(row=3, column=1, padx=15)
    e4.grid(row=4, column=1, padx=15)
    e5.grid(row=5, column=1, padx=15)
    e6.grid(row=6, column=1, padx=15)
    e7.grid(row=7, column=1, padx=15)
    e8.grid(row=8, column=1, padx=15)

    # Botões
    bt8 = Button(top, text='Ok!', width=5, command=click8)
    bt_clear = Button(top, text='Limpar', width=5, )

    # Botão_grid
    bt8.grid(row=9, column=1, stick=W, pady=3)
    bt_clear.grid(row=9, column=1, stick=E, pady=3, padx=3)


def p2():
    global correcao_image
    top = Toplevel()
    top.title('2- Correção de momentos')
    top.iconbitmap("C:\Banco Dados/castello.ico")

    def cacl1():
        xa_get: int = (e1.get())
        xa_int = xa_get
        xb_get: int = (e2.get())
        xb_int = xb_get

        Xme = (int(xa_int) + int(xb_int)) / 2

        if int(xa_int) > int(xb_int):
            Xma = int(xa_int)
            x80 = int(xa_int) * 0.80

        elif int(xb_int) > int(xa_int):
            Xma = int(xb_int)
            x80 = int(xb_int) * 0.80

        if x80 > Xme:
            XE = x80

        elif Xme > x80:
            XE = Xme

        DX = float((int(Xma) - int(XE)) / 2)

        frame3 = LabelFrame(top, text='Insira os Valores', padx=10, pady=15)
        frame3.grid(row=1, column=0, sticky=N, ipady=3, ipadx=3, pady=9)

        med_lbl = Label(frame3, text="Valor de X médio: {:.2f}".format(int(Xme)))
        med_lbl.grid(row=0, column=0)

        Dx_lbl = Label(frame3, text="Valor de X maior: {:.2f} \nValor X80%: {:.2f} \nValor XE: {:.2f}"
                       .format(int(Xma), int(x80), int(XE)))
        Dx_lbl.grid(row=1, column=0)

        delta_lbl = Label(frame3, text="Valor de ΔX: {:.2f}".format(int(DX)))
        delta_lbl.grid(row=2, column=0)

    # frameLabel

    frame = LabelFrame(top, text='Insira os Valores', padx=10, pady=15)


    # frameLabel Grid

    frame.grid(row=0, column=0, sticky=N, ipady=3, ipadx=3, padx=5)

    # Imagem

    correcao_imgae = ImageTk.PhotoImage(Image.open("C:\Banco Dados/a.png"))

    image_label = Label(top, image=correcao_imgae)
    image_label.grid(row=0, column=2, columnspan=2, sticky=W + E + N + S, padx=3, pady=3)

    # Creation of Labels

    Xa_lbn = Label(frame, text="Insira o Valor de XA:")
    Xb_lbn = Label(frame, text="Insira o Valor de XB:")

    # Grid of Labels

    Xa_lbn.grid(row=0, column=0, sticky=W + N, padx=3, pady=3)
    Xb_lbn.grid(row=1, column=0, sticky=N + W, padx=3, pady=3)

    # Creatiopm of Entries

    e1 = Entry(frame, width=10)
    e2 = Entry(frame, width=10)

    # Grid of Enties
    e1.grid(row=0, column=1, sticky=W + N, padx=3, pady=5)
    e2.grid(row=1, column=1, sticky=W + N, padx=3, pady=5)

    # Creation Buttons

    bnt_calc = Button(frame, text='Calcular', width=7, command=cacl1)

    # Location of Buttons

    bnt_calc.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


def p3():
    def frame4():
        frame4 = LabelFrame(frame1, text='Pilar Exemplar ')
        frame4.grid(row=1, column=1, padx=10, pady=10, ipady=4, ipadx=4, sticky=N + W)

        lb_nk = Label(frame4, text="O Valor de ND: {:.2f} Kn".format(Nd))
        lb_nk.grid(row=0, column=0, sticky=W)

        lb_lx = Label(frame4, text='Momento Fletor Min. X: {:.2f} Kn.cm'.format(mdinx))
        lb_lx.grid(row=1, column=0, sticky=W)

        lb_ly = Label(frame4, text='Momento Fletor Min. Y: {:.2f} Kn.cm'.format(mdiny))
        lb_ly.grid(row=2, column=0, sticky=W)

        lb_lex = Label(frame4, text="Excêntricidade Min. X: {:.2f} cm".format(e2x_final))
        lb_lex.grid(row=3, column=0, sticky=W)

        lb_ley = Label(frame4, text="Excêntricidade Min. Y: {:.2f} cm".format(e2y_final))
        lb_ley.grid(row=4, column=0, sticky=W)

    def frame5():

        global entry_mix, entry_miy, aco_final_ent

        CX: int = (r_cong.get())

        frame5 = LabelFrame(frame1, text='Valores do Pilar')
        frame5.grid(row=0, column=2, padx=10, pady=10, ipady=4, ipadx=4, sticky=N + W)

        lb_n1 = Label(frame5, text='μ X: {:.2f}'.format(miX))
        lb_n1.grid(row=4, column=0, sticky=W)

        lb_nk = Label(frame5, text='μ Y: {:.2f}'.format(miY))
        lb_nk.grid(row=5, column=0, sticky=W)

        lb_lx = Label(frame5, text='Momento Fletor 2° ordem X: {:.2f} Kn.cm'.format(mdtotx))
        lb_lx.grid(row=2, column=0, sticky=W)

        lb_ly = Label(frame5, text='Momento Fletor 2° ordem Y: {:.2f} Kn.cm'.format(mdtoty))
        lb_ly.grid(row=3, column=0, sticky=W)

        lb_yv = Label(frame5, text="Valor de V: {:.2f}".format(Yv))
        lb_yv.grid(row=6, column=0, sticky=W)

        lb_cv = Label(frame5, text="O concreto utilizado: {} MPa ".format(CX))
        lb_cv.grid(row=7, column=0, sticky=W)

        lb_ab1 = Label(frame5, text="O Valor no ABACO em X: ")
        lb_ab1.grid(row=8, column=0, sticky=W)

        entry_mix = Entry(frame5, width=10)
        entry_mix.grid(row=8, column=0, sticky=E, rowspan=1, columnspan=1)

        lb_ab2 = Label(frame5, text="O Valor no ABACO em Y: ")
        lb_ab2.grid(row=9, column=0, sticky=W)

        entry_miy = Entry(frame5, width=10)
        entry_miy.grid(row=9, column=0, sticky=E, rowspan=1, columnspan=1)

        aco_final_lbn = Label(frame5, text="DIÂMETRO DAS BARRAS: ")
        aco_final_lbn.grid(row=10, column=0, sticky=W)

        aco_final_ent = Entry(frame5, width=10)
        aco_final_ent.grid(row=10, column=0, sticky=E, rowspan=1, columnspan=1)

        btn = Button(frame5, text="VALIDAR", command=frame6, width=20, borderwidth=2)
        btn.grid(row=11, column=0, pady=4, ipadx=4, sticky=N + S)

        if CX == 25:
            concreto25_png = ImageTk.PhotoImage(Image.open("C:\gui\Images/c25.jpg"))
            top25 = Toplevel()
            top25.title('TABELA C25')
            top25.iconbitmap('C:\Banco de Dados\Icon\castello.ico')
            my_label = Label(top25, image=concreto25_png).pack()

        elif CX == 20:
            concreto20_png = ImageTk.PhotoImage(Image.open("C:\gui\Images/c20.jpg"))
            top20 = Toplevel()
            top20.title('TABELA C20')
            top20.iconbitmap("C:\Banco de Dados\Icon\c20.jpg")
            my_label = Label(top20, image=concreto20_png).pack()

    def frame6():

        acox: float = (entry_mix.get())
        acoy: float = (entry_miy.get())
        aco1: float = (aco_final_ent.get())

        aco_final = float(((pow((float(aco1) / 2), 2)) * pi) / 100)

        asox = (float(acox) / 100) * int(Ac)
        asoy = (float(acoy) / 100) * int(Ac)

        if asox > asoy:
            As_final = asox

        elif asox > asoy:
            As_final = asoy

        else:
            As_final = asox

        n_barras = int(float(As_final) / float(aco_final))

        s_espaco = float(100 / int(n_barras))

        #####

        if lx > ly:
            lmenor = ly

        else:
            lmenor = lx

        cSb = 2 * int(lmenor)

        if 2 * int(lmenor) < 40:
            Sb = cSb

        else:
            Sb = 40

        estribo_diametro = float(aco1) / 4

        if estribo_diametro < 5:
            estribo_diametro_final = 5

        else:
            estribo_diametro_final = estribo_diametro

        distancia_estribo = 12 * (float(aco1) / 10)

        if int(lmenor) < 20:
            distancia_estribo_final = lmenor

        elif distancia_estribo < 20:
            distancia_estribo_final = distancia_estribo

        else:
            distancia_estribo_final = distancia_estribo

        frame6 = LabelFrame(frame1, text='Area do Pilar')
        frame6.grid(row=1, column=2, padx=10, pady=10, ipady=4, ipadx=4, sticky=N + W)

        lb_cv = Label(frame6, text="Área do pilar: {:.2f}cm²".format(Ac))
        lb_cv.grid(row=0, column=0, sticky=W)

        lb_ac = Label(frame6, text="Área de aço: {:.2f}cm²".format(As_final))
        lb_ac.grid(row=1, column=0, sticky=W)

        lb_dnd = Label(frame6, text="BARRAS DE AÇO APRESENTAM")
        lb_dnd.grid(row=2, column=0, sticky=W)

        lb_as = Label(frame6, text='{:.0f} Ø {:.1f} com distânciamento {:.2f}cm²'.format(int(n_barras), float(aco1),
                                                                                         int(s_espaco)))
        lb_as.grid(row=3, column=0, sticky=W)

        lb_est = Label(frame6, text="ESTRIBOS APRESENTAM")
        lb_est.grid(row=4, column=0, sticky=W)

        lb_as = Label(frame6,
                      text='Ø {:.0f} com distânciamento {}cm'.format(estribo_diametro_final, distancia_estribo_final))
        lb_as.grid(row=5, column=0, sticky=W)

        # ARIADNE EU TE AMO

    def calc():
        global r1_final, r2_final, mdinx, mdiny, e2x_final, e2y_final, Nd, miX, miY
        global e2x_final, e2y_final, mdtotx, mdtoty, Yv, Ac, lx, ly

        CX: int = (r_cong.get())
        Nk_n: float = (entry_nk.get())
        nk = Nk_n
        lx_n: int = (entry_lx.get())
        lx = lx_n
        ly_n: int = (entry_ly.get())
        ly = ly_n
        lex_n: int = (entry_lex.get())
        lex = lex_n
        ley_n: int = (entry_ley.get())
        ley = ley_n

        if lx < ly:
            yn = int(lx)

            if yn == 14:
                yn = 1.25
            elif yn == 15:
                yn = 1.20
            elif yn == 16:
                yn = 1.15
            elif yn == 17:
                yn = 1.10
            elif yn == 18:
                yn = 1.05
            elif yn == 19:
                yn = 1
            elif yn > 19:
                yn = (195 / 100) - ((5 / 100) * yn)

        else:
            yn = int(ly)

            if yn == 14:
                yn = 1.25
            elif yn == 15:
                yn = 1.20
            elif yn == 16:
                yn = 1.15
            elif yn == 17:
                yn = 1.10
            elif yn == 18:
                yn = 1.05
            elif yn == 19:
                yn = 1
            elif yn > 19:
                yn = (195 / 100) - ((5 / 100) * yn)

        yc = (14 / 10)

        Nd = float(nk) * float(yc) * float(yn)

        # 2Indicie Esbeltez

        ybelt_x = (346 / 100) * (int(lex) / int(ly))
        ybelt_y = (346 / 100) * (int(ley) / int(lx))

        # 3 Mdin Momento Segunda Ordem

        dinx = (3 / 100) * int(lx)
        diny = (3 / 100) * int(ly)

        mdinx = Nd * ((15 / 10) + dinx)
        mdiny = Nd * ((15 / 10) + diny)

        # Esbeltez Minima

        esbelt_min = 25

        # Momento de 2° Ordem

        Ac = int(lx) * int(ly)

        fcd = (int(CX) / 10) / (14 / 10)

        Yv = float(Nd) / (int(Ac) * float(fcd))

        r1x = 0
        r2x = 0
        r1y = 0
        r2y = 0

        r1x = (5 / 1000) / (int(lx) * (float(Yv) + (5 / 10)))
        r2x = (5 / 1000) / int(lx)

        if r1x < r2x:
            r1_final = r1x
        elif r2x < r1x:
            r1_final = r2x

        if ybelt_x < esbelt_min:
            e2x_final = float(((int(lex) ** 2) / 10) * float(r1_final))

        else:
            e2x_final = 0

        r1y = (5 / 1000) / (int(ly) * (float(Yv) + (5 / 10)))
        r2y = (5 / 1000) / int(ly)

        if r1y < r2y:
            r2_final = r1y
        elif r2y < r1y:
            r2_final = r2y

        if ybelt_y < esbelt_min:
            e2y_final = float(((int(ley) ** 2) / 10) * int(r2_final))

        else:
            e2y_final = 0

        mdtotx = mdinx + (float(Nd) * float(e2x_final))
        mdtoty = mdiny + (float(Nd) * float(e2y_final))

        miX = mdtotx / (int(lx) * int(Ac) * float(fcd))
        miY = mdtoty / (int(ly) * int(Ac) * float(fcd))

        # mylbl = Label(root, text="miX = " + str(miY) + " miX = " + str(mdtotx) + " fcd " + str(mdinx) + " CX " + str(
        #    Nd) + " ex " + str(e2x_final))
        # mylbl.grid(row=3, column=0)

        frame4()
        frame5()
        frame6()

    global pilar_png

    # FRAME 1

    frame1 = Toplevel()
    frame1.title('3- Pilar de extremidade')
    frame1.iconbitmap("C:\Banco Dados/castello.ico")

    frame = LabelFrame(frame1, text='Qual o tipo de Concreto')
    frame.grid(row=0, column=0, ipadx=11, pady=4, stick=N)

    MODE = [

        ("20", 20),
        ("25", 25),
        ("30", 30),
        ("35", 35),
        ("40", 40),
        ("50", 50),

    ]

    r_cong = StringVar()
    r_cong.set("20")

    for text, mode in MODE:
        Radiobutton(frame, text=text, variable=r_cong, value=mode).pack(anchor=W)

    # FRAME 2

    frame2 = LabelFrame(frame1, text='Dados do Pilar ')
    frame2.grid(row=1, column=0, padx=10, pady=2, ipady=2)

    lb_nk = Label(frame2, text='Valor de NK: ')
    lb_nk.grid(row=0, column=0)

    entry_nk = Entry(frame2, width=10)
    entry_nk.grid(row=0, column=1, padx=10, sticky=W)

    lb_lx = Label(frame2, text='Valor de lX: ')
    lb_lx.grid(row=1, column=0, sticky=W)

    entry_lx = Entry(frame2, width=10)
    entry_lx.grid(row=1, column=1)

    lb_ly = Label(frame2, text='Valor de lY: ')
    lb_ly.grid(row=2, column=0, sticky=W)

    entry_ly = Entry(frame2, width=10)
    entry_ly.grid(row=2, column=1)

    lb_lex = Label(frame2, text="Valor de leX")
    lb_lex.grid(row=3, column=0, sticky=W)

    entry_lex = Entry(frame2, width=10)
    entry_lex.grid(row=3, column=1)

    lb_ley = Label(frame2, text="Valor de leY")
    lb_ley.grid(row=4, column=0, sticky=W)

    entry_ley = Entry(frame2, width=10)
    entry_ley.grid(row=4, column=1)

    # END FRAME 2

    btn = Button(frame2, text="VALIDAR", command=calc, width=20, borderwidth=2)
    btn.grid(row=5, column=0, pady=7, ipadx=2, columnspan=3, sticky=N + S)

    # FRAME 3

    frame3 = LabelFrame(frame1, text='Pilar Exemplar ')
    frame3.grid(row=0, column=1, padx=5, pady=10, ipady=4, ipadx=11, sticky=W + E + N + S)

    pilar_png = ImageTk.PhotoImage(Image.open("C:\Banco Dados/pilar.png"))
    image_pilar = Label(frame3, image=pilar_png)
    image_pilar.pack(anchor=CENTER)


def p4():
    frame1 = Toplevel()
    frame1.title('4- Correção de laje')
    frame1.iconbitmap("C:\Banco Dados/castello.ico")

    def calc_correcao():
        frame3 = LabelFrame(frame1, text='Correção das Cargas')
        frame3.grid(row=2, column=0, padx=10, pady=2, ipady=2)

        S_carga: int = (r_cong.get())
        sc = S_carga
        pp_1: int = (entry_pp.get())
        pp1 = pp_1
        pp_2: int = (entry_pp2.get())
        pp2 = pp_2

        pp1c = int(pp1) * 25

        sc1 = int(sc) + int(pp1c) + int(pp2) + 50

        # qcarga = int(sc) + int(pp1c) + int(pp2) + 50

        lb_pp1 = Label(frame3, text='VALOR CARGA CORRIGIDA {} Kgf/m²'.format(sc1))
        lb_pp1.grid(row=0, column=0, sticky=W)

    frame = LabelFrame(frame1, text='Qual o tipo de Concreto')
    frame.grid(row=0, column=0, ipadx=11, pady=4, padx=5, stick=N)

    MODE = [

        ("Engastada", 150),
        ("Balanço", 400),
        ("Banheiro ou Cozinha", 200),

    ]

    r_cong = StringVar()
    r_cong.set("20")

    for text, mode in MODE:
        Radiobutton(frame, text=text, variable=r_cong, value=mode).pack(anchor=W)

        frame2 = LabelFrame(frame1, text='Valores Reservatórios')
        frame2.grid(row=1, column=0, padx=10, pady=2, ipady=2)

        lb_pp1 = Label(frame2, text='Altura da laje em cm ')
        lb_pp1.grid(row=0, column=0, sticky=W)

        entry_pp = Entry(frame2, width=10)
        entry_pp.grid(row=0, column=1, padx=10, sticky=W)

        lb_p2 = Label(frame2, text='Peso da parede  ')
        lb_p2.grid(row=1, column=0, sticky=W)

        entry_pp2 = Entry(frame2, width=10)
        entry_pp2.grid(row=1, column=1, padx=10, sticky=W)

        btn = Button(frame2, text="VALIDAR", width=20, borderwidth=2, command=calc_correcao)
        btn.grid(row=2, column=0, pady=7, ipadx=2, columnspan=3, sticky=N + S)


my_image1 = ImageTk.PhotoImage(Image.open("C:\Banco Dados/FOTOMENU.jpg"))


my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3, pady=5)

# Create a Label

my_icon = Label(image=my_image1)
my_icon.grid(row=0, column=0, columnspan=3)

# Create A button

btn1 = Button(root, text='1- Controle de consumo', command=p1)
btn2 = Button(root, text='2- Correção de momentos', command=p2)
btn3 = Button(root, text='3- Pilar de extremidade', command=p3)
btn4 = Button(root, text='4- Correção de carga', command=p4)

# Position button

btn1.grid(row=1, column=0, ipadx=12, ipady=1, pady=10, padx=10)
btn2.grid(row=1, column=1, ipadx=12, ipady=1, pady=10, padx=10)
btn3.grid(row=2, column=0, ipadx=18, ipady=1, pady=10, padx=10)
btn4.grid(row=2, column=1, ipadx=22, ipady=1, pady=10, padx=10)

root.mainloop()