# UE4-Manager-for-Linux
 This is an unofficial manager for the Unreal Engine 4 for GNU/Linux (**Installs** UE4, **updates** it and allows to **download content from the Marketplace**)
 
 ---

Install:

On Debian, Ubuntu, etc you can simply **install the .deb package** as normal. (Epic Games recommends Ubuntu 16.04 (64 Bit) or newer for the Unreal Engine 4)

On other distros you can execute the UE4_Manager.py in the source folder with python3. Take a look at the dependencies.txt file in the source folder and install the packages you haven't installed already. You must **change into the source directory** and after this you can run `python3 UE4_Manager.py`. You **can not run python3 /path/to/source/UE4_Manager.py**, because the paths into the UE4_Manager.py for the ue4-manager.ui, ue4-installer.ui and Icon.png wouldn't work in this case. But you can change this, give the loaduUi() / QtGui.QIcon() the absolute path to the UE4Manager folder.

Remove:

`sudo apt remove ue4manager` (or delete source folder).
You have to **delete** the **~/UpdateUE4.sh** file, the **~/UE4LinuxLauncher** and the **~/UnrealEngine** folder, if you want to remove the updater script, the Marketplace content downloader and the Unreal Engine.

---

Thanks to:

- Erlandas, who made the [Marketplace downloader](https://github.com/Erlandys/UE4LinuxLauncher.git)

- Epic Games, who made the [Unreal Engine 4](https://github.com/EpicGames/UnrealEngine.git)

- codywohlers, who made most parts of the [update script](https://forums.unrealengine.com/community/community-content-tools-and-tutorials/118456-update-script-for-linux)
