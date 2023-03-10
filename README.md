# Quorum Coding Challenge


## [Coding Challenge File](https://github.com/macdev14/quorum-challenge/blob/main/Quorum%20Coding%20Challenge%20Legislative%20Data.pdf)
## [Q&A File](https://github.com/macdev14/quorum-challenge/blob/main/Quorum.pdf)


## Installation

#### Create Virtual Environment 
```bash
python3 -m venv /path/to/new/virtual/environment
# Mac/Unix
source /path/to/new/virtual/environment/activate
# Windows
path\to\venv\Scripts\activate.bat
```
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