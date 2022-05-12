
| Kind            | Operator                    | Associativity   |
| :-------------: | :-------------------------: | :-------------: |
| Access          | .                           | Left            |
| Type specifier  | :                           | Left            |
| Exponentiation  | ^                           | Right           |
| Unary           | + - √ not                   | Right           |
| Rational        | //                          | Left            |
| Multiply/Divide | * / \% \& \ ÷               | Left            |
| Add/Subtract    | + - \|                      | Left            |
| Range           | .. ...                      | Left            |
| Comparison 	  | & > < >= <= == is != is-not | Non-associative |
| Boolean         | and                         | Right           |
| Boolean         | or                          | Right           |
| Arrow           | ->                          | Left            |
| Assignment      | = += -= *= /= //= \= ^= %=  | Right           |

### Equality operators

#### Value equality

```
C> 1 == 1
true

C> 1 == 2
false

C> 1 == 1.0
true

C> let (a, b) = (1, 1.0)
(a, b)

C> a == b
true

C> 1 != 1.0
false

C> a != b
false
```

#### Reference equality

```
C> 1 is 1
true

C> 1 is 1.0
false

C> let (a, b) = (1, 1)
(a, b)

C> a is b
false

C> a is-not b
true

C> a is a
true

C> 1 is-not 1.0
true
```
