start_section Install-Yosys
(
    if [ ! -e ~/.local-bin/bin/yosys ]; then
        echo '=========================='
        echo 'Building yosys'
        echo '=========================='
        mkdir -p ~/.local-src
        mkdir -p ~/.local-bin
        cd ~/.local-src
        git clone https://github.com/SymbiFlow/yosys.git -b master+wip
        cd yosys
        make config-gcc # Build Yosys using GCC
        PREFIX=$HOME/.local-bin make -j$(nproc)
        PREFIX=$HOME/.local-bin make install
        echo $(which yosys)
        echo $(which yosys-config)
        echo $(yosys-config --datdir)
    fi
)
end_section
