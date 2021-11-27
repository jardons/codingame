using MarsLandersScript;
using System;
using Xunit;

namespace MarsLanderSimulatorTests
{
	public class SimulatorTest
	{
		[Theory]
		[InlineData(2700, 2698, -4, 1)]
		[InlineData(2700, 2693, -7, 2)]
		[InlineData(2700, 2683, -11, 3)]
		[InlineData(2700, 2670, -15, 4)]
		[InlineData(2700, 2654, -19, 5)]
		[InlineData(2700, 2633, -22, 6)]
		[InlineData(2700, 2609, -26, 7)]
		[InlineData(2700, 2581, -30, 8)]
		[InlineData(2700, 2550, -33, 9)]
		[InlineData(2700, 2514, -37, 10)]
		[InlineData(2700, 2475, -41, 11)]
		[InlineData(2700, 2433, -45, 12)]
		[InlineData(2700, 2386, -48, 13)]
		[InlineData(2700, 2336, -52, 14)]
		[InlineData(2700, 2283, -56, 15)]
		[InlineData(2700, 2225, -59, 16)]
		[InlineData(2700, 2164, -63, 17)]
		[InlineData(2700, 2099, -67, 18)]
		[InlineData(2700, 2030, -71, 19)]
		[InlineData(2700, 1958, -74, 20)]
		[InlineData(2700, 1245, -104, 28)]
		public void FreeFall(int altitude, int expected, int expectedSpeed, int turns)
		{
			Simulator sim = new Simulator();
			State s = new State { Y = altitude, X = 2500 };

			for (int i = 0; i < turns; ++i)
				s = sim.ApplyCommand(new Command { Power = 0, Rotate = 0 }, s);

			Assert.Equal(expected, (int)Math.Round(s.Y));
			Assert.Equal(expectedSpeed, (int)Math.Round(s.YSpeed));
		}

		[Theory]
		[InlineData(2700, 2698, -4, 1, 1)]
		[InlineData(2700, 1245, -104, 1, 28)]
		[InlineData(2700, 1245, -104, 2, 28)]
		[InlineData(2700, 1245, -104, 3, 28)]
		[InlineData(2700, 1245, -104, 4, 28)]
		[InlineData(2700, 1245, -104, 5, 28)]
		[InlineData(2700, 1245, -104, 10, 28)]
		[InlineData(2700, 1245, -104, 15, 28)]
		[InlineData(2700, 1245, -104, -5, 28)]
		[InlineData(2700, 1245, -104, -10, 28)]
		[InlineData(2700, 1245, -104, -15, 28)]
		public void FreeFallTilted(int y, int expectedY, int expectedYSpeed, int rotate, int turns)
		{
			Simulator sim = new Simulator();
			State s = new State { Y = y, X = 2500 };

			for (int i = 0; i < turns; ++i)
				s = sim.ApplyCommand(new Command { Power = 0, Rotate = rotate }, s);

			Assert.Equal(expectedY, (int)Math.Round(s.Y));
			Assert.Equal(expectedYSpeed, (int)Math.Round(s.YSpeed));
			Assert.Equal(2500, (int)Math.Round(s.X));
			Assert.Equal(0, (int)Math.Round(s.XSpeed));
		}

		[Theory]
		[InlineData(2700, 2699, -3, 1, 1)]
		[InlineData(2700, 2695, -5, 1, 2)]
		[InlineData(2700, 2688, -8, 1, 3)]
		[InlineData(2700, 2678, -11, 1, 4)]
		[InlineData(2700, 2666, -14, 1, 5)]
		[InlineData(2700, 1224, -89, 1, 33)]
		public void VerticalPower(int altitude, int expected, int expectedSpeed, int power, int turns)
		{
			Simulator sim = new Simulator();
			State s = new State { Y = altitude, X = 2500 };

			for (int i = 0; i < turns; ++i)
				s = sim.ApplyCommand(new Command { Power = power, Rotate = 0 }, s);

			Assert.Equal(expected, (int)Math.Round(s.Y));
			Assert.Equal(expectedSpeed, (int)Math.Round(s.YSpeed));
		}

		[Theory]
		[InlineData(2700, 2500, 2699, 2500, -3, 0, 15, 1, 1)]
		[InlineData(2700, 2500, 2695, 2499, -5, -1, 15, 1, 2)]
		[InlineData(2700, 2500, 2688, 2499, -8, -1, 15, 1, 3)]
		[InlineData(2700, 2500, 2678, 2498, -11, -1, 15, 1, 4)]
		[InlineData(2700, 2500, 2666, 2497, -14, -1, 15, 1, 5)]
		[InlineData(2700, 2500, 1465, 2384, -82, -8, 15, 1, 30)]
		[InlineData(2700, 2500, 2699, 2500, -3, 0, -15, 1, 1)]
		[InlineData(2700, 2500, 2695, 2501, -5, 1, -15, 1, 2)]
		[InlineData(2700, 2500, 2688, 2501, -8, 1, -15, 1, 3)]
		[InlineData(2700, 2500, 2678, 2502, -11, 1, -15, 1, 4)]
		[InlineData(2700, 2500, 2666, 2503, -14, 1, -15, 1, 5)]
		[InlineData(2700, 2500, 1465, 2616, -82, 8, -15, 1, 30)]
		public void TiltedPower(int y, int x, int expectedY, int expectedX, int expectedYSpeed, int expectedXSpeed, int rotate, int power, int turns)
		{
			Simulator sim = new Simulator();
			State s = new State { Y = y, X = x };

			for (int i = 0; i < turns; ++i)
				s = sim.ApplyCommand(new Command { Power = power, Rotate = rotate }, s);

			Assert.Equal(expectedY, (int)Math.Round(s.Y));
			Assert.Equal(expectedYSpeed, (int)Math.Round(s.YSpeed));
			Assert.Equal(expectedX, (int)Math.Round(s.X));
			Assert.Equal(expectedXSpeed, (int)Math.Round(s.XSpeed));
		}
	}
}
