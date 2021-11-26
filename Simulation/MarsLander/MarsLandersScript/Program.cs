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
		public int Rotate;
		public int Power;
	}

	public class Simulator
	{
		public const double GRAVITY = -3.711; // m/s²

		public State ApplyCommand(Command c, State s)
		{
			double newSpeed = GRAVITY + c.Power;
			// ^X = Vi * ^t + 1/2 * a * ^t²
			double deltaY = s.YSpeed + newSpeed / 2.0;

			return new State
			{
				Fuel = s.Fuel - c.Power,
				Y = s.Y + deltaY,
				X = s.X,
				XSpeed = s.XSpeed,
				YSpeed = s.YSpeed + newSpeed,
				Rotate = c.Rotate,
				Power = c.Power
			};
		}
	}
}
