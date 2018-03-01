# pomodoro_timer
Test for DFS

## Usage
Python 2.7
It is best to use a fresh environment.

conda example install:

```bash
conda create -n ptimer python=2.7
source activate ptimer
pip install -r requirements.txt

```

### Run Tests
to run tests, just make sure you are in the correct environment and have the requirements installed. Simply then run

```bash
pytest
```
in the top level directory.


### Running the programs

Both programs can be run the same.  You can just run them with no arguments. In this case they will use the default time values (25, 5, 20).
If you want to use your own time values, run them like this:

```bash
python console_main.py 10 3 10
```

```bash
python gui_main.py 11 5 8
```

The three arguments are time in minutes for each phase in this order: task round time, short break time, long break time.
The above command would start a graphical timer with round times of 11 minutes, break times of 5 minutes and a final break time of 8 minutes.




