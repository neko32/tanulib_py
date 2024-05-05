import MeCab

mecab = MeCab.Tagger("-Owakati")
s = "たこかいなうしかいな、とにわとりとたぬきちゃんが言いましたとさ。"
print(mecab.parse(s))
