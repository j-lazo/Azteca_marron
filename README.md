# Design and construction of a control system for the autonomous driving of the electric car *El Azteca Marron*

This repo contains the codes and some documentation related to the project **Design and construction of a control system to
achieve the autonomous driving of the electric car *El Azteca Marron* under controlled environments.** 

The development of this project different methods and techniques were used, including: the implementation of a fuzzy-logic-based system was implemented in the control of the
steering wheel. The detection of the surroundings was achieved by making use a set of different kind of sensing systems, these were LIDAR and ultrasonic sensors along with cameras and
computer vision algorithms. In the case of the computer vision system different edge detection techniques, including the use of the Hough transform, were implemented in order to detect the
borders of the road.

The master control unit was implemented using the embedded board PcDuino and the programing languages Python and C++. Several tests were carried out by separate for each of the systems, this
were: the braking system, the surroundings and obstacle detection system and the steering wheel system. In the final stage, all the systems were tested altogether. The tests carried out to evaluate the
motion of the vehicle were performed in two different steps; first, the car was set still by placing it over a base from which the response of the actuators, afterward, the test were carried out taking off
the restraints, allowing the movement of the car. A graphic interface was added and connected to the embedded board which was tried within the other systems.
The vehicle was able to avoid obstacles still and in movement, detected between a range of 10 to 25 meters at a speed of 7km/h.

The complete report can be found here:

![PDF](https://drive.google.com/open?id=1AQz76EegUP3XW2wpDUsQXpY6KcQkYidY) (Only in Spanish)

Some videos documenting the tests carried out can be seen here:
https://www.youtube.com/channel/UCT0Ob93REGyEb-Z6Aw5lSOA
