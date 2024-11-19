from pyinfra.operations import pacman, server


def packages():
    pacman.packages(
        packages=[
            "jq",
            "ripgrep",
            "vim",
            "neovim",
            "micro",
            "git",
            "btop",
            "nodejs",
            "docker",
            "tmux",
            "fish",
            "telegram-desktop",
            "mattermost-desktop",
            "make",
            "cmake",
            "fzf",
            "pyenv",
            "tree",
            "gcc",
        ],
        update=True,
        upgrade=True,
        _sudo=True,
    )


# Map Caps to ESC
server.shell(
    commands=[
        "gsettings set org.gnome.desktop.input-sources xkb-options \"['caps:swapescape']\""
    ]
)

# oh-my-fish
server.shell(
    commands=[
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish)"'
    ]
)

# fisher
server.shell(
    commands=[
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher)"  | grep -e "Already installed" -e "installed"'
    ]
)

# NVM
server.shell(commands=['sh -c "$(fisher install jorgebucaran/nvm.fish)"'])

# theme
server.shell(commands=['sh -c "$(fisher install pure-fish/pure)"'])

# rust
server.shell(
    commands=['sh -c "$(curl --proto=https --tlsv1.2 -sSf https://sh.rustup.rs | sh)"']
)

packages()

# TODO:
# google chrome
# vscode
# jetbrains toolbox
