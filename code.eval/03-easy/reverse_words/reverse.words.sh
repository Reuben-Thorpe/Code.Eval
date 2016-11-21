# Reuben Thorpe (2016), CodeEval [Reverse Words v1.4]

while read line || [[ -n "$line" ]]; do
   echo $line | awk '{ for (i=NF; i>1; i--) printf("%s ",$i); print $1; }'
done < $1
