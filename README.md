## Modification Stracture
This code uses cabocha-python to determine sentences with long-term engagements, and converts the sentence that has an engagement to the next clause that has an engagement.

### Library
- mlm-scoring-transformers [code is here](https://github.com/lovelovetrb/mlm-scoring-transformers)
    This Code is based on [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers)


### How to create data
1. DownLoad `mlm-scoring-transformers` and install<br>
    Shell
    ```
    git clone https://github.com/lovelovetrb/mlm-scoring-transformers
    cd mlm-scoring-transformers
    pip install -e .
    ```
    
2. install packages by requirements.txt
    ```
    pip install -r requirements.txt
    ```
3. Add sorce text to text/input.txt
4. Run `get_chunk.py`
5. You can get output file in `text/output.txt`

※You can describe the text to be analyzed in `texts/input.txt`
