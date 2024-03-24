import cv2 as cv 

#카툰처리용 영상 넣어주는 곳.
video_file = '07e288d6-9481-4ffe-b168-e7282f1f8d9f.mp4'

video =  cv.VideoCapture(video_file)


'''엣지전용 설정값'''
#하위 임계값 
#이값보다 작으면 엣지로 안친다.
threshold1 = 1500

#상위 임계값 이것보다 높으면 그것들은 강한놈으로 간주한다.
threshold2 = 2500

#그레디언트 계산을 위한 필터의 값 3 7 사이의 홀수로 놔야함
aperture_size = 5



if video.isOpened() :
    
    #동영상 속도조절용
    fps = video.get (cv.CAP_PROP_FPS )
    wait_msec = int(1 / fps * 500)
    
    
    #루프 돌릴 친구
    while True :
        valid, img = video.read()
        
        #영상 없을때 종료
        if not valid : break
        
        ''' 이 라인 부터 만화적 표현을 넣어 볼겁니다'''
        # 이미지를 그레이 스케일로 변환 엣지잘 뽑아주려고
        gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        
        #블러처리용
        blurred_img = cv.GaussianBlur(img, (3, 3), 0)
        
        #엣지강조용
        edge = cv.Canny(gray_img, threshold1, threshold2, apertureSize=aperture_size)
        edge = cv.adaptiveThreshold(edge, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
        
        
        # 엣지값이용해서 바꿔준 녀석
        cartoon = cv.bitwise_and(blurred_img, blurred_img, mask = edge)
        
        '''위에까지 만화적 표현을 넣어준 과정 '''
        
        cv.imshow('cartoon_player', cartoon)
        
        key = cv.waitKey(wait_msec)
        
        #종료키
        if key == 27 : #'ECS'를 의미
            break
    
    cv.destroyAllWindows()
    