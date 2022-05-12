Grammar Extensions
	
	<Item*> ::= \{ <Item> \} ; \gcomment{zero or more} \gline
	
	<Item{\plus}> ::= <Item>, <Item>* ; \gcomment{one or more} \gline
	
	<CommaList(Item)> ::= <Item>, ( <OptWS>, `,', <OptWS>, <Item> )* ; \gline
	
	<WSList(Item)> ::= <Item>, ( <WS>, <Item> )* ; \gline
	
Symbols

	<AsciiUpper> ::= `A' | `B' | `C' | `D' | `E' | `F' | `G' | `H' | `I' | `J' | `K' | `L' | `M'
	\alt `N' | `O' | `P' | `Q' | `R' | `S' | `T' | `U' | `V' | `W' | `X' | `Y' | `Z' ; \gline
	
	<AsciiLower> ::= `a' | `b' | `c' | `d' | `e' | `f' | `g' | `h' | `i' | `j' | `k' | `l' | `m'
	\alt `n' | `o' | `p' | `q' | `r' | `s' | `t' | `u' | `v' | `w' | `x' | `y' | `z' ; \gline
	
	<Digit> ::= `0' | `1' | `2' | `3' | `4' | `5' | `6' | `7' | `8' | `9' ; \gline
	
	<HexDigit> ::= `0' | `1' | `2' | `3' | `4' | `5' | `6' | `7' | `8' | `9'
	\alt `a' | `b' | `c' | `d' | `e' | `f' | `A' | `B' | `C' | `D' | `E' | `F' ; \gline
	
	<OctalDigit> ::= `0' | `1' | `2' | `3' | `4' | `5' | `6' | `7' ; \gline
	
	<Unicode> ::= ? all unicode characters ? ; \gline
	
	<Ident> ::= ? all unicode characters except forbidden characters (see specification) ? ; \gline
	
	<IdentStart> ::= ? same as ident but without digits 0-9 ? ; \gline
	
	<Indent> ::= ? a number of tabs before a line that is greater than the previous line ? ; \gline
	
	<Dedent> ::= ? a number of tabs before a line that is less than the previous line ? ; \gline
	
	<Newline> ::= `\\n' | `\\r\\n' ; \gline
	
	<OptWS> ::= ( ` ' |  `\\t' )* ; \gline
	
	<WS> ::= ( ` ' |  `\\t' ){\plus} ; \gline

Values
	
	<Integer> ::= <Digit>{\plus} ; \gline
	
	<Float> ::= \gcomment{covers: 1.2, 1.2e+12, 1.2E-3}\newline
	<Integer>, `.', <Integer>, [ (`e'|`E'), (`+'|`-'), <Integer> ]
	\alt \gcomment{covers: 1e+2, 3E+4}\newline
	<Integer>, (`e'|`E'), (`+'|`-'), <Integer> ; \gline
	
	<HexInt> ::= `0x', <HexDigit>{\plus} ; \gline
	
	<OctalInt> ::= `0o', <OctalDigit>{\plus} ; \gline
	
	<BinaryInt> ::= `0b', (`0' | `1'){\plus} ; \gline
	
	<Numeric> ::= <Integer> | <Float> | <HexInt> | <OctalInt> | <BinaryInt> ; \gline
	
	<String> ::= `"', ( <Unicode> - `"' )*, `"'
	\alt `\'', ( <Unicode> - `\'' )*, `\''
	\alt `"""', ( <Unicode> - `"""' )*, `"""' ; \gline
	
	<Boolean> ::= `true' | `false' ; \gline
	
	<ListLit> ::= `[', [ <CommaList>(<Expr>) ], `]' ; \gline
	
	<Literal> ::= <Numeric> | <String> | <Boolean> | <ListLit> ; \gline

Expressions
	
	<Pattern> ::= ; \gline
	
	<Identifier> ::= <IdentStart>, <Ident>* ; \gline
	
	<Assignment> ::= `let', <Pattern>, `=', <Expr> ; \gline
	
	<Term> ::= ; \gline
	
	<Expr> ::= <Term>, (<OptWS>, <Term>)* ; \gline
	
	<Call> ::= <Identifier>, [ <WS>, <WSList>(<Expr>) ] ; \gline
	
	<IfElse> ::= ; \gline
	
	<ForIn> ::= <Pattern>, <WS>, `in', <WS>, <Expr> ; \gline
	
	<MultiForIn> ::= <ForIn>, ( <OptWS>, `,', <OptWS>, <ForIn> )* ; \gline
	
	<For> ::= `for', <WS>, <MultiForIn>, <OptWS>, <Newline>, <Indent> ; \gline
