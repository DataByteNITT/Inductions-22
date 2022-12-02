from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import io

PATH = "/Users/surendrasrinivas/Downloads/chromedriver"
download_path1 = "/Users/surendrasrinivas/Downloads/B.TECH/SEMESTER 5/MISC Sem_05/Avengers/imgs/train/Thor/"
wd = webdriver.Chrome(PATH)

def get_images(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    url = "https://www.google.com/search?q=Thor&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiGxuvPn7X7AhXX7nMBHf_wD1QQ_AUoAXoECAEQAw&biw=902&bih=996&dpr=2"
    wd.get(url) # Load this page with webdriver, access HTML elements.
    image_urls = set()
    thumbnail_path = "rg_i.Q4LuWd"
    image_class_name = "n3VNCb.KAlRDb"
    while len(image_urls) < max_images:
        scroll_down(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME, thumbnail_path)

        for img in thumbnails[len(image_urls):max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            images = wd.find_elements(By.CLASS_NAME, image_class_name)
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
            print("Image is found! ", (len(image_urls)))
    return image_urls

count = 0
def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
            print("Downloaded ! "+str(count+1))
    except Exception as e:
        print("Failed - ", e)

urls = get_images(wd, 3, 100)
#print(urls)
for i, url in enumerate(urls):
    download_image(download_path1, url, "Thor  "+str(i)+".jpg")
    count+=1

wd.quit()
