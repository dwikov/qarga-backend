from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/add-nlu-data', methods=["POST"])
def add_nlu_data():
    data = request.json
    conn = sqlite3.connect('database.db')
    sql = ''' INSERT INTO trainingData(uid,sentence,intent)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, [data["uid"], data["sentence"], data["intent"]])
    conn.commit()
    cur.close()
    conn.close()
    result_code = jsonify("Ok")
    result_code.headers['Access-Control-Allow-Origin'] = '*'
    result_code.headers['Access-Control-Allow-Headers'] = '*'
    return result_code


@app.route('/get-nlu-data', methods=["POST"])
def get_nlu_data():
    data = request.json
    print(data)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT sentence, intent FROM trainingData WHERE uid = ?", [data["uid"]])
    ret = cur.fetchall()
    print(ret)
    conn.commit()
    cur.close()
    conn.close()
    ret = jsonify(ret)
    ret.headers['Access-Control-Allow-Origin'] = '*'
    ret.headers['Access-Control-Allow-Headers'] = '*'
    return ret


if __name__ == '__main__':
    app.run(debug=True, port=5000)

