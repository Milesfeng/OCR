# OCR
## 使用Dockerfile進行佈署
    git clone https://github.com/Milesfeng/OCR.git
    cd OCR
    sudo docker build -t ocr .
    sudo docker run -it --name myocr --net=host ocr
    
    

