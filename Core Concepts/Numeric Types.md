### Primitive types

### Rationals

### Units

```
unit Meter : m

unit Kilometer : km
	km = 1000 * m

unit Centimeter : cm
	cg = m / 100
```

Runtime infers `cm = km / 100000`, `km = cm * 100000`, `m = km / 1000` and `m = cm * 100`

```
measure Length : Meter

measure Time : Second

measure Mass : Kilogram

measure Speed : Length/Time

measure Area : Length*Length

measure Volume : Length*Length*Length

measure Density : Mass/Volume
```

```
unit Cubic-Meter : m^3

unit Liter : L
    L = m^3 / 1000

unit Second : s

unit Newton : N
    N = kg * m / s^2

unit Pascal : Pa
    Pa = N / m^2

unit PartsPerMillion : ppm
    ppm = mg/L
```

```
C> let volume = 500cc
Volume{Liter, 0.5}    # picks unit with representation closest to 1.0

C> let density = 100mg/volume
Density{Gram/Liter, 0.2}

C> density as mg/m^3
Density{Milligram/Cubic-Meter, 200000}

C> density as ppm
Density{PartsPerMillion, 200}
```

### Imaginary numbers

#### Why `im` instead of `i`?

`im` was chosen for the imaginary unit instead of `i` because `i` is an extremely common name for local variables, especially loop indices. Variables named `i` will be much more common in regular code than imaginary numbers, so the slight inconvenience/inaccuracy of using `im` instead of `i` makes sense.