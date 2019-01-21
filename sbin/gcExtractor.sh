currentDate=$(date +%Y%m%d)
fileName=$currentDate.log
if [ -e $fileName ];then
  rm $currentDate.log
fi
while read -r line; do
  if [[ $line == *"concurrent-sweep-start]"* ]];then
    echo $line >>$currentDate.log
  fi
done <../data/gc.log
#done <../data/gc-20190119.csv

#how to use [[]]
#https://stackoverflow.com/questions/13781216/meaning-of-too-many-arguments-error-from-if-square-brackets
# it might work from the console but not from cron, depending on how everything is configured.


