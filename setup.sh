pip install googledrivedownloader
if [ -f saved_models/after_unfreeze_resnet50.pth.tar ]
then
    echo "model downloaded"
else 
    python3 download_models.py
fi

python3 wsgi.py
