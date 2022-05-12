### Error handling

(still very undecided on this)

Functions in Chimera that may fail return a Result type. Any function method that raises an Error automatically has its return values wrapped in a Result.

Error handling is made explicit because any function that raises an Error will return a Result which needs to be unwrapped to get the actual value.

```
fn unsafe-thing x
    if bad-thing
    	raise SomeError
    x * 2

C> unsafe-thing 3
Result::Ok(6)

C> unsafe-thing 3 -> unwrap
6

C> unsafe-thing bad-value
Result::Error(SomeError)

C> unsafe-thing bad-value -> unwrap
Unhandled Error: SomeError
  ...

fn might-fail y
    if bad-thing
        raise SomeError
    do-something-else

match might-fail n
    Ok => nothing
    Error(e) => display e

 # simpler case that excludes `Ok => nothing` for brevity
if let Error(e) = might-fail n
	display e
```

Notice how the parens can be left off of the `Ok` when the inner type is `nothing`. Similarly, matching against `Error` will catch `SomeError` as it is derived from `Error`.

Functions may also return Maybes as well as raise Errors. In this case, the function's return type is Result{Maybe{T}, E}. This can be matched like so:

```
match three-way-func x
    Some(val) => do-something val
    None => nothing
    Error(e) => display e
```

Notice how matching the Ok is unnecessary, and the pattern can match directly against Error and the two variants of Maybe for convenience.
