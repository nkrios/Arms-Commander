import os, sys, operator
sys.path.append("./Facerider")

import eznhlib
bash_cmd = eznhlib.bash_cmd
get_gw = eznhlib.get_gw
userSelectGateway = eznhlib.userSelectGateway
readUserInput = eznhlib.readUserInput
menu_parser = eznhlib.menu_parser
popen_background = eznhlib.popen_background
clean_iptables = eznhlib.clean_iptables

cwd = os.getcwd()
print "Debug: CWD = ", str(cwd)

def nh_fixes():
    menu = """Fix APT Repos to current Kali Rolling and then update python-pip
    Install all Python dependencies for Facerider"""
    menu_parser(menu)

    userInput = int(raw_input("Enter a OPTION: "))
    if userInput == 1:
        os.chdir("./Facerider")
        script = "fix_kali_nethunter_repos_and_upgrade_pip.sh"
        os.system("/bin/sh %s" % script)
        return
    elif userInput == 2:
        os.chdir("./Facerider")
        script = "prerequisite_setup.sh"
        os.system("/bin/sh %s" % script)
        return
    else:
        print "You have entered a invalid option"
        main()
    return

def main():
    menu = """FACERIDER: MITMf improved for Nethunter devices and tablets
    BDFProxy Improved: Backdoor Factory Proxy improved for Nethunter devices
    Ferret-Hamster-NG
    Nethunter Fixes: Common fixes for fresh Nethunter installations (apt repos, pip, etc.)"""
    menu_parser(menu)

    userChoice = int(raw_input("Enter a OPTION: "))

    if userChoice == 1:
        executable = "./Facerider/wip_mitmf_improved.py"
        cmd = "python {}".format(str(executable))
        os.system(cmd)
        return
    elif userChoice == 2:
        executable = "./Facerider/bdfproxy_improved.py"
        cmd = "python {}".format(str(executable))
        os.system(cmd)
        return
    elif userChoice == 3:
        executable = "./Facerider/ferret_hamster_improved.py"
        cmd = "python {}".format(str(executable))
        os.system(cmd)
        return
    elif userChoice == 4:
        nh_fixes()
        return
    else:
        print "You have entered a invalid option"
        main()
    return
main()
