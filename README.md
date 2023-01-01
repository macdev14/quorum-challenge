# Quorum Coding Challenge

## [Q&A File](https://google.com)


## Installation

#### Main Package Required
#### -  [Pandas](https://pandas.pydata.org/getting_started.html)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.



```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```
Generates 'legislators-support-oppose-count.csv'
and
'new_bills.csv'


## Setting Custom CSV file name output

change main.py
```python
from votes import votes

if __name__ == '__main__':
    v = votes()
```
to
```python
from votes import votes

if __name__ == '__main__':
    v = votes(first_task_file_name='custom_file_name.csv', second_task_file_name='second_custom_file_name.csv')
```



## License

[MIT](https://choosealicense.com/licenses/mit/)