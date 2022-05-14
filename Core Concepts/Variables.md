
### Let bindings

The `let` keyword is used to create a {g variable g}, which is a name bound to a value. In the example `let x = 3` (read as "let x equal three") the name `x` is bound to the value `3`. Now, anywhere we use the variable `x`, it will evaluate to the value `3` (at least until we rebind `x` to something else).

### Immutability

Variables are **immutable** by default in Chimera. What this means is that a variable cannot be modified after creation.

```
C> let x = 1
1

C> x
1

C> x = 2
ERROR: cannot assign twice to an immutable binding
```

However, variables can be freely *rebound* using `let`, allowing the name to point to a different value.

```
C> let x = 1
1

C> let x = 2
2
```

When rebinding a variable like this, the old value can no longer be accessed using that name. We say that the new binding "shadows" the old binding.

### Mutable bindings

Variables can also be made **mutably** using the `mut` keyord instead of `let`, as in `mut y = 2`. Mutable variables can then be modified freely without rebinding.

```
C> mut y = 2
2

C> y = 3
3
```

For simple numbers, the distinction feels somewhat arbitrary, but it becomes important when dealing with data structures or references to shared values.

### Variable scope

The "scope" of a variable refers to the parts of code where that variable is bound to a particular value. A variable's scope begins when it is defined, and ends either when the block it was defined in ends, or when it is shadowed by a rebinding. When a variable is shadowed by rebinding, the old variable's scope ends and the new variable's scope begins.

```
fn func
	let x = 1          # scope of `x` begins here

	let y = 2          # scope of `y` begins here

	assert x + y == 3  # both variables are in scope here

 # when the function body ends, so do the scopes of the variables declared within,
 # so neither `x` nor `y` are accessible here

let a = 3

fn foo
	assert a == 3      # `a` is accessible from here
	let a = 4          # now `a` is rebound, so the outer `a` is no longer accessible
	assert a == 4

 # when the function body ends, the inner `a` binding goes out of scope,
 # and now `a` is no longer shadowed and points to its old value

assert a == 3
```

Chimera uses what's known as "lexical scope", which means that the names available in a given scope are based on their location in the code, as opposed to the order of code execution. For example:

```
C> fn f
	let x = 3     # local `x` is bound in the function body
	return x * x
fn f :: Numeric

C> let x = 1      # `x` bound in global scope
1

C> f              # invoke the function `f` which uses its own
9                 # internal binding and returns 3 * 3 == 9

C> x              # the outer `x` is unchanged
1
```

Notice how even though we declare an `x` outside of the function, the `x` inside of the function is totally separate and doesn't affect the `x` outside.

Similarly:

```
C> fn f
	let x = 3
	return x * x
fn f :: Numeric

C> f       # invoke function `f` which creates a local
           # binding to `x` inside the function body

C> x
ERROR: x is not defined
 # the local binding inside function `f` has gone out of scope,
 # and `x` is not bound in the global scope
```

In this example we can see that the variable `x` created inside the function `f` is not accessible outside the function.

As shown in the first example, scopes are "nested", meaning that scopes can exist inside of other scopes. For example:

```
C> fn f1
	let x = 2
	fn f2
		let y = 3
		return x * y     # outer variable `x` can be accessed from
		                 # inside the scope for function `f2`
	f2
fn f1 :: Numeric

C> fn f3 => z * z
ERROR: z is not defined  # no name `z` exists in this function's scope
                         # or any of its outer scopes (in this case, the global scope)

C> let z = 2             # `z` is defined in the global scope
2

C> fn f3 => z * z        # now `z` is accessible from global scope,
fn f3                    # which f3's scope is nested inside of

C> f3
4
```
