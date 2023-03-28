#! /bin/bash

if [ ! -d "/home/vscode/.oh-my-zsh/custom/plugins/zsh-autosuggestions" ]; then
  sudo git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
fi

cp ./.devcontainer/scripts/files/zshrc_template ~/.zshrc
