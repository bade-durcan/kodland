meme_dict = {
            "CREEPY": "korkunc",
            "LOL": "Laugh out loud kisaltilmisi"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("uzgunum bu kelimenin anlamini ben de bilmiyorum")