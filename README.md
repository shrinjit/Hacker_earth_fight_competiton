Problem :

Chotu's father is the owner of a Vada Pav shop. One Sunday, his father takes him to the shop. Father tells him that at the end of the day, Chotu has to give him a list consisting of the names of all the customers on that day who bought Vada Pav(s) from the shop. The list should not have the names of any of the customers being repeated and it should be such that the lexicographically smallest name comes first, ie., the names should be sorted in dictionary order.

As and when a particular customer buys a Vada Pav, Chotu writes down the name of that particular customer. Chotu's initial list is ready, but, he is confused as to how to make the list Father expects from him. Chotu comes to you for help. Your job now is to create the final list, as Father expects from Chotu.

Input :

First line consists of N, the number of names of customers in Chotu's initial list. The next N lines are such that each line consists of a customer's name.

Output :

On the first line, print the total number of names appearing in Chotu's final list. Then print the list such that every customer's name is printed on a new line.

Constraints :

1<=N<=10^6

1<=Length of names of customers<=5

Customers' names consist only of lower case English alphabets (a-z).

Note : Some test files contain large data. Use scanf/printf instead of cin/cout .

SAMPLE INPUT 
11
babu
anand
rani
aarti
nandu
rani
rani
ap
anand
babu
nandu
SAMPLE OUTPUT 
6
aarti
anand
ap
babu
nandu
rani
Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Score is assigned if any testcase passes.
Allowed Languages: Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic