#!/bin/bash
echo -e "$0 - SOB Software - (c) 2020\n"

if [[ $# != 2 ]]; then
   echo -e "Use:\t$0 <diretório> <arquivo>"
   echo -e "Onde:\t<diretório> - path que será processado."
   echo -e "\t<arquivo> - arquivo de saída."
   exit 1
fi

while read file
do
   if [[ "$file" != *"RECYCLE"* && "$file" != *"System Volume Information"* ]]; then
      grep "$file" $2 > /dev/null 2>&1
      if [[ $? != 0 ]]; then
         md5sum=`md5sum "$file" | cut -d \  -f 1` filedata=`ls --full-time "$file"`
         data=`echo $filedata | cut -d \  -f 6,7`
         size=`echo $filedata | cut -d \  -f 5`
         echo file=\"$file\" md5sum=\"$md5sum\" data=\"$data\" size=\"$size\" | tee -a $2
      fi
   fi
done < <(find "$1" -type f)
