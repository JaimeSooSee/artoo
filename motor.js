/*--------------------------------------------
Motor
--------------------------------------------*/
function Motor(gpio1, gpio2)
{
	this.gpio1 = gpio1;
	this.gpio2 = gpio2;
}

Motor.prototype.forward = function()
{
	webiopi().digitalWrite(this.gpio1, 1);
	webiopi().digitalWrite(this.gpio2, 0);
};

Motor.prototype.backward = function()
{
	webiopi().digitalWrite(this.gpio1, 0);
	webiopi().digitalWrite(this.gpio2, 1);
};

Motor.prototype.stop = function()
{
	webiopi().digitalWrite(this.gpio1, 1);
	webiopi().digitalWrite(this.gpio2, 1);
};