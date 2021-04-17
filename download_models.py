from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(
    file_id='1b7b3ilkyI4uED8_jkmSzBLtjV9KhESf6',
    dest_path='./saved_models/after_unfreeze_resnet50.pth.tar'
)
print("done after_unfreeze_resnet50.pth.tar")
