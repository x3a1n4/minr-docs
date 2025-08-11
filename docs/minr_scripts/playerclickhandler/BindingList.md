
# BindingList
This is a structure that holds a list of bindings, for use in an interact entity. 

Bindings are triggered with the following snippet in `trigger.msc`:
```
@console /function execute {{function}}(Player("{{player}}"))
```

!!! note "Important usage instructions!"

    - All bindings must take in a player as a function call and nothing else
        - `foo(Player p)` works, but `foo(Player p, Boolean b)` or `foo()` do not
    - Bindings need a namespace to attach
        - Use `example::foo`, rather than `foo`
    - **Do not include arguments in the call**
        - For instance, call `BindingList.add(example::foo)` **not** `BindingList.add(example::foo(Player p))`

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| <!-- minrdocs:internal --> `BindingList BindingList()` | Default constructor |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Void add(String function)` | Add a binding  |
| `Void remove(String function)` | Remove a binding |
| `Void removeAllBindings()` | Remove all bindings |
| `Void trigger(Player player)` | Trigger all bindings |

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| <!-- minrdocs:internal --> `String[] bindings` | No documentation |
