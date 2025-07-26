
# teraRabbitsUtils
This is the default generated description for the namespace teraRabbitsUtils. Include code examples, screenshots, ect. here.

## Classes
| Class                               | Description                    |
| ----------------------------------- | ------------------------------ |
| [`Colour`](Colour.md) | No description |
| [`Pattern`](Pattern.md) | No description |
| [`BlockAlt`](BlockAlt.md) | No description |
| [`BlockChange`](BlockChange.md) | No description |
| [`BlockCache`](BlockCache.md) | No description |
| [`BlockData`](BlockData.md) | No description |
| [`Action`](Action.md) | No description |
| [`Selection`](Selection.md) | No description |
| [`Clipboard`](Clipboard.md) | No description |

## Functions
| Function                             | Description                                           |
| ------------------------------------ | ----------------------------------------------------- |
| `Void initializeBlockData()` | No documentation |
| `Void trySetBlock(teraRabbitsUtils::Action action, BlockLocation location, String block)` | Try to set a block given an action |
| `Void log(String message)` | No documentation |
| `Block getRelativeBlock(Block block, Int x, Int y, Int z)` | Get the block relative to a target block |
| `String getVanilla(String type)` | convert a block type to its vanilla variantt |
| `Boolean canPlaceBlock(BlockLocation blockLocation, Player player)` | Whether a player can place a block (for instance: regions, masks) |

## Variables
| Variable                                     | Description                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| `stringHashMap::SHashMap blockAltLookup` | No documentation |
| `teraRabbitsUtils::Action[] actionList` | Should be moved to tools? |
| `teraRabbitsUtils::BlockData[] bd` | No documentation |
| `String[] blockTypes` | No documentation |
