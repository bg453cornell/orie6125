schema='(A,C)'
filename='quote_files.txt'
filelines=`cat $filename`
directory=taq.12.2014/
echo Start

for line in $filelines ; do
    echo $line
    locate_dir=$'s3://'$directory$line
    sudo aws s3 cp $locate_dir ./temp.zip;
    name_file="$(unzip -l temp.zip | awk '/-----/ {p = ++p % 2; next} p {print $NF}')";
    date=${name_file: -8};
    echo $name_file
    unzip temp.zip; 
    rm -f temp.zip;
    sh ./import_temporal_quote.sh $name_file $date;
    rm $name_file;
done


