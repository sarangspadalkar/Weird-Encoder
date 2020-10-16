from flask import Flask, render_template, request
from weirdTextEncoder import weirdTextEncoder
from decoder import decoder
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    encodeInputString = None
    decodeInputValues = None

    if request.method == 'POST':
        result = []
        if request.form.get("input_encode") != None:
             
            encodeInputString = request.form.get("input_encode")
            i = 0
            while i < len(encodeInputString):
                result.append(weirdTextEncoder(encodeInputString[i:i+4]))
                i+=4
            return render_template('index.html',result = result,encodeInputString = encodeInputString)

        if request.form.get("input_decode") != None:
             
            isValid = True
            input_string = request.form.get("input_decode")
            decodeInputValues = input_string.replace('[','').replace(']','').replace(" ",'')
            for str in decodeInputValues.split(','):
                if not str.isdecimal():
                    isValid = False
                    break
            if isValid:
                original_string = decoder(decodeInputValues.split(','))
                return render_template('index.html',original_string = original_string, decodeInputValues = input_string)
            else:
                return render_template('index.html',d_message = "Invalid input")
    else:
        return render_template('index.html')

app.run()