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
            "telegram-desctop",
            "mattermost",
            "make",
            "cmake",
            "fzf",
            "pyenv",
            "tree",
        ],
        update=True,
        upgrade=True,
    )


server.shell(
    commands=[
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish)"'
    ]
)

# fisher
server.shell(
    commands=[
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher)"'
    ]
)

server.shell(commands=['sh -c "$(fisher install jorgebucaran/nvm.fish)"'])
# theme
server.shell(commands=['sh -c "$(fisher install pure-fish/pure)"'])
# rust
server.shell(
    commands=['sh -c "$(curl --proto=https --tlsv1.2 -sSf https://sh.rustup.rs | sh)"']
)