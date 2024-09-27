/**\
 * Time Complexity Explanation and Solution in JavaScript
User: A video game developer is creating a game involving enemy aircraft. In the game, each plane
has a starting position above the ground level and a speed at which it is descending. The player
character has a gun that can shoot one aircraft during each second. The game ends when a plane
is allowed to land. Determine the maximum number of planes that can be prevented from landing.
Example startHeight =[1, 3,5,4,8] descentRate =[1, 2,2,1,2]
Assistant:
This problem can be approached by tracking when each aircraft will hit the ground and ensuring that
the player shoots the planes in such a way that prevents the maximum number from landing.
Problem Breakdown:
- You are given two arrays: startHeight and descentRate.
- startHeight[i] indicates the height of the i-th plane at the start.
- descentRate[i] indicates how much the height decreases per second.
- You need to shoot the planes to prevent them from landing, with the constraint that you can shoot
one plane per second.
- The game ends if any plane is allowed to reach the ground (height <= 0).
Approach:
1. Calculate when each plane will land: For each plane, the time it takes to land can be calculated
as:
timeToLand[i] = startHeight[i] / descentRate[i]
This gives the number of seconds before the plane reaches the ground.
2. Sort the planes by their time to land: To maximize the number of planes shot down, prioritize
shooting planes that will land the soonest. This can be done by sorting the planes based on their
landing times.
3. Simulate the shooting: Start from time 0, and at each second, shoot the plane that will land the
soonest. If a plane lands before you can shoot it, the game ends.
 * 
 */


function maxPlanesPrevented(startHeight, descentRate) {
  // Calculate the time each plane takes to land
  let landingTimes = startHeight.map((height, index) => ({
    timeToLand: height / descentRate[index],
    index: index,
  }));
  // Sort the planes by their landing times (earliest first)
  landingTimes.sort((a, b) => a.timeToLand - b.timeToLand);
  let time = 0;
  let planesShot = 0;
  // Simulate shooting the planes
  for (let i = 0; i < landingTimes.length; i++) {
    if (time < landingTimes[i].timeToLand) {
      planesShot++;
      time++; // We shoot one plane per second
    } else {
      break; // If a plane lands before we can shoot, the game ends
    }
  }
  return planesShot;
}

// Example usage:
const startHeight = [1, 3, 5, 4, 8];
const descentRate = [1, 2, 2, 1, 2];
console.log(maxPlanesPrevented(startHeight, descentRate)); // Output: 5


/**
 * Explanation:
1. Landing Time Calculation:
- We use map to create an array of objects, where each object contains:
- timeToLand: the time it takes for each plane to land (startHeight[i] / descentRate[i]).
- index: the index of the plane (for possible reference, though it's not used further).
2. Sorting Planes by Landing Time:
- We sort the planes based on their timeToLand in ascending order so that we can deal with
planes that are closest to landing first.
3. Simulation of Shooting:
- A loop runs over the sorted planes, and if the current time (time) is less than the plane's
timeToLand, it means the plane hasn't landed yet, so we shoot it and increment the time.
- If at any point the current time is greater than or equal to a plane's timeToLand, the game ends.
Output:
- The result for the example inputs is 5, meaning all planes are shot down before landing.
Time Complexity Explanation:
The time complexity of the solution can be broken down as follows:
1. Calculating landing times (map operation):
- The map function iterates through the startHeight and descentRate arrays once, and for each
plane, it calculates the time to land.
- This takes O(n) time, where n is the number of planes.
2. Sorting the planes by landing times:
- The sort function sorts the array of landing times, which is based on comparison sorting.
- The time complexity of sorting is O(n log n).
3. Simulating the shooting of planes (for loop):
- The for loop iterates through the sorted list of planes once to simulate shooting, which takes O(n)
time.
Overall Time Complexity:
- The most time-consuming step is the sorting operation, which is O(n log n).
- Thus, the overall time complexity of the solution is O(n log n).
 */