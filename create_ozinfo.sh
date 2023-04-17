# create global_ozinfo file for a given date
date=$1
# header
echo '! For mls data, pressure and obs errors are pulled from bufr, so not listed here'
echo '! sens/instr/sat lev  use pressure gross   obs    b_oz  pg_oz'
echo '!                                  error  error variational qc'
# loop over satellites
cd ozinfo
for sat in $(cat satellites); do
    # find matching date
    usedate=""
    for f in $sat/*; do
        if [ $f != "$sat/readme" ]; then # skip readme file
           datex=`basename $f`
	   if [ $date -ge $datex ]; then
              usedate=$datex
           fi
        fi
    done
    # cat matching date file, or quit if date not found
    if [ $usedate != "" ]; then
        cat $sat/$usedate
    else
        echo "date not found for $sat"
	exit 1
    fi
done
