search_dir="/tmp/test*.txt"
myuser="demo_drjohndoe"
mypw="passw0rd"
mycd="CD_LINUX"
mysfgcd="VM_SI_CD"

echo "/* BEGIN_REQUESTER_COMMENTS"                  > Copy2SFG.cdp
echo "   \$PNODE\$='$mycd' \$PNODE_OS\$='UNIX'" >> Copy2SFG.cdp
echo "   \$SNODE\$='$mysfgcd' \$SNODE_OS\$='UNIX'" >> Copy2SFG.cdp
echo "   \$OPTIONS\$=''"                           >> Copy2SFG.cdp
echo "   END_REQUESTER_COMMENTS*/"                 >> Copy2SFG.cdp
echo ""  >> Copy2SFG.cdp

echo "COPY2SFG PROCESS"           >> Copy2SFG.cdp
echo "	SNODE=$mysfgcd"           >> Copy2SFG.cdp
echo "	SNODEID=($myuser,$mypw)"  >> Copy2SFG.cdp

i=0
for entry in `ls $search_dir`; do
entry_old="$entry.delete"

echo ""  >> Copy2SFG.cdp
echo "CPY$i COPY"                    >> Copy2SFG.cdp
echo "  FROM ("                  >> Copy2SFG.cdp
echo "    FILE='$entry'"         >> Copy2SFG.cdp
echo "    PNODE"                 >> Copy2SFG.cdp
echo "  )"                       >> Copy2SFG.cdp
echo "  TO ("                    >> Copy2SFG.cdp
echo "    FILE='/MAILBOX/Inbox'" >> Copy2SFG.cdp
echo "    SNODE"                 >> Copy2SFG.cdp
echo "    DISP=RPL"              >> Copy2SFG.cdp
echo "  )"                       >> Copy2SFG.cdp

echo ""  >> Copy2SFG.cdp
echo "/*IFCPY$i IF (CPY$i EQ 0) THEN"  >> Copy2SFG.cdp
echo "  RUN TASK PNODE SYSOPTS='mv $entry $entry_old'"  >> Copy2SFG.cdp
echo "EIF*/"  >> Copy2SFG.cdp

i=$((i+1))
    
done

echo ""      >> Copy2SFG.cdp
echo "RUNECHO RUN TASK PNODE SYSOPTS='echo Dummy'" >> Copy2SFG.cdp
echo ""      >> Copy2SFG.cdp
echo "PEND"  >> Copy2SFG.cdp

#cat Copy2SFG.cdp

# /..../direct submit=Copy2SFG.cdp

