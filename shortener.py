from flask import Flask, render_template, request, redirect, url_for
import random
import xml.etree.ElementTree as ET

xmlFile = "Python/URL Shortener/data.xml"
tree = ET.parse(xmlFile)
root = tree.getroot()

def xmlConfiguration(url, ID):
    doc = ET.SubElement(root, "url")

    ET.SubElement(doc, "id").text = ID
    ET.SubElement(doc, "url").text = url

    tree.write(xmlFile)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def indexPost():
    url = request.form["url"]

    #Generate a path end to the url.
    rootLength = len(root)
    urlID = "url" + str(rootLength)

    #Save the URL in an XML
    xmlConfiguration(url, urlID)

    urlToPass = "192.168.0.105:5000/url/{}".format(urlID)
    return render_template("clipboard.html", url=urlToPass)

@app.route("/url/<ID>")
def indexID(ID):
    for child in root:
        for subChild in child:
            if subChild.text == ID:
                url = child[1].text

    return redirect(url)

app.run(debug=True, host="192.168.0.105")