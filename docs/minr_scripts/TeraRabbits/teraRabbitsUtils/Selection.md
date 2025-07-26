
# Selection
This is the default generated description for the class Selection. Include code examples, screenshots, ect. here.

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `Selection Selection(Player player)` | Default constructor |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Selection Selection(Player player)` | Default constructor |
| `Void addBlockToSelection(BlockLocation location)` | No documentation |
| `Void addCuboidToSelection(BlockLocation location1, BlockLocation location2)` | No documentation |
| `Void resetSelection()` | Reset the selection - so that we only need to do initialize the hashmap once |
| `BlockLocation[] getBlocks()` | No documentation |

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `Player player` | No documentation |
| `stringHashMap::SHashMap blocks` | No documentation |
| `BlockVector3 lowerBound` | No documentation |
| `BlockVector3 upperBound` | No documentation |
