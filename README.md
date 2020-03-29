Instructions to follow while running the script ->
prerequisite: first we need to enter user name and then token value(for the authentication purpose)
After that follow below instructions ->
1) script takes 3 user inputs - name of Org, No of repos to fetch, no of committes
2) run the python script with below format -
     python <Script_name>
3) it will ask for above 3 inputs respectively
4) after providing inputs, it will give required output

Code approach ->
Firstly, we're fetching repos of a given Org and sorting them on the basis of number of forks in descending order.
Then, for each repo, we're calculating top committees with their commit count(in descending order).
it will give us top committees with their commit count against their repos.
