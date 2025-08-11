
# InteractEntity
This is a class that holds utility functions for the `minecraft:interact` entity that rides the player

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `InteractEntity InteractEntity(Player player)` | Create an interact entity, and attach it to the player |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `InteractEntity InteractEntity(Player player)` | Create an interact entity |
| <!-- minrdocs:internal --> `Void onInteract(Player player)` | Function triggered on interact |
| `Void setRemainingUses(Int n)` | Set the number of uses for this InteractEntity. Kills the interact entity after usages are used up |
| `Void setInfiniteUses()` | Set infinite uses |
| `Void kill()` | Kill this interact entity, and trigger all onKillBindings |

Note: to add bindings, the intended method is to access the functions of `onInteractBindings` and `onKillBindings` directly.
## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `playerclickhandler::BindingList onInteractBindings` | List of bindings on the interact entity <br/> **All bindings are triggered on each click** |
| `playerclickhandler::BindingList onKillBindings` | List of bindings on the interact entity <br/> **All bindings are triggered when the entity dies** |
| `Int remainingUses` | Number of remaining uses |
| <!-- minrdocs:internal --> `Boolean hasLimitedUses` | Whether to count down |
| <!-- minrdocs:internal --> `Entity entity` | Internal entity |
| <!-- minrdocs:internal --> `Player player` | Player the entity rides on |
