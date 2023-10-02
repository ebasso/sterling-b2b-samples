#!/bin/bash

set +vx
NDMAPICFG=/home/cdadmin02/cdunix/ndm/cfg/cliapi/ndmapi.cfg
export NDMAPICFG

# executa o sel pro
selpro_output=$(/home/cdadmin02/cdunix/ndm/bin/direct -s << EOJ
selpro;
EOJ
)

count=$(echo "$selpro_output" | grep -c "HOLD" )
if [ $count -gt 0 ]; then
    echo "processos em HOLD - $count vezes:" > processo_HOLD.out
else
    echo "" > processo_HOLD.out
fi

count=$(echo "$selpro_output" | grep -c "WAIT" )
if [ $count -gt 0 ]; then
    echo "processos em WAIT - $count vezes:" > processo_WAIT.out
else
    echo "" > processo_WAIT.out
fi


# Defina os PNAME
strings=("COPY2SFG" "processo2" "processo3")

for str in "${strings[@]}"; do
    # conta HOLD ou WAIT e conta o processo
    count=$(echo "$selpro_output" | grep -e "HOLD" -e "WAIT" | grep -c "$str")

    if [ $count -gt 0 ]; then
        echo "O processo '$str' ocorre $count vezes:" > processo_"$str".out
    else
        echo "" > processo_"$str".out
    fi
done
