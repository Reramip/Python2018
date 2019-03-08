instr=input();
length=len(instr);
for i in range(length):
	if instr[i]==' ':
		continue;
	else:
		if instr[i] in['x','y','z']:
			instr=instr[:i]+chr((ord(instr[i])-23))+instr[i+1:];
		else:
			instr=instr[:i]+chr((ord(instr[i])+3))+instr[i+1:];
print(instr);