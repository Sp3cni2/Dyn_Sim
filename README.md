Dyn_Sim

  branches are just like bread:
  
  a. baked is ready for use.
  
  b. rising is candidate in testing, mostly for exceptions.
  
  c. mixing is experimental, like in-dev or something. Untested, please don't eat dough.


  That is very much pre-alpha phase of the framework.
  
  so far I have done:
  
  1. most classes representing both elements of our model like engine or tank.
  2. their respective builder classes. User will only have to choose from available names. 
  4. will gather everything in a factory (when I finally decide how it will compose together)
  5. Both 3 degrees of freedom and 6 degrees of freedom equation of motion, simplified for the time being.
  6. ordinary differential equation solution method, namely Runge-Kutta 45 method.
  7. Some abstract classes for interfacing and ease of developing
  
  Current testing enviromnent is in /prototype/ItemLoader.py


  TODO:
  1. Factory according to /prototype/Models.py
  2. Equations and Vectors for Quaterion and Spherical coordinate systems.
  3. Add actual dynamics like fluids and stuff.
  4. Add Simulation Schemes. 
  999. rewrite in C++ and C for practice.
