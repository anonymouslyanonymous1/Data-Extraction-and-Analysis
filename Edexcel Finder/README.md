# 🧐 | Edexcel Finder Production Files
[![Website](https://img.shields.io/badge/Website-Edexcel_Finder-1cd9fe.svg)](https://edexcelfinder.onrender.com/)
[![Main Repository](https://img.shields.io/badge/Main%20Repository-Github-cfcfcf.svg)](https://github.com/anonymouslyanonymous1/Edexcel-Finder)
---
- Storing Data: Used **Polars** to store the data as JavaScript Objects accordingly
- Indexing: Used **Whoosh** to create a inverted index of all files in `static/Data`

## Details
```yaml
Edexcel Finder
└─── data_extraction.py : Used it to make the JavaScript Objects with every pdf's each page number, content of each page, QP_Link, MS_Link
└─── indexing.py : Used it to make Whoosh Index files
└───static : As in main repository
    ├───Data : All the Extracted Data is stored here in the form of JS Objects
    │   ├───Biology (2018)
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Chemistry (2018)
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Mathematics (2018)
    │   │   ├───WDM11
    │   │   ├───WFM01
    │   │   ├───WFM02
    │   │   ├───WFM03
    │   │   ├───WMA11
    │   │   ├───WMA12
    │   │   ├───WMA13
    │   │   ├───WMA14
    │   │   ├───WME01
    │   │   ├───WME02
    │   │   ├───WME03
    │   │   ├───WST01
    │   │   ├───WST02
    │   │   └───WST03
    │   ├───Old Biology
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Old Chemistry
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   ├───Unit 6
    │   │   └───Unit 7
    │   ├───Old Mathematics
    │   │   ├───WDM01
    │   │   ├───WFM01
    │   │   ├───WFM02
    │   │   ├───WFM03
    │   │   ├───WME01
    │   │   ├───WME02
    │   │   ├───WME03
    │   │   ├───WST01
    │   │   ├───WST02
    │   │   └───WST03
    │   ├───Old Physics
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   ├───Unit 6
    │   │   └───Unit 7
    │   └───Physics (2018)
    │       ├───Unit 1
    │       ├───Unit 2
    │       ├───Unit 3
    │       ├───Unit 4
    │       ├───Unit 5
    │       └───Unit 6
    ├───Fetch : Contains list of papers and their corresponding links for every exam series as JS Objects
    │   ├───Biology (2018)
    │   ├───Chemistry (2018)
    │   ├───Mathematics (2018)
    │   ├───Old Biology
    │   ├───Old Chemistry
    │   ├───Old Mathematics
    │   ├───Old Physics
    │   └───Physics (2018)
    ├───Index : Self-explanatory, contains the index files that Whoosh utilises to search
    │   ├───Biology (2018)
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Chemistry (2018)
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Mathematics (2018)
    │   │   ├───WDM11
    │   │   ├───WFM01
    │   │   ├───WFM02
    │   │   ├───WFM03
    │   │   ├───WMA11
    │   │   ├───WMA12
    │   │   ├───WMA13
    │   │   ├───WMA14
    │   │   ├───WME01
    │   │   ├───WME02
    │   │   ├───WME03
    │   │   ├───WST01
    │   │   ├───WST02
    │   │   └───WST03
    │   ├───Old Biology
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   └───Unit 6
    │   ├───Old Chemistry
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   ├───Unit 6
    │   │   └───Unit 7
    │   ├───Old Mathematics
    │   │   ├───WDM01
    │   │   ├───WFM01
    │   │   ├───WFM02
    │   │   ├───WFM03
    │   │   ├───WME01
    │   │   ├───WME02
    │   │   ├───WME03
    │   │   ├───WST01
    │   │   ├───WST02
    │   │   └───WST03
    │   ├───Old Physics
    │   │   ├───Unit 1
    │   │   ├───Unit 2
    │   │   ├───Unit 3
    │   │   ├───Unit 4
    │   │   ├───Unit 5
    │   │   ├───Unit 6
    │   │   └───Unit 7
    │   └───Physics (2018)
    │       ├───Unit 1
    │       ├───Unit 2
    │       ├───Unit 3
    │       ├───Unit 4
    │       ├───Unit 5
    │       └───Unit 6
    └───Papers : During production it contained all the Papers' pdfs
        ├───Biology (2018)
        │   ├───Unit 1
        │   ├───Unit 2
        │   ├───Unit 3
        │   ├───Unit 4
        │   ├───Unit 5
        │   └───Unit 6
        ├───Chemistry (2018)
        │   ├───Unit 1
        │   ├───Unit 2
        │   ├───Unit 3
        │   ├───Unit 4
        │   ├───Unit 5
        │   └───Unit 6
        ├───Mathematics (2018)
        │   ├───WDM11
        │   ├───WFM01
        │   ├───WFM02
        │   ├───WFM03
        │   ├───WMA11
        │   ├───WMA12
        │   ├───WMA13
        │   ├───WMA14
        │   ├───WME01
        │   ├───WME02
        │   ├───WME03
        │   ├───WST01
        │   ├───WST02
        │   └───WST03
        ├───Old Biology
        │   ├───Unit 1
        │   ├───Unit 2
        │   ├───Unit 3
        │   ├───Unit 4
        │   ├───Unit 5
        │   └───Unit 6
        ├───Old Chemistry
        │   ├───Unit 1
        │   ├───Unit 2
        │   ├───Unit 3
        │   ├───Unit 4
        │   ├───Unit 5
        │   ├───Unit 6
        │   └───Unit 7
        ├───Old Mathematics
        │   ├───WDM01
        │   ├───WFM01
        │   ├───WFM02
        │   ├───WFM03
        │   ├───WME01
        │   ├───WME02
        │   ├───WME03
        │   ├───WST01
        │   ├───WST02
        │   └───WST03
        ├───Old Physics
        │   ├───Unit 1
        │   ├───Unit 2
        │   ├───Unit 3
        │   ├───Unit 4
        │   ├───Unit 5
        │   ├───Unit 6
        │   └───Unit 7
        └───Physics (2018)
            ├───Unit 1
            ├───Unit 2
            ├───Unit 3
            ├───Unit 4
            ├───Unit 5
            └───Unit 6
```

