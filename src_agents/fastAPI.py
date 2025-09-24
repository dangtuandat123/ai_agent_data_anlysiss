import os
import uuid
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from main import run_data_analysis_agent
from langchain_core.messages import HumanMessage, AIMessage
import time
import json
import io
import base64
import matplotlib.pyplot as plt
import matplotlib
import datetime
import numpy as np
import pandas as pd
import sys

matplotlib.use('Agg')

app = Flask(__name__)
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = 'uploads'
CORS(app, origins=['http://localhost:8080'], supports_credentials=True)


conversation_history = {}

import pandas as pd

def run_and_return_last_printed_output(code: str):
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        exec(code)
        output = captured_output.getvalue().strip().split('\n')[-1]

        sys.stdout = sys.__stdout__

        return output

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def run_and_return_table_html(code: str):
    try:
        exec_locals = {}

        exec(code, {}, exec_locals)

        if 'df' not in exec_locals:
            raise ValueError("Mã phải trả về một DataFrame với tên là 'df'.")

        df = exec_locals['df']

        if isinstance(df, pd.DataFrame):
            html_table = df.to_html(index=False)
            return html_table
        else:
            raise ValueError("Mã phải trả về một DataFrame.")

    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")
        return None


def run_and_return_base64_image(code: str):
    try:
        exec(code)
        img_buffer = io.BytesIO()

        plt.savefig(img_buffer, format='png')
        plt.close()
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
        return img_base64

    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")
        plt.close()
        return None


@app.route('/api/chat', methods=['POST'])
def chat():
    session_id = session.get('session_id')

    if not session_id:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        print(f"DEBUG: New session created with ID: {session_id}")

    data = request.get_json()
    prompt = data.get('prompt')
    file_name_list = data.get('file_name_list')
    print(f"file_name_list {data}")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    history = conversation_history.get(session_id, [])
    history.append(HumanMessage(content=prompt))

    try:
        response_text = run_data_analysis_agent(history)
        history.append(AIMessage(content=response_text))
        conversation_history[session_id] = history

        print(f"Session: {session_id}, Messages: {history}")

        return jsonify({"message": response_text})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An internal error occurred"}), 500


@app.route('/api/chattest', methods=['POST'])
def chattest():
    session_id = session.get('session_id')

    if not session_id:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        print(f"DEBUG: New session created with ID: {session_id}")

    data = request.get_json()
    prompt = data.get('prompt')
    file_name_list = data.get('file_name_list')
    print(file_name_list)
    if len(file_name_list) > 0:
        session['current_list_file'] = file_name_list


    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    history = conversation_history.get(session_id, [])
    history.append(HumanMessage(content=prompt))
    print(os.path.abspath(rf"uploads/{session_id}/{session['current_list_file'][0]}"))
    try:
        response_text = run_data_analysis_agent(os.path.abspath(rf"uploads/{session_id}/{session['current_list_file'][0]}"),history)
        history.append(AIMessage(content=response_text))
        conversation_history[session_id] = history

        print(history)
        response_text = json.loads(response_text)
        print(response_text)

        # Giả lập mã tạo bảng HTML
#         response_text = {
#             "message": "Code processing",
#             "code": """
# import pandas as pd
# df = pd.DataFrame({
#     'Tên': ['Alice', 'Bob', 'Charlie'],
#     'Tuổi': [25, 30, 35],
#     'Thành phố': ['Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng']
# })
# """,
#             "iscode": True,
#             "type": "table_html"
#         }

        # Kiểm tra xem có phải là loại mã bảng HTML hay không
        if response_text['iscode']:
            if response_text['type'] == "img":
                base64_img = run_and_return_base64_image(response_text['code'])
                response_text['img_base64'] = base64_img
            if response_text['type'] == "table_html":
                table_html = run_and_return_table_html(response_text['code'])
                response_text['table_html'] = table_html
            if response_text['type'] == "text":
                print(123)
                response_text['message'] = run_and_return_last_printed_output(response_text['code'])


        print(response_text)

        return jsonify({"message": response_text})
    except Exception as e:
        print(f"Error processing request: {e}")
        response_error = {
            "message": "Đã có lỗi xảy ra!",
            "code": "",
            "iscode": False
        }
        return jsonify({"message": response_error}), 200


@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': 'Không tìm thấy file'}), 400
    session_id = session.get('session_id')

    if not session_id:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        print(f"DEBUG: New session created with ID: {session_id}")
    files = request.files.getlist('files')  # Nhận tất cả các file
    file_paths = []
    file_name_list = []
    for file in files:
        if file.filename == '':
            continue
        filename_random = f"{int(time.time() * 1000)}_{uuid.uuid4().hex}.{file.filename.split('.')[1]}"
        file_name_list.append(filename_random)
        os.makedirs(rf"{UPLOAD_FOLDER}/{session.get('session_id')}", exist_ok=True)

        file_path = os.path.join(rf"{UPLOAD_FOLDER}/{session.get('session_id')}", filename_random)
        file.save(file_path)
        file_paths.append(file_path)


    return jsonify({'message': 'Upload thành công', 'file_name_list': file_name_list})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
