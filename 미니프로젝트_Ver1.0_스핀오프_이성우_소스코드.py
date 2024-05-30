import math
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os.path



### 함수부
## 공통 함수부
def malloc2D(h, w, initValue=0):
    memory = [[initValue for _ in range(w)] for _ in range(h)]
    return memory


def openImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    fullname = askopenfilename(parent=window, filetypes=(('RAW파일', '*.raw'), ('모든파일', '*.*')))
    # 중요! 입력 이미지 크기를 결정
    fsize = os.path.getsize(fullname)  # 파일 크기 (Byte로 알려줌)
    inH = inW = int(math.sqrt(fsize))

    # 메모리 할당
    inImage = malloc2D(inH, inW)  # 초기값을 안 넣으면 0이 들어가고, 필요할 때 지정하고 싶을 때.. initValue 쓰기

    # 3. 파일 --> 메모리
    rfp = open(fullname, 'rb')
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = ord(rfp.read(1))
    rfp.close()
    equalImage()


def saveImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    if (outImage == None or len(outImage)):  # 영상처리를 한 적이 없다면
        return
    wfp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw',
                        filetypes=(('RAW 파일', '*.raw'), ('모든 파일', '*.*')))
    import struct
    for i in range(outH):
        for k in range(outW):
            wfp.write(struct.pack('B', outImage[i][k]))
    wfp.close()
    messagebox.showinfo('성공', wfp.name + ' 저장완료!')


def displayImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    ## 기존에 이미지를 오픈한 적이 있으면, 캔버스 뜯어내는 작업이 필요해!!
    if (canvas != None):
        canvas.destroy()

    # 벽, 캔버스, 종이 설정
    window.geometry(str(outH) + 'x' + str(outW))  # "512x512"
    canvas = Canvas(window, height=outH, width=outW, bg='yellow')  # 칠판
    paper = PhotoImage(height=outH, width=outW)  # 종이
    canvas.create_image((outH // 2, outW // 2), image=paper, state='normal')

    ## 메모리 -> 화면
    # for i in range(inH):
    #     for k in range(inW):
    #         r = g = b = inImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    # 더블 버퍼링이란? 비슷한 기법(모두 다 메모리 상에 출력형태로 생성한 후에, 한 방에 출력)
    rgbString = ""  # 전체에 대한 16진수 문자열
    for i in range(outH):
        oneString = ""  # 한 줄에 대한 16진수 문자열
        for k in range(outW):
            r = g = b = outImage[i][k]
            oneString += '#%02x%02x%02x ' % (r, g, b)  # 작은따옴표 끝 직전에 띄어쓰기 하나 해주기
        rgbString += '{' + oneString + '} '
    paper.put(rgbString)
    canvas.pack()


## 영상처리 함수부
def equalImage():  # 동일 이미지
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
    #   #   #   #   #   #
    displayImage()


def addImage():  # 밝게/어둡게 이미지
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    value = askinteger('정수 입력', '-255 ~ 255 입력', maxvalue=255, minvalue=-255)
    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            px = inImage[i][k] + value
            if (px > 255):
                px = 255
            if (px < 0):
                px = 0
            outImage[i][k] = px
    #   #   #   #   #   #
    displayImage()


def reverseImage():  # 반전 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - inImage[i][k]
    #   #   #   #   #   #
    displayImage()


def bwImage():  # 흑백 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] > 127):
                outImage[i][k] = 255
            if (inImage[i][k] < 127):
                outImage[i][k] = 0
    #   #   #   #   #   #
    displayImage()


def gammaImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    value = askinteger('정수 입력 --> ', '0 ~ 10 입력', maxvalue=10, minvalue=0)
    if value is None:  # 사용자가 취소를 선택한 경우
        return

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            px = inImage[i][k] / 255
            result = pow(px, value)
            result *= 255

            if result < 0:
                result = 0
            elif result > 255:
                result = 255
            outImage[i][k] = int(result)  # 소수점 이하 자리 제거

    #   #   #   #   #   #
    displayImage()



def ParabolCapImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            pixel = inImage[i][k]
            value = int(255 - 255 * ((pixel / 255) ** 2))  # 수정된 부분
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            outImage[i][k] = value

    displayImage()


def ParabolCupImage():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            pixel = inImage[i][k]
            value = int(255 * ((pixel / 255 - 1) ** 2))  # 수정된 부분
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            outImage[i][k] = value

    displayImage()



def andImage():  # AND 처리 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    value = askinteger('정수 입력 --> ', '0 ~ 255 입력', maxvalue=255, minvalue=0)
    if value is None:  # 사용자가 취소를 선택한 경우
        return

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            pixel = inImage[i][k]
            result = pixel & value  # AND 연산 결과 저장
            outImage[i][k] = result  # 결과를 출력 이미지에 할당
    #   #   #   #   #   #
    displayImage()


def orImage():  # OR 처리 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    value = askinteger('정수 입력 --> ', '0 ~ 255 입력', maxvalue=255, minvalue=0)
    if value is None:  # 사용자가 취소를 선택한 경우
        return

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            pixel = inImage[i][k]
            result = pixel | value  # OR 연산 결과 저장
            outImage[i][k] = result  # 결과를 출력 이미지에 할당

    displayImage()

def xorImage():  # XOR 처리 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    value = askinteger('정수 입력 --> ', '0 ~ 255 입력', maxvalue=255, minvalue=0)
    if value is None:  # 사용자가 취소를 선택한 경우
        return

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            pixel = inImage[i][k]
            result = pixel ^ value  # XOR 연산 결과 저장
            outImage[i][k] = result  # 결과를 출력 이미지에 할당

    displayImage()

def zoomOut():  # 축소 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존

    scale = askinteger('정수 입력 --> ', '양수 입력', minvalue=1)  # 0을 입력하지 못하게 수정

    outH = inH // scale  # 정수 나눗셈을 이용하여 소수점 이하 버림
    outW = inW // scale

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(outH):  # 축소된 이미지 크기로 반복
        for k in range(outW):
            # 축소된 이미지의 각 픽셀에 대해 해당하는 원본 이미지 픽셀의 평균 값을 할당
            sum_pixel = 0
            for r in range(i * scale, (i + 1) * scale):
                for c in range(k * scale, (k + 1) * scale):
                    sum_pixel += inImage[r][c]
            outImage[i][k] = sum_pixel // (scale * scale)
    #   #   #   #   #   #
    displayImage()


def zoomIn():  # 확대 알고리즘 (포워딩)
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존

    scale: int | None = askinteger('정수 입력 --> ', '양수 입력', minvalue=0)

    outH = inH * scale
    outW = inW * scale

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            outImage[(i * scale)][(k * scale)] = inImage[i][k]
    #   #   #   #   #   #
    displayImage()


def zoomIn2():  # 확대 알고리즘2 (백워딩)
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존

    scale = askinteger('정수 입력 --> ', '양수 입력', minvalue=1)  # 1보다 큰 양수를 입력해야 함

    outH = inH * scale
    outW = inW * scale

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(outH):
        for k in range(outW):
            in_i = i // scale  # 원본 이미지의 픽셀 위치 계산
            in_k = k // scale
            outImage[i][k] = inImage[in_i][in_k]  # 확대된 이미지에 픽셀 복사
    #   #   #   #   #   #
    displayImage()


def rotate():  # 회전 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존

    angle = askinteger('각도 입력 --> ', '0 ~ 360 사이의 각도를 입력', maxvalue=360, minvalue=0)
    if angle is None:  # 사용자가 취소를 선택한 경우
        return

    radian = math.radians(angle)  # 라디안으로 변환

    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 회전 중심점 계산
    center_x = outH // 2
    center_y = outW // 2

    # 진짜 영상처리 알고리즘
    for i in range(outH):
        for k in range(outW):
            # 회전된 좌표 구하기
            rotated_x = int((i - center_x) * math.cos(radian) - (k - center_y) * math.sin(radian)) + center_x
            rotated_y = int((i - center_x) * math.sin(radian) + (k - center_y) * math.cos(radian)) + center_y

            if 0 <= rotated_x < outH and 0 <= rotated_y < outW:
                outImage[i][k] = inImage[rotated_x][rotated_y]
            else:
                outImage[i][k] = 0  # 회전한 이미지 범위를 벗어나면 0으로 채움
    #   #   #   #   #   #
    displayImage()


def rotate2():  # 회전 알고리즘 + 중앙 / 백워딩
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존

    angle = askinteger('각도 입력 --> ', '0 ~ 360 사이의 각도를 입력', maxvalue=360, minvalue=0)
    if angle is None:  # 사용자가 취소를 선택한 경우
        return

    radian = math.radians(angle)  # 라디안으로 변환

    outH = inH
    outW = inW

    # 중심점 계산
    center_x = inH // 2
    center_y = inW // 2

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(outH):
        for k in range(outW):
            # 회전된 좌표 구하기
            rotated_x = int((i - center_x) * math.cos(radian) - (k - center_y) * math.sin(radian)) + center_x
            rotated_y = int((i - center_x) * math.sin(radian) + (k - center_y) * math.cos(radian)) + center_y

            if 0 <= rotated_x < inH and 0 <= rotated_y < inW:
                outImage[i][k] = inImage[rotated_x][rotated_y]
            else:
                outImage[i][k] = 0  # 회전한 이미지 범위를 벗어나면 0으로 채움
    #   #   #   #   #   #
    displayImage()


def histoStretch():  # 히스토그램 스트레칭 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 최소 및 최대 픽셀 값 찾기
    high = low = inImage[0][0]
    for i in range(inH):
        for k in range(inW):
            pixel_value = inImage[i][k]
            if pixel_value < low:
                low = pixel_value
            if pixel_value > high:
                high = pixel_value

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 진짜 영상처리 알고리즘
    for i in range(inH):
        for k in range(inW):
            old = inImage[i][k]
            new = (old - low) / (high - low) * 255.0
            new = max(0, min(new, 255))  # 픽셀 값이 0 미만 또는 255 초과 시 조정
            outImage[i][k] = int(new)  # 정수형으로 변환하여 할당
    #   #   #   #   #   #
    displayImage()


def endIn():  # 엔드-인 처리 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 최소 및 최대 픽셀 값 찾기
    high = low = inImage[0][0]
    for i in range(inH):
        for k in range(inW):
            pixel_value = inImage[i][k]
            if pixel_value < low:
                low = pixel_value
            if pixel_value > high:
                high = pixel_value

    # 엔드-인 처리 알고리즘
    high -= 50
    low += 50

    # 영상 처리
    for i in range(inH):
        for k in range(inW):
            old = inImage[i][k]
            new = (old - low) / (high - low) * 255
            new = max(0, min(new, 255))  # 픽셀 값이 0 미만 또는 255 초과 시 조정
            outImage[i][k] = int(new)  # 정수형으로 변환하여 할당
    #   #   #   #   #   #
    displayImage()


def histoEqual():  # 히스토그램 평활화 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 1단계 : 빈도 수 세기
    histo = [0] * 256
    for i in range(inH):
        for k in range(inW):
            histo[inImage[i][k]] += 1

    # 2단계 : 누적 히스토그램 생성
    sumHisto = [0] * 256
    sumHisto[0] = histo[0]
    for i in range(1, 256):
        sumHisto[i] = sumHisto[i - 1] + histo[i]

    # 3단계 : 정규화된 히스토그램 생성
    normalHisto = [0] * 256
    total_pixels = inH * inW
    for i in range(256):
        normalHisto[i] = (sumHisto[i] / total_pixels) * 255

    # 4단계 : inImage를 정규화된 값으로 치환
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = int(normalHisto[inImage[i][k]])

    #   #   #   #   #   #
    displayImage()


def emboss():
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW

    # 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [-1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 엠보싱 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k] + 127, 255))

            # 정규화하지 않은 경우, 0 미만이거나 255 초과인 경우 조정
            # tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def blur():  # 블러링 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [1. / 9, 1. / 9, 1. / 9],  # 블러링 마스크
        [1. / 9, 1. / 9, 1. / 9],
        [1. / 9, 1. / 9, 1. / 9]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 엠보싱 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k] + 60, 255))

            # 정규화하지 않은 경우, 0 미만이거나 255 초과인 경우 조정
            # tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def sharp():  # 샤프닝 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [-1.0, -1.0, -1.0],  # 샤프닝 마스크
        [-1.0, 9.0, -1.0],
        [-1.0, -1.0, -1.0]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 엠보싱 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k] + 100, 255))

            # 정규화하지 않은 경우, 0 미만이거나 255 초과인 경우 조정
            # tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def edge1():  # 수직검출 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [1.0, 0.0, -1.0],  # 수직 에지 검출 마스크
        [1.0, 0.0, -1.0],
        [1.0, 0.0, -1.0]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 엠보싱 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k] - 5, 255))

            # 정규화하지 않은 경우, 0 미만이거나 255 초과인 경우 조정
            # tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def edge2():  # 수평검출 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    # 화소영역 처리
    mask = [
        [-1.0, -1.0, -1.0],  # 수평 에지 검출 마스크
        [0.0, 0.0, 0.0],
        [1.0, 1.0, 1.0]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 수평 검출 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k] + 5, 255))

            # 정규화하지 않은 경우, 0 미만이거나 255 초과인 경우 조정
            # tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def Laplacian():  # 라플라시안 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [0.0, -1.0, 0.0],  # 라플라시안 마스크
        [-1.0, 4.0, -1.0],
        [0.0, -1.0, 0.0]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 라플라시안 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def GausianS():  # 가우시안 스무딩 알고리즘
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [1.0 / 16, 1.0 / 8, 1.0 / 16],  # 가우시안 스무딩 마스크
        [1.0 / 8, 1.0 / 4, 1.0 / 8],
        [1.0 / 16, 1.0 / 8, 1.0 / 16]
    ]

    # 임시 입력 메모리 초기화(127)
    tmpInImage = [[127 for _ in range(inW + 2)] for _ in range(inH + 2)]  # 값 127로 초기화

    # 입력 이미지 --> 임시 입력 이미지
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImage[i][k]

    # 임시 출력 이미지 생성
    tmpOutImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # 라플라시안 알고리즘 적용
    for i in range(outH):
        for k in range(outW):
            S = 0.0
            for m in range(3):
                for n in range(3):
                    S += tmpInImage[i + m][k + n] * mask[m][n]
            tmpOutImage[i][k] = S

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 임시 출력 이미지 값을 범위 내로 조정
            tmpOutImage[i][k] = max(0, min(tmpOutImage[i][k], 255))

            # 출력 이미지에 할당
            outImage[i][k] = int(tmpOutImage[i][k])

    # 결과 출력
    displayImage()

def prewittVertical():  # 프리윗 필터 수직
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [-1.0, 0.0, 1.0],  # 프리윗 마스크
        [-1.0, 0.0, 1.0],
        [-1.0, 0.0, 1.0]
    ]

    # 프리윗 필터 적용
    for i in range(outH):
        for k in range(outW):
            total = 0
            # 주변 픽셀의 가중치 합 계산
            for m in range(3):
                for n in range(3):
                    # 입력 이미지 경계 처리
                    ii = max(0, min(inH - 1, i + m - 1))
                    kk = max(0, min(inW - 1, k + n - 1))
                    total += inImage[ii][kk] * mask[m][n]

            # 출력 이미지에 필터 결과 할당
            outImage[i][k] = int(total)

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 출력 이미지 범위 조정
            outImage[i][k] = max(0, min(outImage[i][k], 255))

    # 결과 출력
    displayImage()

def sobelVertical():  # 소벨 필터 수직
    global window, canvas, paper, fullname
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 영상 크기 결정 --> 알고리즘에 의존
    outH = inH
    outW = inW

    # 메모리 할당
    outImage = malloc2D(outH, outW)

    # 화소영역 처리
    mask = [
        [-1.0, 0.0, 1.0],  # 소벨 마스크
        [-2.0, 0.0, 2.0],
        [-1.0, 0.0, 1.0]
    ]

    # 소벨 필터 적용
    for i in range(outH):
        for k in range(outW):
            total = 0
            # 주변 픽셀의 가중치 합 계산
            for m in range(3):
                for n in range(3):
                    # 입력 이미지 경계 처리
                    ii = max(0, min(inH - 1, i + m - 1))
                    kk = max(0, min(inW - 1, k + n - 1))
                    total += inImage[ii][kk] * mask[m][n]

            # 출력 이미지에 필터 결과 할당
            outImage[i][k] = int(total)

    # 출력 영상 후처리
    for i in range(outH):
        for k in range(outW):
            # 출력 이미지 범위 조정
            outImage[i][k] = max(0, min(outImage[i][k], 255))

    # 결과 출력
    displayImage()

## 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], []
inH, inW, outH, outW = [0] * 4
fullname = ''

## 메인 코드부
window = Tk()  # 벽
window.geometry("500x500")
window.resizable(width=False, height=False)
window.title("영상처리 (RC 1)")

# 메뉴 만들기
mainMenu = Menu(window)  # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)  # 상위 메뉴 (파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)

pixelMenu = Menu(mainMenu, tearoff=0)  # 상위 메뉴 (화소 점 처리)
mainMenu.add_cascade(label='화소 점 처리', menu=pixelMenu)
pixelMenu.add_command(label='동일 이미지', command=equalImage)
pixelMenu.add_command(label='밝게/어둡게', command=addImage)
pixelMenu.add_command(label='반전', command=reverseImage)
pixelMenu.add_command(label='흑백', command=bwImage)
pixelMenu.add_command(label='감마', command=gammaImage)
pixelMenu.add_command(label='파라볼라 Cap', command=ParabolCapImage)
pixelMenu.add_command(label='파라볼라 Cup', command=ParabolCupImage)
pixelMenu.add_command(label='AND', command=andImage)
pixelMenu.add_command(label='OR', command=orImage)
pixelMenu.add_command(label='XOR', command=xorImage)

geometryMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='기하학 처리', menu=geometryMenu)
geometryMenu.add_command(label='축소', command=zoomOut)
geometryMenu.add_command(label='확대(포워딩)', command=zoomIn)
geometryMenu.add_command(label='확대(백워딩)', command=zoomIn2)
geometryMenu.add_command(label='회전', command=rotate)
geometryMenu.add_command(label='회전(중앙,백워딩)', command=rotate2)

histogramMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='히스토그램 처리', menu=histogramMenu)
histogramMenu.add_command(label='히스토그램 스트래칭', command=histoStretch)
histogramMenu.add_command(label='엔드-인', command=endIn)
histogramMenu.add_command(label='평활화', command=histoEqual)

localpixelMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label='화소 영역 처리', menu=localpixelMenu)
localpixelMenu.add_command(label='엠보싱', command=emboss)
localpixelMenu.add_command(label='블러링', command=blur)
localpixelMenu.add_command(label='샤프닝', command=sharp)
localpixelMenu.add_command(label='수직 검출', command=edge1)
localpixelMenu.add_command(label='수평 검출', command=edge2)
localpixelMenu.add_command(label='라플라시안', command=Laplacian)
localpixelMenu.add_command(label='가우시안 스무딩', command=GausianS)
localpixelMenu.add_command(label='프리윗 수직', command=prewittVertical)
localpixelMenu.add_command(label='소벨 수직', command=sobelVertical)

window.mainloop()