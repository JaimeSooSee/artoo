/*--------------------------------------------
R2D2
--------------------------------------------*/
var _artoo;
function r2d2()
{
	if (_artoo == undefined)
	{
		_artoo = new R2D2();
	}
	return _artoo;
}

function R2D2()
{
}

R2D2.prototype.moveForward = function()
{
	webiopi().callMacro("moveForward", []);
}

R2D2.prototype.moveBackward = function()
{
	webiopi().callMacro("moveBackward", []);
}

R2D2.prototype.turnLeft = function()
{
	webiopi().callMacro("turnLeft", []);
}

R2D2.prototype.turnRight = function()
{
	webiopi().callMacro("turnRight", []);
}

R2D2.prototype.stop = function()
{
	webiopi().callMacro("motorStop", []);
}

R2D2.prototype.shutdown = function()
{
	webiopi().callMacro("shutdown", []);
}

