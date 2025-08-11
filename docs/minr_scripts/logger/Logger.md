
# Logger
Any function that returns `logger::Logger` is returning itself, allowing for single-line definitions.

Note that any format will search and replace the following codes:

- `{name}` is replaced with the Logger's `name`
- `{time}` is replaced with the timestamp (or removed if timestamps are disabled)
- `{message}` is replaced with the message to be logged

## Constructors
| Constructor  | Description              |
| ------------ | ------------------------ |
| `Logger Logger(String name)` | Create a `Logger` object with name `name` |

## Methods
| Method                                                  | Description                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `Void debug(String debug)` | Log a debug message |
| `Void log(String log)` | Log a log (or info) |
| `Void warning(String warning)` | Log a warning |
| `Void error(String error)` | Log an error |
| <!-- minrdocs:internal --> `Void tellAllPlayers(String message, String format)` | Send messages to all players in `playerList` |
| `logger::Logger setPlayerList(Player[] players)` | Set the player list that this logger logs to |
| `logger::Logger showTimestamps(Boolean showTimestamps)` | Sets whether to display timestamps in log messages. <br/> Timestamps are always shown in square brackets, and use server-time. |
| `logger::Logger showDebug(Boolean showDebug)` | Sets whether to display debug messages |
| `logger::Logger setDebugFormat(String format)` | Change the debug format <br/> Default: `"&2{time}&l{name} Debug: &r&a{message}"` |
| `logger::Logger setLogFormat(String format)` | Change the log format <br/> Default: `"&8{time}&l{name}: &r&7{message}"` |
| `logger::Logger setWarningFormat(String format)` | Change the warning format <br/> Default: `"&6{time}&l{name} Warning: &r&e{message}"` |
| `logger::Logger setErrorFormat(String format)` | Change the error format <br/> Default: `"&4{time}&l{name} Error: &c&l{message}"` |

## Fields
| Field                                                  | Description                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| `String name` | No documentation |
| `Player[] playerList` | No documentation |
| `Boolean showingTimestamps` | No documentation |
| `Boolean showingDebugs` | No documentation |
| `String debugFormat` | No documentation |
| `String logFormat` | No documentation |
| `String warningFormat` | No documentation |
| `String errorFormat` | No documentation |
