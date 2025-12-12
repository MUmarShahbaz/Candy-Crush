# Candy Crush

This is a candy crush clone made without using OOP. `dataclass` does not count as an OOP, I think.

## File Structure
| Filename           | Purpose                             |
|:------------------:|:------------------------------------|
| `candy_crush.py`   | The outer container/game controller |
| `main.py`          | Main Logic                          |
| `structs.py`       | Structure Definition                |
| `misc.py`          | Miscellaneous/Helper Functions      |
| `console_print.py` | Code for help in Debugging          |

## How to use

You simply need to download the src files into a single folder and then execute `candy_crush.py`. You should have python installed on your machine to run it.

## Understanding the Notation

Each candy is displayed as 99 where the first digit is the Mode and the second is the color.

| First Digit | Mode | Second Digit | Color |
|:-:|:-:|:-:|:-:|
| `0` | No Mode               | `0` | No Color |
| `1` | Vertically Stripped   | `1` | Red |
| `2` | Horizontally Stripped | `2` | Orange |
| `3` | Wrapped               | `3` | Yellow |
| `4` | Color Bomb            | `4` | Green |
||                            | `5` | Blue |
||                            | `6` | Purple |

## Example

https://github.com/user-attachments/assets/ac6ab25f-0e74-4a67-bd8d-dbcdb89e1649

## WIP

This code is still in development. So far the following remains to be done:

- Manual Handling of the Color Bomb
- Auto Handling of the Color Bomb
- GUI Implementation
- Removing Debugging scrap

## Debugging
The following lines are only for debugging and if you wish to use this code, you should remove them.

- main.py
  - 3
  - 27
  - 75
  - 80
  - 88
- candy_crush.py
  - 22
  - 23
  - 24
  - 25
  - 26
  - 27
  - 28
