import instaloader
import os , time
ig=instaloader.Instaloader()
print(""""\033[1;34;40m\n
  _               _           ___              ___                      _                      _              
 (_)             ( )_        (  _ \           (  _ \                   (_ )                   ( )             
 | |  ___    ___ |  _)   _ _ | | ) | _ _      | | ) |   _    _   _   _  |(|    _      _ _    _| |   __   _ __ 
 | |/  _  \/  __)| |   / _  )| | | )(  _ \    | | | ) / _ \ ( ) ( ) ( ) |()  / _ \  / _  ) / _  | / __ \(  __)
 | || ( ) |\__  \| |_ ( (_| || |_) || (_) )   | |_) |( (_) )| \_/ \_/ | | | ( (_) )( (_| |( (_| |(  ___/| |   
 (_)(() (_)(__(_/)\__) \(_ _)(____/ |  __/    (____/  \ __/  \  /\___/ ( (_) \ __/  \(_ _) ) _ _) )\___)(()   
    (_)      /( (__)   (_)          | |               /(      \(       (_)   /(     (_)   (__)   (__)   (_)   
            (__)                    (_)              (__)     (_)           (__)                              
""")
profile=input("\033[1;31;40m\n Enter username:- ")
ig.download_profile(profile,profile_pic_only=True)
x="\033[1;32;40m\nPlease Support Me By Giving Star..."
y=0
while y <=len(x):
    os.system('cls')
    print (x[:y])
    time.sleep(.1)
    y=y+1