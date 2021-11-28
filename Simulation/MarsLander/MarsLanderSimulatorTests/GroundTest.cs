using MarsLandersScript;
using System;
using Xunit;

namespace MarsLanderSimulatorTests
{
	public class GroundTest
	{
		[Fact]
		public void Create()
		{
			Point[] points = { new Point(0, 100), new Point(100, 500), new Point(600, 400), new Point(1000, 400), new Point(1200, 401) };
			
			Ground g = new Ground(points);

			Assert.Equal(400, g.Altitude);
			Assert.Equal(600, g.Left);
			Assert.Equal(1000, g.Right);
			Assert.Equal(800, g.Center);
		}
	}
}
