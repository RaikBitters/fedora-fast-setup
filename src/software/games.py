# Games app install

import os
os.system("sudo dnf update -y")

# Games launchers
os.system("sudo dnf install -y steam")
os.system("sudo dnf install -y lutris")

# Discord
os.system("flatpak install -y flathub com.discordapp.Discord")