import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

# 앱 제목
st.title("PDF to JPG Converter")

# PDF 파일 업로드 받기
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # PDF 파일 열기
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    # 모든 페이지를 JPG 이미지로 변환
    images = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)  # 페이지 로드
        pix = page.get_pixmap()  # 페이지를 픽셀 이미지로 변환
        img = Image.open(io.BytesIO(pix.tobytes("png")))  # 이미지를 PNG로 변환
        images.append(img)

    # 각 페이지의 이미지를 화면에 표시
    for i, img in enumerate(images):
        st.image(img, caption=f"Page {i+1}", use_column_width=True)

    # 여러 페이지가 있는 경우, 다운로드 링크로 제공하기 위해 ZIP 파일로 압축할 수 있습니다.
else:
    st.info("Please upload a PDF file to start the conversion.")
