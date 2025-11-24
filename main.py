from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# --- 您的核心查詢邏輯：請將 get_fcu_course_link 函數貼在這裡 ---
def get_fcu_course_link(course_code: str) -> str:
    """
    請貼上您調整好的 requests/BeautifulSoup 邏輯。
    """
    # 範例代碼 (請替換為您的實際邏輯)
    if course_code == "1234":
        return "https://coursesearch03.fcu.edu.tw/result_1234"
    return "無效的選課代號"

# Flask 路由設定：接收 GET 請求
@app.route('/search', methods=['GET'])
def search_api():
    # 從 URL 參數獲取 'code' (Power Automate 將使用此參數)
    course_code = request.args.get('code') 

    if not course_code:
        return jsonify({'error': 'Missing course code parameter.'}), 400

    result_link = get_fcu_course_link(course_code)
    
    return jsonify({
        'url': result_link,
        'status': 'success' if result_link.startswith('http') else 'not_found'
    })

# Render 將使用 gunicorn 運行 app
# if __name__ == '__main__':
#     app.run(debug=True)