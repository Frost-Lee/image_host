# Image Host
A simple server - client system for personal image hosting.



## Features

- Simplest implementation of image host server with Flask.
- JPEG image compress customizable.
- Easy to upload, the direct link will be copied to your clipboard.



## Configuration

To configure this system, rename all files named `config_secure.example.py` to `config_secure.py` and modify the content to your personal configuration.



## Usage

To start the image host server, use the following command.

``` shell
nohup python3 image_host_server/app.py &
```

Use the following command to see the detailed instructions for uploading an image.

``` shell
python3 image_host_client/image_upload.py -h
```



## To Do List

- [ ] Make the client application a menu bar macOS application
- [ ] Database and better local file saving
- [ ] Compressing .png images
- [ ] Use HTTPS on the server application



## Donation

If you are purchasing a server instance from [VULTR](https://www.vultr.com), you can go via my linking code: https://www.vultr.com/?ref=8304275-4F.

