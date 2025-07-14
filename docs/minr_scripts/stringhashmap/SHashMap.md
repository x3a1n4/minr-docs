# SHashMap
This class offers all the hashmap functionality. Hash collisions are handled with separate chaining.

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| <!-- minrdocs:internal --> `KVPArrayWrapper[] hashMap` | The variable that the hashmap is actually stored in.                                              |
| `String[] keys`                                        | All keys saved in the hashmap. Shouldn't be written to directly, but can be iterated over freely. |

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `SHashMap()` | Create an empty SHashMap |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `set(String key, String value)`                         | Set the key `key` to value `value`                                                  |
| `String get(String key)`                                | Get the value associated with `key`. Returns the null value (`"null"`) if not found |
| `String tryGetDefault(String key, String defaultValue)` | Try to get the value associated with `key`, return `defaultValue` if not found      |
| `String remove(String key)`                             | Remove the key `key` and associated value from the SHashMap                         |