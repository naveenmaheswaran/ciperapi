from flask import Flask, jsonify, request

app = Flask(__name__)
#############
def eceaser(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
###############
@app.route("/eceaser/<string:name>")
def dummy_apid(name: str):
    print(name)
    a=name.split("^")
    name=eceaser(a[0],int(a[1]))
    return jsonify(data=name), 200

@app.route("/dceaser/<string:name>")
def dummy_api(name: str):
    return jsonify(hi=name), 200


## encrypt hex
@app.route("/ehex/<string:name>")
def ehex(name: str):
    res=name.encode().hex()
    return jsonify(data=name,algo="hex",result=res), 200

## decrypt hex
@app.route("/dhex/<string:name>")
def dhex(name: str):
    import binascii
    res=str(binascii.unhexlify(name),'ascii')    
    return jsonify(data=name,algo="dehex",result=res), 200


## encrypt binary
@app.route("/ebinary/<string:name>")
def ebinary(name: str):
    res = ''.join(format(ord(i), 'b') for i in name) 
    return jsonify(data=name,algo="ebinary",result=res), 200

########## decrypt binary
@app.route("/dbinary/<string:name>")
def dbinary(name: str):
    bin_data =name



    str_data =' '


    for i in range(0, len(bin_data), 7): 
            temp_data = int(bin_data[i:i + 7]) 
            decimal_data = BinaryToDecimal(temp_data) 
            str_data = str_data + chr(decimal_data)
            
    return jsonify(data=name,algo="dbinary",result=str_data), 200



      
 
def BinaryToDecimal(binary): 
            
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
            dec = binary % 10
            decimal = decimal + dec * pow(2, i) 
            binary = binary//10
            i += 1
    return (decimal)	 




if __name__ == "__main__":
    app.run()
