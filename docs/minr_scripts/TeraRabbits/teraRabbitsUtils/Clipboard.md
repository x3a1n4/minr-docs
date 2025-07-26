
# Clipboard
This is the default generated description for the class Clipboard. Include code examples, screenshots, ect. here.

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `Clipboard Clipboard(BlockLocation offset, Player player)` | No documentation |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Clipboard Clipboard(BlockLocation offset, Player player)` | No documentation |
| `Void createFromSelection(teraRabbitsUtils::Selection selection)` | No documentation |
| `Void pasteIntoWorldWithOffset(teraRabbitsUtils::Action action, BlockVector3 offset, Boolean ignoreAir)` | If Ignore Air true, will ignore air blocks |
| `Void rotateY(BlockVector3 pivot, Double degrees)` | Rotates in Y by degrees Not fully implemented |
| `Void flip(BlockVector3 pivot, String axis)` | Flips on specific axis ["x", "y", "z"] Not implemented |
| `Void showOrigin()` | Render the origin point |

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `teraRabbitsUtils::BlockCache[] blocks` | No documentation |
| `BlockLocation offset` | Offset of copy position |
| `Player player` | No documentation |
