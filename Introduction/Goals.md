### Essential

* **Gradual typing**
* **Multiple dispach**
* **Whitespace-sensitive**
    * Whitespace is code structure for humans to interpret, braces are code structure for computers to interpret. Why redundantly use both systems to mark the same structure? A whitespace-sensitive system like Python's allows you to organize code for humans and for parsers using the same representation, and it frees up the curly braces for other uses too.
    * Indenting with spaces is a syntax error. I'm solving the tabs vs spaces debate right now, tabs are the canonical indentation in Chimera. Tabs are nice discrete units to work with that map 1:1 to indentation levels, which makes everything simpler. Also, indenting with tabs allows each user to configure their dev environment to show indentation as deep as they want, while the codebase remains identical. Spaces and any other obscure unicode spacing characters will be a syntax error if used before the first non-whitespace character on a line, but a REPL or IDE can automatically replace them with tabs for you.
* **Designed for multiple environments**: application dev, web, embedded scripting, high-performance
* **First-class support for integer rationals** (`2//3`)

### Important

* Macros, metaprogramming, reflection
* Elegant, easy to read and write
    * `x² for x in 0..100 -> filter is-prime -> sort`
* Simple file-oriented module system like rust/python (module `foo` in either `foo.ext` or `foo/_magic_.ext`)
* Robust pattern matching
* Dead-simple FFI
* `snake-case-names`
* Coroutines

### Nice to have

* Per-method static specialization
* Intelligent type promotion
* Coefficients, adjacent terms multiply
* Imaginary numbers, unit types (e.g. `1km / 500cm == 200m == 0.2km == 20000cm`)
* Lisp-style spaced syntax
* Operators as regular functions
* Utilities for managing other processes
* First-class parallelism
* Arbitrary string prefixes? `raw"\a\\b"`, `big"271897892129782347298"`, `bits"01001111"`
* Clean block syntax for accepting closures a la ruby
* `with`/`..` for copying immutable structures with changes e.g. `{ x: 1, ..var }` (like rust) or `{ var with x: 1 }` (like TS) or `var with { x: 1 }`

### Trivial

* All code is UTF-8, period. As many unicode characters supported as possible for identifiers (basically everything but reserved, non-printing/control, RTL, combining chars, homoglyph bait)
    * `?` and `!` are allowed in identifiers: `is-done?`
* Arbitrary underscores in numbers - `1_000_000, 0b1011_0100, 0xc0_ff_ee`
* Simple unicode builtins - `²` for `^2`, `√` for sqrt, `×` and `÷` as aliases for `*` and `/`, etc
* Chained comparison operators are allowed: `2 < x ≥ 7 > y` is a valid expression which evaluates to a `Bool`
* Plain word keywords for boolean operators: `a and b`, `true xor foo()`, and so on
    * Boolean operators are lowercase (`a and b`), bitwise operators are uppercase (`a XOR b`) (?)
    * Boolean operators are short-circuiting
* Positive and negative modulo

### Auxilliary goals

* Emphasis on interactive development, with strong tooling (REPL/notebooks)
    * REPL has shortcuts for unicode chars: `\^2`-tab for `²`, `\delta`-tab for `∆`, etc (reference latex sequences)
    * Use `?` command to show input sequences in REPL
* Good package manager - SemVer, locked versions should be 100\% repeatable, allows fetch from github etc, write-only with yank, designed with security and dependency auditing in mind

### Misc notes

* REPL workspaces
    * In the base Chimera folder (`~/.chimera`?), each folder is a workspace that you can easily create and quickly switch between in the REPL
    * Un/install/version packages from inside the REPL
    * A temporary scratch workspace is created when first opening the REPL, and more can be created on demand
