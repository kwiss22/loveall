"""
간단한 Flask 테스트 - 연결 문제 진단용
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Flask 테스트 성공!</h1>
    <p>웹 서버가 정상적으로 작동하고 있습니다.</p>
    <p>이제 <a href="/main">메인 앱</a>으로 이동하거나</p>
    <p>web_vocab_app.py를 실행해보세요.</p>
    """

@app.route('/main')
def main():
    return """
    <h1>메인 앱으로 이동</h1>
    <p>이제 web_vocab_app.py를 실행하세요.</p>
    <p>명령어: python web_vocab_app.py</p>
    """

if __name__ == '__main__':
    print("="*60)
    print("Flask 간단한 테스트 서버 시작")
    print("="*60)
    print("브라우저에서 접속: http://127.0.0.1:5000")
    print("="*60)
    print("\n중지하려면 Ctrl+C를 누르세요.\n")
    try:
        app.run(debug=True, host='127.0.0.1', port=5000)
    except OSError as e:
        if "Address already in use" in str(e) or "address is already in use" in str(e):
            print(f"\n[ERROR] 5000번 포트가 이미 사용 중입니다!")
            print("다른 포트로 시도합니다...\n")
            app.run(debug=True, host='127.0.0.1', port=5001)
        else:
            print(f"\n[ERROR] 서버 시작 실패: {e}")
            raise

