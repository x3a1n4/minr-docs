<!-- minrdocs:scripting --> <!-- minrdocs:msc -->
<!-- utilityinfo:name entityCapture -->
<!-- utilityinfo:author eggshells -->
<!-- utilityinfo:dependencies akutils -->
<!-- utilityinfo:description A small tools for returning entities from selectors. Credit to Vaporizor -->

# entityCapture
This is a small utility namespace to capture entities from selectors. Heavily based on the similar features in vprutils.

### getEntityFromSelector() example:
<div class="annotate breakword" markdown>
```
@bypass /execute in minecraft:theta run summon minecraft:rabbit ~ ~ ~ {Glowing:1b, Tags:["eggshellUtilsTest"]}

@define Entity test = entityCapture::getEntityFromSelector("@e[tag=eggshellUtilsTest,limit=1]", "theta") (1)

@player "Got entity {{test}}"
```
</div>

1. This line captures a single entity from a selector, in this case the tag given. **Note that the limit argument must be provided**. In this case, it returns the rabbit just spawned!

### getAllEntitiesFromSelector() example:

<div class="annotate breakword" markdown>
```
@define Entity[] rabbits = entityCapture::getAllEntitiesFromSelector("@e[type=minecraft:rabbit]", "theta") (1)
@player "Found all rabbits {{rabbits}}"

@define Entity[] rabbits2 = entityCapture::getAllEntitiesFromSelector("@e[limit=1,type=minecraft:rabbit]", "theta") (2)
@player "Found only one rabbit {{rabbits2}}"
```
</div>
1. This code gets all rabbits on the server, and returns them as an `Entity[]` list
2. By providing a limit argument, you can make sure to get only a limited number of entities.


## Functions
| Function                             | Description                                           |
| ------------------------------------ | ----------------------------------------------------- |
| `Entity getEntityFromSelector(String selector, String world)` | Returns an entity from a vanilla selector in world `world`. Fails if `limit=1` is not provided. |
| `Entity[] getAllEntitiesFromSelector(String selector, String world)` | Returns a list of all entities matched from the selector in world `world`. |
| <!-- minrdocs:internal --> `Int[] getDecUUIDFromSelector(String selectorm String world)` | Returns the decimal UUID from a selector. Copy of vprutils::getDecUUID |
| <!-- minrdocs:internal --> `Void tests()` | Unit tests |

