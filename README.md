# dicewarepy

_dicewarepy_ is a minimalist Python library for Diceware-based word selection from cryptographic wordlists.

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
   - [Example](#example)
   - [Wordlists](#wordlists)
- [Security](#security)
  - [Entropy](#entropy)
  - [Randomness](#randomness)
- [Development](#development)
  - [Tools](#tools)
- [Credits](#credits)

## About

Many scenarios require the manual input and memorization of passwords, such as the master password for a password manager or the encryption password for a device.

Two key considerations emerge in this context:
- The password must be difficult to guess.
- The password should be easy to remember.

The [Diceware method](https://theworld.com/~reinhold/diceware.html) [(archived)](https://web.archive.org/web/20240913072907/https://theworld.com/~reinhold/diceware.html), created by Arnold G. Reinhold, addresses both of these considerations.
Instead of relying on a hard-to-remember string of characters, which often suffers from a lack of randomness and therefore security when thought up by humans, Diceware uses dice and a special wordlist to generate secure passphrases.

The process for creating a Diceware passphrase can be broken down into the following four steps:
1. A six-sided dice is rolled five times, with the resulting numbers recorded after each roll.
2. For instance, if the rolls come up with `4-3-6-4-4`, one would look through a Diceware wordlist to find the word corresponding to the number `43644`.
3. In this case, the word “password” would be identified and written down.
4. This process is repeated until the desired number of words is gathered for the passphrase, with each word separated by a space.

_dicewarepy_ provides a compact simulation of the steps described above.

## Installation

```shell
pip install dicewarepy
```

Or if you have multiple Python / pip versions installed, use `pip3`:

```shell
pip3 install dicewarepy
```

## Usage

`dicewarepy.diceware(n=6, language="en")`

Returns a list of `n` words selected from a Diceware wordlist specified by `language`.

- `n`: `int`
  - The desired number of words to generate.
  - Default: `6`
- `language`: `str`
  - The language tag of the wordlist to select from. 
  - Default: `"en"`

### Example

Import the `diceware` function:

```python
from dicewarepy import diceware
```

Assign a list of six randomly selected words to the variable `words`:

```python
words = diceware()
```

Print the list to the terminal:

```python
print(words)
```

Output: `['dainty', 'swimmable', 'thimble', 'stuffing', 'armrest', 'little']`

Use the previously selected words to build a passphrase string:

```python
# Define a space as delimiter.
delimiter = " "

# Build the passphrase string.
passphrase = delimiter.join(words)
```

Print the passphrase to the terminal:

```python
print(passphrase)
```

Output: `dainty swimmable thimble stuffing armrest little`

### Wordlists

| Language | Tag  | Wordlist                                                                       | File                                                                                                                                          |
|----------|------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| English  | `en` | [EFF Large Word List](https://www.eff.org/document/passphrase-wordlists)       | [eff_large_wordlist.txt](https://github.com/inwerk/dicewarepy/blob/main/src/dicewarepy/wordlists/eff_large_wordlist.txt?raw=true)             |
| French   | `fr` | [French Word List](https://github.com/ArthurPons/diceware-fr-alt)              | [diceware-fr-alt.txt](https://github.com/inwerk/dicewarepy/blob/main/src/dicewarepy/wordlists/diceware-fr-alt.txt?raw=true)                   |
| German   | `de` | [Mnemonische deutsche Wortliste](https://github.com/dys2p/wordlists-de)        | [de-7776-v1-diceware.txt](https://github.com/inwerk/dicewarepy/blob/main/src/dicewarepy/wordlists/de-7776-v1-diceware.txt?raw=true)           |
| Spanish  | `es` | [dadoware-bonito-es](https://github.com/mir123/dadoware-bonito-es)             | [DW-es-bonito.txt](https://github.com/inwerk/dicewarepy/blob/main/src/dicewarepy/wordlists/DW-es-bonito.txt?raw=true)                         |
| ...      | ...  | ...                                                                            | ...                                                                                                                                           |

## Security

For information on supported versions and how to report vulnerabilities, please refer to the [Security Policy](https://github.com/inwerk/dicewarepy/blob/main/SECURITY.md).

This section provides further details on the security aspects of the Diceware method and the implementation of this package.

### Entropy

Entropy measures the unpredictability of a given element. A passphrase with higher entropy is more challenging to guess, making entropy a useful metric for assessing passphrase strength.

The word lists included in this package are standard Diceware word lists, featuring $7,776$ unique words. The total number of possible passphrases from such a word list can be calculated using the formula $7,776^n$, where $n$ represents the number of words in the passphrase.

The entropy is determined by taking the base-2 logarithm of the number of possible passphrases, leading to the formula: $E_{pass} = \log_2(7,776^n)$.

As shown in the following table, each word in the passphrase contributes an additional $12.925$ bits of entropy. Given the time required to guess the correct combination, it is recommended to use Diceware passphrases that consist of at least 6 words.

| Words | Possible Passphrases | Entropy  | Time to guess*                    |
|-------|----------------------|----------|-----------------------------------|
| $1$   | $7,776$              | $12.925$ | $\lt 1 \textrm{ second}$          |
| $2$   | $\approx 6.04e^7$    | $25.85$  | $\lt 1 \textrm{ second}$          |
| $3$   | $\approx 4.7e^{11}$  | $38.774$ | $\lt 1 \textrm{ second}$          |
| $4$   | $\approx 3.65e^{15}$ | $51.7$   | $\approx 30 \text{ minutes}$      |
| $5$   | $\approx 2.84e^{19}$ | $64.62$  | $\approx 165 \text{ days}$        |
| $6$   | $\approx 2.21e^{23}$ | $77.55$  | $\approx 3,505 \text{ years}$     |
| $7$   | $\approx 1.71e^{27}$ | $90.47$  | $\approx 27,256 \text{ millenia}$ |
| $8$   | $\approx 1.33e^{31}$ | $103.4$  | ...                               |

*_Assuming an average of attempting 50% of possible combinations to successfully guess the correct passphrase, and considering an adversary capable of making one trillion (1,000,000,000,000) guesses per second._

### Randomness

The strength of random passphrases relies heavily on the randomness of the underlying number generator.

The [Diceware FAQ](https://theworld.com/~reinhold/dicewarefaq.html#computer) [(archived)](https://web.archive.org/web/20240912113815/https://theworld.com/~reinhold/dicewarefaq.html#computer) states that for most users, using dice is by far the better method for selecting passphrase words than relying on a computer, as the random number generators provided by most programming libraries are nowhere near good enough.

For this reason, Python's [random library](https://docs.python.org/3/library/random.html), which produces cryptographically weak pseudo-random numbers, was not utilized in this implementation. Instead, this implementation relies on Python's [secrets library](https://docs.python.org/3/library/secrets.html), specifically designed for generating cryptographically strong random numbers suitable for passwords, account authentication, security tokens, and other sensitive information.

## Development

Ensure that uv is installed on your system. If not, follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

1. Clone the repository and navigate to the project directory:

```shell
git clone https://github.com/inwerk/dicewarepy.git
cd dicewarepy
```

2. Install the required development dependencies:

```shell
uv sync --extra dev
```

### Tools
This project uses the following development tools:

Code formatting with [ruff](https://github.com/astral-sh/ruff)...

```shell
uv run -- ruff format
```

Type checking with [ty](https://github.com/astral-sh/ty)...

```shell
uv run -- ty check
```

Testing with [pytest](https://github.com/pytest-dev/pytest)...

```shell
uv run -- pytest
```

## Credits
- [Diceware](https://theworld.com/~reinhold/diceware.html) [(archived)](https://web.archive.org/web/20240913072907/https://theworld.com/~reinhold/diceware.html) by Arnold G. Reinhold
- [EFF Large Word List](https://www.eff.org/document/passphrase-wordlists) by Electronic Frontier Foundation
- [French Word List](https://github.com/ArthurPons/diceware-fr-alt) by Arthur Pons
- [Mnemonische deutsche Wortliste](https://github.com/dys2p/wordlists-de) by dys2p
- [dadoware-bonito-es](https://github.com/mir123/dadoware-bonito-es) by mir123
