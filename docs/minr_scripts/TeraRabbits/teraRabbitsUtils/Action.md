
# Action
This is the default generated description for the class Action. Include code examples, screenshots, ect. here.

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `Action Action(String name, Player player)` | All tool usages should be logged through Actions, so that they can be undone |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Action Action(String name, Player player)` | All tool usages should be logged through Actions, so that they can be undone |
| `Void add(teraRabbitsUtils::BlockChange change)` | Add a block change to this action |
| `Int length()` | get number of blocks changed |
| `Void undo()` | undo this action |

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `String name` | No documentation |
| `Player player` | No documentation |
| `teraRabbitsUtils::BlockChange[] allBlocksChanged` | No documentation |
