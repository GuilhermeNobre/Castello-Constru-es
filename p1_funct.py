from tkinter import *

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

