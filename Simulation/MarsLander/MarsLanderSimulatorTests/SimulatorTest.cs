using MarsLandersScript;
using System;
using Xunit;

namespace MarsLanderSimulatorTests
{
	public class SimulatorTest
	{
		[Theory]
		[InlineData(2700, 2698, 4, 1)]
		[InlineData(2700, 2693, 7, 2)]
		[InlineData(2700, 2683, 11, 3)]
		[InlineData(2700, 2670, 15, 4)]
		[InlineData(2700, 2654, 19, 5)]
		[InlineData(2700, 2633, 22, 6)]
		[InlineData(2700, 2609, 26, 7)]
		[InlineData(2700, 2581, 30, 8)]
		[InlineData(2700, 2550, 33, 9)]
		[InlineData(2700, 2514, 37, 10)]
		[InlineData(2700, 2475, 41, 11)]
		[InlineData(2700, 2433, 45, 12)]
		[InlineData(2700, 2386, 48, 13)]
		[InlineData(2700, 2336, 52, 14)]
		[InlineData(2700, 2283, 56, 15)]
		[InlineData(2700, 2225, 59, 16)]
		[InlineData(2700, 2164, 63, 17)]
		[InlineData(2700, 2099, 67, 18)]
		[InlineData(2700, 2030, 71, 19)]
		[InlineData(2700, 1958, 74, 20)]
		[InlineData(2700, 1245, 104, 28)]
		public void FreeFall(int altitude, int expected, int expectedSpeed, int turns)
		{
			Simulator sim = new Simulator();
			State s = new State { Y = altitude, X = 2500 };

			for (int i = 0; i < turns; ++i)
				s = sim.ApplyCommand(new Command { Power = 0, Rotate = 0 }, s);

			Assert.Equal(expected, (int)Math.Round(s.Y));
			Assert.Equal(expectedSpeed, (int)Math.Round(s.YSpeed));
		}
	}
}
