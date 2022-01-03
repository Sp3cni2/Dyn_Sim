Dyn_Sim

  branches are just like bread:
  a. baked is ready for use.
  b. rising is candidate in testing, mostly for exceptions.
  c. mixing is experimental, like in-dev or something. Untested, please don't eat dough.


  That is very much pre-alpha phase of the framework.
  
  so far I have done:
  
  1. most classes representing both elements of our model like engine or tank.
  2. their respective builder classes. User will only have to choose from available names. 
  2.a. will gather everything in a factory (when I finally decide how it will compose together)
  3. Both 3 degrees of freedom and 6 degrees of freedom equation of motion, simplified for the time being.
  4. ordinary differential equation solution method, namely Runge-Kutta 45 method.
  5. Some abstract classes for interfacing and ease of developing
  
  Current testing enviromnent is in /prototype/ItemLoader.py
