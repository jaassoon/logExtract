source ./envConst.sh
source ./fileNameConst.sh
outputFile=$CURRENT_DATE.log
if [ -e $outputFile ];then
  rm $outputFile
fi
while read -r line; do
  if [[ $line == *"concurrent-sweep-start]"* ]];then
    echo $line >>$outputFile
  fi
done <$BASE_PATH$GC_LOG_NAME
#done <../data/gc-20190119.csv

#how to use [[]]
#https://stackoverflow.com/questions/13781216/meaning-of-too-many-arguments-error-from-if-square-brackets
# it might work from the console but not from cron, depending on how everything is configured.


