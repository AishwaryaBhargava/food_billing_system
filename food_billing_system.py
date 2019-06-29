from tkinter import *
import time
import datetime
import random
from tkinter import messagebox

root = Tk()          #Creates the window

root.title("Food Billing System")
root.configure(background='#ff8a65')

Tops = Frame(root,bg='#ff8a65',bd=15,pady=0,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',30,'bold'),text='Food Billing System',bg='black',fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='#ff8a65',bd=10)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='#ff8a65',bd=3)
Buttons_F.pack(side=BOTTOM)

Receipt_F=Frame(ReceiptCal_F,bg='#ff8a65',bd=4)
Receipt_F.pack(side=TOP)

MenuFrame = Frame(root,bg='#ff8a65',bd=10)
MenuFrame.pack(side=LEFT)

Cost_F=Frame(MenuFrame,bg='#ff8a65',bd=4)
Cost_F.pack(side=BOTTOM)

Name_F=Frame(MenuFrame,bg='#ff8a65',bd=4)
Name_F.pack()

Sweets_F=Frame(MenuFrame,bg='#ff8a65',bd=4)
Sweets_F.pack(side=LEFT)

Namkeens_F=Frame(MenuFrame,bg='#ff8a65',bd=4)
Namkeens_F.pack(side=LEFT)

AchaarAndChutneys_F=Frame(MenuFrame,bg='#ff8a65',bd=4)
AchaarAndChutneys_F.pack(side=BOTTOM)

####################################################################### variables #####################################################################################

DateOfDelivery = StringVar()
Receipt_Ref = StringVar()
TotalCost = StringVar()

E_NameOfCustomer = StringVar()

PriceOfSweets = StringVar()
PriceOfNamkeens = StringVar()
PriceOfAchaarAndChutney = StringVar()

CostOfSweets = StringVar()
CostOfNamkeens = StringVar()
CostOfAchaarAndChutney = StringVar()

text_Input = StringVar()
operator = ""

##### SWEETS #####

var1=DoubleVar()
var2=DoubleVar()
var3=DoubleVar()
var4=DoubleVar()
var5=DoubleVar()
var6=DoubleVar()
var7=DoubleVar()
var8=DoubleVar()
var9=DoubleVar()
var10=DoubleVar()
var11=DoubleVar()
var12=DoubleVar()
var13=DoubleVar()
var14=DoubleVar()
var15=DoubleVar()

E_GondKeLadduInDesiGhee = StringVar()
E_MethiKeLadduInDesiGhee = StringVar()
E_BesanKeLadduInDesiGhee = StringVar()
E_BesanKeModakInDesiGhee = StringVar()
E_TilKeLadduInDesiGhee = StringVar()
E_ShakkarParaInDesiGhee = StringVar()
E_GudParaInDesiGhee = StringVar()
E_MithiMathriInDesiGhee = StringVar()
E_GunjiyaInDesiGhee = StringVar()
E_GunjiyaInDesiGheeWithoutChasniCoat = StringVar()
E_MisriMawa = StringVar()
E_TilMawaLadduBarfi = StringVar()
E_GajjarKaHalwaInDesiGhee = StringVar()
E_BikaneriGondPakInDesiGhee = StringVar()
E_ShakkarParaInRefinedOil = StringVar()

E_GondKeLadduInDesiGhee.set("0")
E_MethiKeLadduInDesiGhee.set("0")
E_BesanKeLadduInDesiGhee.set("0")
E_BesanKeModakInDesiGhee.set("0")
E_TilKeLadduInDesiGhee.set("0")
E_ShakkarParaInDesiGhee.set("0")
E_GudParaInDesiGhee.set("0")
E_MithiMathriInDesiGhee.set("0")
E_GunjiyaInDesiGhee.set("0")
E_GunjiyaInDesiGheeWithoutChasniCoat.set("0")
E_MisriMawa.set("0")
E_TilMawaLadduBarfi.set("0")
E_GajjarKaHalwaInDesiGhee.set("0")
E_BikaneriGondPakInDesiGhee.set("0")
E_ShakkarParaInRefinedOil.set("0")

##### NAMKEENS #####

var18=DoubleVar()
var19=DoubleVar()
var20=DoubleVar()
var21=DoubleVar()
var22=DoubleVar()
var23=DoubleVar()
var24=DoubleVar()
var25=DoubleVar()
var26=DoubleVar()
var27=DoubleVar()
var28=DoubleVar()
var29=DoubleVar()
var30=DoubleVar()
var31=DoubleVar()

E_SangeetaSpecialBesanKiKachori = StringVar()
E_MoongDalKiKachori = StringVar()
E_Mathri = StringVar()
E_AttaMathri = StringVar()
E_MethiMathri = StringVar()
E_AttaMethiMathri = StringVar()
E_BinaMirchKiChakli = StringVar()
E_MasalaChakli = StringVar()
E_PapdiForChaat = StringVar()
E_NamkeenPara = StringVar()
E_AttaNamkeenPara = StringVar()
E_MasalaNamkeenPara = StringVar()
E_NamkeenSankhiye = StringVar()
E_RoastedChirwa = StringVar()

E_SangeetaSpecialBesanKiKachori.set("0")
E_MoongDalKiKachori.set("0")
E_Mathri.set("0")
E_AttaMathri.set("0")
E_MethiMathri.set("0")
E_AttaMethiMathri.set("0")
E_BinaMirchKiChakli.set("0")
E_MasalaChakli.set("0")
E_PapdiForChaat.set("0")
E_NamkeenPara.set("0")
E_AttaNamkeenPara.set("0")
E_MasalaNamkeenPara.set("0")
E_NamkeenSankhiye.set("0")
E_RoastedChirwa.set("0")

##### ACHAAR AND CHUTNEYS'S #####

var49=DoubleVar()
var50=DoubleVar()
var51=DoubleVar()
var52=DoubleVar()
var53=DoubleVar()
var54=DoubleVar()
var55=DoubleVar()
var57=DoubleVar()
var58=DoubleVar()
var59=DoubleVar()
var60=DoubleVar()
var62=DoubleVar()
var63=DoubleVar()
var64=DoubleVar()

E_ChanneKaAchaar = StringVar()
E_GobhiGajjarKaAchaar = StringVar()
E_HeengAamKaAchaar = StringVar()
E_LasodaKaAchaar = StringVar()
E_AamKaAchaar = StringVar()
E_MirchNimbuKaAchaar = StringVar()
E_MeethaNimbuKaAchaar = StringVar()
E_AmchoorKiChatni = StringVar()
E_DhaniyeKiChatni = StringVar()
E_ImliKiChatni = StringVar()
E_LehsunKiChatni = StringVar()
E_NariyalKiChatni = StringVar()
E_PodinaKiChatni = StringVar()
E_TangyMayoCheeseDip = StringVar()

E_ChanneKaAchaar.set("0")
E_GobhiGajjarKaAchaar.set("0")
E_HeengAamKaAchaar.set("0")
E_LasodaKaAchaar.set("0")
E_AamKaAchaar.set("0")
E_MirchNimbuKaAchaar.set("0")
E_MeethaNimbuKaAchaar.set("0")
E_AmchoorKiChatni.set("0")
E_DhaniyeKiChatni.set("0")
E_ImliKiChatni.set("0")
E_LehsunKiChatni.set("0")
E_NariyalKiChatni.set("0")
E_PodinaKiChatni.set("0")
E_TangyMayoCheeseDip.set("0")

DateOfDelivery.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################


def Reset():

    TotalCost.set("")

    E_NameOfCustomer.set("")
    
    PriceOfSweets.set("")
    PriceOfNamkeens.set("")
    PriceOfAchaarAndChutney.set("")
    
    txtReceipt.delete("1.0",END)


    ##### SWEETS #####
    E_GondKeLadduInDesiGhee.set("0")
    E_MethiKeLadduInDesiGhee.set("0")
    E_BesanKeLadduInDesiGhee.set("0")
    E_BesanKeModakInDesiGhee.set("0")
    E_TilKeLadduInDesiGhee.set("0")
    E_ShakkarParaInDesiGhee.set("0")
    E_GudParaInDesiGhee.set("0")
    E_MithiMathriInDesiGhee.set("0")
    E_GunjiyaInDesiGhee.set("0")
    E_GunjiyaInDesiGheeWithoutChasniCoat.set("0")
    E_MisriMawa.set("0")
    E_TilMawaLadduBarfi.set("0")
    E_GajjarKaHalwaInDesiGhee.set("0")
    E_BikaneriGondPakInDesiGhee.set("0")
    E_ShakkarParaInRefinedOil.set("0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)

    ##### NAMKEENS #####
    E_SangeetaSpecialBesanKiKachori.set("0")
    E_MoongDalKiKachori.set("0")
    E_Mathri.set("0")
    E_AttaMathri.set("0")
    E_MethiMathri.set("0")
    E_AttaMethiMathri.set("0")
    E_BinaMirchKiChakli.set("0")
    E_MasalaChakli.set("0")
    E_PapdiForChaat.set("0")
    E_NamkeenPara.set("0")
    E_AttaNamkeenPara.set("0")
    E_MasalaNamkeenPara.set("0")
    E_NamkeenSankhiye.set("0")
    E_RoastedChirwa.set("0")
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)

    ##### ACHAAR AND CHUTNEY'S #####
    E_ChanneKaAchaar.set("0")
    E_GobhiGajjarKaAchaar.set("0")
    E_HeengAamKaAchaar.set("0")
    E_LasodaKaAchaar.set("0")
    E_AamKaAchaar.set("0")
    E_MirchNimbuKaAchaar.set("0")
    E_MeethaNimbuKaAchaar.set("0")
    E_AmchoorKiChatni.set("0")
    E_DhaniyeKiChatni.set("0")
    E_ImliKiChatni.set("0")
    E_LehsunKiChatni.set("0")
    E_NariyalKiChatni.set("0")
    E_PodinaKiChatni.set("0")
    E_TangyMayoCheeseDip.set("0")
    var49.set(0)
    var50.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var57.set(0)
    var58.set(0)
    var59.set(0)
    var60.set(0)
    var62.set(0)
    var63.set(0)
    var64.set(0)

    txtGondKeLadduInDesiGhee.configure(state=DISABLED)
    txtMethiKeLadduInDesiGhee.configure(state=DISABLED)
    txtBesanKeLadduInDesiGhee.configure(state=DISABLED)
    txtBesanKeModakInDesiGhee.configure(state=DISABLED)
    txtTilKeLadduInDesiGhee.configure(state=DISABLED)
    txtShakkarParaInDesiGhee.configure(state=DISABLED)
    txtGudParaInDesiGhee.configure(state=DISABLED)
    txtMithiMathriInDesiGhee.configure(state=DISABLED)
    txtGunjiyaInDesiGhee.configure(state=DISABLED)
    txtGunjiyaInDesiGheeWithoutChasniCoat.configure(state=DISABLED)
    txtMisriMawa.configure(state=DISABLED)
    txtTilMawaLadduBarfi.configure(state=DISABLED)
    txtGajjarKaHalwaInDesiGhee.configure(state=DISABLED)
    txtBikaneriGondPakInDesiGhee.configure(state=DISABLED)
    txtShakkarParaInRefinedOil.configure(state=DISABLED)

    txtSangeetaSpecialBesanKiKachori.configure(state=DISABLED)
    txtMoongDalKiKachori.configure(state=DISABLED)
    txtMathri.configure(state=DISABLED)
    txtAttaMathri.configure(state=DISABLED)
    txtMethiMathri.configure(state=DISABLED)
    txtAttaMethiMathri.configure(state=DISABLED)
    txtBinaMirchKiChakli.configure(state=DISABLED)
    txtMasalaChakli.configure(state=DISABLED)
    txtPapdiForChaat.configure(state=DISABLED)
    txtNamkeenPara.configure(state=DISABLED)
    txtAttaNamkeenPara.configure(state=DISABLED)
    txtMasalaNamkeenPara.configure(state=DISABLED)
    txtNamkeenSankhiye.configure(state=DISABLED)
    txtRoastedChirwa.configure(state=DISABLED)

    txtChanneKaAchaar.configure(state=DISABLED)
    txtGobhiGajjarKaAchaar.configure(state=DISABLED)
    txtHeengAamKaAchaar.configure(state=DISABLED)
    txtLasodaKaAchaar.configure(state=DISABLED)
    txtAamKaAchaar.configure(state=DISABLED)
    txtMirchNimbuKaAchaar.configure(state=DISABLED)
    txtMeethaNimbuKaAchaar.configure(state=DISABLED)
    txtAmchoorKiChatni.configure(state=DISABLED)
    txtDhaniyeKiChatni.configure(state=DISABLED)
    txtImliKiChatni.configure(state=DISABLED)
    txtLehsunKiChatni.configure(state=DISABLED)
    txtNariyalKiChatni.configure(state=DISABLED)
    txtPodinaKiChatni.configure(state=DISABLED)
    txtTangyMayoCheeseDip.configure(state=DISABLED)


def CostOfItem():
    
    ##### SWEETS #####
    Item1 = float(E_GondKeLadduInDesiGhee.get())
    Item2 = float(E_MethiKeLadduInDesiGhee.get())
    Item3 = float(E_BesanKeLadduInDesiGhee.get())
    Item4 = float(E_BesanKeModakInDesiGhee.get())
    Item5 = float(E_TilKeLadduInDesiGhee.get())
    Item6 = float(E_ShakkarParaInDesiGhee.get())
    Item7 = float(E_GudParaInDesiGhee.get())
    Item8 = float(E_MithiMathriInDesiGhee.get())
    Item9 = float(E_GunjiyaInDesiGhee.get())
    Item10 = float(E_GunjiyaInDesiGheeWithoutChasniCoat.get())
    Item11 = float(E_MisriMawa.get())
    Item12 = float(E_TilMawaLadduBarfi.get())
    Item13 = float(E_GajjarKaHalwaInDesiGhee.get())
    Item14 = float(E_BikaneriGondPakInDesiGhee.get())
    Item15 = float(E_ShakkarParaInRefinedOil.get())

    ##### NAMKEENS #####
    Item18 = float(E_SangeetaSpecialBesanKiKachori.get())
    Item19 = float(E_MoongDalKiKachori.get())
    Item20 = float(E_Mathri.get())
    Item21 = float(E_AttaMathri.get())
    Item22 = float(E_MethiMathri.get())
    Item23 = float(E_AttaMethiMathri.get())
    Item24 = float(E_BinaMirchKiChakli.get())
    Item25 = float(E_MasalaChakli.get())
    Item26 = float(E_PapdiForChaat.get())
    Item27 = float(E_NamkeenPara.get())
    Item28 = float(E_AttaNamkeenPara.get())
    Item29 = float(E_MasalaNamkeenPara.get())
    Item30 = float(E_NamkeenSankhiye.get())
    Item31 = float(E_RoastedChirwa.get())

    ##### ACHAAR AND CHUTNEY'S #####
    Item49 = float(E_ChanneKaAchaar.get())
    Item50 = float(E_GobhiGajjarKaAchaar.get())
    Item51 = float(E_HeengAamKaAchaar.get())
    Item52 = float(E_LasodaKaAchaar.get())
    Item53 = float(E_AamKaAchaar.get())
    Item54 = float(E_MirchNimbuKaAchaar.get())
    Item55 = float(E_MeethaNimbuKaAchaar.get())
    Item57 = float(E_AmchoorKiChatni.get())
    Item58 = float(E_DhaniyeKiChatni.get())
    Item59 = float(E_ImliKiChatni.get())
    Item60 = float(E_LehsunKiChatni.get())
    Item62 = float(E_NariyalKiChatni.get())
    Item63 = float(E_PodinaKiChatni.get())
    Item64 = float(E_TangyMayoCheeseDip.get())

    ##### PRICE OF SUB-SECTIONS #####
    PriceOfSweets = (Item1 * 560) + (Item2 * 660) + (Item3 * 500) + (Item4 * 520) + (Item5 * 400) + (Item6 * 500) + (Item7 * 520) + (Item8 * 540) + (Item9 * 500) + (Item10 * 550) + (Item11 * 460) + (Item12 * 520) + (Item13 * 480) + (Item14 * 700) + (Item15 * 300)
    PriceOfNamkeens = (Item18 * 360) + (Item19 * 380) + (Item20 * 300) + (Item21 * 320) + (Item22 * 360) + (Item23 * 380) + (Item24 * 300) + (Item25 * 300) + (Item26 * 300) + (Item27 * 300) + (Item28 * 340) + (Item29 * 360) + (Item30 * 300) + (Item31 * 300)
    PriceOfAchaarAndChutney = (Item49 * 300) + (Item50 * 360) + (Item51 * 360) + (Item52 * 360) + (Item53 * 360) + (Item54 * 300) + (Item55 * 300) + (Item57 * 800) + (Item58 * 800) + (Item59 * 800) + (Item60 * 800) + (Item62 * 800) + (Item63 * 800) + (Item64 * 1400)
   
    SweetsPrice = "Rs",str('%.2f'%(PriceOfSweets))
    NamkeensPrice = "Rs",str('%.2f'%(PriceOfNamkeens))
    AchaarAndChutneyPrice = "Rs",str('%.2f'%(PriceOfAchaarAndChutney))

    CostOfSweets.set(SweetsPrice)
    CostOfNamkeens.set(NamkeensPrice)
    CostOfAchaarAndChutney.set(AchaarAndChutneyPrice)

    TC = "Rs",str('%.2f'%(PriceOfSweets + PriceOfNamkeens + PriceOfAchaarAndChutney))
    TotalCost.set(TC)



##### SWEETS #####
def chkGondKeLadduInDesiGhee():
    if(var1.get() == 1):
        txtGondKeLadduInDesiGhee.configure(state = NORMAL)
        txtGondKeLadduInDesiGhee.focus()
        txtGondKeLadduInDesiGhee.delete('0',END)
        E_GondKeLadduInDesiGhee.set("")
    elif(var1.get() == 0):
        txtGondKeLadduInDesiGhee.configure(state = DISABLED)
        E_GondKeLadduInDesiGhee.set("0")

def chkMethiKeLadduInDesiGhee():
    if(var2.get() == 1):
        txtMethiKeLadduInDesiGhee.configure(state = NORMAL)
        txtMethiKeLadduInDesiGhee.focus()
        txtMethiKeLadduInDesiGhee.delete('0',END)
        E_MethiKeLadduInDesiGhee.set("")
    elif(var2.get() == 0):
        txtMethiKeLadduInDesiGhee.configure(state = DISABLED)
        E_MethiKeLadduInDesiGhee.set("0")

def chkBesanKeLadduInDesiGhee():
    if(var3.get() == 1):
        txtBesanKeLadduInDesiGhee.configure(state = NORMAL)
        txtBesanKeLadduInDesiGhee.focus()
        txtBesanKeLadduInDesiGhee.delete('0',END)
        E_BesanKeLadduInDesiGhee.set("")
    elif(var3.get() == 0):
        txtBesanKeLadduInDesiGhee.configure(state = DISABLED)
        E_BesanKeLadduInDesiGhee.set("0")

def chkBesanKeModakInDesiGhee():
    if(var4.get() == 1):
        txtBesanKeModakInDesiGhee.configure(state = NORMAL)
        txtBesanKeModakInDesiGhee.focus()
        txtBesanKeModakInDesiGhee.delete('0',END)
        E_BesanKeModakInDesiGhee.set("")
    elif(var4.get() == 0):
        txtBesanKeModakInDesiGhee.configure(state = DISABLED)
        E_BesanKeModakInDesiGhee.set("0")

def chkTilKeLadduInDesiGhee():
    if(var5.get() == 1):
        txtTilKeLadduInDesiGhee.configure(state = NORMAL)
        txtTilKeLadduInDesiGhee.focus()
        txtTilKeLadduInDesiGhee.delete('0',END)
        E_TilKeLadduInDesiGhee.set("")
    elif(var5.get() == 0):
        txtTilKeLadduInDesiGhee.configure(state = DISABLED)
        E_TilKeLadduInDesiGhee.set("0")

def chkShakkarParaInDesiGhee():
    if(var6.get() == 1):
        txtShakkarParaInDesiGhee.configure(state = NORMAL)
        txtShakkarParaInDesiGhee.focus()
        txtShakkarParaInDesiGhee.delete('0',END)
        E_ShakkarParaInDesiGhee.set("")
    elif(var6.get() == 0):
        txtShakkarParaInDesiGhee.configure(state = DISABLED)
        E_ShakkarParaInDesiGhee.set("0")

def chkGudParaInDesiGhee():
    if(var7.get() == 1):
        txtGudParaInDesiGhee.configure(state = NORMAL)
        txtGudParaInDesiGhee.focus()
        txtGudParaInDesiGhee.delete('0',END)
        E_GudParaInDesiGhee.set("")
    elif(var7.get() == 0):
        txtGudParaInDesiGhee.configure(state = DISABLED)
        E_GudParaInDesiGhee.set("0")

def chkMithiMathriInDesiGhee():
    if(var8.get() == 1):
        txtMithiMathriInDesiGhee.configure(state = NORMAL)
        txtMithiMathriInDesiGhee.focus()
        txtMithiMathriInDesiGhee.delete('0',END)
        E_MithiMathriInDesiGhee.set("")
    elif(var8.get() == 0):
        txtMithiMathriInDesiGhee.configure(state = DISABLED)
        E_MithiMathriInDesiGhee.set("0")

def chkGunjiyaInDesiGhee():
    if(var9.get() == 1):
        txtGunjiyaInDesiGhee.configure(state = NORMAL)
        txtGunjiyaInDesiGhee.focus()
        txtGunjiyaInDesiGhee.delete('0',END)
        E_GunjiyaInDesiGhee.set("")
    elif(var9.get() == 0):
        txtGunjiyaInDesiGhee.configure(state = DISABLED)
        E_GunjiyaInDesiGhee.set("0")

def chkGunjiyaInDesiGheeWithoutChasniCoat():
    if(var10.get() == 1):
        txtGunjiyaInDesiGheeWithoutChasniCoat.configure(state = NORMAL)
        txtGunjiyaInDesiGheeWithoutChasniCoat.focus()
        txtGunjiyaInDesiGheeWithoutChasniCoat.delete('0',END)
        E_GunjiyaInDesiGheeWithoutChasniCoat.set("")
    elif(var10.get() == 0):
        txtGunjiyaInDesiGheeWithoutChasniCoat.configure(state = DISABLED)
        E_GunjiyaInDesiGheeWithoutChasniCoat.set("0")

def chkMisriMawa():
    if(var11.get() == 1):
        txtMisriMawa.configure(state = NORMAL)
        txtMisriMawa.focus()
        txtMisriMawa.delete('0',END)
        E_MisriMawa.set("")
    elif(var11.get() == 0):
        txtMisriMawa.configure(state = DISABLED)
        E_MisriMawa.set("0")

def chkTilMawaLadduBarfi():
    if(var12.get() == 1):
        txtTilMawaLadduBarfi.configure(state = NORMAL)
        txtTilMawaLadduBarfi.focus()
        txtTilMawaLadduBarfi.delete('0',END)
        E_TilMawaLadduBarfi.set("")
    elif(var12.get() == 0):
        txtTilMawaLadduBarfi.configure(state = DISABLED)
        E_TilMawaLadduBarfi.set("0")

def chkGajjarKaHalwaInDesiGhee():
    if(var13.get() == 1):
        txtGajjarKaHalwaInDesiGhee.configure(state = NORMAL)
        txtGajjarKaHalwaInDesiGhee.focus()
        txtGajjarKaHalwaInDesiGhee.delete('0',END)
        E_GajjarKaHalwaInDesiGhee.set("")
    elif(var13.get() == 0):
        txtGajjarKaHalwaInDesiGhee.configure(state = DISABLED)
        E_GajjarKaHalwaInDesiGhee.set("0")

def chkBikaneriGondPakInDesiGhee():
    if(var14.get() == 1):
        txtBikaneriGondPakInDesiGhee.configure(state = NORMAL)
        txtBikaneriGondPakInDesiGhee.focus()
        txtBikaneriGondPakInDesiGhee.delete('0',END)
        E_BikaneriGondPakInDesiGhee.set("")
    elif(var14.get() == 0):
        txtBikaneriGondPakInDesiGhee.configure(state = DISABLED)
        E_BikaneriGondPakInDesiGhee.set("0")

def chkShakkarParaInRefinedOil():
    if(var15.get() == 1):
        txtShakkarParaInRefinedOil.configure(state = NORMAL)
        txtShakkarParaInRefinedOil.focus()
        txtShakkarParaInRefinedOil.delete('0',END)
        E_ShakkarParaInRefinedOil.set("")
    elif(var15.get() == 0):
        txtShakkarParaInRefinedOil.configure(state = DISABLED)
        E_ShakkarParaInRefinedOil.set("0")


##### NAMKEENS #####
def chkSangeetaSpecialBesanKiKachori():
    if(var18.get() == 1):
        txtSangeetaSpecialBesanKiKachori.configure(state = NORMAL)
        txtSangeetaSpecialBesanKiKachori.focus()
        txtSangeetaSpecialBesanKiKachori.delete('0',END)
        E_SangeetaSpecialBesanKiKachori.set("")
    elif(var18.get() == 0):
        txtSangeetaSpecialBesanKiKachori.configure(state = DISABLED)
        E_SangeetaSpecialBesanKiKachori.set("0")

def chkMoongDalKiKachori():
    if(var19.get() == 1):
        txtMoongDalKiKachori.configure(state = NORMAL)
        txtMoongDalKiKachori.focus()
        txtMoongDalKiKachori.delete('0',END)
        E_MoongDalKiKachori.set("")
    elif(var19.get() == 0):
        txtMoongDalKiKachori.configure(state = DISABLED)
        E_MoongDalKiKachori.set("0")

def chkMathri():
    if(var20.get() == 1):
        txtMathri.configure(state = NORMAL)
        txtMathri.focus()
        txtMathri.delete('0',END)
        E_Mathri.set("")
    elif(var20.get() == 0):
        txtMathri.configure(state = DISABLED)
        E_Mathri.set("0")

def chkAttaMathri():
    if(var21.get() == 1):
        txtAttaMathri.configure(state = NORMAL)
        txtAttaMathri.focus()
        txtAttaMathri.delete('0',END)
        E_AttaMathri.set("")
    elif(var21.get() == 0):
        txtAttaMathri.configure(state = DISABLED)
        E_AttaMathri.set("0")

def chkMethiMathri():
    if(var22.get() == 1):
        txtMethiMathri.configure(state = NORMAL)
        txtMethiMathri.focus()
        txtMethiMathri.delete('0',END)
        E_MethiMathri.set("")
    elif(var22.get() == 0):
        txtMethiMathri.configure(state = DISABLED)
        E_MethiMathri.set("0")

def chkAttaMethiMathri():
    if(var23.get() == 1):
        txtAttaMethiMathri.configure(state = NORMAL)
        txtAttaMethiMathri.focus()
        txtAttaMethiMathri.delete('0',END)
        E_AttaMethiMathri.set("")
    elif(var23.get() == 0):
        txtAttaMethiMathri.configure(state = DISABLED)
        E_AttaMethiMathri.set("0")

def chkBinaMirchKiChakli():
    if(var24.get() == 1):
        txtBinaMirchKiChakli.configure(state = NORMAL)
        txtBinaMirchKiChakli.focus()
        txtBinaMirchKiChakli.delete('0',END)
        E_BinaMirchKiChakli.set("")
    elif(var24.get() == 0):
        txtBinaMirchKiChakli.configure(state = DISABLED)
        E_BinaMirchKiChakli.set("0")

def chkMasalaChakli():
    if(var25.get() == 1):
        txtMasalaChakli.configure(state = NORMAL)
        txtMasalaChakli.focus()
        txtMasalaChakli.delete('0',END)
        E_Sprite.set("")
    elif(var25.get() == 0):
        txtMasalaChakli.configure(state = DISABLED)
        E_MasalaChakli.set("0")

def chkPapdiForChaat():
    if(var26.get() == 1):
        txtPapdiForChaat.configure(state = NORMAL)
        txtPapdiForChaat.focus()
        txtPapdiForChaat.delete('0',END)
        E_PapdiForChaat.set("")
    elif(var26.get() == 0):
        txtPapdiForChaat.configure(state = DISABLED)
        E_PapdiForChaat.set("0")

def chkNamkeenPara():
    if(var27.get() == 1):
        txtNamkeenPara.configure(state = NORMAL)
        txtNamkeenPara.focus()
        txtNamkeenPara.delete('0',END)
        E_NamkeenPara.set("")
    elif(var27.get() == 0):
        txtNamkeenPara.configure(state = DISABLED)
        E_NamkeenPara.set("0")

def chkAttaNamkeenPara():
    if(var28.get() == 1):
        txtAttaNamkeenPara.configure(state = NORMAL)
        txtAttaNamkeenPara.focus()
        txtAttaNamkeenPara.delete('0',END)
        E_AttaNamkeenPara.set("")
    elif(var28.get() == 0):
        txtAttaNamkeenPara.configure(state = DISABLED)
        E_AttaNamkeenPara.set("0")

def chkMasalaNamkeenPara():
    if(var29.get() == 1):
        txtMasalaNamkeenPara.configure(state = NORMAL)
        txtMasalaNamkeenPara.focus()
        txtMasalaNamkeenPara.delete('0',END)
        E_MasalaNamkeenPara.set("")
    elif(var29.get() == 0):
        txtMasalaNamkeenPara.configure(state = DISABLED)
        E_MasalaNamkeenPara.set("0")

def chkNamkeenSankhiye():
    if(var30.get() == 1):
        txtNamkeenSankhiye.configure(state = NORMAL)
        txtNamkeenSankhiye.focus()
        txtNamkeenSankhiye.delete('0',END)
        E_NamkeenSankhiye.set("")
    elif(var30.get() == 0):
        txtNamkeenSankhiye.configure(state = DISABLED)
        E_NamkeenSankhiye.set("0")

def chkRoastedChirwa():
    if(var31.get() == 1):
        txtRoastedChirwa.configure(state = NORMAL)
        txtRoastedChirwa.focus()
        txtRoastedChirwa.delete('0',END)
        E_RoastedChirwa.set("")
    elif(var31.get() == 0):
        txtRoastedChirwa.configure(state = DISABLED)
        E_RoastedChirwa.set("0")


##### ACHAAR AND CHUTNEY'S #####
def chkChanneKaAchaar():
    if(var49.get() == 1):
        txtChanneKaAchaar.configure(state = NORMAL)
        txtChanneKaAchaar.focus()
        txtChanneKaAchaar.delete('0',END)
        E_ChanneKaAchaar.set("")
    elif(var49.get() == 0):
        txtChanneKaAchaar.configure(state = DISABLED)
        E_ChanneKaAchaar.set("0")

def chkGobhiGajjarKaAchaar():
    if(var50.get() == 1):
        txtGobhiGajjarKaAchaar.configure(state = NORMAL)
        txtGobhiGajjarKaAchaar.focus()
        txtGobhiGajjarKaAchaar.delete('0',END)
        E_GobhiGajjarKaAchaar.set("")
    elif(var50.get() == 0):
        txtGobhiGajjarKaAchaar.configure(state = DISABLED)
        E_GobhiGajjarKaAchaar.set("0")

def chkHeengAamKaAchaar():
    if(var51.get() == 1):
        txtHeengAamKaAchaar.configure(state = NORMAL)
        txtHeengAamKaAchaar.focus()
        txtHeengAamKaAchaar.delete('0',END)
        E_HeengAamKaAchaar.set("")
    elif(var51.get() == 0):
        txtHeengAamKaAchaar.configure(state = DISABLED)
        E_HeengAamKaAchaar.set("0")

def chkLasodaKaAchaar():
    if(var52.get() == 1):
        txtLasodaKaAchaar.configure(state = NORMAL)
        txtLasodaKaAchaar.focus()
        txtLasodaKaAchaar.delete('0',END)
        E_LasodaKaAchaar.set("")
    elif(var52.get() == 0):
        txtLasodaKaAchaar.configure(state = DISABLED)
        E_LasodaKaAchaar.set("0")

def chkAamKaAchaar():
    if(var53.get() == 1):
        txtAamKaAchaar.configure(state = NORMAL)
        txtAamKaAchaar.focus()
        txtAamKaAchaar.delete('0',END)
        E_AamKaAchaar.set("")
    elif(var53.get() == 0):
        txtAamKaAchaar.configure(state = DISABLED)
        E_AamKaAchaar.set("0")

def chkMirchNimbuKaAchaar():
    if(var54.get() == 1):
        txtMirchNimbuKaAchaar.configure(state = NORMAL)
        txtMirchNimbuKaAchaar.focus()
        txtMirchNimbuKaAchaar.delete('0',END)
        E_MirchNimbuKaAchaar.set("")
    elif(var54.get() == 0):
        txtMirchNimbuKaAchaar.configure(state = DISABLED)
        E_MirchNimbuKaAchaar.set("0")

def chkMeethaNimbuKaAchaar():
    if(var55.get() == 1):
        txtMeethaNimbuKaAchaar.configure(state = NORMAL)
        txtMeethaNimbuKaAchaar.focus()
        txtMeethaNimbuKaAchaar.delete('0',END)
        E_MeethaNimbuKaAchaar.set("")
    elif(var55.get() == 0):
        txtMeethaNimbuKaAchaar.configure(state = DISABLED)
        E_MeethaNimbuKaAchaar.set("0")

def chkAmchoorKiChatni():
    if(var57.get() == 1):
        txtAmchoorKiChatni.configure(state = NORMAL)
        txtAmchoorKiChatni.focus()
        txtAmchoorKiChatni.delete('0',END)
        E_AmchoorKiChatni.set("")
    elif(var57.get() == 0):
        txtAmchoorKiChatni.configure(state = DISABLED)
        E_AmchoorKiChatni.set("0")

def chkDhaniyeKiChatni():
    if(var58.get() == 1):
        txtDhaniyeKiChatni.configure(state = NORMAL)
        txtDhaniyeKiChatni.focus()
        txtDhaniyeKiChatni.delete('0',END)
        E_DhaniyeKiChatni.set("")
    elif(var58.get() == 0):
        txtDhaniyeKiChatni.configure(state = DISABLED)
        E_DhaniyeKiChatni.set("0")

def chkImliKiChatni():
    if(var59.get() == 1):
        txtImliKiChatni.configure(state = NORMAL)
        txtImliKiChatni.focus()
        txtImliKiChatni.delete('0',END)
        E_ImliKiChatni.set("")
    elif(var59.get() == 0):
        txtImliKiChatni.configure(state = DISABLED)
        E_ImliKiChatni.set("0")

def chkLehsunKiChatni():
    if(var60.get() == 1):
        txtLehsunKiChatni.configure(state = NORMAL)
        txtLehsunKiChatni.focus()
        txtLehsunKiChatni.delete('0',END)
        E_LehsunKiChatni.set("")
    elif(var60.get() == 0):
        txtLehsunKiChatni.configure(state = DISABLED)
        E_LehsunKiChatni.set("0")

def chkNariyalKiChatni():
    if(var62.get() == 1):
        txtNariyalKiChatni.configure(state = NORMAL)
        txtNariyalKiChatni.focus()
        txtNariyalKiChatni.delete('0',END)
        E_NariyalKiChatni.set("")
    elif(var62.get() == 0):
        txtNariyalKiChatni.configure(state = DISABLED)
        E_NariyalKiChatni.set("0")

def chkPodinaKiChatni():
    if(var63.get() == 1):
        txtPodinaKiChatni.configure(state = NORMAL)
        txtPodinaKiChatni.focus()
        txtPodinaKiChatni.delete('0',END)
        E_PodinaKiChatni.set("")
    elif(var63.get() == 0):
        txtPodinaKiChatni.configure(state = DISABLED)
        E_PodinaKiChatni.set("0")

def chkTangyMayoCheeseDip():
    if(var64.get() == 1):
        txtTangyMayoCheeseDip.configure(state = NORMAL)
        txtTangyMayoCheeseDip.focus()
        txtTangyMayoCheeseDip.delete('0',END)
        E_TangyMayoCheeseDip.set("")
    elif(var64.get() == 0):
        txtTangyMayoCheeseDip.configure(state = DISABLED)
        E_TangyMayoCheeseDip.set("0")
        


def Receipt():
    txtReceipt.delete("1.0",END)
    
    name = E_NameOfCustomer.get()

    txtReceipt.insert(END,'Name:\t'+name+'\n')
    txtReceipt.insert(END,'Date:\t' + DateOfDelivery.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Amount of Items\t\t"+"Cost of Items\n")

    ##### SWEETS #####
    if (float(E_GondKeLadduInDesiGhee.get()) != 0) :
        Item1 = float(E_GondKeLadduInDesiGhee.get())
        cost = Item1 * 560
        txtReceipt.insert(END,'Gond Ke Laddu In Desi Ghee:\t\t\t\t\t' + E_GondKeLadduInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MethiKeLadduInDesiGhee.get()) != 0) :
        Item2 = float(E_MethiKeLadduInDesiGhee.get())
        cost = Item2 * 660
        txtReceipt.insert(END,'Methi Ke Laddu In Desi Ghee:\t\t\t\t\t' + E_MethiKeLadduInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_BesanKeLadduInDesiGhee.get()) != 0) :
        Item3 = float(E_BesanKeLadduInDesiGhee.get())
        cost = Item3 * 500
        txtReceipt.insert(END,'Besan Ke Laddu In Desi Ghee:\t\t\t\t\t' + E_BesanKeLadduInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_BesanKeModakInDesiGhee.get()) != 0) :
        Item4 = float(E_BesanKeModakInDesiGhee.get())
        cost = Item4 * 520
        txtReceipt.insert(END,'Besan Ke Modak In Desi Ghee:\t\t\t\t\t' + E_BesanKeModakInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_TilKeLadduInDesiGhee.get()) != 0) :
        Item5 = float(E_TilKeLadduInDesiGhee.get())
        cost = Item5 * 400
        txtReceipt.insert(END,'Til Ke Laddu In Desi Ghee:\t\t\t\t\t' + E_TilKeLadduInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_ShakkarParaInDesiGhee.get()) != 0) :
        Item6 = float(E_ShakkarParaInDesiGhee.get())
        cost = Item6 * 500
        txtReceipt.insert(END,'Shakkar Para In Desi Ghee:\t\t\t\t\t' + E_ShakkarParaInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_GudParaInDesiGhee.get()) != 0) :
        Item7 = float(E_GudParaInDesiGhee.get())
        cost = Item7 * 520
        txtReceipt.insert(END,'Gud Para In Desi Ghee:\t\t\t\t\t' + E_GudParaInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MithiMathriInDesiGhee.get()) != 0) :
        Item8 = float(E_MithiMathriInDesiGhee.get())
        cost = Item8 * 540
        txtReceipt.insert(END,'Mithi Mathri In Desi Ghee:\t\t\t\t\t' + E_MithiMathriInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_GunjiyaInDesiGhee.get()) != 0) :
        Item9 = float(E_GunjiyaInDesiGhee.get())
        cost = Item9 * 500
        txtReceipt.insert(END,'Gunjiya In Desi Ghee:\t\t\t\t\t' + E_GunjiyaInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_GunjiyaInDesiGheeWithoutChasniCoat.get()) != 0) :
        Item10 = float(E_GunjiyaInDesiGheeWithoutChasniCoat.get())
        cost = Item10 * 550
        txtReceipt.insert(END,'Gunjiya In Desi Ghee Without Chasni Coat:\t\t\t\t\t' + E_GunjiyaInDesiGheeWithoutChasniCoat.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MisriMawa.get()) != 0) :
        Item11 = float(E_MisriMawa.get())
        cost = Item11 * 460
        txtReceipt.insert(END,'Misri Mawa:\t\t\t\t\t' + E_MisriMawa.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_TilMawaLadduBarfi.get()) != 0) :
        Item12 = float(E_TilMawaLadduBarfi.get())
        cost = Item12 * 520
        txtReceipt.insert(END,'Til Mawa Laddu/Barfi:\t\t\t\t\t' + E_TilMawaLadduBarfi.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_GajjarKaHalwaInDesiGhee.get()) != 0) :
        Item13 = float(E_GajjarKaHalwaInDesiGhee.get())
        cost = Item13 * 480
        txtReceipt.insert(END,'Gajjar Ka Halwa In Desi Ghee:\t\t\t\t\t' + E_GajjarKaHalwaInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_BikaneriGondPakInDesiGhee.get()) != 0) :
        Item14 = float(E_BikaneriGondPakInDesiGhee.get())
        cost = Item14 * 700
        txtReceipt.insert(END,'Bikaneri Gond Pak In Desi Ghee:\t\t\t\t\t' + E_BikaneriGondPakInDesiGhee.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_ShakkarParaInRefinedOil.get()) != 0) :
        Item15 = float(E_ShakkarParaInRefinedOil.get())
        cost = Item15 * 300
        txtReceipt.insert(END,'Shakkar Para In Refined Oil:\t\t\t\t\t' + E_ShakkarParaInRefinedOil.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    ##### NAMKEENS #####
    if (float(E_SangeetaSpecialBesanKiKachori.get()) != 0) :
        Item18 = float(E_SangeetaSpecialBesanKiKachori.get())
        cost = Item18 * 360
        txtReceipt.insert(END,'Sangeeta Special Besan Ki Kachori:\t\t\t\t\t' + E_SangeetaSpecialBesanKiKachori.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MoongDalKiKachori.get()) != 0) :
        Item19 = float(E_MoongDalKiKachori.get())
        cost = Item19 * 380
        txtReceipt.insert(END,'Moong Dal Ki Kachori:\t\t\t\t\t' + E_MoongDalKiKachori.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_Mathri.get()) != 0) :
        Item20 = float(E_Mathri.get())
        cost = Item20 * 300
        txtReceipt.insert(END,'Mathri:\t\t\t\t\t' + E_Mathri.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_AttaMathri.get()) != 0) :
        Item21 = float(E_AttaMathri.get())
        cost = Item21 * 320
        txtReceipt.insert(END,'Atta Mathri:\t\t\t\t\t' + E_AttaMathri.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MethiMathri.get()) != 0) :
        Item22 = float(E_MethiMathri.get())
        cost = Item22 * 360
        txtReceipt.insert(END,'Methi Mathri:\t\t\t\t\t' + E_MethiMathri.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_AttaMethiMathri.get()) != 0) :
        Item23 = float(E_AttaMethiMathri.get())
        cost = Item23 * 380
        txtReceipt.insert(END,'Atta Methi Mathri:\t\t\t\t\t' + E_AttaMethiMathri.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_BinaMirchKiChakli.get()) != 0) :
        Item24 = float(E_BinaMirchKiChakli.get())
        cost = Item24 * 300
        txtReceipt.insert(END,'Bina Mirch Ki Chakli:\t\t\t\t\t' + E_BinaMirchKiChakli.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MasalaChakli.get()) != 0) :
        Item25 = float(E_MasalaChakli.get())
        cost = Item25 * 300
        txtReceipt.insert(END,'Masala Chakli:\t\t\t\t\t' + E_MasalaChakli.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_PapdiForChaat.get()) != 0) :
        Item26 = float(E_PapdiForChaat.get())
        cost = Item26 * 300
        txtReceipt.insert(END,'Papdi For Chaat:\t\t\t\t\t' + E_PapdiForChaat.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_NamkeenPara.get()) != 0) :
        Item27 = float(E_NamkeenPara.get())
        cost = Item27 * 300
        txtReceipt.insert(END,'Namkeen Para:\t\t\t\t\t' + E_NamkeenPara.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_AttaNamkeenPara.get()) != 0) :
        Item28 = float(E_AttaNamkeenPara.get())
        cost = Item28 * 340
        txtReceipt.insert(END,'Atta Namkeen Para:\t\t\t\t\t' + E_AttaNamkeenPara.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MasalaNamkeenPara.get()) != 0) :
        Item29 = float(E_MasalaNamkeenPara.get())
        cost = Item29 * 360
        txtReceipt.insert(END,'Masala Namkeen Para:\t\t\t\t\t' + E_MasalaNamkeenPara.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_NamkeenSankhiye.get()) != 0) :
        Item30 = float(E_NamkeenSankhiye.get())
        cost = Item30 * 300
        txtReceipt.insert(END,'Namkeen Sankhiye:\t\t\t\t\t' + E_NamkeenSankhiye.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_RoastedChirwa.get()) != 0) :
        Item31 = float(E_RoastedChirwa.get())
        cost = Item31 * 300
        txtReceipt.insert(END,'Roasted Chirwa:\t\t\t\t\t' + E_RoastedChirwa.get() + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    ##### ACHAAR AND CHUTNEY'S #####
    if (float(E_ChanneKaAchaar.get()) != 0) :
        Item49 = float(E_ChanneKaAchaar.get())
        cost = Item49 * 300
        txtReceipt.insert(END,'Channe Ka Achaar:\t\t\t\t\t' + E_ChanneKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_GobhiGajjarKaAchaar.get()) != 0) :
        Item50 = float(E_GobhiGajjarKaAchaar.get())
        cost = Item50 * 360
        txtReceipt.insert(END,'Gobhi Gajjar Ka Achaar:\t\t\t\t\t' + E_GobhiGajjarKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_HeengAamKaAchaar.get()) != 0) :
        Item51 = float(E_HeengAamKaAchaar.get())
        cost = Item51 * 360
        txtReceipt.insert(END,'Heeng Aam Ka Achaar:\t\t\t\t\t' + E_HeengAamKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_LasodaKaAchaar.get()) != 0) :
        Item52 = float(E_LasodaKaAchaar.get())
        cost = Item52 * 360
        txtReceipt.insert(END,'Lasoda Ka Achaar:\t\t\t\t\t' + E_LasodaKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_AamKaAchaar.get()) != 0) :
        Item53 = float(E_AamKaAchaar.get())
        cost = Item53 * 360
        txtReceipt.insert(END,'Aam Ka Achaar:\t\t\t\t\t' + E_AamKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MirchNimbuKaAchaar.get()) != 0) :
        Item54 = float(E_MirchNimbuKaAchaar.get())
        cost = Item54 * 300
        txtReceipt.insert(END,'Mirch Nimbu Ka Achaar:\t\t\t\t\t' + E_MirchNimbuKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_MeethaNimbuKaAchaar.get()) != 0) :
        Item55 = float(E_MeethaNimbuKaAchaar.get())
        cost = Item55 * 300
        txtReceipt.insert(END,'Meetha Nimbu Ka Achaar:\t\t\t\t\t' + E_MeethaNimbuKaAchaar.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_AmchoorKiChatni.get()) != 0) :
        Item57 = float(E_AmchoorKiChatni.get())
        cost = Item57 * 800
        txtReceipt.insert(END,'Amchoor Ki Chatni:\t\t\t\t\t' + E_AmchoorKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_DhaniyeKiChatni.get()) != 0) :
        Item58 = float(E_DhaniyeKiChatni.get())
        cost = Item58 * 800
        txtReceipt.insert(END,'Dhaniye Ki Chatni:\t\t\t\t\t' + E_DhaniyeKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_ImliKiChatni.get()) != 0) :
        Item59 = float(E_ImliKiChatni.get())
        cost = Item59 * 800
        txtReceipt.insert(END,'Imli Ki Chatni:\t\t\t\t\t' + E_ImliKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_LehsunKiChatni.get()) != 0) :
        Item60 = float(E_LehsunKiChatni.get())
        cost = Item60 * 800
        txtReceipt.insert(END,'Lehsun Ki Chatni:\t\t\t\t\t' + E_LehsunKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_NariyalKiChatni.get()) != 0) :
        Item62 = float(E_NariyalKiChatni.get())
        cost = Item62 * 800
        txtReceipt.insert(END,'Nariyal Ki Chatni:\t\t\t\t\t' + E_NariyalKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_PodinaKiChatni.get()) != 0) :
        Item63 = float(E_PodinaKiChatni.get())
        cost = Item63 * 800
        txtReceipt.insert(END,'Podina Ki Chatni:\t\t\t\t\t' + E_PodinaKiChatni.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')

    if (float(E_TangyMayoCheeseDip.get()) != 0) :
        Item64 = float(E_TangyMayoCheeseDip.get())
        cost = Item64 * 1400
        txtReceipt.insert(END,'Tangy Mayo Cheese Dip:\t\t\t\t\t' + E_TangyMayoCheeseDip.get()  + 'kg' +'\t'+ 'Rs.' + str('%.2f'%(cost)) +'\n')


    txtReceipt.insert(END,'\nTotal Cost:\t\t\t\t'+ str(TotalCost.get())+"\n")


##### NAME #####
lblName = Label(Name_F,font=('arial',12,'bold'),text='Customer Name',bg='#ff8a65',bd=7,fg='black',justify=CENTER)
lblName.grid(row=0,column=0)
txtName = Entry(Name_F,bg='white',bd=7,font=('arial',10,'bold'),insertwidth=2,justify=RIGHT,textvariable=E_NameOfCustomer)
txtName.grid(row=0,column=1)

    
##### SWEETS #####
GondKeLadduInDesiGhee = Checkbutton(Sweets_F,text='Gond Ke Laddu In Desi Ghee',variable=var1,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGondKeLadduInDesiGhee).grid(row=0,sticky=W)
MethiKeLadduInDesiGhee = Checkbutton(Sweets_F,text='Methi Ke Laddu In Desi Ghee',variable=var2,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMethiKeLadduInDesiGhee).grid(row=1,sticky=W)
BesanKeLadduInDesiGhee = Checkbutton(Sweets_F,text='Besan Ke Laddu In Desi Ghee',variable=var3,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkBesanKeLadduInDesiGhee).grid(row=2,sticky=W)
BesanKeModakInDesiGhee = Checkbutton(Sweets_F,text='Besan Ke Modak In Desi Ghee',variable=var4,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkBesanKeModakInDesiGhee).grid(row=3,sticky=W)
TilKeLadduInDesiGhee = Checkbutton(Sweets_F,text='Til Ke Laddu In Desi Ghee',variable=var5,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkTilKeLadduInDesiGhee).grid(row=4,sticky=W)
ShakkarParaInDesiGhee = Checkbutton(Sweets_F,text='Shakkar Para In Desi Ghee',variable=var6,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkShakkarParaInDesiGhee).grid(row=5,sticky=W)
GudParaInDesiGhee = Checkbutton(Sweets_F,text='Gud Para In Desi Ghee',variable=var7,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGudParaInDesiGhee).grid(row=6,sticky=W)
MithiMathriInDesiGhee = Checkbutton(Sweets_F,text='Mithi Mathri In Desi Ghee',variable=var8,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMithiMathriInDesiGhee).grid(row=7,sticky=W)
GunjiyaInDesiGhee = Checkbutton(Sweets_F,text='Gunjiya In Desi Ghee',variable=var9,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGunjiyaInDesiGhee).grid(row=8,sticky=W)
GunjiyaInDesiGheeWithoutChasniCoat = Checkbutton(Sweets_F,text='Gunjiya In Desi Ghee Without Chasni Coat',variable=var10,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGunjiyaInDesiGheeWithoutChasniCoat).grid(row=9,sticky=W)
MisriMawa = Checkbutton(Sweets_F,text='Misri Mawa',variable=var11,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMisriMawa).grid(row=10,sticky=W)
TilMawaLadduBarfi = Checkbutton(Sweets_F,text='Til Mawa Laddu/Barfi',variable=var12,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkTilMawaLadduBarfi).grid(row=11,sticky=W)
GajjarKaHalwaInDesiGhee = Checkbutton(Sweets_F,text='Gajjar Ka Halwa In Desi Ghee',variable=var13,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGajjarKaHalwaInDesiGhee).grid(row=12,sticky=W)
BikaneriGondPakInDesiGhee = Checkbutton(Sweets_F,text='Bikaneri Gond Pak In Desi Ghee',variable=var14,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkBikaneriGondPakInDesiGhee).grid(row=13,sticky=W)
ShakkarParaInRefinedOil = Checkbutton(Sweets_F,text='Shakkar Para In Refined Oil',variable=var15,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkShakkarParaInRefinedOil).grid(row=14,sticky=W)

txtGondKeLadduInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GondKeLadduInDesiGhee)
txtGondKeLadduInDesiGhee.grid(row=0,column=1)
txtMethiKeLadduInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MethiKeLadduInDesiGhee)
txtMethiKeLadduInDesiGhee.grid(row=1,column=1)
txtBesanKeLadduInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_BesanKeLadduInDesiGhee)
txtBesanKeLadduInDesiGhee.grid(row=2,column=1)
txtBesanKeModakInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_BesanKeModakInDesiGhee)
txtBesanKeModakInDesiGhee.grid(row=3,column=1)
txtTilKeLadduInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_TilKeLadduInDesiGhee)
txtTilKeLadduInDesiGhee.grid(row=4,column=1)
txtShakkarParaInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_ShakkarParaInDesiGhee)
txtShakkarParaInDesiGhee.grid(row=5,column=1)
txtGudParaInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GudParaInDesiGhee)
txtGudParaInDesiGhee.grid(row=6,column=1)
txtMithiMathriInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MithiMathriInDesiGhee)
txtMithiMathriInDesiGhee.grid(row=7,column=1)
txtGunjiyaInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GunjiyaInDesiGhee)
txtGunjiyaInDesiGhee.grid(row=8,column=1)
txtGunjiyaInDesiGheeWithoutChasniCoat = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GunjiyaInDesiGheeWithoutChasniCoat)
txtGunjiyaInDesiGheeWithoutChasniCoat.grid(row=9,column=1)
txtMisriMawa = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MisriMawa)
txtMisriMawa.grid(row=10,column=1)
txtTilMawaLadduBarfi = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_TilMawaLadduBarfi)
txtTilMawaLadduBarfi.grid(row=11,column=1)
txtGajjarKaHalwaInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GajjarKaHalwaInDesiGhee)
txtGajjarKaHalwaInDesiGhee.grid(row=12,column=1)
txtBikaneriGondPakInDesiGhee = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_BikaneriGondPakInDesiGhee)
txtBikaneriGondPakInDesiGhee.grid(row=13,column=1)
txtShakkarParaInRefinedOil = Entry(Sweets_F,font=('arial',8,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_ShakkarParaInRefinedOil)
txtShakkarParaInRefinedOil.grid(row=14,column=1)


##### NAMKEENS #####
SangeetaSpecialBesanKiKachori = Checkbutton(Namkeens_F,text='Sangeeta Special Besan Ki Kachori',variable=var18,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkSangeetaSpecialBesanKiKachori).grid(row=0,sticky=W)
MoongDalKiKachori = Checkbutton(Namkeens_F,text='Moong Dal Ki Kachori',variable=var19,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMoongDalKiKachori).grid(row=1,sticky=W)
Mathri = Checkbutton(Namkeens_F,text='Mathri',variable=var20,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMathri).grid(row=2,sticky=W)
AttaMathri = Checkbutton(Namkeens_F,text='Atta Mathri',variable=var21,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkAttaMathri).grid(row=3,sticky=W)
MethiMathri = Checkbutton(Namkeens_F,text='Methi Mathri',variable=var22,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMethiMathri).grid(row=4,sticky=W)
AttaMethiMathri = Checkbutton(Namkeens_F,text='Atta Methi Mathri',variable=var23,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkAttaMethiMathri).grid(row=5,sticky=W)
BinaMirchKiChakli = Checkbutton(Namkeens_F,text='Bina Mirch Ki Chakli',variable=var24,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkBinaMirchKiChakli).grid(row=6,sticky=W)
MasalaChakli = Checkbutton(Namkeens_F,text='Masala Chakli',variable=var25,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMasalaChakli).grid(row=7,sticky=W)
PapdiForChaat = Checkbutton(Namkeens_F,text='Papdi For Chaat',variable=var26,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkPapdiForChaat).grid(row=8,sticky=W)
NamkeenPara = Checkbutton(Namkeens_F,text='Namkeen Para',variable=var27,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkNamkeenPara).grid(row=9,sticky=W)
AttaNamkeenPara = Checkbutton(Namkeens_F,text='Atta Namkeen Para',variable=var28,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkAttaNamkeenPara).grid(row=10,sticky=W)
MasalaNamkeenPara = Checkbutton(Namkeens_F,text='Masala Namkeen Para',variable=var29,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMasalaNamkeenPara).grid(row=11,sticky=W)
NamkeenSankhiye = Checkbutton(Namkeens_F,text='Namkeen Sankhiye',variable=var30,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkNamkeenSankhiye).grid(row=12,sticky=W)
RoastedChirwa = Checkbutton(Namkeens_F,text='Roasted Chirwa',variable=var31,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkRoastedChirwa).grid(row=13,sticky=W)

txtSangeetaSpecialBesanKiKachori = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_SangeetaSpecialBesanKiKachori)
txtSangeetaSpecialBesanKiKachori.grid(row=0,column=1)
txtMoongDalKiKachori = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MoongDalKiKachori)
txtMoongDalKiKachori.grid(row=1,column=1)
txtMathri = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_Mathri)
txtMathri.grid(row=2,column=1)
txtAttaMathri = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_AttaMathri)
txtAttaMathri.grid(row=3,column=1)
txtMethiMathri = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MethiMathri)
txtMethiMathri.grid(row=4,column=1)
txtAttaMethiMathri = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_AttaMethiMathri)
txtAttaMethiMathri.grid(row=5,column=1)
txtBinaMirchKiChakli = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_BinaMirchKiChakli)
txtBinaMirchKiChakli.grid(row=6,column=1)
txtMasalaChakli = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MasalaChakli)
txtMasalaChakli.grid(row=7,column=1)
txtPapdiForChaat = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_PapdiForChaat)
txtPapdiForChaat.grid(row=8,column=1)
txtNamkeenPara = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_NamkeenPara)
txtNamkeenPara.grid(row=9,column=1)
txtAttaNamkeenPara = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_AttaNamkeenPara)
txtAttaNamkeenPara.grid(row=10,column=1)
txtMasalaNamkeenPara = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MasalaNamkeenPara)
txtMasalaNamkeenPara.grid(row=11,column=1)
txtNamkeenSankhiye = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_NamkeenSankhiye)
txtNamkeenSankhiye.grid(row=12,column=1)
txtRoastedChirwa = Entry(Namkeens_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_RoastedChirwa)
txtRoastedChirwa.grid(row=13,column=1)


##### ACHAAR AND CHUTNEY'S #####
ChanneKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Channe Ka Achaar',variable=var49,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkChanneKaAchaar).grid(row=0,sticky=W)
GobhiGajjarKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Gobhi Gajjar Ka Achaar',variable=var50,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkGobhiGajjarKaAchaar).grid(row=1,sticky=W)
HeengAamKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Heeng Aam Ka Achaar',variable=var51,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkHeengAamKaAchaar).grid(row=2,sticky=W)
LasodaKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Lasoda Ka Achaar',variable=var52,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkLasodaKaAchaar).grid(row=3,sticky=W)
AamKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Aam Ka Achaar',variable=var53,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkAamKaAchaar).grid(row=4,sticky=W)
MirchNimbuKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Mirch Nimbu Ka Achaar',variable=var54,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMirchNimbuKaAchaar).grid(row=5,sticky=W)
MeethaNimbuKaAchaar = Checkbutton(AchaarAndChutneys_F,text='Meetha Nimbu Ka Achaar',variable=var55,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkMeethaNimbuKaAchaar).grid(row=6,sticky=W)
AmchoorKiChatni = Checkbutton(AchaarAndChutneys_F,text='Amchoor Ki Chatni',variable=var57,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkAmchoorKiChatni).grid(row=8,sticky=W)
DhaniyeKiChatni = Checkbutton(AchaarAndChutneys_F,text='Dhaniye Ki Chatni',variable=var58,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkDhaniyeKiChatni).grid(row=9,sticky=W)
ImliKiChatni = Checkbutton(AchaarAndChutneys_F,text='Imli Ki Chatni',variable=var59,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkImliKiChatni).grid(row=10,sticky=W)
LehsunKiChatni = Checkbutton(AchaarAndChutneys_F,text='Lehsun Ki Chatni',variable=var60,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkLehsunKiChatni).grid(row=11,sticky=W)
NariyalKiChatni = Checkbutton(AchaarAndChutneys_F,text='Nariyal Ki Chatni',variable=var62,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkNariyalKiChatni).grid(row=13,sticky=W)
PodinaKiChatni = Checkbutton(AchaarAndChutneys_F,text='Podina Ki Chatni',variable=var63,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkPodinaKiChatni).grid(row=14,sticky=W)
TangyMayoCheeseDip = Checkbutton(AchaarAndChutneys_F,text='Tangy Mayo Cheese Dip',variable=var64,onvalue=1,offvalue=0,font=('arial',10,'bold'),bg='#ff8a65',command=chkTangyMayoCheeseDip).grid(row=15,sticky=W)

txtChanneKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_ChanneKaAchaar)
txtChanneKaAchaar.grid(row=0,column=1)
txtGobhiGajjarKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_GobhiGajjarKaAchaar)
txtGobhiGajjarKaAchaar.grid(row=1,column=1)
txtHeengAamKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_HeengAamKaAchaar)
txtHeengAamKaAchaar.grid(row=2,column=1)
txtLasodaKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_LasodaKaAchaar)
txtLasodaKaAchaar.grid(row=3,column=1)
txtAamKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_AamKaAchaar)
txtAamKaAchaar.grid(row=4,column=1)
txtMirchNimbuKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MirchNimbuKaAchaar)
txtMirchNimbuKaAchaar.grid(row=5,column=1)
txtMeethaNimbuKaAchaar = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_MeethaNimbuKaAchaar)
txtMeethaNimbuKaAchaar.grid(row=6,column=1)
txtAmchoorKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_AmchoorKiChatni)
txtAmchoorKiChatni.grid(row=8,column=1)
txtDhaniyeKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_DhaniyeKiChatni)
txtDhaniyeKiChatni.grid(row=9,column=1)
txtImliKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_ImliKiChatni)
txtImliKiChatni.grid(row=10,column=1)
txtLehsunKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_LehsunKiChatni)
txtLehsunKiChatni.grid(row=11,column=1)
txtNariyalKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_NariyalKiChatni)
txtNariyalKiChatni.grid(row=13,column=1)
txtPodinaKiChatni = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_PodinaKiChatni)
txtPodinaKiChatni.grid(row=14,column=1)
txtTangyMayoCheeseDip = Entry(AchaarAndChutneys_F,font=('arial',10,'bold'),bd=8,width=3,justify=LEFT,state=DISABLED,textvariable=E_TangyMayoCheeseDip)
txtTangyMayoCheeseDip.grid(row=15,column=1)

##### Total Cost #####
lblTotalCost = Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='#ff8a65',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

##### RECEIPT #####
lblReceipt=Label(Receipt_F,font=('arial',20,'bold'),text='Receipt',bg='#ff8a65',fg='black')
lblReceipt.grid(row=0)
txtReceipt = Text(Receipt_F,width=62,height=31,bg='white',bd=4,font=('arial',10,'bold'))
txtReceipt.grid(row=1)


##### BUTTONS #####
btnTotal = Button(Buttons_F,padx=10,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',bg='#ff8a65',command=CostOfItem).grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=10,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',bg='#ff8a65',command=Receipt).grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=10,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',bg='#ff8a65',command=Reset).grid(row=0,column=2)

root.mainloop()         #runs the application till we manually close it
