# Complexity Finder

## Intro 
Complexity finder is a tool that enables it's user to determine computational comlexity of a function in python.

### Instalation
If you want to install it as a library just do:
```bash
pip install git+https://github.com/AGHPythonCourse2017/zad2-bartosz822
```
#### Using as a library 
When you've installed successfully this tool you can simply:
```python
import complexityfinder.finder as cf
```
and then you can use it
```python
complexity = cf.complexity_finder(sorted, cf.arr_generator, cf.simple_cleaner, timeout=10)
complexity.print_some_info()
```

### Simple testing
If you want to use this tool as an executable you can clone the repository and run main.py
```bash
git clone https://github.com/AGHPythonCourse2017/zad2-bartosz822
cd zad2-bartosz822/complexity
python main.py
```

####Using as an executable
Function to test should be implemented in _your_function.py_. After implementing it you can run the program.

#####Command line arguments
- **--log, -l** enable logging
- **--demo,  -d** run demo


##Functionality
###Find complexity of a function:
```python
complexity = cf.complexity_finder(fun, setup, clean)
```
where:
- _fun_ - is a function to be tested
- _setup_ - is a function that takes a nuber and returnes structure for _fun_ to work on
- _clean_ - is a function that cleans after fun execution

functions should provide this functionality:
```python
#n - problem size
structure = setup(n)
res = function(setup)
clean(res)
```
###Complexity class
Objects of class Complexity are results of running complexity_finder and provide methods such as:
- _estimate_time(size)_ - returns info of how long will the function run for a given problem size 
- _estimate_size(time)_ - returns info of how big can the problem be for the function to end in given time
- _get_info_ - returns information about functions complexity

###Helper functions
- arr_generator(n) - simple setuper for list - based problems
- simple_cleaner - del based cleaner
- simple_setup - identity function
- test_it(f, n, setup, clean) - return execution time of a single function



