from flask import Flask, render_template, request


MAX_FILE_SIZE = 1024 * 1024*10 + 1

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files["file"]
        filestr = file.read()
        npimg = np.fromstring(filestr, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imsave("./templates/new.jpg",img)
        #cv2.imwrite ("new.jpg",cv2.cvtColor(z, cv2.COLOR_BGR2RGB))
        if bool(file.filename):
            file_bytes = file.read(MAX_FILE_SIZE)
            args["file_size_error"] = len(file_bytes) == MAX_FILE_SIZE
        args["method"] = "POST"
    return render_template("index.html", args=args)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
