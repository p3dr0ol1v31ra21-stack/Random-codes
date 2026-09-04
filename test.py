import time

import os

iniciar = input("Iniciar? Y/N ")
start = False

if iniciar == "Y":
    start = True
    os.system("cls" if os.name == "nt" else "clear")
else:
    print("Programa não iniciado")

if start:
    import time

    print("$$$$$$$\\  $$$$$$$\\   $$$$$$\\   $$$$$$\\  $$$$$$\\ $$\\       ")
    time.sleep(0.3)
    print("$$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ \\_$$  _|$$ |      ")
    time.sleep(0.3)
    print("$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  \\__|  $$ |  $$ |      ")
    time.sleep(0.3)
    print("$$$$$$$\\ |$$$$$$$  |$$$$$$$$ |\\$$$$$$\\    $$ |  $$ |      ")
    time.sleep(0.3)
    print("$$  __$$\\ $$  __$$< $$  __$$ | \\____$$\\   $$ |  $$ |      ")
    time.sleep(0.3)
    print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\\   $$ |  $$ |  $$ |      ")
    time.sleep(0.3)
    print("$$$$$$$  |$$ |  $$ |$$ |  $$ |\\$$$$$$  |$$$$$$\\ $$$$$$$$\\ ")
    time.sleep(0.3)
    print("\\_______/ \\__|  \\__|\\__|  \\__| \\______/ \\______|\\________|")
    time.sleep(2)

    import time
    texto = """No dia 7 de setembro de 1822, às margens do rio Ipiranga, o Brasil deu o primeiro passo como nação independente. Aquele grito não encerrou uma história passada, mas iniciou um desafio para um futuro ainda mais importante: construir um país.
    Independência não é só uma data. É um compromisso que se renova todos os dias. Renova-se quando escolhemos encarar as dificuldades da vida, reconhecendo que, por sermos humanos, somos em nossa alma seres sós — e, por isso, independentes.
    Na escola, esse compromisso tem nome: respeito. Respeito à professora que dedica tempo para ensinar. Respeito à diretoria, que se dedica a gerenciar. Respeito à secretaria, que se dedica a atender. E respeito ao colega que senta ao lado, mesmo quando todos pensam de forma diferente. Respeito ao hino que cantamos hoje e à história que estudamos um pouco todos os dias.
    Nossa sala de aula é um pedaço pequenininho do Brasil. Quando cuidamos do pátio, quando ouvimos sem interromper, quando valorizamos o que o outro tem a nos dizer, estamos honrando o mesmo espírito que nasceu há mais de duzentos anos. O 7 de Setembro nos lembra que a Pátria não se constrói só com desfiles. Constrói-se também no silêncio de quem presta atenção, de quem ouve, observa e está disposto a cuidar de um espaço, não porque estamos nele sós, mas porque há outras pessoas que também desfrutam dele conosco.
    Que esta data nos ensine a ser independentes de verdade: capazes de pensar, de escolher, de ter esperança e de respeitar quem caminha ao nosso lado, mesmo nos dias em que quase não suportamos o peso desta vida tão maravilhosamente normal e extremamente passageira.
    Que aprendamos a florir onde a vida nos plantar..."""
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.1)
    
ascii_art = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx;:::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx+;:::::::::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx+;:::::::::::::::::::::;+xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::::::::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::;;;;;;;;;::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::++xX$$$$$$$$$$$Xx+;::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::;+x$$$$$$$$$$$$$$$$$$$$$x+;:::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::;x$$$$$$$$$$$$$$$$$$$$$$$$$$$x;::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::::+X$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$X+:::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::;x$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$x;::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::::+X$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$X+::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::::::+$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$+::::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXxx;::::::::::::::::::;;;:;;.;;.;::;;:;;+++x$$$$$$$$$$$$$$$$$$$$$$+::::::::::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXxx+;::::::::::::::::::::.::.;:.;;:;::;;  ;+. .;;:+xX$;x$$$$$$$$$$$$$X::::::::::::::::::::;+xxXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXx+;::::::::::::::::::::::+xXX$$$$$$$$$$$$XXXXx+;:.::;.:;;xX$$$$$$$$$$$$x::::::::::::::::::::::;+xXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXx+;:::::::::::::::::::::::::X$$X;$$$$$$$$$$$$$$$$$$$$Xx+;;.:;.;+x$$$$$$$$$X:::::::::::::::::::::::::;+xXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXx+;::::::::::::::::::::::::::::$$$$$$$$$$$$$$$$$$$$$$$$$$$$$+Xx+:.::;;+X$$$$$$::::::::::::::::::::::::::::;+xXXXXXXXXXXXXX",
    "XXXXXXXXXXXx;::::::::::::::::::::::::::::::;$$$$$$$$$$$$$$X$$$$$$$$$$$$$$X$$$$X+;:.;;:+$$$$;::::::::::::::::::::::::::::::;xXXXXXXXXXXX",
    "XXXXXXXXXXXXXx+;::::::::::::::::::::::::::::$$$$$$$$$$$$$$+$$$$$$$$$$$$$$$$$$$$$$$x+::;:;x$::::::::::::::::::::::::::::;+xXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXx+;:::::::::::::::::::::::::X$$$$$$$X$$$$$$$$$$$$$$;$$$$$$$$$$$$$$$$$X;:;;::::::::::::::::::::::::::;+xXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXx+;::::::::::::::::::::::+$$$$X:$$$$$$$$$$$$$Xx$$$X+$$$$$$$$$$$$$$$$X;.;::::::::::::::::::::::;+xXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXxx+;::::::::::::::::::::X$+$$$$$$X+$$$$$$$$$$x$$$$$$$$$$$$$$$$xx$$X$X::::::::::::::::::::;+xxXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXxx;::::::::::::::::::+$$$$$$$$XX$$$$$$$$$$$$$$$$$$$$$$$$$$$Xx$$+$+::::::::::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::::::+$$$$$$$;$$$$$$$$$$$X:X$$$$$$$$$$$$$$Xx+$$+::::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::::+$$$$$$$$$++$$$$$$$$$$$$$;X$$x$$x$X$;$$$+::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::;X$$$$$$$$$$$$$$$$$$$$$$$$X$X$$+$$$$$X;::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::::+X$$$$$$$$$$$$$$$$$$$$$$;$$$$X$$$X+:::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::;x$$$$$$$$$$$$$$$$$$$$$$$$$+$x;::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::;+x$$$$$$$$$$$$$$$$$$$$$x+;:::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::++xX$$$$$$$$$$$Xx++::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;::::::::::::;;;;;;;;;::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::::::::::::::::::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx+;:::::::::::::::::::::;+xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx;:::::::::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::::::::;xxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;:::::;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+;+xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

for linha in ascii_art:
    print(linha)
    time.sleep(0.1)

    print("   ")
    print("   ")
    print("   ")
    print("   ")

    
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("███████╗    ██████╗ ███████╗    ███████╗███████╗████████╗███████╗███╗   ███╗██████╗ ██████╗  ██████╗ ")
    time.sleep(0.1)
    print("╚════██║    ██╔══██╗██╔════╝    ██╔════╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██╔═══██╗")
    time.sleep(0.1)
    print("    ██╔╝    ██║  ██║█████╗      ███████╗█████╗     ██║   █████╗  ██╔████╔██║██████╔╝██████╔╝██║   ██║")
    time.sleep(0.1)
    print("   ██╔╝     ██║  ██║██╔══╝      ╚════██║██╔══╝     ██║   ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══██╗██║   ██║")
    time.sleep(0.1)
    print("   ██║      ██████╔╝███████╗    ███████║███████╗   ██║   ███████╗██║ ╚═╝ ██║██████╔╝██║  ██║╚██████╔╝")
    time.sleep(0.1)
    print("   ╚═╝      ╚═════╝ ╚══════╝    ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("##********************************+*+++++++++++++++++++++++++++*********************")
    time.sleep(0.1)
    print("******************************++++++++++*=   .+++++++++++++++++++*******************")
    time.sleep(0.1)
    print("**************************++++++++++++++#%#.. ++++++++++++++++++++++****************")
    time.sleep(0.1)
    print("***********************+++++++++++++++++%#+  .-++++++++++++++++++++++++*************")
    time.sleep(0.1)
    print("********************++++++++++++++++++++@@@-..-++++++++++++++++++++++++++***********")
    time.sleep(0.1)
    print("***************++++++++++++++++++++++++*@*.   :=+++++++++++++++++++++-:*%=-=********")
    time.sleep(0.1)
    print("**********+++=::-+++++++++++=.                          .-:.. ..   :=...:*#*+*******")
    time.sleep(0.1)
    print("********+++:.. .. -.     .   ++.                                  *#***+++++++******")
    time.sleep(0.1)
    print("****+++++++++++++++@:.:=.  :-.+@@@=.                    .  ...   .+++++++++++++*****")
    time.sleep(0.1)
    print("*+++++++++++++++++++@#...#%+..=@@@@@%%#**=..  .      .. .-*====: .+++++++++++++++***")
    time.sleep(0.1)
    print("+++++++++++++++++++++#@@@@@@@@@@@@.. :+.   .  .    :-#@@@@@@%#*+++++++++++++++++++**")
    time.sleep(0.1)
    print("+++++++++++++++++++++++++++++++*@@::   .-.    :    ##+++++++++++++++++++++++++++++++")
    time.sleep(0.1)
    print("++++++++++++++++++++++++++=+=====*.- ..       .    :======+=++++++++++++++++++++++++")
    time.sleep(0.1)
    print("++++++++++++++++++++=============*:: ...      .    .=========+++++++++++++++++++++++")
    time.sleep(0.1)
    print("+++++++++++++++++=====================%. - :.     .     ==============++++++++++++++++++")
    time.sleep(0.1)
    print("+++++++++========================*%  .= =     .     ===============+++++++++++++++++")
    time.sleep(0.1)
    print("++==+============================@+   *. :    .     ====================++++++++++++")
    time.sleep(0.1)
    print("++===============================#@.-  *  ..        ======================++++++++++")
    time.sleep(0.1)
    print("==================================@=.  :=           -========================+++++++")
    time.sleep(0.1)
    print("==================================@.-.  :-          :==========================+++++")
    time.sleep(0.1)
    print("====================-=-----------=#...   .-         :--===========================++")
    time.sleep(0.1)
    print("===========-----------------------#.       =  -     .----===========================")
    time.sleep(0.1)
    print("======----------------------------+*%#      .     .+=----------=====================")
    time.sleep(0.1)
    print("==--------------------------------*. . .#-          ---------------=================")
    time.sleep(0.1)
    print("----------------------------------#. :     .-:      -------------------=============")
    time.sleep(0.1)
    print("----------------------------------#..:      ..  .   -----------------------=========")
    time.sleep(0.1)
    print("---------------:--:::::::::::::::-+ :.       .      :-------------------------======")
    time.sleep(0.1)
    print("-------::::::::::::::::::::::::::-: =.      .. .   :::::::----------------------====")
    time.sleep(0.1)
    print("---::::::::::::::::::::::::::::::=..=.  .   .. .   ::::::::::::---------------------")
    time.sleep(0.1)
    print(":::::::::::::::::::::::::::::::::+ .:.  .   .. .   ::::::::::::::::-----------------")
    time.sleep(0.1)
    print(":::::::::::::::::::::::::::::::::+....  .   .. .   :::::::::::::::::::::------------")
    time.sleep(0.1)
    print(":::::::::::::::::::::::::::::::::+.: .  :   .. :   :::::::::::::::::::::::::--------")
    time.sleep(0.1)
    print(":::::::::::::::::::::::::::::::::+:. .. - . .. -   .::::::::::::::::::::::::::::----")
    time.sleep(0.1)
    print(":::::::::::::::::::::::::::::::::==.  . = . .. :   .::::::::::::::::::::::::::::::--")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("_____ _   _______ ___________ _____ _   _______ _____ _   _ _____ _____  ___  ")
    time.sleep(0.1)
    print("|_   _| \\ | |  _  \\  ___| ___ \\  ___| \\ | |  _  \\  ___| \\ | /  __ \\_   _|/ _ \\ ")
    time.sleep(0.1)
    print("  | | |  \\| | | | | |__ | |_/ / |__ |  \\| | | | | |__ |  \\| | /  \\/ | | / /_\\ \\")
    time.sleep(0.1)
    print("  | | | . ` | | | |  __||  __/|  __|| . ` | | | |  __|| . ` | |     | | |  _  |")
    time.sleep(0.1)
    print(" _| |_| |\\  | |/ /| |___| |   | |___| |\\  | |/ /| |___| |\\  | \\__/\\_| |_| | | |")
    time.sleep(0.1)
    print(" \\___/\\_| \\_/___/ \\____/\\_|   \\____/\\_| \\_/___/ \\____/\\_| \\_/\\____/\\___/\\_| |_/")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("..............--...-------------------++++++++++++++++++++++++++######+++++++-------")
    time.sleep(0.1)
    print("............---..----++-------------....----..----++++++++++++++++++++####+++-+-----")
    time.sleep(0.1)
    print("-.........-.-------------------..   ..    ...      .-++++###++++#+#####+####+++---++")
    time.sleep(0.1)
    print(".......---.------------------.   ....-..---.  ..      .-###################++++-++++")
    time.sleep(0.1)
    print("....-----------------------...   .-+--.-+---...         .++################+++++++++")
    time.sleep(0.1)
    print("--------------------------. ..  -+########+++-..          .+###############+++++++++")
    time.sleep(0.1)
    print("--------------------------.    -#############+-....         -##################+++++")
    time.sleep(0.1)
    print("-----------------------++.  . .###############++--..        .+###############+++++++")
    time.sleep(0.1)
    print("...--------------------++......###############++-.          .+#############+++++----")
    time.sleep(0.1)
    print(".--..------------------+++..  .##############-....          -#############++++++----")
    time.sleep(0.1)
    print("..---------------------+++-.  -#############+--.           .+############+++++--+---")
    time.sleep(0.1)
    print(".------------------------++-..-###+###+-###+----          .+############++++--------")
    time.sleep(0.1)
    print(".........------------------+-.-##--##+--+-------         -##############+++---------")
    time.sleep(0.1)
    print(".....-.........-----.--------+######+-####+----...---.  +##############+++++++------")
    time.sleep(0.1)
    print(".........................----+######-+#######+--.------################+++----------")
    time.sleep(0.1)
    print("..................--.....-----######-+######+--..----#################+-----..---...")
    time.sleep(0.1)
    print("...........................---#####---#####+--..--+++++++++++#######++---...........")
    time.sleep(0.1)
    print("..............................####++-+#####--. .--++++++++--++++++-----.............")
    time.sleep(0.1)
    print("..............................+##------+##+-...  -++-+------------------............")
    time.sleep(0.1)
    print("............................--+###++++#####+.  .---++---------------.---............")
    time.sleep(0.1)
    print("..............................-+#########+  .....-++--------------......--..........")
    time.sleep(0.1)
    print("..........................-...-.-++-##+.  .--...------....................-.........")
    time.sleep(0.1)
    print(".....--..............-..--...-----    .--+..-+-----..-.........................-....")
    time.sleep(0.1)
    print(".....----...------.--------..----+###++-..++--------.---.........................---")
    time.sleep(0.1)
    print("--.......-......----.-.........--+++.-++#----------------+--.....-+++-..............")
    time.sleep(0.1)
    print("---........---+++++++++--.--. ----+++++----------.. .+++++++++++++++++---...........")
    time.sleep(0.1)
    print("----......--+##+#++++++--......---------------------++- .-+++++++++++++-+...........")
    time.sleep(0.1)
    print("-.......-+++----+++++--.  .+-.++-------------+##+++#-+++++  +######+##++............")
    time.sleep(0.1)
    print("--..--..+###++--++-+--...--#+-+++--+-+++++++#+######+##++-.-+++#++--------..........")
    time.sleep(0.1)
    print("--...-.-+#####+##++----++++##+++--+###-+-++#######++++#++++###+#+#++++++--.........-")
    time.sleep(0.1)
    print("--..----+++++++++-+---##++###+##+++++++#+---+++#++##-..---+#+###++#++-+++-......--.-")
    time.sleep(0.1)
    print("---.----++-++++-+++--.####+######+-+#######-++##++++#+--+-+#+++++++-+-+---......----")
    time.sleep(0.1)
    print("------.-++-++-++++++--##+#####+####+######---#+######+--...++++-++-+------.....-----")
    time.sleep(0.1)
    print("+-------++++-----. -++##+++#####++++-+##+-+###+####++####. .-++----------....  .----")
    time.sleep(0.1)
    print("+++--------.       -++###+##+##++###+++#+-++######++++-###    .   .-...         .---")
    time.sleep(0.1)
    print("+++++------    .-  -++###+#++++#+-++#++##++##++###+-++-##.    -+#                .--")
    time.sleep(0.1)
    print("-++++++---    ++-. ---###++--+++++++#++########.###++####-    --+-  -+           .--")
    time.sleep(0.1)
    print("---+#+++-.   -+--  -+-+###+++-++++++-####+#+-###########.      .++.+++.           .-")
    time.sleep(0.1)
    print("----++++-    .-..  .-+-###+-+-++++##+#####+--+####.----.        .--+++-           ..")
    time.sleep(0.1)
    print("+----++-     .+--  ----+###+++-+-+########+-###+.#++--++        -++--+.  .        ..")
    time.sleep(0.1)
    print("+++++-.    .#--.-..++-+-+###+++++#############+.-++##+--..       -++#-.+++        ..")
    time.sleep(0.1)
    print("+++++.     +---+-. -+----+###++++#########++###+++#####---        .-+--#++         .")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("_____ _   _  ___  ______________ _____ _____ _ ")
    time.sleep(0.1)
    print("|  _  | | | | |  \\/  |  _  | ___ \\_   _|  ___| |")
    time.sleep(0.1)
    print("| | | | | | | | .  . | | | | |_/ / | | | |__ | |")
    time.sleep(0.1)
    print("| | | | | | | | |\\/| | | | |    /  | | |  __|| |")
    time.sleep(0.1)
    print("\\ \\_/ / |_| | | |  | \\ \\_/ / |\\ \\  | | | |___|_|")
    time.sleep(0.1)
    print(" \\___/ \\___/  \\_|  |_/\\___/\\_| \\_| \\_/ \\____/(_)")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    import time

    print(".---...          ")
    time.sleep(0.1)
    print("                                                                 ..--.......          ")
    time.sleep(0.1)
    print("                                                             ..+-+-...-.....          ")
    time.sleep(0.1)
    print("                                                        .-+++++---..+--....           ")
    time.sleep(0.1)
    print("                                                   ..++#++++----..-+.-.....           ")
    time.sleep(0.1)
    print("                                                 .+++++++----+...+-.-..-...           ")
    time.sleep(0.1)
    print("                                             .-+++++++---.++...-+-.+..-...            ")
    time.sleep(0.1)
    print("                                            .+++-.   ....-....-+-.+..-....            ")
    time.sleep(0.1)
    print("                                           -++....-.          -..+..-......           ")
    time.sleep(0.1)
    print("                                          -+..##########+.        .........           ")
    time.sleep(0.1)
    print("                                        .-++#############+-        ........           ")
    time.sleep(0.1)
    print("                                     ...++++#########++#++.      .-..-...             ")
    time.sleep(0.1)
    print("                                     -++++#+++...-++-++++.    ............            ")
    time.sleep(0.1)
    print("                                    .+#. ++#############+   ....-........             ")
    time.sleep(0.1)
    print("                                   .+#+  ############+#+  ..-....-........            ")
    time.sleep(0.1)
    print("                                  .-++   +#########++++ ..++...-+.. ......            ")
    time.sleep(0.1)
    print("                                 .++.     +###########+-.+-...--......-...            ")
    time.sleep(0.1)
    print("                                .+..     .    +#####+-..+-.-..-...........            ")
    time.sleep(0.1)
    print("                                ++++++++++-...      .+------...............           ")
    time.sleep(0.1)
    print("                                ++++###++-....---...+....-+...............            ")
    time.sleep(0.1)
    print("                               .++###+++-.........++#....+++...    ..... ..           ")
    time.sleep(0.1)
    print("                               .++##+++-........+++++....                .            ")
    time.sleep(0.1)
    print("                               ++##++--.....-++++-.                      +             ")
    time.sleep(0.1)
    print("                              .+#++++---......                           -+             ")
    time.sleep(0.1)
    print("                            .++++++-...                                   +            ")
    time.sleep(0.1)
    print("                            ...-..                                         -")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    print("++++++++++++++++++++++++++++++#.  ######++++++++++++-.#-+++++++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++-.######## -++++-...--. ##+-++++++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++.   ---++-  -######  .....###+#-####..+++++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++-######   .###+################+#######-++++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++-#############+######+###############++ ..-+++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++- ############++#++###++########+-#++######+  ..-+++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++ ##############+#######++######################   .-+++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++-.########################+################++#######-.     -++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++-.  +#######################++###############+-###############  .++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++- +###########################+################+########-#++######+   .++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++-+###########################++###############++#########+##-###########.+++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++-.############################+################+##########+##+####.-+#-##-+++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++##################+++########+###############+##-####-+######-+-#-#-+###+-++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++--##+++++########++-##-#######+###############+####+#+####+++--#--+######++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++-+######+++############-+++++##+#+#+#+############+#+##+#-+##-####.+###--+++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++-... ######-   ####### -+###############+++######+-----##############.-++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++--.....-++.#########++###############+#######+################# .++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++- #########+###############+#######+################ -+++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++-    -###++###############+-+--+++ ##############  -++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++.   ##################+#+#++-  #+#++++###### ++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++-################++#####- ##########++### +#++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++-##############++#######.################.++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++-. +###+#####++###+###+ #############+#--++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++- +#+++++#+##+-.     ############### +++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++-##########+-.####################--+++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++##########+- ##################### ++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++-+#########-.#####+++############. -++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++#######+-- ##+++####+########### ++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++--...#+-+#####################  .++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++-#+#####++++#######+      -++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++++++- #########+###   .+++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++++- ##########  -++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++++++-  .-.-+-++## ++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++++-  ######+++###.++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++-  #############+-++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++++#############+ -+++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++- -##########+.+++++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" +++++++++++++++++++++++++++++++++++++++++++++.  .###### .++#+++++++++++++++++++++++++++++++++++++++++ ")
    time.sleep(0.1)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++++.  ##  -+++++++++++++++++++++++++++++++++++++++++++++")
    time.sleep(0.1)

    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)
    print("   ")
    time.sleep(0.1)

    import time

    print(" BBBBBBBBBBBBBBBBB   RRRRRRRRRRRRRRRRR                  AAA                 SSSSSSSSSSSSSSS IIIIIIIIIILLLLLLLLLLL             ")
    time.sleep(0.1)
    print("B::::::::::::::::B  R::::::::::::::::R                A:::A              SS:::::::::::::::SI::::::::IL:::::::::L             ")
    time.sleep(0.1)
    print("B::::::BBBBBB:::::B R::::::RRRRRR:::::R              A:::::A            S:::::SSSSSS::::::SI::::::::IL:::::::::L             ")
    time.sleep(0.1)
    print("BB:::::B     B:::::BRR:::::R     R:::::R            A:::::::A           S:::::S     SSSSSSSII::::::IILL:::::::LL             ")
    time.sleep(0.1)
    print("  B::::B     B:::::B  R::::R     R:::::R           A:::::::::A          S:::::S              I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::B     B:::::B  R::::R     R:::::R          A:::::A:::::A         S:::::S              I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::BBBBBB:::::B   R::::RRRRRR:::::R          A:::::A A:::::A         S::::SSSS           I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B:::::::::::::BB    R:::::::::::::RR          A:::::A   A:::::A         SS::::::SSSSS      I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::BBBBBB:::::B   R::::RRRRRR:::::R        A:::::A     A:::::A          SSS::::::::SS    I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::B     B:::::B  R::::R     R:::::R      A:::::AAAAAAAAA:::::A            SSSSSS::::S   I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::B     B:::::B  R::::R     R:::::R     A:::::::::::::::::::::A                S:::::S  I::::I    L:::::L               ")
    time.sleep(0.1)
    print("  B::::B     B:::::B  R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A               S:::::S  I::::I    L:::::L         LLLLLL")
    time.sleep(0.1)
    print("BB:::::BBBBBB::::::BRR:::::R     R:::::R   A:::::A             A:::::A  SSSSSSS     S:::::SII::::::IILL:::::::LLLLLLLLL:::::L")
    time.sleep(0.1)
    print("B:::::::::::::::::B R::::::R     R:::::R  A:::::A               A:::::A S::::::SSSSSS:::::SI::::::::IL::::::::::::::::::::::L")
    time.sleep(0.1)
    print("B::::::::::::::::B  R::::::R     R:::::R A:::::A                 A:::::AS:::::::::::::::SS I::::::::IL::::::::::::::::::::::L")
    time.sleep(0.1)
    print("BBBBBBBBBBBBBBBBB   RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAASSSSSSSSSSSSSSS   IIIIIIIIIILLLLLLLLLLLLLLLLLLLLLLLL")
    time.sleep(0.1)

print("   ")
print("   ")
print("   ")
print("   ")

import time

ascii_art = [
    "██████╗ ██████╗ ██████╗ ██╗ ██████╗  █████╗ ██████╗  ██████╗ ██╗",
    "██╔═══██╗██╔══██╗██╔══██╗██║██╔════╝ ██╔══██╗██╔══██╗██╔═══██╗██║",
    "██║   ██║██████╔╝██████╔╝██║██║  ███╗███████║██║  ██║██║   ██║██║",
    "██║   ██║██╔══██╗██╔══██╗██║██║   ██║██╔══██║██║  ██║██║   ██║╚═╝",
    "╚██████╔╝██████╔╝██║  ██║██║╚██████╔╝██║  ██║██████╔╝╚██████╔╝██╗",
    " ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝",
]

for linha in ascii_art:
    print(linha)
    time.sleep(0.1)

import time

ascii_art = [
    ";;;;;;;;;;;;;;;;+;                                                                       ",
    "                                                                   ;;x$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$+;                                                              ",
    "                                                              ;X&&&&&&$                              &&&&&&&X;                                                        ",
    "                                                         +X&&&&&              .. .            .. ..         &&&&&x;                                                   ",
    "                                                     +$&&&&       .            .   X&&&&&. &&&       . ..       .&&&&X;                                               ",
    "                                                 ;X&&&&             +    &&&&&&  . &&&+&&  &&&  &&&& .      . .      &&&&x;                                           ",
    "                                              ;$&&&       .      &&&&&& ;&&  &&    &&&     &$&  &&&$ .  &&&      .       &&&x                                         ",
    "                                           $x&&&          &  &&& &&X &&& &&  &&  . &&&&&& &&$& &&$&    ;&&  &&&             &&&+                                      ",
    "                                         +&&&    .    :&  &&  &&; &&     &&  &&&   &&&.&  &&+& &&&&    &&  &&&& &&. .         $&&$;                                   ",
    "                                      +X&&&           &&&& &&  && &&&  . &&& x&&   &&&    && &&& &&   &&& &&&& &&  &&&&&  .  .   &&&x                                 ",
    "                                    ;$&&     .  x&&&&  &&&& && &&& &&  &&$&&  && . &&&&&&&&:;&& &&    && &&$:& && &&&  &&          +&&x                               ",
    "                                  ;$&&    &    &&&  && $&&.&&&& &&&&&& &&:&&&&&;    &X+x+ & $&& &&   &&& && &&&& &&&     &&&&&  ..   .&&x                             ",
    "                                ;X&&     && &&+ &&&      && &&&& && .&&&                             && &&  &&& &&&&&& &&&  &&&        +&&x                           ",
    "                               x&&.       &&&    &&&   &&:&&  &&& &                                        &&& &&&    &&&  &&&  &&   .   &&&+                         ",
    "                             &$&&   .     &&&     &&&  &&&&&&               &&&&&&&&&&&&&&&&&&&&              &&&    &&&  &&& ;&&&&&       &&$                        ",
    "                            ;&&   .   &&&  &&&&&&  x&&&&&&    .      &&&&&&&&&.              ;&&&&&&&&&           . &&   &&  &&&  &&&        &&;                      ",
    "                          ;&&&  . . &&&&&    &&&     &&&.       .&&&&&&         :. &$ &&$ :.        .&&&&&&     ..  &&&&&& &&&& $&&&  &&  :.  &&$;                    ",
    "                         x&&     .. &: &&&&   $&&&&&&;       &&&&&          x  $&      x      &          $&&&&&       && &&&  &&&$  &&&&&.  .   &&+                   ",
    "                        X&&  .           &&&&   &&&       &&&&&     &.& $& &&&  & +&&. &  &+& && & & +&      &&&&+      $&&  &&&  &&&&&      .   &&+                  ",
    "                      ;X&$      ;&.    .   &&&&         &&&&      & &&   &  &&  &  &&  &  &&   $ &&   &  &&     &&&&       &&& &&& &&  :&&&&  ..  &&+                 ",
    "                     &$&+  .. +&&&&&&+       &&&     X&&&    && &&&  & &&&  &  &&  &  &&  &  &&&  & &&& .&  &&     &&&      &&&& &&&x&&&&&&     .  &&x                ",
    "                    ;$&  .... &&&   &&&&           X&&&   &; && &&&  & &&&  &  &&  &  &&  .: &&&  & $$&  &  &&       &&&       :&&&&+&&&&           &&X               ",
    "                    X&  .      &&&&    &&&  .     &&&     &. &&  x& x&  ;&  &&  &  &&  &  &&  $+ &&  :&  &&  &  &&     &&&   . &&  &&&    &&&&&&&&&  &&x              ",
    "                  ;x&   .  &&&&&  &&&&   &&     &&&    &  &. & &  & &:& ;& &&&  & X&&. &  &;& X& & &  & &x&  & &x&  &    &&&     &&&  &&&&& &&&       &&;             ",
    "                  x&&  .  &&&        &&&&&     &&$               .      .       .      .       .                          &&&     &&&&&  :&&&   :  ..  &&;            ",
    "                 ;&&       &&&&&&&&&&&&      &&&  +&&&x;xXx &&&& &&& && &&& && &;&  & &+&  &  &&& &&.&+& &x&&&&&&&&&&&&&&   &&&       &&&&&     &&      &&;           ",
    "                ;&&  ..      .&&     &&:    &&&   &&:&&.;;+ && & $&  .  :&  .   &   x  &   X  .&     X&  . &&&&      &&&&    &&&  . .&&&:     &&&&&  ..  &$;          ",
    "                x&   .  &&&&&&    &&&&& .  &&                .&   & :&&. &. &&& && &;& $& X&&  & x&&  &  &  :&                &&&  . x   x&&&&&  &&&     ;&+          ",
    "               ;&&  .  &&&   &&&&&&&:     &&&&&&&&&&&&&&&&   :&   &  &&  &  &&$  $ &&+  &  &&  &  &&  &  &  && .  &&&&&&&&&&&&&&&&    &&&&&        &  :   &&;         ",
    "              ;$&    . &&&&&&&&    &&    &&&             &   x&  &&  &. &&  &  &&&  & +&&  &  &&  &  &&. &X && .. &             &&&          :&&&&&&&  :.  &x         ",
    "              ;&&   .       &&&&&&      &&& ..           &   ;&  &&X && &&$ x; &&&  & &x&  &  &&. &. &&$ &: &&    &          .:  &&x .. &&&&&&&        ..  &&;        ",
    "              x&  ..  &&&&&&&:   &&&   :&&      &&&&&&&&&&  &$ &      &  :   &      &   +  &+  $  &x  x  & &. &.  &&&&&&&&&&      &&  . &&   &&&&&&&&&  ..  &+        ",
    "             ;&&             &&&&&     &&  . .&&            &&&& .    &X &  &+& && &:& .& &&&; & &&&     x &&&&             &&    &&&    &&&&&&:    &&& ..  &$X       ",
    "             +&    . &&&&&&&     &&   &&&    &    . .              && .                                &&                    && .  &&    &&       &&&&    . .&+       ",
    "            ;x&  ..       &&&&&&&&    &&  .. &              x&&  . &&   &x& ;& &&&  & X&&& && &&& &&.  &&    &             . && .  x&&    &&&&&          :   &X;      ",
    "            ;&&  .. ;&&&&   ;&&    . $&&     &    &&&&&&&&&&& && . && .                .               &&  && &&&&&&&&&&& .  &&     &&    &&&&&&&&&&&&&      &$;      ",
    "            ;&x  .. &&        x&&x . &&+ .   &    &         x&&  . && .. &&&&&&&&&&&&&&&&&&&&&&&&&&  . &&   &&&        :&    && ..  &&& .    &&     &&&& :   &&;      ",
    "            ;&  . . &&&&&&&&&x.&&+.  &&  ..  &   .&    ;&&         && .  &                        &    &+         &    &&    &&  .   &&      &&&&&&&&&x  ..  X&;      ",
    "            ;&   ..      &&&&&&&     && ..   &: &&&&& &&&&&&&&&&&&&&&    &                        &    &&&&&&&&&&&&&& &&&&   $&   .  &&   x&&&&x              &;      ",
    "            ;&  . ... ..          : :&&      &   &&;    &                &                      . &               &&   &&     &      &&  .      ..            &;      ",
    "            ;& .. .  :       .. .   :&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    &                      . &   ;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  . .  .        :.     &;      ",
    "            ;&         &&&&& ... .. ;&&                            &&    &                      . &   $&                             &&          &&&&&  ..    &;      ",
    "            ;&        $&&$&& ... ..  &&   x&&&&&&&&&&&&&&&&&&&&&&&  &:   &                      . &   && &&&&&&&&&&&&&&&&&&&&&&&&$ . &&  ..      &&$&&$ ...   &;      ",
    "            ;& .        &&&    ...   &&   &&&&&&&$$$$$$$$$$$$$$$$&& &&   &                .       &   &  &$$$$$$$$$$$$$$$$&&&&&&&    && ..        &&&         &;      ",
    "            ;&        .  &       .   &&       :&&&&&&&$$$$$$$$$$$$&  &&  & +XXX$XxX$.&& XXXXXXXX: &  && &&$$$$$$$$$$$$&&&&&&.     . &&&  .      .  &         &&;      ",
    "            ;&&      .   &&     ...  &&& .          &&&&$$$$$$$$$$&&  && &$ .....    &&    ..... && && &&$$$$$$$$$$$&&&.       . .  &&&  ..     . x&         &&;      ",
    "            ;&&      ... &&  ...      &&  .            &&$$$$$$$$$$&&  &&   :...  &&    &&  .;.   :&& &&&$$$$$$$$$$&&     .     ..  &&   ..       &&      .  &X;      ",
    "            ;x&          &&  ...      &&& .             &&$$$$$$$$$$&&& &&&       &      &      ;&&  &&&$$$$$$$$$$&&            .  &&& .:.        &&         &+       ",
    "             +&:     . .  &&   .       &&               +&$$$$$$$$$$$&&&  :&&&  ..;$&&&&;: :  &&&  &&&$$$$$$$$$$$$&             .  &&    .       &&         &&;       ",
    "             ;&&  ...     &&   .     . &&&     .         &$$$$$$$$$$$$$&&&&  &&&&&&     .&&&&&   &&&$$$$$$$$$$$$$$&               &&&     ....:  &&         &x&       ",
    "              +&  ..    .  &&           &&  ....     .  &&$$$$$$$$$$$$$$$&&&&&     &&&&&+     &&&&$$$$$$$$$$$$$$$$&&             &&&        .   &&   .     X&;        ",
    "              ;&&  : . ..  X&;       ..  &&   .        &&$$$$$$$$$$$$$$$$$$$$&&&&&&&&$$&&&&&&&&$$$$$$$$$$$$$$$$$$$$&&            &&         .. x&+  ..     &$;        ",
    "               x&  . .      &&       .   &&&    . .   &&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&  ....:   &&         .   &&  . . .  ;&+         ",
    "               ;&&  ..       &&      ...  &&&  .  :  .&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&  ..    &&.   .     .  &&  ......  &$x         ",
    "                +&&  .        &&     . ..  &&&   .  :&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&$  .   &&   .         &&  . ..    &&;          ",
    "                &x&       ...  &&  ..        &&.  . &&&$$$$$$$$$$$$$$&&&$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&$$$$$$$$$$$$$&&&:   &&&          .  &&       :  X&;           ",
    "                 &&&       ..   &&   .    .   &&&    &&&$$$$$$$$$&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$&&&&&&.&&&&&$$$$$$$$&&&&    &&&             &&           &X            ",
    "                  ;&&        .   &&&       ..  &&&     &&&$$$$&&&&&       X&&&$$$$$$$$$$$$$$$$&&&        .&&&&&$$$&&&    &&&$        .   &&&           &&;            ",
    "                   ;&&  . .      &&&&& :..       &&&     &&&&&&              &&$$$$$$$$$$$$$$&&              $&&&&&     &&&   ..     . &&&&&     ...  &&;             ",
    "                    ;&&  ..     +&&&&&   .        x&&&                     .  &&$$$$$$$$$$$$&&             .          &&&   .: :     . &&&&&: ....   &&;              ",
    "                     ;&&              ....      .   $&&&     ...  . ..     .  &&$$$$$$$$$$$$&X            ..        &&&   .   .               ....  &&+               ",
    "                      ;&&   ....           ...   .:   &&&&     .  .        ..  &&$$$$$$$$$$&&  .                 &&&&                              &&;                ",
    "                       ;&&                ..      . .    &&&&     ...     .  .  &&$$$$$$$$$&.  .              .&&&&    .:..          ..          .&&&                 ",
    "                        ;$&+  ..             &&&&    .:.    &&&&           ...  &&&&&&&&&&&&  ..    .      .&&&&    ... .          .;.          &&$;                  ",
    "                          X&&              &&&&&&      :.      &&&&&        ...                .       :&&&&&             &&&&&&: ..      ..   &&+                    ",
    "                           x&&          &&&& &&x x&&&&    :...    :&&&&&&&                        &&&&&&&         .     &&&&&  &&   .        ;&&+                     ",
    "                            ;$&&      &&&&. &&  &&& &&& .     .        +&&&&&&&&&&&&&&&&&&&&&&&&&&&&                 &&&&: &&&:&&&&         &&X                       ",
    "                              ;&&;   &&x &&&&  &&&  &&&&&&&&                     ;&&&&&&&&;            .    .     &x.&&X    &&&& &&&&  .  &&&;                        ",
    "                                +&&      &&&  &&   && &&& &&&&&X        .   .. .              . ..: ..        X&&&&&& &&&&&&  &&&  &&&   &&+                          ",
    "                                 &X&&     & &&&  &&& &&&    &&&     :          .   .. . .....:.          &x &&:&&&  && &&&     &&&&    &&X;                           ",
    "                                   ;$&&     &&&&&&& &&&&&& &&&     &&&&  &&                        &&&& &&&& && &&& x&& &&&  &&&    +&&x                              ",
    "                                     $x&&X     &&  &&&     &&     &&$&& &&&&&&&&& &&&&&&:. &&  &&&&&X.&& &&&&X&& &&: :&& &&&&&;   &&&x                                ",
    "                                        +&&;      &&&&$   &&& .  &&&&&  && &&& &&&&&&      &&&X&& &&  &&$ &&&&&&& &&& &&&       &&&&                                  ",
    "                                          +&&&       &&& &&&    &&& &&  && &&x && &&     . &&&&&  x&&  && &&  &&&  &&&&&     &&&X$                                    ",
    "                                             $&&&;      .&&&&& &&&&&&& &&& &&  && &&&&&+..  &$$&   &&; &&+ &&  &&& $&     &&&$;                                       ",
    "                                                x&&&&       &&&&&  &&+ &&  &&  && &&     .  &&&&&; &&& :&& &&&  &      &&&$;                                          ",
    "                                                   ;$&&&&          &&X&&& &&& &&& &&     .: &&  &&x &&&&&&         &&&&xx                                             ",
    "                                                      ;+&&&&&             :&&&&&  &&&&&&  . &&&  &&           +&&&&$+                                                 ",
    "                                                           ;x&&&&&&.                     .              +&&&&&&x;                                                     ",
    "                                                                &;X&&&&&&&&&;                  :&&&&&&&&&x;&                                                          ",
    "                                                                        &xx$&&&&&&&&&&&&&&&&&&&&X+&&",
]

for linha in ascii_art:
    print(linha)
    time.sleep(0.1)

