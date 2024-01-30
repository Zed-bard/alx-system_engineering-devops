# 0x06. Regular Expression

## Project Title
This project focuses on building regular expressions using the Oniguruma library. The regular expressions will be utilized within Bash scripts, specifically designed to be executed on Ubuntu 20.04 LTS. The scripts will process input strings and extract specific patterns using the Oniguruma regular expression engine, which is the default library used by Ruby.

## Requirements

### General
- **Allowed Editors:** vi, vim, emacs
- **Interpreter:** All files will be interpreted on Ubuntu 20.04 LTS.
- **File Ending:** All project files should end with a new line.
- **README.md:** A README.md file, located at the root of the project folder, is mandatory.
- **Executable Scripts:** All Bash script files must be executable.
- **Shebang:** The first line of all Bash scripts should be exactly `#!/usr/bin/env ruby`.
- **Oniguruma Library:** All regular expressions must be built for the Oniguruma library.

## Background Context
The primary objective of this project is to work with regular expressions (regex) using the Oniguruma library, commonly employed by Ruby. It is crucial to note that the properties of Oniguruma may differ from other regular expression libraries.

To illustrate the usage of regular expressions within Bash scripts, the following Ruby code snippet is provided. The focus is on replacing the `regexp` part with the actual regular expression:
Oniguruma is a regular expression library that originated as a Ruby extension but has since become a standalone library. It provides powerful and flexible support for regular expressions and is widely used in various programming languages, including Ruby.

# Oniguruma
 is a regular expression library that originated as a Ruby extension but has since become a standalone library. It provides powerful and flexible support for regular expressions and is widely used in various programming languages, including Ruby.
Here are some key features and syntax elements of Oniguruma regular expressions:

1. **Character Classes:**
   - `\d`: Matches any digit (equivalent to `[0-9]`).
   - `\D`: Matches any non-digit.
   - `\w`: Matches any word character (alphanumeric + underscore).
   - `\W`: Matches any non-word character.
   - `\s`: Matches any whitespace character.
   - `\S`: Matches any non-whitespace character.

2. **Quantifiers:**
   - `*`: Matches zero or more occurrences.
   - `+`: Matches one or more occurrences.
   - `?`: Matches zero or one occurrence.
   - `{n}`: Matches exactly `n` occurrences.
   - `{n,}`: Matches `n` or more occurrences.
   - `{n,m}`: Matches between `n` and `m` occurrences.

3. **Anchors:**
   - `^`: Matches the start of a line.
   - `$`: Matches the end of a line.

4. **Character Sets:**
   - `[...]`: Matches any single character within the brackets.
   - `[^...]`: Matches any single character not within the brackets.

5. **Groups:**
   - `(...)`: Capturing group.
   - `(?:...)`: Non-capturing group.

6. **Alternation:**
   - `|`: Acts as an OR operator.

7. **Escape Characters:**
   - `\`: Escapes a metacharacter, allowing it to be treated as a literal character.

8. **Ranges:**
   - `a-z`: Matches any lowercase letter from 'a' to 'z'.
   - `A-Z`: Matches any uppercase letter from 'A' to 'Z'.

9. **Special Characters:**
   - `.`: Matches any single character except a newline.
   - `(...)` and `|`: Used for grouping and alternation, respectively.

10. **Quantifier Greediness:**
    - By default, quantifiers are greedy, meaning they match as much as possible. Adding `?` after a quantifier makes it lazy (matches as little as possible).

11. **Custom Character Classes:**
    - `\p{...}`: Matches any character with the specified Unicode property.

For example, in the provided Ruby script snippet:

```ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

The regular expression `/127.0.0.[0-9]/` matches the pattern "127.0.0." followed by any single digit. This regex is used to extract and print matching patterns from an input string representing an IP address. You can customize and build upon these elements to create more complex and tailored regular expressions for specific matching patterns.

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

This script takes an IP address as a command line argument (`ARGV[0]`) and uses the `scan` method with the specified regular expression to extract and print matching patterns. For example:

```bash
$ ./example.rb 127.0.0.2
127.0.0.2
$ ./example.rb 127.0.0.1
127.0.0.1
$ ./example.rb 127.0.0.a
```
