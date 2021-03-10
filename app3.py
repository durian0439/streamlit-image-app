import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import os
from datetime import datetime

        #https://kylog.tistory.com/17
#깃 연동
def load_image(image_file):
    img = Image.open(image_file)
    return img

def save_uploaded_file(directory, img):
    #1. 디렉토리가 있는지 확인, 없으면 만들기.  # import os하기
    if not os.path.exists(directory):
        os.makedirs(directory)
    #2. 디렉토리가 있으니 파일 저장
    # with open(os.path.join(directory, file.name),'wb') as f:
    #     f.write(file.getbuffer())


    # 현재시간을 파일명으로 #print(datetime.now().isoformat())
    filename = datetime.now().isoformat().replace(':','-').replace('.','-')
    img.save(directory + '/'+filename+'.jpg')
    return st.success("Saved file : {} in {}".format(filename+'.jpg', directory)) #success 성공 시 메세지 표츌


def main():
    # img = Image.open('data/birds.jpg')
    # st.image(img, use_column_width= True)
    # 파일 업로드하기
    st.subheader("이미지 파일 업로드")
    image_file_list = st.file_uploader("upload Image", type = ['png','jpg','jpeg'], accept_multiple_files= True)#위젯 만들기
    print(image_file_list)

    if image_file_list is not None:
        # 각 파일을 이미지로 바꿔줘야함
        image_list = []  #이미지 리스트를 모아놓음.

        #모든 파일이 이미지 리스트에 저장됨.
        for file in image_file_list:
            img = load_image(file)
            image_list.append(img)

        # 이미지를 화면에 확인하기.//디버깅용
        # for image in image_list:
        #     st.image(image)


        option_list = ['Show Image', 'Rotate Image','Creat Thumbnail', 'Crop Image','Merge Image', 
        'Flip Image', 'change color','Filters - Sharpen','Filters - Edge Enhance', 'Contrast Image'] 
        # 보이기/ 돌리기/ 썸네일/ 자르기/ 합치기/ 플립(좌우반전)/흑백/ 날카롭게/ 가장자리 강화/ 배경과의 대조강화

        option=st.selectbox('옵션을 선택하세요', option_list)  #메뉴 선택하기0
        print(option) #메뉴의 셀렉트박스를 누를 경우 터미널에 찍힌다.

        # 2.하드코딩 조정하기

        if option == 'Show Image' :
            for image in image_list:
                st.image(image)
             
            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                #파일저장
                for img in image_list :
                    save_uploaded_file(directory, img)

        #     # file_name_list = []
        #     if st.button('저장',key = '저장'):
        #         save_uploaded_file('temp_files',image_file)
        #     # for img_files in uploaded_file:
        #     #     save_uploaded_file('temp_files',img_files)
        #     #     file_name_list.append(img_files.name)


        elif option == 'Rotate Image' :
            #1. 유저가 입력
            rotate_num = st.slider('각도', 0,360)
            #2. 모든 이미지를 돌린다
            tranforem_image_list = []
            for image in image_list:  
                rotated_img = image.rotate(rotate_num)
                st.image(rotated_img)
                tranforem_image_list.append(rotated_img)
                
            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                #파일저장
                for img in tranforem_image_list :
                    save_uploaded_file(directory, img)

        elif option =='Creat Thumbnail':
            # 이미지의 사이즈를 알아야겠다.
            size = img.size
            st.write('원래 사이즈 = {}'.format(size))
            width = st.number_input('가로 사이즈를 입력하세요',1,100)   
            height = st.number_input('세로 사이즈를 입력하세요',1,100)
            size1 = (width,height)

            transformed_img_list=[]
            for image in image_list:
                img.thumbnail(size1)
                st.image(img)
                transformed_img_list.append(img)

            
            #저장은 여기에서
            for img in tranforem_image_list :
                save_uploaded_file(directory, img)

            # img.thumbnail(size1)
            # img.save('data/thumb.png')
            # st.image(img)

        # elif option =='Crop Image':
        #     #왼쪽 위 부분부터 너비와 깊이만큼 잘라라~
        #     #왼쪽 위 부분 좌표 = (50,100)
        #     #너비 x축으로 200, 깊이 y축으로 200을 계산한 종료좌표 = (200,200)
        #     #https://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-40-Cropping-Images-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%9E%98%EB%9D%BC%EB%82%B4%EA%B8%B0
        #     start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1)
        #     start_y = st.number_input('시작 y 좌표', 0, img.size[1]-1)
        #     max_width = img.size[0] - start_x
        #     max_height = img.size[1] - start_y
        #     width = st.number_input('width 입력', 1, img.size[0])
        #     height = st.number_input('height 입력', 1, img.size[1])
                    
        #     box = (start_x, start_y, start_x + width, start_y + height)
        #     cropped_img = img.crop(box)
        #     # cropped_img.save('data/crop.png')
        #     st.image(cropped_img)

        # elif option =='Merge Image':
        #     merge_file = st.file_uploader("upload Image", type = ['png','jpg','jpeg'], key = 'merge') #키가 같으면 안됨
        #     merge_img = Image.open(merge_file)

        #     if merge_img is not None:
        #         start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1)
        #         start_y = st.number_input('시작 y 좌표', 0, img.size[1]-1)
        #         position = (start_x,start_y)
        #         img.paste(merge_img, position)
        #         st.image(img)

        elif option =='Flip Image':
            # if st.button("좌우"):
            #     flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
            # if st.button("상하"):
            #     flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)

            # st.image(flipped_image)
            status = st.radio('플립선택', ['상하', '좌우'])
            if status == '상하':
                transformed_img_list=[]
                for img in image_list:
                    flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_image)
                    transformed_img_list.append(flipped_image)

            elif status == '좌우':
                transformed_img_list=[]
                for img in image_list:
                    flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_image)
                    transformed_img_list.append(flipped_image)
            #저장은 여기에
            directory = st.text_input('파일경로 입력')
            if st.button('파일 저장'):
                #파일저장
                for img in tranforem_image_list :
                    save_uploaded_file(directory, img)

            

        # elif option =='change color':
        #     status = st.radio('색 변경',['RGB','Gray Scale','Black & White'])
        #     if status == 'RGB':
        #         color = 'RGB'
        #     elif status == 'Gray Scale':
        #         color = 'L'
        #     elif status == 'Black & White':
        #         color = '1'

        #     bw = img.convert(color)
        #     st.image(bw)

        # elif option == 'Filters - Sharpen':
        #     sharp_img = img.filter(ImageFilter.SHARPEN)
        #     st.image(sharp_img)

        # elif option =='Filters - Edge Enhance':
        #     edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
        #     st.image(edge_img)

        # elif option =='Contrast Image':
        #     contrast_img = ImageEnhance.Contrast(img).enhance(2)
        #     st.image(contrast_img)




    # 1. 이미지를 내 맘대로 올릴 수 있어야 한다.
    # (이미지는 한 장)
    
    # !! 하드코딩 된 코드를 유저들이 변경 할 수 있도록 코딩하시오
    # 코딩에 숫자 등 조건이 정해져있는 경우  - 하드코딩
    # 2. 로테이트 이미지에 각도 조절을 위한 도구 필요
    # 3. 썸네일에 이미지 사이즈 얻어오기. 시작점과 너비 높이를 받으면 유저가 원하는대로 크롭할 수 있게
    # flip 조건 추가(옵션)
    # b/w는 알아서
    # 

    # !! 어러파일을 변환할 수 있도록 수정.
    # 각 옵션마다 저장하기 버튼이 있어서 버튼을 누르면 저장하도록
    # 저장시에는 디렉토리 이름을 유저가 직접 입력하여 저장.

if __name__ == '__main__':
    main()