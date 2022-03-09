dir="$PWD"
#python mmocr/utils/ocr.py ttttt.png --output demo/output.jpg --det FCE_CTW_DCNv2 --det-ckpt fcenet_r50dcnv2_fpn_1500e_ctw1500_20211022-e326d7ec.pth --recog SAR_CN --recog-ckpt sar_r31_parallel_decoder_chineseocr_20210507-b4be8214.pth

#nohup jupyter notebook --no-browser --ip=0.0.0.0 --port 8416 --allow-root > logsfile.logs & disown

docker run -it --gpus all -d -v $dir:/$dir -w $dir --expose 8416 -p 8416:8416 mmocr
#docker run -it  --runtime=nvidia -v $dir:/$dir -w $dir --expose 8416 -p 8416:8416 mmocr
#docker run -it --gpus '"device=0"' -v /DATA:/DATA --expose 8416 -p 8416:8416 mmocr
