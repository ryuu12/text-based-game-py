import os

class Entity:
    def __init__(self, type, name):
        self.name = name
        self.type = type
        self.health = 100
        self.exp = 0
    
    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getExp(self):
        return self.exp

    def healthDecrease(self, minus):
        print(f"[{self.type} Health -{minus}]")
        self.health = self.health-minus

    def healthIncrease(self, plus):
        print(f"[{self.type} Health +{plus}]")
        self.health = self.health+plus

    def expIncrease(self, plus):
        print(f"[{self.type} EXP +{plus}]")
        self.exp = self.exp + plus
    
    def expDecrease(self, minus):
        self.exp = self.exp - minus

    def status(self):
        print(f"{self.type} Status:\n[Name: {self.getName()}]\n[Health: {self.getHealth()}/100]\n[EXP: {self.getExp()}]")

    def talk(self, content):
        print(f"[{self.name}]: {content}")

os.system('clear')
username = input("Masukkan username anda: ")
player = Entity("Player", username)
monster = Entity("Monster","Caveman")

def statusReset():
    player.health=100
    player.exp=0
    monster.health=100
    monster.exp="Undefinded"

def gameA():
    os.system('clear')
    print("Kau tiba di dalam sebuah goa.")
    input()
    print("Lalu kau mendengar suara langkah yang besar.")
    input()
    print("Langkah itu semakin dekat dan dekat.")
    input()
    print("Hingga akhirnya...")
    input()
    monster.talk("Siapa yang berani menggangguku?")
    input()
    monster.status()
    input()
    print("Kau punya dua pilihan:\nBila kau ingin menjawabnya, maka ketik [jawab].\nBila ingin menyerang, maka ketik [serang].")
    gameAInput()

def gameAA():
    os.system('clear')
    print("Kau memilih untuk menyerangnya.")
    input()
    print("Serangan dilakukan.")
    input()
    monster.healthDecrease(10)#90
    input()
    print(f"Seranganmu mengenai tangan dari monster itu.")
    input()
    player.expIncrease(50)
    input()
    print("Monster itu mengerang kesakitan.")
    input()
    monster.talk("Beraninya kau...")
    input()
    print("Tiba-tiba saja, monster itu berlari ke arahmu.")
    input()
    print("Kau punya dua pilihan:\nBila ingin menghindar, ketik [menghindar].\nBila ingin menyerangnya secara langsung, ketik [serang].")
    gameAAInput()

def gameAB():
    os.system('clear')
    player.talk("Siapa kau?")
    input()
    monster.talk("Aku adalah penjaga tempat ini. Karena kau sudah menggangguku, kau akan ku serang!")
    input()
    print("Monster itu mulai menyerangmu.")
    input()
    print("Kau terkena serangannya.")
    input()
    player.healthDecrease(10)
    input()
    print("Kau merasakan tangan kananmu mengeluarkan darah yang sangat banyak. Ternyata serangan monster itu mengenai tanganmu secara langsung.")
    input()
    print("Kau punya dua pilihan:\nBila ingin lari, maka ketik [lari].\nBila ingin terus menyerang, maka ketik [serang].")
    gameABInput()

def gameBA1():
    os.system('clear')
    print("Kau memutuskan untuk lari")
    input()
    print("Kau pun berlari secepat mungkin hingga melihat cahaya di ujung goa.")
    input()
    print("Kau pun berhasil keluar dari goa tersebut.")
    input()
    print("Setelahnya, kau langsung pergi ke kota dan mencari rumah sakit untuk segera mengobati luka di tanganmu.")
    input()
    print(f"Pilihan yang bijak, [{player.getName()}].")
    input()
    gameEnd1()

def gameBA2():
    os.system('clear')
    print("Walaupun tangan kananmu berdarah, tapi kau tetap memaksakan untuk menyerangnya.")
    input()
    print("Kau mulai menyerangnya.")
    input()
    print("Tapi sayangnya, sebelum kau sempat maju, monster itu sudah terlebih dahulu menyekik leher mu.")
    input()
    print("Kau merasakan cengkraman yang luar biasa.")
    input()
    print("Nafasmu mulai terasa sesak.")
    input()
    player.healthDecrease(15)
    input()
    print('Cengkramannya semakin keras.')
    input()
    print("Kau bisa merasakan nafasmu semakin sulit dan sulit.")
    input()
    player.healthDecrease(15)
    input()
    print("Air matamu mulai keluar. Pandanganmu mulai berbayang-bayang.")
    input()
    player.healthDecrease(20) #40
    input()
    print("Hidungmu mulai mengeluarkan darah.")
    input()
    print("Seketika, bayang-bayang tentang rekam jejak kehidupanmu mulai muncul dalam pikiranmu.")
    input()
    player.healthDecrease(20) #20
    input()
    player.talk("Tolong... hentikan...")
    input()
    print("Monster itu tidak bekutik sedikitpun. Melihat dirimu yang semakin menyedihkan, monster itu tersenyum.")
    input()
    monster.talk("Hahaha...")
    input()
    print("Hingga akhirnya...")
    input()
    print("Terdengar suara remukan, dan seketika itu juga pandanganmu menjadi gelap.")
    input()
    player.healthDecrease(20)
    input()
    player.status()
    input()
    gameEnd2()

def gameBB1():
    os.system('clear')
    print("Kau menghindar dari serangan monster itu.")
    input()
    print("Monster itu pun tanpa sadar menghantamkan kepalanya ke dinding goa tersebut.")
    input()
    monster.healthDecrease(10)#80
    input()
    monster.talk("AAARRGHHH")
    input()
    print("Monster itu merasa kesakitan. Melihat dia tidak bergerak, kau merasa dapat menyerangnya kembali.")
    input()
    print("Kau pun berlari ke arah monster tersebut dan mengincar lehernya.")
    input()
    print("Kau tebas leher monster tersebut.")
    input()
    monster.healthDecrease(20)#60
    input()
    player.expIncrease(50)
    input()
    monster.talk("AAAARRRGHHHHH")
    input()
    print("Monster itu semakin kesakitan. Tanpa membuang waktu, kau kembali menebas leher monster itu.")
    input()
    monster.healthDecrease(20)#40
    input()
    player.expIncrease(50)
    input()
    print("Kau tebas lagi.")
    input()
    monster.healthDecrease(20)#20
    input()
    player.expIncrease(50)
    input()
    print("Hingga akhirnya...")
    input()
    monster.healthDecrease(20)
    input()
    player.expIncrease(50)
    input()
    monster.status()
    input()
    print("Kepala monster itu terpisah dari tubuhnya setelah tebasan terakhir.")
    input()
    print("Akhirnya kau dapat bernafas lega.")
    input()
    print("Kau merasa sangat kelelahan. Tidak ingin berlama-lama di dalam goa itu, kau pun berjalan keluar.")
    input()
    print("Cahaya yang terang terlihat dari luar goa. Akhirnya, kau berhasil mengalahkan monster tersebut.")
    input()
    print(f"Pilihan yang bagus, Player [{player.getName()}].")
    input()
    gameEnd1()

def gameBB2():
    os.system('clear')
    print("Ketika monster itu semakin dekat, kau juga ikut maju sambil menodongkan pedang mu.")
    input()
    print("Ketika pedang tersebut akan mengenai dada monster itu...")
    input()
    player.talk("Apa?!")
    input()
    print("Monster itu secepat mungkin menghindar dari pedang itu.")
    input()
    print("Lalu...")
    input()
    print("Dari samping, monster itu menahan pedang yang kau pegang dengan tangan nya.")
    input()
    monster.talk("Hehe...")
    input()
    print("Ia pun mengangkat pedang tersebut dan membantingnya ke tanah. Kau pun ikut terbanting.")
    input()
    player.healthDecrease(20)#80
    input()
    print("Kau pun terbaring di tanah dan merasakan sakit yang luar biasa di tubuhmu.")
    input()
    print("Monster tersebut mengambil pedang yang kau pegang. Kau tidak punya kekuatan untuk menahannya.")
    input()
    player.talk("Tidak... jangan...")
    input()
    print("Kau melihat monster itu mengarahkan pedangnya ke dadamu. Kau tahu ini bukan situasi yang bagus.")
    input()
    player.talk("Tolong... jangan... aku minta ampun...")
    input()
    print("Sambil tersenyum, monster itu pun menggerakkan pedang tersebut ke arah dadamu.")
    input()
    print("Dan...")
    input()
    player.healthDecrease(30)#50
    input()
    player.talk("AAAAAKKKHHH")
    input()
    print("Kau dapat melihat darah keluar dari mulut, hidung, dan dada mu.")
    input()
    print("Pedang itu sekarang tertancap di dadamu.")
    input()
    print("Monster itu mencabut pedang tersebut dari tubuhmu. Kau merasakan sakit yang sangat pedih.")
    input()
    print("Lalu...")
    input()
    player.healthDecrease(30)#20
    input()
    player.talk("AAAAAAAAKKKHHHH")
    input()
    print("Monster tersebut kembali menusukkan pedang tersebut ke tubuhmu.")
    input()
    player.talk("...")
    input()
    print("Kau sudah tidak dapat berkata-kata. Nafasmu mulai melemah. Pandanganmu mulai kabur. Tercium bau amis darah yang berasal dari tubuhmu.")
    input()
    print("Kau pun mulai teringat rekam jejak kehidupanmu.")
    input()
    print("Hingga akhirnya...")
    input()
    player.healthDecrease(20)
    input()
    player.status()
    input()
    print(f"Kau mati.")
    input()
    gameEnd2()

def gameEnd1():
    os.system('clear')
    print(f"Selamat, [{player.getName()}]! Kau berhasil bertahan hidup dan keluar dari goa tersebut.")
    input()
    player.status()
    print("Press any key to return to main menu...")
    input()
    menuShow()
    
def gameEnd2():
    os.system('clear')
    print(f"Player {player.getName()}, kau mati di tangan monster itu. Sayang sekali.")
    input()
    player.status()
    print("Press any key to return to main menu...")
    input()
    menuShow()

def gamePlay():
    os.system('clear')
    print(f"Selamat datang di permainan, [{player.getName()}].")
    input()
    player.status()
    input()
    print("Semoga beruntung!\nTekan apapun untuk memulai permainan...")
    input()
    gameA()

def creditShow():
    os.system('clear')
    print("Pembuat game ini:\nRayhan Rusyd\nDaffa Asyqar\nArdhien Fadhillah Suhartono\nUntuk kembali ke menu utama, ketik [kembali].")
    creditInput()

def menuShow():
    os.system('clear')
    statusReset()
    print("Selamat datang di Text-based Adventure Game!\nUntuk memulai permainan silahkan ketik [mulai].\nUntuk melihat pembuat game, silahkan ketik [credit].\nUntuk keluar, cukup ketik [Exit].")
    menuInput()

def gameAInput():
    pilihan = input(">")
    pilihan.lower()
    if pilihan == "serang":
        gameAA()
    elif pilihan == "jawab":
        gameAB()
    else:
        print("Mohon maaf, input anda tidak ada di pilihan.")
        input("Press anything to continue...")
        gameAInput()

def gameAAInput():
    pilihan = input(">")
    pilihan.lower()
    if pilihan == "serang":
        gameBB2()
    elif pilihan == "menghindar":
        gameBB1()
    else:
        print("Mohon maaf, input anda tidak ada di pilihan.")
        input("Press anything to continue...")
        gameAAInput()

def gameABInput():
    pilihan = input(">")
    pilihan.lower()
    if pilihan == "serang":
        gameBA2()
    elif pilihan == "lari":
        gameBA1()
    else:
        print("Mohon maaf, input anda tidak ada di pilihan.")
        input("Press anything to continue...")
        gameABInput()

def menuInput():
    pilihan = input(">")
    pilihan.lower()
    if pilihan == "credit":
        creditShow()
    elif pilihan == "mulai":
        gamePlay()
    elif pilihan == "exit":
        os.system('^Z')
    else:
        print("Mohon maaf, input anda tidak ada di pilihan.")
        input("Press anything to continue...")
        menuShow()

def creditInput():
    pilihan = input(">")
    pilihan.lower()
    if pilihan == "kembali":
        menuShow()
    else:
        print("Mohon maaf, input anda tidak ada di pilihan.")
        input("Press anything to continue...")
        creditShow()

menuShow()
