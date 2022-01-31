# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import subprocess

app = QApplication(sys.argv)
mainwindow = loadUi("ue4-manager.ui")
installuewindow = loadUi("ue4-installer.ui")
app.setWindowIcon(QtGui.QIcon('Icon.png'))

#Functions
def installUE():
    installuewindow.show()

def installMarketplace():
    subprocess.call('xterm -e "cd ~/; git clone https://github.com/Erlandys/UE4LinuxLauncher.git; chmod +x UE4LinuxLauncher/Compiled/start.sh; exit" ', shell=True)

def installUpdater():
    subprocess.call('''echo 'UNREAL_DIR="~/UnrealEngine/"' > ~/UpdateUE4.sh; echo 'set -e' >> ~/UpdateUE4.sh; echo 'cd "$UNREAL_DIR"' >> ~/UpdateUE4.sh; echo 'git pull https://github.com/EpicGames/UnrealEngine.git release' >> ~/UpdateUE4.sh; echo './Setup.sh' >> ~/UpdateUE4.sh; echo './GenerateProjectFiles.sh' >> ~/UpdateUE4.sh; echo 'if [ "$1" == "-clean" ] ;then' >> ~/UpdateUE4.sh; echo 'make CrashReportClient-Linux-Shipping ShaderCompileWorker UnrealPak UnrealLightmass UnrealFrontend UE4Editor ARGS=-clean' >> ~/UpdateUE4.sh; echo 'fi' >> ~/UpdateUE4.sh; echo 'make' >> ~/UpdateUE4.sh; echo '~/UnrealEngine/Engine/Binaries/Linux/UE4Editor' >> ~/UpdateUE4.sh; chmod +x ~/UpdateUE4.sh; exit ''', shell=True)

def updateUE():
    subprocess.call('xterm -e "cd ~/; ./UpdateUE4.sh; exit"', shell=True)

def openMarketplace():
    subprocess.call("xdg-open https://www.unrealengine.com/marketplace/en-US/store", shell=True)

def openMarketplaceDownloader():
    subprocess.call("cd ~/UE4LinuxLauncher/Compiled/; ./start.sh", shell=True)

def launch():
    subprocess.call("~/UnrealEngine/Engine/Binaries/Linux/UE4Editor", shell=True)

def createGithubAcc():
    subprocess.call("xdg-open https://github.com/join?source=header-home", shell=True)

def createEpicAcc():
    subprocess.call("xdg-open https://accounts.unrealengine.com/login?redirectUrl=https%3A%2F%2Fwww.unrealengine.com%2F&client_id=932e595bedb643d9ba56d3e1089a5c4b&noHostRedirect=true", shell=True)

def linkAcc():
    subprocess.call("xdg-open https://www.unrealengine.com/account/connected", shell=True)

def activate():
    subprocess.call("xdg-open https://www.unrealengine.com/account/password", shell=True)

def install():
    installuewindow.destroy()
    #Update script
    subprocess.call('''echo 'UNREAL_DIR="~/UnrealEngine/"' > ~/UpdateUE4.sh; echo 'set -e' >> ~/UpdateUE4.sh; echo 'cd "$UNREAL_DIR"' >> ~/UpdateUE4.sh; echo 'git pull https://github.com/EpicGames/UnrealEngine.git release' >> ~/UpdateUE4.sh; echo './Setup.sh' >> ~/UpdateUE4.sh; echo './GenerateProjectFiles.sh' >> ~/UpdateUE4.sh; echo 'if [ "$1" == "-clean" ] ;then' >> ~/UpdateUE4.sh; echo 'make CrashReportClient-Linux-Shipping ShaderCompileWorker UnrealPak UnrealLightmass UnrealFrontend UE4Editor ARGS=-clean' >> ~/UpdateUE4.sh; echo 'fi' >> ~/UpdateUE4.sh; echo 'make' >> ~/UpdateUE4.sh; echo '~/UnrealEngine/Engine/Binaries/Linux/UE4Editor' >> ~/UpdateUE4.sh; chmod +x ~/UpdateUE4.sh; exit ''', shell=True)
    #Marketplace content downloader
    subprocess.call('xterm -e "cd ~/; git clone https://github.com/Erlandys/UE4LinuxLauncher.git; chmod +x UE4LinuxLauncher/Compiled/start.sh; exit" ', shell=True)
    #Unreal Engine 4
    subprocess.call('xterm -e "cd ~/; git clone https://github.com/EpicGames/UnrealEngine.git; cd UnrealEngine; ./Setup.sh; ./GenerateProjectFiles.sh; make; ~/UnrealEngine/Engine/Binaries/Linux/UE4Editor; exit" ', shell=True)

def cancel():
    installuewindow.destroy()

#Buttons
mainwindow.installButton.clicked.connect(installUE)
mainwindow.installMarketplace.clicked.connect(installMarketplace)
mainwindow.installUpdater.clicked.connect(installUpdater)
mainwindow.updateButton.clicked.connect(updateUE)
mainwindow.openMarketplaceButton.clicked.connect(openMarketplace)
mainwindow.marketplaceDownloaderButton.clicked.connect(openMarketplaceDownloader)
mainwindow.launchButton.clicked.connect(launch)
installuewindow.githubButton.clicked.connect(createGithubAcc)
installuewindow.epicButton.clicked.connect(createEpicAcc)
installuewindow.linkButton.clicked.connect(linkAcc)
installuewindow.activateButton.clicked.connect(activate)
installuewindow.installButton.clicked.connect(install)
installuewindow.cancelButton.clicked.connect(cancel)

mainwindow.show()
app.exec_()
