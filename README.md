# Naming Game

The Minimal Naming Game simulates a group of actors agreeing on a single word as the label for an abstract object.

The Algorithm:

On each iteration:
1. Select one actor as a speaker
1. Select another actor as a listener (based on network topology)
1. The speaker selects a word at random. If the speaker knows no words in the vocabulary list, create one.
1. The speaker communicates the word to the hearer.  If the hearer doesn't know the word, he includes it in his vocabulary.  If the hearer knows the word, both actors erase all other words from their vocabularies.

# How to run:
`python3 namingGameApp.py`

Input parameters are:
- 'number_of_actors': 
- 'maximum_iterations': 
- 'generate_plots': 
- 'show_plots': 

## Testing:
Generate code statement coverage:
`coverage run -m unittest tests/*.py`
Generate code branch coverage:
`coverage run --branch -m unittest tests/*.py`
View coverage percentages on console:
`coverage report`
View detailed coverage via html:
`coverage html`

## The Minimal Naming Game
- Baronchelli, 2006

Properties to analyze:
- Total number of words owned by the population `Nw(t)`
- Number of unique words owned by the population `Nd(t)`
- Success rate `S(t)`

Dynamics characterized by:
- Convergence time
- Time and height of peak of `Nw(t)`
These quantities are expected to followe power law behaviors [reference p.31]

### Reproduction of results
Using a single pre-generated run of 10,000 iteratoins with 140 actors, we can see **total number of words** and **number of unique words** match those in **Baronchelli, 2006**:

* Total number of words over time:
![Total number of words-run1689137288](/docs/NamingGameTotalWords-run-1689137288.0891356.json.png)

* Number of unique words over time:
![Number of unique words-run1689137288](/docs/NamingGameUniqueWords-run-1689137288.0891356.json.png)

Any evidence of reproducing the Success Rate reported in **Baronchelli, 2006** will be provided in the future.

## License

Distributed under the GNU General Public License version 3.

See https://choosealicense.com/licenses/gpl-3.0/ or the included LICENSE file for full text.
