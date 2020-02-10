# Answers

## `gps.py`
 1. Is the GPS problem solver implemented as a class or as a function?
   - it is implemented as a function that takes `initial_states`. `goal_states`, and `operators` as input and returns a list of strings of sequence of actions.

 2. The solver requires initial states, goal states and operators. Of what type are these objects?
  - They are all `python` list types. Upon inspection of the `monkeys.py` file, it seems like initial and goal states are lists of strings and operators are lists of `python` dictionaries.
  
 3. Is the mechanism recursive? If so, how does it implement its recursion?
  - Yes.
  - The `achieve_all` function calls the `achieve` function that calls `apply_operators` function that eventually calls the `achieve_all` function. The base case is handled by the `achieve` function through inspecting the `goal_stack`.

## `monkeys.py`
 1. What famous puzzle does this code model and what are the rules of that puzzle? Does the code faithfully implement the puzzle?
  - The code is modeled after the [Monkey and Banana Problem](https://en.wikipedia.org/wiki/Monkey_and_banana_problem).
  - A few states are different from the example given by the Wikipedia entry. The monkey has a ball that it needs to drop, and there is not stick that extends the monkey's reach in order to get the banana. Nevertheless, the basic premise is the same, and the modifications are interchangeable.

 2. What components does each domain action specify?
  - Each domain action specifies an action, preconditions, added state(s), and deleted state(s).

 3. How does the GPS mechanism solve the problem? Be prepared to specify this in detail. You can use the logging feature to print a trace of the mechanism’s deliberations.
  - The GPS starts from the desired goal state and recursively looks for states that satisfy each of the their preconditions until it finds the initial state. Then it returns actions that have met preconditions up the recursion tree. As it climbs back up the tree, if it meets an unsatisfied goal condition (for instance the drop ball condition in our example) it down another branch until it finds a satisfied state and continues climb back up the tree until the final precondition is fulfilled.
  
 4. Is this code artificially intelligent? If so, which definition (or definitions) of AI from the text does it satisfy?
  - It is somewhat intelligent once given a predefined chain of instructions. It is not "Acting Humanly" because we cannot prove that it passes the Turing Test. It cannot be "Acting Rationally" because it does not handle uncertainty like a Rational Agent, that is, the best expected outcome. Likewise, we cannot conclude that it is "thinking humanly" because there is not proof of it reflecting "human behavior". Thus, it is most likely "Thinking Rationally". It shows conditional and logical approach of reaching a goal.
  
 5. Would a monkey who/that solves the problem in the real world be displaying intelligence?
  - Yes. If a monkey were to solve the problem in the real world, it would be more intelligent than our predefined program. It would have to define the actions and the necessary conditions based on the data it collects in the environment, and then it would have to link the tasks in sequential order like what the GPS did.
