letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Nancy G").replace("<|Date|>", "10 March 2026"))