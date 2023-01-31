#!/bin/bash
for ((i=0;i < 10000;i++));do 
	echo "$i hyu" >> hook
	git add .
	git commit -m "$i kun"
	git push 
	echo "$i hyn" >> hook
        git add .
        git commit -m "$i kuno"
        git push
done
