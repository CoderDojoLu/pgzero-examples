pgzero wants to be a zero boilerplate framework for pygame.

Whilst this is mostly achieved by having a runner wrapper, pgzrun, there are other possibilities to get your files running.

# Documentation

[Pygame Zero Reference PDF](https://media.readthedocs.org/pdf/pygame-zero/latest/pygame-zero.pdf)

# Installation

# Dependencies

Python 3.6

# virtualenv

During installation into a dedicated virtualenv I ran into execution problems.
Thus I will not cover this case just yet.

# MacOS

Make sure you use python3 and pip3 during installation.

Install both packages as follows

# Dependencies, homebrew
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install sdl sdl_image sdl_mixer sdl_sound sdl_ttf python3 hg
$ pip3 install -U pip
$ pip3 install -U hg+http://bitbucket.org/pygame/pygame
$ pip3 install -U hg+http://bitbucket.org/SteveClement/pgzero
```

# Anaconda

Anaconda is an all-in-one Python development studio.
It is feature rich and has it's own self-contained virtual environment (with a default virtualenv called 'root')

## MacOS

Installation is easy, just download the installer and go through.

## CLI

To use the CLI tools you need to add the anaconda bin directory to your PATH:

export PATH=~/anaconda/bin:"$PATH"

## packages

Anaconda provides some packages that can be installed from their repo.
Luckily we can also use the pip installer.

```
$ conda update conda
$ source activate
(root) $ pip install -U pip
(root) $ pip install hg+http://bitbucket.org/pygame/pygame
(root) $ pip install hg+http://bitbucket.org/SteveClement/pgzero
```


## Linux

Installation is easy, download the installer, and run it with 'bash'

```
$ pip3 install pygame pgzero
```

If pip3 is not installed: sudo apt-get install python3-pip

# CLI

To use the CLI tools you need to add the anaconda bin directory to your PATH:

export PATH=~/anaconda3/bin:"$PATH"

