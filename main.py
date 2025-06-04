import time, os, platform

# Try to import PrettyTable, install if not found
try:
    from prettytable import PrettyTable
except ImportError:
    os.system("pip install prettytable")
    from prettytable import PrettyTable  # Try again after install

# Colors
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

# Typing effect function
def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)

# Windows colorama init
if 'Windows' in platform.uname():
    from colorama import init
    init()

# Banner
banner = f"""
{k}                                                                
                              -     -                            
                            .+       +.                          
                           :#         #:                         
                          =%           %-                        
           {lrd}REPORTER{k}     -*%.   {g}SpiDer{k}   .%+    {be}TELEGRAM      {k}       
                        #@:             -@#                      
                     :  #@:             :@*  :                   
                    -=  *@:             -@*  =-                  
                   -%   *@-             =@+   %-                 
                  -@=  .*@+             +@+.  =@-                
                 =@%   .+@%-    :.:    -@@+.   #@:               
                =@@#:     =%%-+@@@@@+-%%=     .#@@=              
                 .+%@%+:.   -#@@@@@@@#-   .:=#@%=                
                    -##%%%%%#*@@@@@@@*#%%%%%##-                  
                  .*#######%@@@@@@@@@@@%#######*.                
               .=#@%*+=--#@@@@@@@@@@@@@@@#--=+*%@#=.             
            .=#@%+:     *@@@@@+.   .+@@@@@*     :+%@#=.          
          :*@@=.    .=#@@@@@@@       @@@@@@@#=.    .=@@*.        
            =@+    .%@@*%@@@@@*     *@@@@@%*@@%.    +@=          
             :@=    +@# :@@@@@#     #@@@@%. #@+    =@:           
              .#-   :@@  .%@@#       #@@#.  @@:   -#.            
                +:   %@:   =%         %=   :@%   -+              
                 -.  +@+                   +@+  .-               
                  .  :@#                   #@:  .                
                      %@.    {cn}@EsFelUrM{k}    .@%                    
                      :+@:               =@+:                    
                        =@:             :@-                      
                         -%.           .%:                       
                          .#           #.                        
                            +         +                          
                             -       -                     
"""

# Show banner and warning
re(banner)
re(f"\n{lrd}Warning ! This is a test reporter, any offense is the responsibility of the user !{k}\n")

# PrettyTable Menu
print(lrd)
t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Info{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Reporter Channel{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Reporter Account{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Reporter Group [Updating]{lrd}'])
print(t)

# User input
number = input(f"{gn}Enter Number : {cn}")

# Menu logic
if number == "1":
    os.system("python report/reporter.py")
elif number == "2":
    os.system("python report/report.py")
elif number == "3":
    print(f"{be}This section is being updated and will be added soon \n\nChannel : @Buyer_infinity{rd}")
else:
    print(f"{rd}Invalid input. Please select 1, 2, or 3.")
