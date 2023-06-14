counter=0
inc = 1
DST='.'
for i in `ls all_audio`
    cp ./all_audio/$i $DST
    counter=`expr $counter + $inc`
    if `$counter -eq 500`
        break
    fi
done