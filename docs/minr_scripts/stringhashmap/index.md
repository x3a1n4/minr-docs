<!-- minrdocs:scripting --> <!-- minrdocs:msc --> <!-- minrdocs:github https://github.com/x3a1n4/minr -->
<!-- utilityinfo:name StringHashMap -->
<!-- utilityinfo:author eggshells -->
<!-- utilityinfo:no_dependencies -->
<!-- utilityinfo:description A small implementation of string:string hashmaps in minr -->

# String Hash Map
This is an implementation of string:string hashmaps in minr.

Example Code (copied from `tests()`)

``` minr
@using stringHashMap

@define SHashMap testMap = SHashMap()
@player "Setting Test Value"
@var testMap.set("Test Value", "Success!")

@player "Value at Test Value (e: 'Success!'):"
@player {{testMap.get("Test Value")}}
@player "Value at Bad Value (e: null):"
@player {{testMap.get("Bad Value")}}
@player "Value at Bad Value (tryGetDefault) (e: 'Not Found!'):"
@player {{testMap.tryGetDefault("Bad Value", "Not Found!")}}
```

## Classes

| Class                                        | Description                                       |
| -------------------------------------------- | ------------------------------------------------- |
| **[`SHashMap`](./SHashMap.md)**              | The string hash map object                        |
| **[`KeyValuePair`](./KeyValuePair.md)**      | A structure that holds associated keys and values |
| <!-- minrdocs:internal --> `KVPArrayWrapper` | A structure that holds an array of `KeyValuePair` |

## Functions

| Function                             | Description                                           |
| ------------------------------------ | ----------------------------------------------------- |
| `Int hash(String s)`                 | Return a hash of a string, from 1 to 997              |
| `Int getCharIndex(String char)`      | Get the position of the input character in `alphabet` |
| <!-- minrdocs:internal --> `tests()` | Unit tests for the SHashMap module                    |

## Variables
| Variable                                     | Description                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| <!-- minrdocs:internal --> `Int arraySize`   | The size of the array used to store the values. Set to 997 as a constant |
| <!-- minrdocs:internal --> `String alphabet` | List of all ascii characters, in order                                   |