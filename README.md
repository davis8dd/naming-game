# Naming Game

The Algorithm:

On each iteration:
1. Select one actor as a speaker
1. Select another actor as a listener (based on network topology)
1. The speaker selects a word at random. If the speaker knows no words in the vocabulary list, create one.
1. The speaker communicates the word to the hearer.  If the hearer doesn't know the word, he includes it in his vocabulary.  If the hearer knows the word, both actors erase all other words from their vocabularies.

## The Minimal Naming Game
- Baronchelli, 2006

Properties to analyze:
- Total number of words owned by the population Nw(t)
- Number of unique words owned by the population Nd(t)
- Success rate S(t)

Dynamics characterized by:
- Convergence time
- Time and height of peak of Nw(t)
These quantities are expected to followe power law behaviors [reference p.31]

# How to run:
`python3 namingGameApp.py`

## Testing:
Generate code statement coverage:
`coverage run -m unittest tests/*.py`
Generate code branch coverage:
`coverage run --branch -m unittest tests/*.py`
View coverage percentages on console:
`coverage report`
View detailed coverage via html:
`coverage html`
