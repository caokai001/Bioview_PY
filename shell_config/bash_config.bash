#！bin/bash
#https://linux.cn/article-9954-1.html

path_dir_src=$(pwd)/../src
cd $path_dir_src

#修改src *.py 执行权限
for i in `ls`;
do 
	chmod 755 $i
done
# 将src 中python导入环境变量中，并恢复原始目录
export PATH=`pwd`/../src:$PATH
cd ${path_dir_src}/../shell_config


bio_less(){
	file=$1
	echo $file
	if [[ $file==*.fa ]];then
		dna_fa.py fa $file |less -rS
	else
		less -S $file
	fi
}

fa_less(){
	file=$1
	dna_fa.py fa $file |less -rS
}

