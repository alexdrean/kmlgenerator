# kmlgenerator

Example network linked kml generator

# Usage

1. Set `hostname` and `port` in `config.py`
2. `pip3 install -r requirements.txt`
3. `python3 main.py`
4. In google earth `Add` > `Network Link`
    - Set Link URL to hostname and port set previously. By default this is `http://localhost:1234`
5. Edit `pygenerator.py` to change the data source and visualization

Read more at [https://simplekml.readthedocs.io/en/latest/geometries.html#simplekml.Point]()