import turtle as t;
import time;
def drawgap():
	t.penup();
	t.fd(5);
def drawline(draw):
	drawgap();
	if draw:
		t.pendown();
	else:
		t.penup();
	t.fd(40);
	drawgap();
	t.right(90);
def drawdigit(digit):
	if digit in [2,3,4,5,6,8,9]:
		drawline(True);
	else:
		drawline(False);
	if digit in [0,1,3,4,5,6,7,8,9]:
		drawline(True);
	else:
		drawline(False);
	if digit in [0,2,3,5,6,8,9]:
		drawline(True);
	else:
		drawline(False);
	if digit in [0,2,6,8]:
		drawline(True);
	else:
		drawline(False);
	t.left(90);
	if digit in [0,4,5,6,8,9]:
		drawline(True);
	else:
		drawline(False);
	if digit in [0,2,3,5,6,7,8,9]:
		drawline(True);
	else:
		drawline(False);
	if digit in [0,1,2,3,4,7,8,9]:
		drawline(True);
	else:
		drawline(False);
	t.left(180);
	t.penup();
	t.fd(20);
def drawdate(date):
	t.pencolor('red')
	for i in date:
		if i=='-':
			t.right(90);
			t.fd(50);
			t.write('年',font=('MS Gothic',18,'normal'));
			t.pencolor('green');
			t.bk(50);
			t.left(90);
			t.fd(40);
		elif i=='=':
			t.right(90);
			t.fd(50);
			t.write('月',font=('MS Gothic',18,'normal'));
			t.pencolor('blue');
			t.bk(50);
			t.left(90);
			t.fd(40);
		elif i=='+':
			t.right(90);
			t.fd(50);
			t.write('日',font=('MS Gothic',18,'normal'));
		else:
			drawdigit(eval(i));
def main():
	t.setup(800,350,200,200);
	t.penup();
	t.fd(-300);
	t.pensize(5);
	drawdate(time.strftime('%Y-%m=%d+',time.gmtime()));
	t.hideturtle();
	t.done();
main();