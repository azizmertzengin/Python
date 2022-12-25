from bs4 import BeautifulSoup
import requests
import smtplib

productURL = "https://www.hepsiburada.com/modern-dunya-klasikleri-seti-7-kitap-takim-p-hbv000007sb0c"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206"}

def checkPrice():
    page = requests.get(productURL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="product-name").get_text()
    price = soup.find(id="originalPrice").get_text()
    convertedPrice = float(price[0:5].replace(",", "."))
    discountedPrice = soup.find(id="offering-price").get_text()
    convertedDiscount = float(discountedPrice[0:6].replace(",", "."))
    
    if (convertedDiscount < convertedPrice):
        sendMail()

    print(title.strip())
    print(convertedPrice)
    print(convertedDiscount)


def sendMail():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login("senderMail@mail.com", "senderPassword")

        subject = "Price down!"

        body = "Check your product: " + productURL
        author = "Saintethic"
        msg = f"Subject: {subject},\n\n{body}"
        server.sendmail(
            "Hepsiburada Discount Tracker",
            "toMail@mail.com",
            msg.encode("utf-8")

        )

        print("E-Mail sent bro.")
        server.quit()
    except Exception as e:
        print("ERROOOOOOORRRRR: " + e)

checkPrice()