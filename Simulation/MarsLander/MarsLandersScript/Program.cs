using System;

namespace MarsLandersScript
{
	public class State
	{
		public int Fuel;
		public double Y;
		public double X;
		public double XSpeed;
		public double YSpeed;
		public int Rotate;
		public int Power;
	}

	public class Command
	{
		public int Rotate;	// degree
		public int Power;   // m/s²

		public double XPower => Power * Math.Sin(Rotate / 180.0 * Math.PI);
		public double YPower => Power * Math.Cos(Rotate / 180.0 * Math.PI);
	}

	public class Simulator
	{
		public const double GRAVITY = -3.711; // m/s²

		public State ApplyCommand(Command c, State s)
		{
			double newYSpeed = GRAVITY + c.YPower;
			double newXSpeed = -c.XPower;

			// ^X = Vi * ^t + 1/2 * a * ^t²
			double deltaY = s.YSpeed + newYSpeed / 2.0;
			double deltaX = s.XSpeed + newXSpeed / 2.0;

			return new State
			{
				Fuel = s.Fuel - c.Power,
				Y = s.Y + deltaY,
				X = s.X + deltaX,
				XSpeed = s.XSpeed + newXSpeed,
				YSpeed = s.YSpeed + newYSpeed,
				Rotate = c.Rotate,
				Power = c.Power
			};
		}
	}
}
