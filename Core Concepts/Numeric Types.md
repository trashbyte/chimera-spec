### Primitive types

Chimera has a full range of fundamental numeric types, including integers and floating-point real numbers.

Integers for every power of 2 bits from 8 to 128 are available in both signed and unsigned variants.

| type      | minimum value                                        | maximum value                                       |
| :-------: | :--------------------------------------------------- | :-------------------------------------------------- |
| `Int8`    | -128                                                 | 127                                                 |
| `UInt8`   | 0                                                    | 255                                                 |
| `Int16`   | -32,768                                              | 32,767                                              |
| `UInt16`  | 0                                                    | 65,535                                              |
| `Int32`   | -2,147,483,648                                       | 2,147,483,647                                       |
| `UInt32`  | 0                                                    | 4,294,967,295                                       |
| `Int64`   | -9,223,372,036,854,775,808                           | 9,223,372,036,854,775,807                           |
| `UInt64`  | 0                                                    | 18,446,744,073,709,551,615                          |
| `Int128`  | -170,141,183,460,469,231,731,687,303,715,884,105,728 | 170,141,183,460,469,231,731,687,303,715,884,105,727 |
| `UInt128` | 0                                                    | 340,282,366,920,938,463,463,374,607,431,768,211,455 |

Floating point values are available in 16, 32, and 64 bit variants.

| type      | precision | smallest possible value | largest possible value |
| :-------: | :-------: | :---------------------: | :--------------------: |
| `Float16` | Half      | 5.9604645e-8            | 65504.0                |
| `Float32` | Full      | 1.40129846432e-45       | 3.40282346639e+38      |
| `Float64` | Double    | 2.22507385850e-308      | 1.79769313486e+308     |

#### Integer overflow

#### Division errors

### Arbitrary-precision arithmetic

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