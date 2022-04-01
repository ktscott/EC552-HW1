# EC552-HW1
// What you are inputting into the command window:
When you run the code you will be prompted with several inputs in the command line
First you must input the two json libraries you want to use, one for the gates and one for the inputs
Then the number of gates and the gates in a netlist in Verilog format
Next, you enter the names of the input model you are using
Then you enter the actual model that is associated with each gate in the net list 

// What our program does:
Our program then takes all these inputs and use our optimization algorithm to improve the score
The algorithm iterates through each variable one at a time and alters each variable to improve the score the most
These changes are then added together in summation to get the most optimal gate changes. 


// Outputs:
The program outputs the original truth table with values and the original score.
Then it outputs all the improvements it made to each model.
Finally it outputs a new truth table with the new score. 
