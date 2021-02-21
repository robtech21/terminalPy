import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
import time
print("--------------------------------------------------------------------------------")
print("                            WELCOME USER!                                       ")
print("--------------------------------------------------------------------------------")
answer = input("User@Computer:~$")
if answer == "help":
    print("pkg                command for installing and removing packages(N:not in function)(N:find animal!)")
    print("ls                 show files")
    print("python             python")
    print("exit               exit terminal!")
    print("whoami             show user in terminal")
    print("version            show version of terminal")
    print("credits            show credits")
    print("txt                txt command for text files")
    print("zip                zip command for zip files(NOTE:not in function")
elif answer == "exit":
    answer3 = input("Do you want to continue? [y/n]")
    if answer3 == "y":
        quit()
    else:
        print("abort!")
elif answer == "pkg":
    print("pkg is a command for using installing packages and more!")
    print("pkg most used commands:")
    print("install")
    print("remove")
    print("N:itn command is not in function right now!")
elif answer == "version":
    print("version of console is 1.0")
elif answer == "credits":
    print("made by luksi :)")
elif answer == "whoami":
    print("home/user")
elif answer == "python":
    print("this terminal can't open python but there are some python commands!")
    print("python-list")
    print("python-help")
elif answer == "python-list":
    print("pygame")
    print("karel")
    print("discord")
    print("this are one of the packages of python,they are not python applications!")
elif answer == "karel":
    answer4 = input("NOTE:this will just show you a karel but you can't control him,do you want to continue anyway [y/n] ")
    if answer4 == "y":
        import karel_robot.run
        move()
        move()
        move()
        move()
        move()
    else:
        print("abort!")
elif answer == "discord":
    import discord
    print("discord imported!")
elif answer == "pygame":
    import pygame
    pygame.init()
    print("welcome to pygame!")
    pygameanswer = input("what do you want to do?")
    if pygameanswer == "window":
        screen = pygame.display.set_mode([500, 500])
    elif pygameanswer == "help":
        print("pygame is using to make a game with python,visit a site www.pygame.org")
    else:
        print("no command found")
elif answer == "python-help":
    help()
elif answer == "ls":
    print("README.txt")
elif answer == "txt README.txt":
    print("hi,welcome to my terminal!")
    print("i hope you will enjoy here cause there are a lot of things to do!")
    print("have a nice day!")
    input("press enter to exit . . .")
elif answer == "pkg woof":
    print("🐶 do you have dog?")
elif answer == "zip":
    print("use this command for unziping or ziping files!(N:not in function)")
    print("-u, --unzip          unzip ziped files")
    print("-z, --zip            zip files")
    print("-r, --remove         remove zip files")
elif answer == "txt":
    print("this command is not finished you can just open text files!")
elif answer == "txt -v":
    print("what are you doing?")
    print("this command can harm your PC please stop.")
elif answer == "txt -vv":
    print("stop!")
elif answer == "txt -vvv":
    print("this command is now disabled")
elif answer == "txt -vvv":
    print("alright alright, i will show you a message,do that command with one more V")
elif answer == "txt -vvvv":
    print("hi,you found this secret message,this message is for peoples like you, you are nice guy cause you are helping other peoples, i wish you luck in everything good or anything good!")
elif answer == "tux":
    print("im everywhere 🐧!")
else:
    print("no command found")
