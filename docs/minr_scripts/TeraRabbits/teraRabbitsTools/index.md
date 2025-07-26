
# teraRabbitsTools
This is the default generated description for the namespace teraRabbitsTools. Include code examples, screenshots, ect. here.

## Classes
| Class                               | Description                    |
| ----------------------------------- | ------------------------------ |


## Functions
| Function                             | Description                                           |
| ------------------------------------ | ----------------------------------------------------- |
| `Void selectSingleBlockPattern(Block targetBlock, Player player)` | Set single block pattern |
| `Void sphere(Block targetBlock, Int size, Player player)` | Create sphere at targetBlock |
| `Void paint(Block targetBlock, Int size, Player player)` | Paint at the target block (don't replace air, TODO: use block replacements) |
| `Void erase(Block targetBlock, Int size, Player player)` | Erase in a sphere |
| `Void smooth(Block targetBlock, Int size, Player player)` | Smooth area around targetBlock |
| `Void pull(Block targetBlock, Int size, Player player)` | Pull area towards player (like spikes) |
| `Void flatten(Block targetBlock, Int size, Player player)` | Flatten area (like a mesa) |
| `Void cuboidSelect(Block targetBlock, Player player)` | set cubiod selection |
| `Void cuboidExtend(Block targetBlock, Player player)` | Extend cuboid to encompass target block |
| `Void set(Block targetBlock, Player player)` | Set blocks in selection (rclick on block) |
| `Void setOnlyAir(Block targetBlock, Player player)` | Set blocks in selection (rclick on block) |
| `Void deleteSelection(Block targetBlock, Player player)` | Delete blocks in selection |
| `Void copy(Block targetBlock, Player player)` | Copy to clipboard from block location |
| `Void paste(Block targetBlock, Player player)` | Paste clipboard at block location |
| `Void stack(Int size, Player player)` | Stack selection in facing direction |
| `Void replace(Block targetBlock, Item heldItem, Player player)` | Replace the block at the target block |
| `Void undo(Player player)` | undo |
| `Void spawnRabbit(Block targetBlock, Player player)` | Spawn invisible rabbit (at top middle of block) |
| `Void showRabbits(Player player)` | Show all rabbits within 25 blocks |
| `Void endSession(Player player)` | End the session |

## Variables
| Variable                                     | Description                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------ |
| `teraRabbitsUtils::Pattern pattern` | sets block selection |
| `teraRabbitsUtils::Selection selection` | No documentation |
| `teraRabbitsUtils::Clipboard clipboard` | No documentation |
| `Int selectionPosition` | No documentation |
| `BlockLocation firstPosition` | No documentation |
