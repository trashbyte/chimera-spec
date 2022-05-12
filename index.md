<div id="logo-container"><img alt="Chimera logo" src="Logo.png" id="logo-main"></div>

<h1 id="title-main">Living Standard</h1>

<h2 id="subtitle-main">Working Draft ⨳ May 2022</h2>

<hr/>

<h1 id="table-of-contents-title">Contents</h1>

%%TOC%%

<hr/>

# Introduction

```
 # A palindromic number reads the same both ways.
 # The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 # Find the largest palindrome made from the product of two 3-digit numbers.

fn is-palindrome n:Numeric :: Bool => is-palindrome n.to-string
fn is-palindrome s:String :: Bool
    for i in 0..(s.length/2)
        if s[i] != s[s.length - i - 1] then return false
        true

gen combinations items
    if items.length < 2 then raise Error(
        "Provided iterator too short: `combinations` requires at least two items")
    for i in 0..<(items.length - 1), j in i..<items.length
        yield (items[i], items[j])

combinations 100..999 -> map `*` -> filter is-palindrome -> max
```

%INCLUDE% Introduction/Goals

---

# Core Concepts

%INCLUDE% Core Concepts/Variables
%INCLUDE% Core Concepts/Numeric Types
%INCLUDE% Core Concepts/Operators
%INCLUDE% Core Concepts/Strings
%INCLUDE% Core Concepts/Collections
%INCLUDE% Core Concepts/Functions and Methods
%INCLUDE% Core Concepts/Control Flow
%INCLUDE% Core Concepts/Types

---

# The Language

%INCLUDE% The Language/Lexical Conventions
%INCLUDE% The Language/Expressions
%INCLUDE% The Language/Pattern Matching
%INCLUDE% The Language/Coroutines
%INCLUDE% The Language/Documentation
%INCLUDE% The Language/Metaprogramming
%INCLUDE% The Language/Modules

---

# The Standard Library

%INCLUDE% The Standard Library/Basic Functions
%INCLUDE% The Standard Library/List Manipulation
%INCLUDE% The Standard Library/Math Functions
%INCLUDE% The Standard Library/Coroutines
%INCLUDE% The Standard Library/Input and Output
%INCLUDE% The Standard Library/Operating System Facilities
%INCLUDE% The Standard Library/Debugging

---

# Embedded Scripting API

---

# Appendix A - Grammar

---

# Glossary
