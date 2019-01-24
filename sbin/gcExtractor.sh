. ../config/shell_env.sh
. ../config/file_const.sh
. ./validator.sh
IS_PATH_EXIST
outputFile=$TODAY.log
if [ -e $outputFile ];then
  rm $outputFile
fi
while read -r line; do
  if [[ $line == *"concurrent-sweep-start]"* ]];then
    echo $line >>$outputFile
  fi
done <$BASE_PATH/$GC_LOG_NAME

gzip $BASE_PATH/$GC_LOG_NAME
#how to use [[]]
#https://stackoverflow.com/questions/13781216/meaning-of-too-many-arguments-error-from-if-square-brackets
# it might work from the console but not from cron, depending on how everything is configured.


