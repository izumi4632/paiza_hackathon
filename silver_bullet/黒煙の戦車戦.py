h,w,k=[int(i) for i in input().split()]
stage = [input() for i in range(h)]
now_w = stage[0].index(str(k))
if w == 1:
	print(stage[-1][0])
	exit()
for now_h in range(1, h-1):
	if now_w == 0:
		if stage[now_h][1] == ".":
			now_w = 2
	elif now_w == w-1:
		if stage[now_h][w-2] == ".":
			now_w = w-3
	else:
		if stage[now_h][now_w-1] == ".":
			now_w -= 2
		elif stage[now_h][now_w+1] == ".":
			now_w += 2
print(stage[h-1][now_w])