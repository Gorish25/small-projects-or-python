import pywhatkit as pw

# asking user input
txt='''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics developed by Guido van Rossum. It was originally released in 1991. Designed to be easy as well as fun, the name "Python" is a nod to the British comedy group Monty Python.'''


# converting text to handwritting 
# txt is text, demo1.png is file created his name, [0,0,138] is color code
pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print("END")