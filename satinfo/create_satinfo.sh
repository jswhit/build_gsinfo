date=$1
echo '!sensor/instr/sat      chan iuse  error  error_cld  ermax   var_b    var_pg  icld_det icloud iaerosol'
for sat in $(cat satellites); do
    usedate=""
    for f in $sat/*; do
        if [ $f != "$sat/readme" ]; then
           datex=`basename $f`
	   if [ $date -ge $datex ]; then
              usedate=$datex
           fi
        fi
    done
    if [ $usedate != "" ]; then
        cat $sat/$usedate
    else
        echo "date not found for $sat"
	exit 1
    fi
done
