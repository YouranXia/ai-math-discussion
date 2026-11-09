import regex as re
input_path="E:/programming/cs336/assignment1-basics/tests/fixtures/tinystories_sample.txt"
with open(input_path, encoding="utf-8") as file:
    a=file.read()
documents=a.split("<|endoftext|>")    #题目给出每个文章之间的分隔符
PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
token_groups=[]
for document in documents:
    for match in re.finditer(PAT, document):
        text_pieces=match.group()
        raw_bytes=text_pieces.encode("utf-8")
        tokens=[]
        for i in raw_bytes:
            tokens.append(bytes([i]))
        token_groups.append(tokens)
vocabulary={}   #创建一个空字典
for i in range(256):
    vocabulary[i]=bytes([i])
merges=[]    #创建一个空列表
for round_index in range(1):
    counts={}
    for tokens in token_groups:
        for i in range(len(tokens)-1):
            pair=(tokens[i], tokens[i+1])
            counts[pair]=counts.get(pair, 0)+1
    if counts=={}:
        break
    best_count=0
    for pair,count in counts.items():
        if count > best_count or (count==best_count and best_pair<pair):
            best_count = count
            best_pair = pair
    new_id=len(vocabulary)
    vocabulary[new_id]=best_pair[0]+best_pair[1]
    merges.append(best_pair)
    new_token_groups=[]
    new_id=len(vocabulary)
    vocabulary[new_id]=best_pair[0]+best_pair[1] 
    new_token_groups=[]
    for tokens in token_groups:
        merged=[]
        i=0
        while i<len(tokens):
            if i+1<len(tokens) and (tokens[i], tokens[i+1]) == best_pair:
                merged.append(tokens[i]+tokens[i+1])
                i+=2
                continue
            merged.append(tokens[i])
            i+=1
        new_token_groups.append(merged)
    token_groups=new_token_groups
print(merges)
print(len(vocabulary))
print(token_groups[:5])