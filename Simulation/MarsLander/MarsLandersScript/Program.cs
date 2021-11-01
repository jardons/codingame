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
		public const double GRAVITY = 3.711; // m/s²

		public State ApplyCommand(Command c, State s)
		{
			if (c.Power == 0)
			{
				// ^X = Vi * ^t + 1/2 * a * ^t²
				double deltaY = s.YSpeed + (GRAVITY * (1.0)) / 2.0;

				return new State
				{
					Fuel = s.Fuel,
					Y = s.Y - deltaY,
					X = s.X,
					XSpeed = s.XSpeed,
					YSpeed = s.YSpeed + GRAVITY,
					Rotate = c.Rotate,
					Power = c.Power
				};
			}
			else if (c.Power == s.Power)
				return new State
				{
					Fuel = s.Fuel - 1,
					Y = s.Y,
					X = s.X,
					XSpeed = s.XSpeed,
					YSpeed = s.YSpeed,
					Rotate = c.Rotate,
					Power = c.Power
				};
			else
				throw new NotImplementedException();
		}
	}

	class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");
		}
	}
}
