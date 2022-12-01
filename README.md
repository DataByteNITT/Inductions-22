# Inductions-22
##### Fork the repo and create a pull request of your solution to this repository for the corresponding tasks 
##### Note : Do not send pull requests to the main repo. Make sure you are sending requests inside your tasks folder
Parameter :
A variable that is internal to the the model and whose value can be estimated from data.
-They are required by the model when making predictions
-They are often saved as part of the learned model 

Hyperparameter :
A variable that is external to the the model and whose value cannot be estimated from data.
-They are often used in processes to help estimate model parameters.
-They are often specified by the practitioner.

Gaussian process:
It's a powerful algorithm for both regression and classification 
-Gaussian process is a probaility distribution over possible functions
Kernal :
The method of classifying linearly for the non-linear problems

Surrogate method :
A statistical model to accurately approximate the simulation output

Probablistic model :
Probabilistic modeling is a statistical approach that uses the effect of random occurrences or actions to forecast the possibility of future results
-it provides a comprehensive understanding of the uncertainty associated with predictions. 
-Using this method, we can quickly determine how confident any mobile learning model is and how accurate its prediction is.

Nomenclatures:

1. suurogate model (gaussian function in this case)
It is the statistical/probabilistic modelling of the “blackbox” function. 
It works as a proxy to the later. For experimenting with different parameters
This model is used to simulate function output instead of calling the actual costly function

2. Acquisition Function 
It is a metric function which decides which parameter value that can return the optimal value from the function. 
There are many variations of it. We will work with the one “Expected Improvement”



Problem statement 
To summarize  a research paper which talks about efficiency and implementation of bayesian optimaization 


Pseudo code for Bayesian optimization  

SURROGATE FUNCTION (Gaussian process)
step1 Looping over all the samples values of input x, where the evaluatation takes place .
  2. Building k and f vectors i.e the data 
  3. Building matrices X and Y
  4. Calculating mu and sigma.
  5. Appending mu to predictedMu array and sigma to predictedSigma array
step6 Calculation of Omega as the mean of blackbox function for sampled points
step7 Calculation of Kappa =PredictedMu + Omega 
step8 Returning values
  Kappa(estimated mean of suurogate func.) and predictedSigma (estimated variance of surrogate func.)
 I have used sklearn module to import gaussian Process in my model
ACQUISITION FUNCTION
Usually acquisition functiopn consist of :
1.Upper confidence bound 
2.Lower confidence bound 
3.Probability of imbprovement 
4.Expected Improvement 


Mathematical inpretation

let us take the actual function be f(x)
bayesian function be y= f(x) + e(Etta) where e is small value to optimize the return value
instead y can be represenated as gaussian distribution of (f(x), variance)
GP is completely specified by its mean function mu(x) and its covariance k(x,x')

Loss function can be representated by gaussian distribution of its mean and covariance as mentioned above

Coming to acquisition function

expected improvement EI(x)= E[max {0, f(x)-f(x")
where x" isthe current potimal set of hyperparameters. Maximizingthis parameter will give
us the point that improves upon function the most

EI(x)= mu (x)- f(x"))psi(Z) + sigma (x)Pi(Z) if sigma (x) >0
     = 0 if sigma (x) =0
therffore, 
  Z= (mu (x)- f(x") )/sigma (x)

here, Psi (x) is cumulative function and pi(z) is probability density 


Final points, 
1.Given observed values f(x), update the posterior expectation of f using the GP model.
2.Find xnew that maximises the EI: xnew=argmaxEI(x).
3.Compute the value of f for the point xnew.

by iterating for different values we can make a perfect model or function which suits the actual function
