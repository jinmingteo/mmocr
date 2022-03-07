#for i in {01..26}; do
#    echo "$i"
#    wget "https://cloud.tsinghua.edu.cn/d/6f1cfc516c324f41a07b/files/?p=%2Fctw-public%2Fimages-trainval%2Fctw-trainval-$i-of-26.tar&dl=1" -O ctwdataset/ctw-trainval-$i.tar
#done


#for i in {01..26}; do
#    echo "$i"
#    tar -xvf ctwdataset/ctw-trainval-$i.tar -C ctwdataset/images/
#done

#LSVT Full training dataset
wget https://rrc.cvc.uab.es/?com=downloads&action=download&ch=16&f=aHR0cHM6Ly9kYXRhc2V0LWJqLmNkbi5iY2Vib3MuY29tL2xzdnQvdHJhaW5fZnVsbF9pbWFnZXNfMC50YXIuZ3o= -O dataset/LSVT/train_0.tar.gz
wget https://rrc.cvc.uab.es/?com=downloads&action=download&ch=16&f=aHR0cHM6Ly9kYXRhc2V0LWJqLmNkbi5iY2Vib3MuY29tL2xzdnQvdHJhaW5fZnVsbF9pbWFnZXNfMS50YXIuZ3o= -O dataset/LSVT/train_1.tar.gz
wget https://rrc.cvc.uab.es/?com=downloads&action=download&ch=16&f=aHR0cHM6Ly9kYXRhc2V0LWJqLmNkbi5iY2Vib3MuY29tL2xzdnQvdHJhaW5fZnVsbF9sYWJlbHMuanNvbg== -O dataset/LSVT/train_labels.json

tar -xf dataset/LSVT/train_0.tar.gz
tar -xf dataset/LSVT/train_1.tar.gz
