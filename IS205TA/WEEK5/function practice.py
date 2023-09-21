#write a function called cleaned text
#that should take in a phrase called input_text
#and clean it up lowercase all the
#return the cleaned up textwrap
#called the whitepace off both sides
#return the cleaned up text
#lowercase text via "stuff".lower()

def cleaned_text(input_text):
    lower = input_text.lower() #如果左对齐在编译时会出现这样的错IndentationError:expected an indented block说明此处需要缩进，你只要在出现错误的那一行，按空格或Tab（但不能混用）键缩进就行
    cleaned = lower.strip()
    return cleaned
result=cleaned_text(" here's some TeXT ")
print(result)
    #return output_text