#!/usr/bin/env bash
for i in $(seq 0 9)
do for j in $(seq 0 9)
	do for k in $(seq 0 9)
			do for l in $(seq 0 9)
				do echo $i$j$k$l | ./breakme.out 
			done
		done
	done
done

# for i in {0000..9999}; do echo $i | ./breakme.out; done