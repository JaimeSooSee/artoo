/*--------------------------------------------
R2D2
--------------------------------------------*/
var _artoo;
function r2d2()
{
	if (_artoo == undefined)
	{
		var motor1 = new Motor(2,3);
		var motor2 = new Motor(4,17);
		_artoo = new R2D2(motor1, motor2);
	}
	return _artoo;
}

function R2D2(motor1, motor2)
{
	this.motor1 = motor1;
	this.motor2 = motor2;
}

R2D2.prototype.moveForward = function()
{
	this.motor1.forward();
	this.motor2.forward();
}

R2D2.prototype.moveBackward = function()
{
	this.motor1.backward();
	this.motor2.backward();
}

R2D2.prototype.turnLeft = function()
{
	this.motor1.backward();
	this.motor2.forward();
}

R2D2.prototype.turnRight = function()
{
	this.motor1.forward();
	this.motor2.backward();
}

R2D2.prototype.stop = function()
{
	this.motor1.stop();
	this.motor2.stop();
}

R2D2.prototype.shutdown = function()
{
	this.motor1.shutdown();
	this.motor2.shutdown();
}

