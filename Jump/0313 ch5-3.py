# 패키지
# 패키지란 무엇인가 ?
# 패키지는 도트(.)를 사용하여 파이썬 모듈을 계층적 (디렉터리 구조)로 관리할 수 있게 해준다.
# 예를 들어 이름이 A.B인 경우에 A는 패키지이름이 되고 B는 A 패키지의 B 모듈이 된다.
# 패키지 구조는 디렉터리와 모듈로 이루어 진다.
# 가장의 game 패키지 예

# # game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

# game이 루트 디렉터리가 되고, sound, graphic, play는 서브 디렉터리이다.
# 패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나, 유지 보수 등 여러 면에서 유리.
# 패키지 구조로 모듈을 만든다면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용 할 수 있다.

# 패키지 만들기